#!/usr/bin/env python
from pathlib import Path

from cookiecutter.main import cookiecutter
from rich import print

BRICKMAN_ROOT = "/maps/projects/dan1/data/Brickman"

if __name__ == "__main__":
    project_path = (
        Path(BRICKMAN_ROOT) / Path("projects") / Path("{{ cookiecutter.__project_name }}")
    )

    # Mandatory description field
    if "{{ cookiecutter.description }}" == "":
        print("Description is [bold red]mandatory[/bold red], try again!")
        import shutil
        import sys

        shutil.rmtree(project_path.as_posix())
        sys.exit()

    try:
        print(f"Your project has been created in [italic grey]{project_path}[/italic grey]")

        # Fix permissions
        print("Fixing permissions, please wait ...")
        project_path.chmod(0o775)

    except Exception as e:
        print(f"[bold red]{e}[/bold red]")