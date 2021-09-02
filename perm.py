# Heap's permutation algorithm
def perm_recursive(elements, n, permutations):

    if n == 1:
        permutations.append(elements.copy())

    for i in range(n):
        perm_recursive(elements, n-1, permutations)

        if n & 1:
            elements[0], elements[n-1] = elements[n-1], elements[0]
        else:
            elements[i], elements[n-1] = elements[n-1], elements[i]

    return permutations


def perm(n):
    # create elements for range 1 - n
    elements = [i for i in range(1, n + 1)]

    # calculate permutations
    permutations = perm_recursive(elements, n, [])

    # write result formatted as required
    result = ''
    result += '{}\n'.format(len(permutations))

    for permutation in permutations:
        result += '{}\n'.format(' '.join([str(i) for i in permutation]))

    return result


if __name__ == '__main__':
    with open('rosalind_perm.txt', 'r') as f:
        _n = int(f.readline())
        print(perm(_n))
