"""Dependencies not yet sorted by topic"""


def hamming_distance(s, t):
    """
    Counting Point Mutations (HAMM)

    Compute the number of nucleotides differing (the Hamming distance) between two
    same-strand DNA nucleotide sequences of equal length

    :param str s: DNA sequence
    :param str t: DNA sequence
    :return int: Hamming distance dH(s,t)
    """
    hdist, s, t = 0, s.upper(), t.upper()
    for i in range(len(s)):
        if s[i] != t[i]:
            hdist += 1
    return hdist
