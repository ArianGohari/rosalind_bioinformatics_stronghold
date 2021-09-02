# each string is a node of a tree with empty string as root and a branch for each element in alphabet
# -> find all strings using a recursive approach
def lexv_recursive(a, n, current_string):
    strings = []

    # iterate through alphabet, append char to current word, recursively repeat until word has length n
    for char in a:
        word = current_string + char
        strings.append(word)

        if len(word) < n:
            strings += lexv_recursive(a, n, word)

    return strings


def lexv(a, n):
    strings = lexv_recursive(a, n, '')
    return '\n'.join(strings)


if __name__ == '__main__':
    with open('rosalind_lexv.txt', 'r') as f:
        _a = f.readline().rstrip().split(' ')
        _n = int(f.readline())
        print(lexv(_a, _n))
