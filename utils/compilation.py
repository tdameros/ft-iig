import subprocess


def compile(out_name, *files):
    # print(*["gcc", "-Wall", "-Werror", "-Wextra","-fsanitize=address", *files, "-o", out_name])
    gcc = subprocess.Popen(
        ["gcc", "-Wall", "-Werror", "-Wextra", *files, "-o", out_name],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    gcc.wait()
    if gcc.returncode != 0:
        return 0
    return 1


def make_re(path):
    make = subprocess.Popen(["make", "re"], cwd=path)
    make.wait()
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
