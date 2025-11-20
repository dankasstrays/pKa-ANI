## INSTALLATION (using PyPI)


The package requires ambertools which can be installed as given below (only works with Python versions <3.14)

```bash
conda create -n pkaani python=3.13
conda activate pkaani
conda install conda-forge::ambertools
```

Then, simply use the command below:

```bash
pip install pkaani
```

## Python script usage
The snippet below shows how to use the `calculate_pka` function within a python script - the input argument is a list of strings which are PDB file names in the working directory. Given a list of PDBs titled "1brs.pdb" and "6oge_de.pdb":

```python
from pkaani.pkaani import calculate_pka as calculate_pkaani
  
pKas = calculate_pkaani(["1brs.pdb","6oge_de.pdb"])
```



## INSTALLATION (from source code)

Navigate to this repository for the source code for this pyPI upload: https://github.com/adnaksskanda/pKa-ANI/tree/pyPI_upload

Prior to the installation of pKa-ANI, users should make sure they have installed conda.

To install pKa-ANI, navigate to the directory of the source that you've downloaded and;

```bash     
conda env create -f pkaani_env.yaml
```
This will create a conda environment named `pkaani` and install all required packages.
After the environment is created, activate the environment and install the package.
   
```bash    
conda activate pkaani 
pip install .
```

### **PREREQUISITES:**

* miniconda/anaconda

If `pkaani_env.yaml` is not used, users should make sure the following packages are installed.
* python>=3.10
* numpy
* scipy
* pytorch
* torchani==2.2.0
* scikit-learn==1.6.1
* ase
* joblib
* ambertools
* setuptools
		
## **USAGE**

pKa-ANI requires PDB files to have H atoms that are added with default ionization states of residues: ASP, GLU, LYS, TYR, HIE. 

Due to this reason, input PDB file(s) are prepared before the calculation of pKa values (output PDB file __'PDBID_pkaani.pdb'__). 

__We would like to warn users, that our models are trained to predict pKa values for apo-proteins. 
Due to this, any residue that is not an aminoacid is removed from PDB file(s) during the preparation.__


### Example command line usages:

* If PDB file doesnt exist, it is downloaded and prepared for pKa calculations.

```bash
pkaani -i 1BNZ
      
pkaani -i 1BNZ.pdb
```

* Multiple files can be given as inputs

```bash
pkaani -i 1BNZ,1E8L
```

* If a specific directory is wanted:

```bash
pkaani -i path_to_file/1BNZ
      
pkaani -i path_to_file/1BNZ,path_to_file/1E8L
```

### Arguments: 

```bash
-h: Help

-i: Input files. Inputs can be given with or without file extension (.pdb). 
    If PDB file is under a specific directory (or will be downloaded) the path                 
    can also be given as path_to_file/PDBFILE. Multiple PDB files can be given 
    by using "," as separator (i.e. pkaani -i 1BNZ,1E8L).
```				 

## **CITATION**

Gokcan, H.; Isayev, O. Prediction of Protein p K a with Representation Learning. Chem. Sci. 2022, 13 (8), 2462–2474. https://doi.org/10.1039/D1SC05610G.				 
## **LICENSING**

Please read LICENSE file.

