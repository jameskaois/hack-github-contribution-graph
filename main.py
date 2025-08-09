import git
import os

# Assuming 'my_repo' is the path to your repository
repo_path = './'
repo = git.Repo(repo_path)

# Add a file to the staging area
# For this example, let's create and add a file first
with open(os.path.join(repo_path, 'example_file.txt'), 'w') as f:
    f.write('Hello, GitPythonnn!')
repo.index.add(['example_file.txt'])

# Set the desired commit date in the format "YYYY-MM-DDTHH:MM:SS"
date_string = "2025-07-26T12:00:00"
os.environ['GIT_COMMITTER_DATE'] = date_string

# Perform the commit with a message
repo.index.commit("Test commit")

# Optional: Clean up the environment variable
del os.environ['GIT_COMMITTER_DATE']

origin = repo.remote(name="origin")
origin.push()

# Trigger