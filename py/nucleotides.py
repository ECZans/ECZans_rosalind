"""Nucleotide sequence manipulation methods"""
import sys
from decimal import Decimal
from collections import Counter
from ECZ_ROSALIND.py import common


def lex_order_strings():
    """
    (LEXV) Ordering Strings of Varying Length Lexicographically

    :return:
    """


def count_nucleotides(s):
    """
    (DNA) Counting DNA Nucleotides

    Count number of nucleotides A, C, G, T in the given input

    :param str s: DNA sequence containing A, C, G, T
    :return str: Integer nucleotide counts separated by spaces
    """
    counts = []
    s = s.upper()
    for n in common.NUCLEOTIDES:
        counts.append(str(s.count(n)))
    return ' '.join(counts)


def transcribe_dna(s):
    """
    (RNA) Transcribing DNA into RNA

    Substitute U(racil) for T(hymine) in the provided input DNA sequence, and return
    the same-stranded RNA sequence

    :param str s: DNA sequence containing A, C, G, T
    :return str: RNA sequence containing A, C, G, U
    """
    return s.upper().replace('T', 'U')


def complement_dna(s):
    """
    (REVC) Complementing a Strand of DNA

    Reverse complement a DNA sequence

    :param str s: DNA sequence containing A, C, G, T
    :return str: Complimentary DNA sequence
    """
    s = s.upper()
    forward_alphabet = ''.join(common.NUCLEOTIDES.keys())
    reverse_alphabet = ''.join(common.NUCLEOTIDES.values())
    return s.translate(s.maketrans(forward_alphabet, reverse_alphabet))[::-1]


def percent_gc(fasta_file, ndec=5):
    """
    Computing GC Content (GC)

    Compute % GC content of sequences in provided fasta file. Sequences
    and headers must be on separate lines.

    :param str fasta_file: Path to fasta file
    :param int ndec: Round % GC to int decimal places
    :return [str]: Fasta sequence header and % GC, separated by newlines
    """
    max_header, max_percentage = None, 0
    fasta_gen = common.iter_fasta(fasta_file)
    for header, seq in fasta_gen:
        gc = round(Decimal((seq.count('G') + seq.count('C')) / len(seq) * 100), ndec).__float__()
        if gc <= max_percentage:
            continue
        max_header, max_percentage = header.lstrip('>'), gc
    print('\n'.join([max_header, str(max_percentage)]))


def reverse_palindrome(s, n_char):
    """
    Exhaustive solution for location of reverse palindromes of len n_char in DNA sequence s

    :param s: 
    :param n_char: 
    :return: 
    """
    start_sites = []
    for i in range(len(s) + 1 - n_char):
        segment = s[i:i + n_char]
        if segment == complement_dna(segment):
            start_sites.append(i + 1)
    return start_sites


def consensus_and_profile(fasta_file, output=sys.stdout):
    """
    (CONS) Consensus and Profile

    Write the consensus string and profile matrix for the collection of up to 10
    equal-length DNA sequences in the specified fasta to output

    :param str fasta_file: Path to fasta file
    :param str or io output:
    """
    fasta_sequences = [elem[1] for elem in common.iter_fasta(fasta_file)]