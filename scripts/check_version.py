import toml
import re
import subprocess


def compare_versions(new_version: str, current_version: str) -> int:
    """
    Compare two versions
    :param new_version: The version from the PR
    :param current_version: The version that is currently in the main branch
    :return: Status of the comparison (1 if new_version > current_version, -1 if new_version < current_version, 0 if equal)
    """
    pr_parts = list(map(int, new_version.split(".")))
    main_parts = list(map(int, current_version.split(".")))

    # Compare each part of the version (major, minor, patch)
    if pr_parts > main_parts:
        return 1
    elif pr_parts < main_parts:
        return -1
    else:
        return 0


with open("pyproject.toml", "r") as file:
    pyproject = toml.load(file)
    pr_version = pyproject["tool"]["poetry"]["version"]

print(f"PR Version: {pr_version}")

subprocess.run(["git", "fetch", "origin", "main"], check=True)
subprocess.run(["git", "checkout", "origin/main"], check=True)

with open("pyproject.toml", "r") as file:
    main_branch_pyproject = toml.load(file)
    main_version = main_branch_pyproject["tool"]["poetry"]["version"]

print(f"Main Branch Version: {main_version}")

# Validate the format of the versions
version_regex = r"^\d+\.\d+\.\d+$"
if not re.match(version_regex, pr_version) or not re.match(version_regex, main_version):
    raise ValueError(
        "One of the versions does not match the expected format (major.minor.patch)."
    )

comparison_result = compare_versions(pr_version, main_version)

if comparison_result <= 0:
    raise ValueError(
        f"PR version ({pr_version}) must be greater than the main branch version ({main_version})."
    )
else:
    print(
        f"PR version {pr_version} is greater than the main branch version {main_version}."
    )
