import os
import subprocess

"""
Updates all repos and (re-)installs editable in list below.
Note this doesn't seem to work in Debug mode for some reason.
"""

def update_repos(repo_dirs):
    """
    Updates multiple git repositories by pulling from origin and installing in editable mode.

    Args:
        repos_dir (str): The directory containing the repositories.
    """
    for repo_dir in repo_dirs:

        if os.path.isdir(repo_dir) and os.path.exists(os.path.join(repo_dir, ".git")):
            print(f"Updating repository: {repo_dir}")

            try:
                # Git pull from origin
                subprocess.run(["git", "pull", "origin"], cwd=repo_dir, check=True, capture_output=True)

                # Install in editable mode
                if os.path.exists(os.path.join(repo_dir, "pyproject.toml")):
                    subprocess.run(
                        ["pip", "install", "--config-settings", "editable-mode=strict", "-e", "."], 
                        cwd=repo_dir, check=True, capture_output=True
                    )
                else:
                    print(f"No setup.py found in {repo_dir}")

                print(f"Repository {repo_dir} updated successfully.")

            except subprocess.CalledProcessError as e:
                print(f"Error updating {repo_dir}: {e}")

            except Exception as e:
                print(f"Unexpected error with {repo_dir}: {e}")

if __name__ == "__main__":
    repos_directories = [
        r"C:\github\dirigo",
        r"C:\github\dirigo-configs",
        r"C:\github\dirigo-gui",
        r"C:\github\atsbindings",
        r"C:\github\imaqbindings",
        r"C:\github\dirigo-alazar",
        r"C:\github\dirigo-e2v-line-camera",
        r"C:\github\dirigo-ni-frame-grabber",
        r"C:\github\dirigo-ecu",
        r"C:\github\dirigo-strip-acquisition",
        r"C:\github\dirigo-thorlabs-stage",
        r"C:\github\dirigo-thorlabs-detectors",
        r"C:\github\nlm-lib",
        r"C:\github\mph-acquisition"
    ] 
    update_repos(repos_directories)

