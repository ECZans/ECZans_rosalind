"""Helper objects"""
from collections import Counter

# DNA nucleotide alphabet
NUCLEOTIDES = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

# Number of sig-figs for default float value reporting - ROSALIND expects error <= 0.001
DECIMAL_PLACES = 4


class ElemCounter(object):
    """Counter handler for known alphabets"""
    def __init__(self, alphabet):
        self.alphabet = set(alphabet)

    def _count(self, iterable):
        c = Counter(iterable)
        return [(a, c[a]) for a in self.alphabet]

    def __call__(self, *args, **kwargs):
        return self._count(*args, **kwargs)


def iter_fasta(fasta_file):
    """
    Iterate lines in a fasta file with sequences and headers on separate lines. Sequence
    may be wrapped or unwrapped.
    :param fasta_file:
    :return:
    """
    with open(fasta_file) as fa:
        sequence = []
        # Get first fasta header
        header = fa.readline()[1:].rstrip()
        for line in fa:
            if line.startswith('>'):
                yield header, "".join(sequence).replace(" ", "").replace("\r", "")
                sequence, header = [], line[1:].rstrip()
                continue
            sequence.append(line.rstrip())

        yield header, "".join(sequence).replace(" ", "").replace("\r", "")
