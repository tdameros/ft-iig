import subprocess

if __name__ == "__main__":
    git_pull = subprocess.Popen(["git", "pull", "origin", "main"],
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    git_pull.wait()
    exec(open("main.py").read())