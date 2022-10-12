# Prediction-of-Pt-NMR-chem-shifts
Code repo of article "Predicting 195Pt NMR Chemical Shifts in (In)Organic Complexes with a Fast and Simple Protocol Combining Semi-Empirical Modeling and Machine Learning" by Evgeniia E. Ondar, Mikhail V. Polynski, Valentine P. Ananikov. [link]

![alt text](https://github.com/ondevg/Prediction-of-Pt-NMR-chem-shifts/blob/main/maimain1.png?raw=true)

## Dataset
1. pt_dataset.csv - Set of 113 Pt complexes with features calculated by use of `GFN2-xTB`. 
2. no_corr_pt_dataset.csv - Set of 113 Pt complexes with weakly correlated features calculated by use of `GFN2-xTB`.
3. qtaim.csv - Set of 113 Pt complexes with features calculated by use of `ZORA-TPSS/triple-$/zeta$`. 
4. no_corr_qtaim.csv - Set of 113 Pt complexes with weakly correlated features calculated by use of `ZORA-TPSS/triple-$/zeta$`.
### Features 
The explanation of column features of pt_dataset.csv is listed below:
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
