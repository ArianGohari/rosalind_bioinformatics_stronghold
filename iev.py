def iev(a):
    n = len(a)
    probs = [1, 1, 1, 0.75, 0.5, 0]
    sum = 0

    for i in range(n):
        sum += (a[i] * probs[i])

    return sum * 2


if __name__ == '__main__':
    with open('rosalind_iev.txt', 'r') as f:
        _a = [int(element) for element in f.readline().split(' ')]
        print(iev(_a))