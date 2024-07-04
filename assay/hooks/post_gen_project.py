#!/usr/bin/env python
from pathlib import Path

from cookiecutter.main import cookiecutter
from rich import print

BRICKMAN_ROOT = "/maps/projects/dan1/data/Brickman"
CPR_ROOT = "smb:/unicph.domain/groupdir/SUN-CPR-genomics_data/"

if __name__ == "__main__":
    assay_path = (
        Path(BRICKMAN_ROOT) / Path("assays") / Path("{{ cookiecutter.__assay_id }}")
    )
    cpr_path = "~/ucph/ndir/SUN-CPR-genomics_data/"
    cpr_path += (
        Path("{{ cookiecutter.genomics_path }}").as_posix().replace(CPR_ROOT, "")
    )

    # mandatory fields
    if "{{ cookiecutter.codename }}" == "":
        print("Initials are [bold red]mandatory[/bold red], try again!")
        import shutil
        import sys

        shutil.rmtree(assay_path.as_posix())
        sys.exit()

    try:
        print(f"Your assay has been created in [italic grey]{assay_path}[/italic grey]")

        # Fix permissions
        print("Fixing permissions, please wait ...")
        assay_path.chmod(0o775)

        if "{{ cookiecutter.genomics_path }}" != "":
            # Copy files from CPR
            print("Dont forget to copy the FASTQ files!")
            print(
                f"rsync -avzh --progress --chmod=2775 {cpr_path}/*.fastq.gz {assay_path.resolve()}/raw/fastq/"
            )

    except Exception as e:
        print(f"[bold red]{e}[/bold red]")
