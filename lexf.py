
def lexf_recursive(alphabet, n, s):

    # for each position < n, letter can be any element of given alphabet
    # -> there are |alphabet|^n possible strings
    #
    # every string of length using given alphabet is a leaf of a tree of height n
    # with |alphabet| new branches at each level
    # -> build every possible string using a recursive approach (walking down the tree)
    if n > 0:
        strings = []
        for a in alphabet:
            new_s = s + a
            strings += lexf_recursive(alphabet, n-1, new_s)

        return strings

    else:
        return [s]


def lexf(alphabet, n):

    # get all possible strings of length n using given alphabet
    strings = lexf_recursive(alphabet, n, '')

    # write result formatted as required
    result = ''
    for s in strings:
        result += '{}\n'.format(s)

    return result


if __name__ == '__main__':
    with open('rosalind_lexf.txt', 'r') as f:
        _alphabet = f.readline().rstrip().replace(' ', '')
        _n = int(f.readline())
        print(lexf(_alphabet, _n))
