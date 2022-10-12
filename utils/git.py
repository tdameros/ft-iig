import subprocess


def git_pull(path):
    git_process = subprocess.run(["git", "pull", "origin", "main"],
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 cwd=path)
    return git_process.returncode


def git_clone(url, path):
    git_process = subprocess.run(["git", "clone", url, "ft_iig"],
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 cwd=path)
    return git_process.returncode
