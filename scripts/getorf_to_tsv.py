from Bio import SeqIO
import pandas as pd

#run first using:
    #1. the getorf fasta file output containing nucleotide sequences of detected ORFs
file = ''
    #2. the full nucleotide sequence fasta used as getorf's input
origfile = ''


origrecs = SeqIO.parse(origfile, 'fasta')

origacc = []
for orec in origrecs:
	origacc.append(orec.description)


records = SeqIO.parse(file, 'fasta')

allacc = []
for rec in records:
	allacc.append(rec.description)
	

cols = ['accession', 'sameaccdup', 'start', 'end', 'orientation', 'cross_bp']
infodic = {c:[] for c in cols}

for a in allacc:
    acc = a.split(' ')[0][:-2]
    dup = a.split(' ')[0][-1]
    st = a.split(' ')[1][1:]
    en = a.split(' ')[3][:-1]
    
    infodic['accession'].append(acc)
    infodic['sameaccdup'].append(dup)
    infodic['start'].append(st)
    infodic['end'].append(en)
    
    if "(REVERSE SENSE)" in a:
        infodic['orientation'].append(-1)
    else:
        infodic['orientation'].append(1)
        
          
    if "(ORF crosses the breakpoint)" in a:
        infodic['cross_bp'].append('Y')
    else:
        infodic['cross_bp'].append('N')


df = pd.DataFrame(infodic)

df.sort_values(by=['accession', 'sameaccdup'], ascending = False, inplace = True)


#if you were to keep one per duplicate
df.sort_values(by=['sameaccdup'], inplace = True)

df.drop_duplicates(subset='accession', keep="last", inplace = True)

df.sort_index(inplace = True)

print(df)


#this script will create a '.tsv' file that will be used in the rotator.py script
df.to_csv(file.replace('.fas','.tsv'),sep='\t', index = False)


#check if some accessions don't have an ORF1 picked up
unpicked = list(set(origacc) - set(infodic['accession']))

print(unpicked)

#and a '_noORF.txt' file that includes accessions with no ORF detected
with open(file.replace('.fas','_noORF.txt'), 'w+') as out:
    for a in unpicked:
        out.write('%s\n'%a)
