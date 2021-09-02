from difflib import SequenceMatcher
from templates.fasta_template import FastaTemplate


def lcsm(records):
    # start recursion with first two sequences
    return lcsm_recursive(records[0].seq, records[1].seq, records, 1)


def lcsm_recursive(seq1, seq2, records, i):
    len1 = len(seq1)
    len2 = len(seq2)

    # match sequence 1 with sequence 2
    match = SequenceMatcher(None, seq1, seq2, autojunk=False).find_longest_match(0, len1, 0, len2)

    # create substring
    substring = seq1[match.a: match.a + match.size]

    if i == len(records) - 1:
        return substring

    # recursively repeat with substring and next sequence
    else:
        return lcsm_recursive(substring, records[i+1].seq, records, i+1)


if __name__ == '__main__':
    FastaTemplate('rosalind_lcsm.txt').run(lcsm)