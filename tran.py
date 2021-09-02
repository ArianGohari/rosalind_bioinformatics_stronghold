from templates.fasta_template import FastaTemplate


def tran(records):
    s1 = records[0].seq
    s2 = records[1].seq

    n = len(s1)

    transitions = 0
    transversions = 0

    # iterate through equal length words
    for i in range(n):

        # check for transition -> increment transitions
        if (s1[i] == 'A' and s2[i] == 'G') or (s1[i] == 'G' and s2[i] == 'A') or (s1[i] == 'C' and s2[i] == 'T') or (
                s1[i] == 'T' and s2[i] == 'C'):
            transitions += 1
            pass

        # if not transition and s1[i] != s2[i] -> transversion -> increment transversions
        elif s1[i] != s2[i]:
            transversions += 1

    return transitions / transversions


if __name__ == '__main__':
    FastaTemplate('rosalind_tran.txt').run(tran)
