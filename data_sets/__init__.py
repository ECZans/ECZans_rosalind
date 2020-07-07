"""Toy data variables & methods"""
import os

DATA_DIR = os.path.dirname(os.path.realpath(__file__))

# Nucleotides
COUNT_NUCLEOTIDES = os.path.join(DATA_DIR, 'rosalind_dna.txt')
TRANSCRIBE_DNA = os.path.join(DATA_DIR, 'rosalind_dna.txt')
COMPLEMENT_DNA = os.path.join(DATA_DIR, 'rosalind_revc.txt')
PERCENT_GC = os.path.join(DATA_DIR, 'rosalind_gc.txt')
DNA_MOTIF = os.path.join(DATA_DIR, 'rosalind_subs.txt')
RESTRICTION_SITES = os.path.join(DATA_DIR, 'rosalind_revp.txt')

# Fibonacci
RECURRENCE_RABBITS = os.path.join(DATA_DIR, 'rosalind_fib.txt')

# UNSORTED
HAMMING_DISTANCE = os.path.join(DATA_DIR, 'rosalind_hamm.txt')

