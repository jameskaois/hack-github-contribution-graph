import git
import os
import datetime

# Assuming 'my_repo' is the path to your repository
repo_path = './'
repo = git.Repo(repo_path)
author = git.Actor("James Cao", "cao.james069@gmail.com")

# Add a file to the staging area
# For this example, let's create and add a file first
with open(os.path.join(repo_path, 'example_file.txt'), 'w') as f:
    f.write('Testing!')
repo.index.add(['example_file.txt'])

dates = [
    datetime.datetime(2023, 1, 2, 12, 1, 0),
]

# Perform the commit with a message
repo.index.commit("Testinggg", commit_date=dates[0].isoformat(), author=author)

origin = repo.remote(name="origin")
origin.push()