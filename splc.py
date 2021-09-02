from templates.fasta_template import FastaTemplate


def splc(records):

    # get length of records
    n_records = len(records)

    # first record is raw dna string
    s = records[0].seq

    # following records are introns
    introns = [records[i].seq for i in range(1, n_records)]

    # cut out introns from dna string
    for intron in introns:
        s = s.replace(intron, '')

    # return resulting protein
    return s.transcribe().translate()[:-1]


if __name__ == '__main__':
    FastaTemplate('rosalind_splc.txt').run(splc)