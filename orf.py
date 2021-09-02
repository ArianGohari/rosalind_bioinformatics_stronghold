from prot import prot
from templates.fasta_template import FastaTemplate


# find all start codons in given rna sequence
def start_codons(seq):
    ret = []
    n = len(seq)

    # minimum: start codon; aa codon; stop codon -> n - 9 as last location of interest
    for i in range(n-9):

        # check for start codon
        if seq[i:i+3] == 'AUG':
            ret.append(i)

    return ret


# find next stop codon for given start codon location in given rna sequence
def next_stop_codon(seq, start):
    n = len(seq)

    # minimum: start codon; aa codon; stop codon -> n + 6 as first location of interest
    # increment 3 steps (codon) -> n - ((n - start) % 3 as last location of interest
    for i in range(start + 6, n - ((n - start) % 3), 3):
        codon = seq[i:i+3]

        # check for stop codon
        if codon == 'UAA' or codon == 'UAG' or codon == 'UGA':
            return i

    return None


def find_orfs(seq):

    # get start locations
    start_locations = start_codons(seq)

    # initialize orf locations list
    orf_locations = []

    # for each start location -> find next stop location
    for start in start_locations:
        stop = next_stop_codon(seq, start)

        # add orf location tuple (start, stop) to orf locations list
        if stop:
            orf_locations.append((start, stop))

    return orf_locations


def orf(records):

    # initialize orfs list
    orfs = []

    # read sequence from record (only one element)
    seq = records[0].seq

    # get reverse complement
    seq_rc = seq.reverse_complement()

    # transcribe to rna
    seq_rna = seq.transcribe()
    seq_rc_rna = seq_rc.transcribe()

    # find orf locations
    seq_orf_locations = find_orfs(seq_rna)
    seq_rc_orf_locations = find_orfs(seq_rc_rna)

    # for each orf location (start, stop) of seq -> translate into protein
    # -> add to orfs list
    for location in seq_orf_locations:
        start = location[0]
        stop = location[1]
        protein = prot.prot(seq_rna[start: stop + 1])
        orfs.append(protein)

    # for each orf location (start, stop) of seq_rc -> translate into protein
    # -> add to orfs list
    for location in seq_rc_orf_locations:
        start = location[0]
        stop = location[1]
        protein = prot.prot(seq_rc_rna[start: stop + 1])
        orfs.append(protein)

    # write result formatted as required
    result = ''
    for _orf in set(orfs):
        result += '{}\n'.format(_orf)

    return result


if __name__ == '__main__':
    FastaTemplate('rosalind_orf.txt').run(orf)