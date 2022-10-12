import subprocess
import logging


def compile(out_name, *files):
    logging.debug(out_name)
    print_files = " ".join([str(file) for file in files])
    logging.debug(" ".join(
        ["gcc", "-Wall", "-Wextra", "-Werror", "-fsanitize=address",
         print_files, "-o", str(out_name)]))
    gcc = subprocess.Popen(
        ["gcc", "-Wall", "-Werror", "-Wextra", "-fsanitize=address", *files,
         "-o", out_name],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    gcc.wait()
    if gcc.returncode != 0:
        return 0
    return 1


def make(rule, path):
    logging.debug(f"make {rule} ({str(path)})")
    make = subprocess.run(["make", rule], cwd=path, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    if "No rule to make target" in make.stderr.decode():
        return 2
    if make.returncode != 0:
        return 0
    return 1


def inject_argv(path_bin, *args, timeout=3):
    str_args = [str(arg) for arg in args]
    run = subprocess.Popen([path_bin, *str_args],
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        run.wait(timeout=timeout)
    except subprocess.TimeoutExpired:
        return 999, "Time Out"
    out, err = run.communicate()
    if run.returncode != 0:
        return run.returncode, err.decode()
    return run.returncode, out.decode()
