import git
import os

# Assuming 'my_repo' is the path to your repository
repo = git.Repo('my_repo')

# Add a file to the staging area
# For this example, let's create and add a file first
with open(os.path.join(repo.working_dir, 'example_file.txt'), 'w') as f:
    f.write('Hello, GitPython!')
repo.index.add(['example_file.txt'])

# Set the desired commit date in the format "YYYY-MM-DDTHH:MM:SS"
date_string = "2023-01-01T12:00:00"
os.environ['GIT_COMMITTER_DATE'] = date_string

# Perform the commit with a message
repo.index.commit("Initial commit")

# Optional: Clean up the environment variable
del os.environ['GIT_COMMITTER_DATE']

origin = repo.remote()
origin.push()