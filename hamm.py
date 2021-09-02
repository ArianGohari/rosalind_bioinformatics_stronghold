def hamm(seq1, seq2):
    n = len(seq1)
    ret = 0

    for i in range(n):
        if seq1[i] != seq2[i]:
            ret += 1

    return ret


if __name__ == '__main__':
    f = open("rosalind_hamm.txt", "r")
    print(hamm(f.readline(), f.readline()))
