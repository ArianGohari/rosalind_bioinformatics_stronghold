from templates.fasta_template import FastaTemplate


def cons(records):
    n = len(records[0].seq)

    # map each base pair to a index from 0 to 3
    base_pairs = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}

    # initialize consensus matrix
    matrix = [[0 for _ in range(4)] for __ in range(n)]

    # iterate through each record
    for record in records:

        # iterate through sequence
        seq = record.seq

        # append counts to matrix
        for i in range(n):
            if seq[i] == 'A':
                matrix[i][0] += 1
            elif seq[i] == 'C':
                matrix[i][1] += 1
            elif seq[i] == 'G':
                matrix[i][2] += 1
            elif seq[i] == 'T':
                matrix[i][3] += 1

    ret = ''

    # write consensus string (take max of each row)
    for j in range(n):
        ret += base_pairs[matrix[j].index(max(matrix[j]))]

    ret += '\n'

    # write consensus matrix formatted
    for k in range(4):
        counts = [matrix[m][k] for m in range(n)]
        ret += '{}: {}\n'.format(base_pairs[k], ' '.join([str(count) for count in counts]))

    return ret


if __name__ == '__main__':
    FastaTemplate('rosalind_cons.txt').run(cons)