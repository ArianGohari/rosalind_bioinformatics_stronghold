import re

from Bio import SeqIO
from io import StringIO
import requests


def mprt(ids):
    pattern = 'N(?![P])[A-Z][ST](?![P])[A-Z]'
    result = {}

    # iterate through protein ids
    for prot in ids:

        # get fasta from uniprot
        url = 'http://www.uniprot.org/uniprot/{}.fasta'.format(prot)
        raw_fasta = requests.get(url).text
        fasta_iterator = SeqIO.parse(StringIO(raw_fasta), "fasta")

        # iterate through received fastas
        for fasta in fasta_iterator:
            name, seq = fasta.id, str(fasta.seq)
            n = len(seq)

            # find pattern matches in protein sequence
            matches = []
            for i in range(n-4):
                if re.match(pattern, seq[i:i+4]):
                    matches.append(i+1)

            # if matches found -> add to result dict
            if matches:
                result[prot] = matches

    # write result formatted
    result_str = ''
    for prot in result.keys():
        result_str += '{}\n'.format(prot)
        result_str += '{}\n'.format(' '.join([str(location) for location in result[prot]]))

    return result_str


if __name__ == '__main__':
    with open('rosalind_mprt.txt', 'r') as f:
        lines = f.readlines()
        ids = [line.rstrip() for line in lines]
        print(mprt(ids))