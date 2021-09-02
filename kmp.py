from templates.fasta_template import FastaTemplate


def kmp(records):
    seq = records[0].seq
    n = len(seq)

    p = [0 for _ in range(n)]

    for i in range(1, n):
        j = p[i - 1]
        while j > 0 and seq[i] != seq[j]:
            j = p[j - 1]
        if seq[i] == seq[j]:
            j += 1
        p[i] = j

    return ' '.join([str(element) for element in p])


if __name__ == '__main__':
    FastaTemplate('rosalind_kmp.txt').run(kmp)