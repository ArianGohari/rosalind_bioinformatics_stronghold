import math


def prob(s, a):
    result = []

    # for each given GC content in a
    for x in a:

        # split GC content into probabilities for each base
        p_for_base = {'G': x / 2, 'C': x / 2, 'A': (1 - x) / 2, 'T': (1 - x) / 2}

        # initialize p as 0 (neutral element for additions)
        p = 0

        # add log10 of calculated p-value for each base to p
        # -> p_dna = p_base_1 * p_base_2 * p_base_3 ...
        # -> logarithmic rules -> log10(p_dna) = log10(p_base_1) + log10(p_base_2) + log10(p_base_3) + ...
        for base in s:
            p += math.log10(p_for_base[base])

        # add p to result list
        result.append(str(p))

    return ' '.join(result)


if __name__ == '__main__':
    with open('rosalind_prob.txt', 'r') as f:
        _s = f.readline().rstrip()
        _a = [float(element) for element in f.readline().split(' ')]
        print(prob(_s, _a))