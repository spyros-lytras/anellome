# Expanding the genomic diversity of human anelloviruses

Online supplementary for ***Modha, S., Hughes, J., Orton, R.J., Lytras, S.* Expanding the genomic diversity of human anelloviruses.**


[preprint](https://www.biorxiv.org/content/10.1101/2024.05.13.593858v1)


### Content

- 829 Anellovirus genomes assembled in this study:

	- [assembled anellovirus contigs (fasta)](data/Modha_contigs.fas)
	
	- [completeness of assembled contigs (ViralComplete)](data/Modha_contigs_viralcomplete.csv)
	
	- [annotated assembled genomes (genbank)](data/Modha_genomes_annotated.gbk)
	

- [Metadata](data/Modha_allsequence_data.csv):

	- Metadata and analysis results associated with each sequence used in this study.

- [Alignments](alignments):

	- [Full genome alignment](alignments/genomes_rotated_linsialn.fas) of all sequences 
	and its [trimmed version](alignments/genomes_rotated_linsialn_1pungap.fas) used for the recombination analysis.
	
	- [Full ORF1 amino acid alignment](alignments/humanAnellos_ORF1_aa_aln.fas) of all sequences
	and the [trimmed ORF1 codon alignment](alignments/fig1_humanAnellos_ORF1_cod_aln_70pungap.fas) used for the phylogenetic analysis.
	
	- [Trimmed ORF1 codon alignment of all *Anelloviridae*](alignments/figS1_allAnelloviridae_ORF1_70pungap.fas)
	(used for Figure S1 phylogeny).
	
	- Reference constrained alignments for each human-associated anellovirus genus.

- [Recombination](recombination):

	- Raw [RDP5 analysis results](recombination/genomes_rotated_linsialn_1pungap_all.csv).
	
	- Raw breakpoint clustering analysis results: [BDT](recombination/genomes_rotated_linsialn_1pungap_all_BDT.csv) 
	and [RRT](recombination/genomes_rotated_linsialn_1pungap_all_RRT.csv).
	
- [Phylogenetics](trees):

	- [ORF1 phylogeny of human-associated *Anelloviridae*](trees/fig1_humanAnellos_ORF1_cod_aln_70pungap.treefile) (Figure 1).
	
	- [ORF1 phylogeny of all *Anelloviridae*](trees/figS1_allAnelloviridae_ORF1_70pungap.treefile) (Figure S1).

- Other data:

	- [Raw data for Figure S4 depth vs GC content comparison](data/figS4B_depthVSgc_window100step50_ranked.csv)