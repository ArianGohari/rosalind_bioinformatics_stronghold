from Bio import SeqIO


class FastaTemplate:
    def __init__(self, filename):
        self.records = []
        with open(filename) as handle:
            for record in SeqIO.parse(handle, "fasta"):
                self.records.append(record)

    def run(self, fun):
        print(fun(self.records))
