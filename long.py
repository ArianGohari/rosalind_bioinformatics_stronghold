from templates.fasta_template import FastaTemplate


# calculate edge with highest overlap
# return edge and overlap
def calc_highest_overlap(seqs, n):
    highest_overlap = 0
    highest_overlap_edge = None

    for i in range(n):
        for j in range(n):
            if i != j:
                seq1 = seqs[i]
                seq2 = seqs[j]
                overlap = 0

                for k in range(1, min(len(seq1), len(seq2))+1):
                    if seq1[-k:] == seq2[:k]:
                        overlap = k

                if overlap > highest_overlap:
                    highest_overlap = overlap
                    highest_overlap_edge = (i, j)

    return highest_overlap_edge, highest_overlap


def long(records):
    seqs = [record.seq for record in records]
    n = len(seqs)

    # simple greedy alg: n-1 times, calculate edge with highest overlap -> merge seqs
    for x in range(n-1):
        edge_to_merge, overlap = calc_highest_overlap(seqs, n)
        i, j = edge_to_merge
        seqs[i] = seqs[i] + seqs[j][overlap:]
        seqs.remove(seqs[j])
        n = len(seqs)

    return seqs[0]


if __name__ == '__main__':
    FastaTemplate('rosalind_long.txt').run(long)
