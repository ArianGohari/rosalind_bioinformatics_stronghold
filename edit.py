from templates.fasta_template import FastaTemplate


def edit(records):
    s = records[0].seq
    t = records[1].seq

    n = len(s)
    m = len(t)

    matrix = [[0 for __ in range(m+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):

            if i == 0:
                matrix[i][j] = j

            elif j == 0:
                matrix[i][j] = i

            elif s[i - 1] == t[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]

            else:
                matrix[i][j] = min(matrix[i][j - 1], matrix[i - 1][j], matrix[i - 1][j - 1]) + 1

    return matrix[n][m]


if __name__ == '__main__':
    FastaTemplate('rosalind_edit.txt').run(edit)