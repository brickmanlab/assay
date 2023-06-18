# README

This repository contains a template for creating either `Assay` or `Project`.
For more info please read out [RDM guidelines](https://brickmanlab.github.io/wiki/rdm/).

## Creating `Assay`

```bash
module load miniconda/latest
source activate brickman

cd /home/$USER/Brickman/assays
cruft create https://github.com/brickmanlab/ngs-template --directory="assay"
```

## Creating `Project`

```bash
module load miniconda/latest
source activate brickman

cd /home/$USER/Brickman/projects
cruft create https://github.com/brickmanlab/ngs-template --directory="project"
```
