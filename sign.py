
# idea: each permutation of length n is a leaf of a tree with '' as root and a new branch for
# each remaining element from elements list
# -> find all leaves using recursion
def sign_rec(perm, elements, result, n):
    if len(perm) < n:
        for element in elements:
            if not perm.count(str(0 - element)):
                remaining_elements = elements.copy()
                remaining_elements.remove(element)
                result = sign_rec(perm.copy() + [str(element)], remaining_elements, result, n)

    elif len(perm) == n:
        result.append(perm)

    return result


def sign(n):
    # signed elements -> elements for range -n, n + 1 without 0
    elements = [i for i in range(-n, n + 1)]
    elements.remove(0)

    permutations = sign_rec([], elements, [], n)

    # write result formatted as required
    result = ''
    result += '{}\n'.format(len(permutations))

    for permutation in permutations:
        result += '{}\n'.format(' '.join([str(i) for i in permutation]))

    return result


if __name__ == '__main__':
    with open('rosalind_sign.txt', 'r') as f:
        _n = int(f.readline())
        print(sign(_n))
