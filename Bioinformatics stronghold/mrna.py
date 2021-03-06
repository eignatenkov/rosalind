__author__ = 'egor'

# Given: A protein string of length at most 1000 aa.
#
# Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)
#
# Sample Dataset
#
# MA

# Sample Output
#
# 12

with open("/home/egor/Загрузки/rosalind_mrna.txt","r") as f:
    prot=f.readline().strip()

codon={"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V", "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V", "UUA": "L",
            "CUA": "L", "AUA": "I", "GUA": "V", "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V", "UCU": "S", "CCU": "P",
            "ACU": "T", "GCU": "A", "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A", "UCA": "S", "CCA": "P", "ACA": "T",
            "GCA": "A", "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A", "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
            "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D", "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
            "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E", "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
            "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G", "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
            "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"}

total = 1

for i in prot:
    total = (total*len([x for x in codon if codon[x]==i])) % 1000000

total = total*len([x for x in codon if codon[x]=="Stop"]) % 1000000

print(total)