from pathlib import Path
from utils.git import git_pull

if __name__ == "__main__":
    git_pull(Path().absolute())
    exec(open("main.py").read())