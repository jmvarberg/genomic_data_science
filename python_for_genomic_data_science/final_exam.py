'''
Final project for the course "Python for Genomic Data Science"
'''

#Loading packages and modules required for analysis



#path to dataset
my_data = "./data/dna.example.fasta"

#Q1: How many records are in the file? Pseudocode - count number of lines that start with ">"

def count_seqs_in_fasta(file):
    f = open(file)
    seqs=0
    for line in f:
        if line.startswith('>'):
            seqs += 1
    f.close()
    print("This FASTA file contains %d sequences" %seqs)

count_seqs_in_fasta(my_data)

#Q2 What are the lengths of the sequences in the file? What is the longest sequence and what is the shortest
# sequence? Is there more than one longest or shortest sequence? What are their identifiers?

#Pseudocode if doing manually: instead of just counting, store the sequences and IDs in a dictionary.
#Rather than reinventing the wheel, lets use some of the tools available in the Biopython SeqIO module

from Bio import SeqIO

records = list(SeqIO.parse(my_data, "fasta")) #this parses the fasta file and puts individual sequences/entries into a list

print(records[0]) #see info on the first entry/sequence with ID information
print(len(records[0])) #return the length of the first sequence/entry

lengths = [len(x.seq) for x in records] #extract sequence lengths to a new list
print(lengths)

max_len = max(len(seq_record.seq) for seq_record in records)

