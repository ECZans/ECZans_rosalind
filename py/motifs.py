"""Sequence structure and motif methods"""
import ECZ_ROSALIND.py.nucleotides as nuc


def pattern_matching():
    """
    (TRIE) Introduction to Pattern Matching

    :return:
    """


def quick_motif():
    """
    (KMP) Speeding Up Motif Finding

    :return:
    """


def shared_motif():
    """
    (LCSM) Finding a Shared Motif

    :return:
    """


def similar_motifs():
    """
    (KSIM) Finding All Similar Motifs

    :return:
    """


def interleaf_motifs():
    """
    (SCSP) Interleaving Two Motifs

    :return:
    """


def spliced_motif():
    """
    (SSEQ) Finding a Spliced Motif

    :return:
    """


def paired_spliced_motif():
    """
    (LCSQ) Finding a Shared Spliced Motif

    :return:
    """


def disjointed_gene_motifs():
    """
    (ITWV) Finding Disjoint Motifs in a Gene

    :return:
    """


def restriction_sites(s, p_min=4, p_max=12):
    """
    (REVP) Locating Restriction Sites

    Print the 1-based start sites and subsequence length for all reverse palindromes
    of length p_min <= len <= p_max in DNA sequence s

    :param str s: DNA sequence
    :param int p_min: Minimum reportable palindrome length
    :param int p_max: Maximum reportable palindrome length
    """
    restrict_starts = []
    for k in range(p_min, p_max + 1):
        for i in nuc.reverse_palindrome(s, k):
            restrict_starts.append('{} {}'.format(i, k))
    print('\n'.join(restrict_starts))


def dna_motif(s, t):
    """
    (SUBS) Finding a Motif in DNA

    Find all 1-based start positions of substring t in DNA nucleotide sequence s

    :param str s: DNA sequence to query
    :param str t: DNA subsequence to search for
    :return str: 1-based start locations of t in s as space-delimited list
    """
    motif_starts, s, t = [], s.upper(), t.upper()
    # Position of first match
    idx = s.find(t)
    while idx != -1:
        motif_starts.append(str(idx + 1))
        idx = s.find(t, idx + 1)
    return ' '.join(motif_starts)


def rna_splicing():
    """
    (SPLC) RNA Splicing

    :return:
    """


def rna_perfect_structure():
    """
    (PMCH) Perfect Matchings and RNA Secondary Structures

    :return:
    """


def rna_catalan_numbers():
    """
    (CAT) Catalan Numbers and RNA Secondary Structures

    :return:
    """


def rna_motzkin_numbers():
    """
    (MOTZ) Motzkin Numbers and RNA Secondary Structures

    :return:
    """


def rna_maximum_structure():
    """
    (MMCH) Maximum Matchings and RNA Secondary Structures

    :return:
    """











