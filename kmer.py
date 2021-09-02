from lexf import lexf_recursive
from templates.fasta_template import FastaTemplate


def find_occurrences(s, t):
    n = len(s)
    m = len(t)

    occurrences = 0
    for i in range(n):
        if s[i:i+m] == t:
            occurrences += 1

    return occurrences


def kmer(records):
    s = records[0].seq
    alphabet = sorted(set(s))
    k = 4
    kmers = lexf_recursive(alphabet, k, '')
    a = [find_occurrences(s, t) for t in kmers]

    # write result formatted
    return ' '.join([str(element) for element in a])


if __name__ == '__main__':
    FastaTemplate('rosalind_kmer.txt').run(kmer)