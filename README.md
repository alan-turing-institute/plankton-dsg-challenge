# plankton-dsg-challenge

Repository for the [Rapid identification of plankton using machine learning](https://www.turing.ac.uk/events/data-study-group-november-2021) challenge with CEFAS, the November/December 2021 Data Study Group.

### People

- Challenge owner: Sophie Pitois (Cefas)
- PIs: Alejandro Coca Castro, Beatriz Costa Gomes, Evangeline Corcoran (Turing)
- Facilitators: TBD

People also with access to the data safe haven:
- From the Turing: Ed Chalstrey, Oliver Strickson, Scott Hosking
- From Cefas: James Scott, Phil Culverhouse, Robert Blackwell

### Structure 

#### Challenge
- Contains the long description of the challenge, and any additional information.

#### Notebooks
- Instructions to prepare the environment to run the notebooks
- Jupyter notebooks to explore the metadata
- Jupyter notebooks using [scivision](https://github.com/alan-turing-institute/scivision) to handle the data hosted in Azure

#### Metadata
- CSV files with the information regarding the challenge data, before (```../data/raw/```) and after (```../data/processed/```) being split into training and testing datasets, using the script available in ```../src/```
