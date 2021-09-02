from templates.fasta_template import FastaTemplate


def grph(records):
    adj_list = []

    # for each record compare with each other record
    for record1 in records:
        for record2 in records:

            # do not compare a record with itself
            if record1 is record2:
                continue

            match = True

            # match suffix of seq1 with prefix of seq 3 (3 characters)
            if record1.seq[-3:] != record2.seq[:3]:
                match = False

            # add edge to adjacency list
            if match:
                adj_list.append([record1.id, record2.id])

    # write adjacency list formatted
    ret = ''
    for edge in adj_list:
        ret += '{}\n'.format(' '.join(edge))

    return ret


if __name__ == '__main__':
    FastaTemplate('rosalind_grph.txt').run(grph)