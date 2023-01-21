import os

class Repository:
    def __init__(self, repo_link):
        self.repo_link = repo_link
        self.repo_path = self.repo_link.split("/")[-1]

    def clone(self):
        """Clone the repo and prepare it for analysis."""
        os.system(f'git clone {self.repo_link}')
        # Remove the `.git` folder and .gitignore.
        os.system(f'rm -rf {self.repo_path}/.git')
        os.system(f'rm -rf {self.repo_path}/.gitignore')

    def files(self):
        """Generator function which yields the files in the repo."""
        for root, dirs, files in os.walk(self.repo_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Read file path into memory.
                with open(file_path, "r") as f:
                    try:
                        file_content = f.read()
                    except UnicodeDecodeError:
                        file_content = "Error: Could not read file " + file_path

                yield file_path, file_content

    