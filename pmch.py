import math
from templates.fasta_template import FastaTemplate


def pmch(records):
    seq = records[0].seq

    # get AU and GC counts
    counts = {'AU': seq.count('A'), 'GC': seq.count('G')}

    # possible number of perfect matchings is |AU|! * |GC|!
    return math.factorial(counts['AU']) * math.factorial(counts['GC'])


if __name__ == '__main__':
    FastaTemplate('rosalind_pmch.txt').run(pmch)
