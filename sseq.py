from templates.fasta_template import FastaTemplate


# Simple linear algorithm
def sseq(records):
    s = records[0].seq
    t = records[1].seq

    n = len(s)
    m = len(t)

    i = 0
    j = 0

    indices = []

    while True:

        # if subsequence element found at i: append i to indices list, increment j
        if s[i] == t[j]:
            indices.append(i + 1)
            j += 1

        # increment i every iteration
        i += 1

        # interrupt loop if either i or j has reached maximum
        if i == n or j == m:
            break

    return ' '.join([str(i) for i in indices])


if __name__ == '__main__':
    FastaTemplate('rosalind_sseq.txt').run(sseq)