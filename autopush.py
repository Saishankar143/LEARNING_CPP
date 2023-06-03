import os
import subprocess

# Specify the path to your local Git repository
repo_path = "C:\\Users\\saish\\OneDrive\Desktop\\repos\\learning_cpp"

# Change to the repository directory
os.chdir(repo_path)

# Add all new files to the Git repository
subprocess.run(["git", "add", "."])

# Commit the changes with a custom commit message
commit_message = "Automatically added new files"
subprocess.run(["git", "commit", "-m", commit_message])

# Push the changes to the remote repository
subprocess.run(["git", "push"])
