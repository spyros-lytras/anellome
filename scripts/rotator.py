from Bio import SeqIO
import pandas as pd


#this script uses:
    #1. the full nucleotide fasta file used as getorf's input
fastaname = ''
#and the two files produced by the getorf_to_tsv.py script
    #2. the tsv file 
tabname = ''
    #3. the noORF.txt file
noORFfile = ''

noORFacc = []
with open(noORFfile, 'r+') as noORF:
    noORFacc = [x[:-1] for x in noORF.readlines()]
    


df = pd.read_csv(tabname, sep = '\t')

inforows = df.to_dict('records')

infodic = {}
for i in range(len(inforows)):
    acc = inforows[i]['accession']
    #exclude accessions that didn't give an ORF >1000bp
    if acc not in noORFacc:
        infodic.update({acc:inforows[i]})



records = SeqIO.parse(fastaname, 'fasta')


fastaout = ''

sanity_check = ''


for rec in records:
    
    #exclude accessions that didn't give an ORF >1000bp
    if rec.id not in noORFacc:
            
        info = infodic[rec.id]                
        
        #if the orientation is positive it doesn't matter whether the ORF crosses the breakpoint or not, 
        #since the start position will always be within the sequence length
        
        thelen = len(rec.seq)
        
        if info['orientation'] == 1:
            
            theseq = str(rec.seq)
            
            start = info['start'] -1
                        
            fnseq = theseq[start:] + theseq[0:start]
            
            fastaout = fastaout + '>%s\n%s\n'%(rec.id, fnseq)         

            sanity_check = sanity_check + '%s\t%s\n'%(rec.id, len(fnseq))
            
        
        elif (info['orientation'] == -1) and (info['cross_bp'] == 'Y'):
            
            theseq = str(rec.seq.reverse_complement())
            
            start = int(thelen) - (info['start'] - int(thelen))
                        
            fnseq = theseq[start:] + theseq[0:start]

            fastaout = fastaout + '>%s\n%s\n'%(rec.id, fnseq)            

            sanity_check = sanity_check + '%s\t%s\n'%(rec.id, len(fnseq))
            

        elif (info['orientation'] == -1) and (info['cross_bp'] == 'N'):
            
            theseq = str(rec.seq.reverse_complement())
            
            start = int(thelen) - info['start']
                        
            fnseq = theseq[start:] + theseq[0:start]

            fastaout = fastaout + '>%s\n%s\n'%(rec.id, fnseq)            

            sanity_check = sanity_check + '%s\t%s\n'%(rec.id, len(fnseq))
        
        
outname = fastaname.replace('.fas', '_rotated.fas')
outname = outname.replace('../', '')

with open(outname, 'w+') as out:
    out.write(fastaout[:-1])
    
with open('sanity_check.tsv', 'w+') as out:
    out.write(sanity_check)