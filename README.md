# Diversity and evolution of the human anellome

Online supplementary for [*Modha, S., Hughes, J., Orton, R.J., Lytras, S.* (2024).
Diversity and evolution of the human anellome.](https://www.biorxiv.org/content/10.1101/2024.05.13.593858v1)


### Contents

- [Metadata](anellome_alldata.csv):

	- Metadata and analyses results associated with each sequence used in this study.

- [Alignments](alignments):

	- [Full genome alignment](alignments/AN11.7_nt_rotated_linsi.fas) of all sequences 
	and its [trimmed version](alignments/AN11.7_nt_rotated_linsi_1pungap.fas) used for the recombination analysis.
	
	- [Full ORF1 codon alignment](alignments/AN11.7_ORF1_cod_einsi.fas) of all sequences
	and its [trimmed version](alignments/AN11.7_ORF1_cod_einsi_70pungap.fas) used for the phylogenetic analysis.
	
	- Reference constrained full genome alignment separated by clade: [alpha](alignments/al_AN11.7_nt_alpha_ref.fas), [beta](alignments/al_AN11.7_nt_beta_ref.fas), [gamma](alignments/al_AN11.7_nt_gamma_ref.fas), [he](alignments/al_AN11.7_nt_he_ref.fas); 
	and clade-specific alignments of novel clades [X1](alignments/al_AN11.7_nt_X1.fas) and [X2](alignments/al_AN11.7_nt_X2.fas)
	
- [Recombination](recombination):

	- Raw [RDP5 analysis results](recombination/AN11.7_nt_rotated_linsi_1pungap_all.csv).
	
	- Raw breakpoint clustering analysis results: [BDT](recombination/AN11.7_nt_rotated_linsi_1pungap_BDT.csv) 
	and [RRT](recombination/AN11.7_nt_rotated_linsi_1pungap_RRT.csv).
	
- [Phylogenetics](tree):

	- [ORF1 phylogeny](tree/AN11.7_ORF1_cod_einsi_70pungap.fas.treefile) of all sequences used in this study. 
	
- [Scripts](scripts):

	- Python scripts for rotating anellovirus genomes to the start of ORF1.
