import distance
from templates.fasta_template import FastaTemplate


def lowest_hamming_dist(incorrect, corrects):
    d = len(incorrect)
    seq = None

    for correct in corrects:
        ham = distance.hamming(incorrect, correct)
        if ham <= d:
            d = ham
            seq = correct

    return seq


def corr(records):
    seqs = [record.seq for record in records]
    correct = []

    # iterate trough each seq in seqs
    for seq in seqs:

        # get reverse complement of seq
        rc = seq.reverse_complement()

        # correct if seq and reverse complement exists > 1 times in sequenced records
        if seqs.count(seq) + seqs.count(rc) > 1:
            correct.append(seq)
            correct.append(rc)
            seqs = list(filter(lambda s: s != seq and s != rc, seqs))

    # remaining seqs are incorrects
    incorrect = seqs

    # get seq with lowest hamming distance from corrects for each incorrect seq
    result = {seq: lowest_hamming_dist(seq, correct) for seq in incorrect}

    # return result formatted as required
    return '\n'.join(['{}->{}'.format(key, value) for (key, value) in result.items()])


if __name__ == '__main__':
    FastaTemplate('rosalind_corr.txt').run(corr)
