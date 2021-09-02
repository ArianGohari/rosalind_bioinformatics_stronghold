from templates.fasta_template import FastaTemplate


# matrix stores the result of subproblem: longest common subsequence for s[1:i+1] and t[1:j+1]
def create_matrix(s, t, n, m):
    matrix = [[0] * m for _ in range(n)]

    for i in range(1, n):
        for j in range(1, m):
            if s[i] == t[j]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

    return matrix


# backtrace dp matrix
# -> start at max value (matrix[row-1][col-1])
# -> add char at given position to result string
# -> move row up or col up depending where value came from
# -> repeat while value in matrix > 0
def backtrace_matrix(matrix, s, n, m):
    row = n - 1
    col = m - 1
    match = matrix[row][col]
    result = ''

    while match > 0:

        if matrix[row][col] > max(matrix[row-1][col], matrix[row][col-1]):
            result += s[row]
            row -= 1
            col -= 1
            match = matrix[row][col]

        elif matrix[row-1][col] == match:
            row -= 1

        elif matrix[row][col-1] == match:
            col -= 1

    return result[::-1]


def lcsq(records):
    # append '$' to front of s and t since matrix needs one extra row and extra column at position 0
    s = '$' + records[0].seq
    t = '$' + records[1].seq

    n = len(s)
    m = len(t)

    # create dp matrix
    matrix = create_matrix(s, t, n, m)

    return backtrace_matrix(matrix, s, n, m)


if __name__ == '__main__':
    FastaTemplate('rosalind_lcsq.txt').run(lcsq)