### Conda

Create a Conda environment with the required Python version and packages:

1. `conda env create -f environment.yml`
2. `conda activate scivis-plankton`
3. `python -m ipykernel install --user --name scivis-plankton --display-name "Python (scivis-plankton)"`

The third command makes `scivis-plankton` available as a notebook kernel.

### pip

Install the required Python version and packages:

1. Make sure you are running Python `>=3.7`
    - run `pyenv global 3.8.8`
2. `pip install -r requirements.txt`
3. Set up a kernel for the jupyter notebook
    - `python -m ipykernel install --user --name scivis-plankton --display-name "Python (scivis-plankton)"`
