# Water-Soluble Pt Complexes: Workflow for Predicting 195Pt Chemical Shifts
Code repo of article "Predicting 195Pt NMR Chemical Shifts in (In)Organic Complexes with a Fast and Simple Protocol Combining Semi-Empirical Modeling and Machine Learning" by Evgeniia E. Ondar, Mikhail V. Polynski, Valentine P. Ananikov. [link]

Water-soluble Pt complexes are vital components in medicinal chemistry and catalysis, including the well-known cisplatin family of anticancer drugs and industrial hydrosylilation catalysts. Understanding the activity mechanisms of these complexes is crucial, and 195Pt NMR spectroscopy is a valuable tool for operando monitoring. However, correlating Pt complex structure with 195Pt chemical shifts can be challenging, limiting their use in everyday research practice.

We present a new workflow for predicting the lowest-energy configurational/conformational isomers of water-soluble Pt(II) and Pt(IV) anionic, neutral, and cationic complexes with halide, NO2−, (di)amino, and (di)carboxylate ligands. The workflow uses the GFN2-xTB semiempirical method to determine 3D structures and a Machine Learning (ML) model tuned for Pt complexes to predict corresponding chemical shifts.

![alt text](https://github.com/ondevg/Prediction-of-Pt-NMR-chem-shifts/blob/main/maimain.png?raw=true)

The ML model offers an impressive accuracy of 0.98% (normalized root-mean-square deviation / RMSD) on the held-out test set, with chemical shift values ranging from -6293 to 7090 ppm. This workflow can be a valuable tool for researchers in the field, as it provides a reliable approach for the rapid correlation of Pt complex structure with 195Pt chemical shifts.

We hope that this workflow will contribute to the advancement of research in the field of water-soluble Pt complexes and catalysis.

## Dataset
Generation of 3D structure of complexes was performed automatically by convertion of SMILES (3D_structure_generation.ipynb). Dataset was constructed from 3D geometry optimization outputs of 122 Pt water-soluble complexes. Optimization procedure consisted of 1) GFN2-xTB method, or 2) ZORA-TPSS/triple-zeta. Descriptors based on ZORA-TPSS/triple-zeta computations were used as a baseline set to compare the GFN2-xTB with. 

Additionally to GFN2-xTB optimized parameters of complexes, three descriptors were calculated: FCHL, aSLATM, Coulomb matrix. Comparative analysis showed that descriptors based on Coloumb matrix enable good generalization. 

### Features 
The explanation of features of Coulomb matrix-based dataset is listed below:
```
Complex ID - Pt complex ID
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
In models.ipynb the train, validation and test procedures are introduced. Random forest, ridge and support vector regressor were taken into consideration. Models explanation by use of Shapley values are presented as well.

## Contribution

Evgeniia E. Ondar - 

Mikhail V. Polynski - 

Valentine P. Ananikov - 

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
