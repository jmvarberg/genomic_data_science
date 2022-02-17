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

#print(records[0]) #see info on the first entry/sequence with ID information
#print(len(records[0])) #return the length of the first sequence/entry

lengths = [len(x.seq) for x in records] #extract sequence lengths to a new list
print(sorted(lengths))

max_len = max(len(seq_record.seq) for seq_record in records)
print("The maximum sequence length in this FASTA is %d bases long" %max_len)
min_len = min(len(seq_record.seq) for seq_record in records)
print("The minimum sequence length in this FASTA is %d bases long" %min_len)

for seq_record in records:
    if len(seq_record.seq) == max_len:
        print("ID of sequence with max length: ", seq_record.id, len(seq_record.seq))
    if len(seq_record.seq) == min_len:
        print("ID of sequence with min length: ", seq_record.id, len(seq_record.seq))


#Given an input reading frame on the forward strand (1, 2, or 3) your program should be able to identify 
# all ORFs present in each sequence of the FASTA file, and answer the following questions: 
# 1) What is the length of the longest ORF in the file? 
# 2) What is the identifier of the sequence containing the longest ORF? 
# 3) For a given sequence identifier, what is the longest ORF contained in the sequence represented by that identifier? 
# 4) What is the starting position of the longest ORF in the sequence that contains it? The position should indicate the character number in the sequence.

#Pseudocode approach: go through records list object for each seq_record. Identify first "ATG" position; move to next codon (index of "ATG" +1) and ask if there is a STOP codon (TAG/TAA/TGA)
# if there isn't, append those 3 bases to string and move to next 3; continue until stop codon found, then store the output in a dictionary of ORFs

seq1 = records[0].seq

for seq_record in records:
    start = seq_record.seq.find('ATG')
    if start != 0:
        print(start)
        #if there is a start codon, then parse string from seq_record.seq[start::] and find ORFS


