# Prediction-of-Pt-NMR-chem-shifts
Code repo of article "Predicting 195Pt NMR Chemical Shifts in (In)Organic Complexes with a Fast and Simple Protocol Combining Semi-Empirical Modeling and Machine Learning" by Evgeniia E. Ondar, Mikhail V. Polynski, Valentine P. Ananikov. [link]

## Dataset
1. pt_dataset.csv - Set of 113 Pt complexes with 56 features. 
2. no_corr_pt_dataset.csv - Set of 113 Pt complexes with 29 weakly correlated features obtained after EDA. 
### Features 
The explanation of column features is listed below:
```
Complex - Pt complex ID
Source_doi - DOI of article where the experimental value of 195Pt NMR chemical shift was taken from
Charge - Charge of complex scaled 1000 times
Shift - Experimental value of 195Pt NMR chemical shift of complex
Dipole - full molecular dipole value calculated by use of GFN2-xTB
q - Pt atom charge in the complex calculated by use of GFN2-xTB
Brutto - Brutto formula of complex
Charge_class - charge of complex as neutral \anion \ cation
Geometry - geometry of complex as sq-pl (square-planar) \ oct (octahedral)
Ligand - type of ligands in the complex as hal (halogen) \ org (organic) \ inorg (inorganic) \ hal-org \ hal-inorg
Smiles - SMILES of the complex
1-46 - vector descriptor of Pt atom from Coulomb matrix of the complex
```
## EDA
Explorative data analysis and visualizations are in EDA.ipynb

## Models
In models.ipynb the train, validation and test procedures are introduced. Models explanation by use of Shapley values are presented as well

## Requirements
One can find the requirements in requirements.txt file

## Citing
Please cite as:
```
@article{,
  title={},
  author={},
  journal={},
  pages={},
  year={},
  publisher={},
  doi={}
}
```
