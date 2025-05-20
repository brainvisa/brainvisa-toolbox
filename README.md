# BrainVISA Toolbox Template

This project contains a minimal BrainVISA (i.e. Axon) toolbox with a single process that can be used with the neuro-forge distribution of Axon.

## Installation

First [install Pixi](https://pixi.sh) and Git on your system.
Then clone the project, start the environment with `pixi` and start `brainvisa`:
```
git clone https://github.com/brainvisa/brainvisa-toolbox
cd brainvisa-toolbox
pixi shell
brainvisa
```

The toolbox and its process are available in BrainVISA.

## Modify the toolbox

The toolbox files used by BrainVISA must be located in a directory located in the Python `site-packages` directory. This file copy is done by installing the toolbox with `pip`. This is done a first time by `pixi` through `pyproject.toml`. But when source files are modified, it is necessary to copy the modified files at the right place:
```
pip install "$PIXI_PROJECT_ROOT"
```
