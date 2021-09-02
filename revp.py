from templates.fasta_template import FastaTemplate


def revp(records):
    reverse_palindromes = []

    # get sequence (only one record)
    seq = records[0].seq
    n = len(seq)

    # iterate over every k of given range (4-12)
    for k in range(4, 13):
        for i in range(n-k+1):

            # get kmer
            kmer = seq[i:i+k]

            # check if kmer is reverse palindrome (kmer == reverse_complement)
            # -> add to reverse_palindromes list
            if kmer == kmer.reverse_complement():
                reverse_palindromes.append((i + 1, k))

    # write result formatted as required
    result = ''
    for reverse_palindrome in reverse_palindromes:
        result += '{}\n'.format(' '.join(str(i) for i in reverse_palindrome))

    return result


if __name__ == '__main__':
    FastaTemplate('rosalind_revp.txt').run(revp)