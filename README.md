# Ti–V–H Machine-Learning Interatomic Potentials (MTP)

This repository contains trained Moment Tensor Potentials (MTPs) for the Ti–V–H system, an example LAMMPS molecular dynamics (MD) script for relaxing Ti\(_{1-y}\)V\(_y\)H\(_x\) hydrides, and the main results obtained with these potentials.

The potentials accompany the paper asigned to Computetional Materials Science Journal:

> P. V. Chirkov, A. A. Mirzoev, A. V. Verkhovykh,  
> *Atomistic simulation of Ti–V solid solution hydrides by machine-learning potentials*,  

## Trained MTP potentials

The directory `01_trained_potentials/` contains the MTPs of different levels used in the paper. It was trained on DFT data (VASP, GGA-PBE) for:

- fcc Ti\(_{1-y}\)V\(_y\)H\(_x\) hydrides with \(x = 1.0\)–\(2.0\) and \(y = 0\)–\(1.0\),
- bcc Ti–V alloys with dilute H,
- H on both tetrahedral and octahedral sites.

Validation details, error metrics, and parity plots are given in the paper.

## Example LAMMPS MD script

The script `lammps/in.relax_TiVH` performs a short relaxation of an fcc Ti\(_{1-y}\)V\(_y\)H\(_x\) supercell at 300 K using the MLIP-3 interface. A minimal example is shown below.

## Results

The results/ directory contains the main figures and underlying data from the paper.
