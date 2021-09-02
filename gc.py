from templates.fasta_template import FastaTemplate


def gc_content(records):
    max_gc = 0
    rec_id = None

    # iterate through records
    for record in records:

        # calc gc content of record 100 * (g count + c count) / sequence length
        gc = 100 * (record.seq.count('G') + record.seq.count('C')) / len(record.seq)

        # override max gc and id
        if gc > max_gc:
            max_gc = gc
            rec_id = record.id

    return '{}\n{}'.format(rec_id, max_gc)


if __name__ == '__main__':
    FastaTemplate('rosalind_gc.txt').run(gc_content)
