import math


# number of permutations for n and k: n! / (n-k)!
def pper(n, k):
    return int((math.factorial(n) / math.factorial(n-k)) % 1000000)


if __name__ == '__main__':
    with open('rosalind_pper.txt', 'r') as f:
        n, k = [int(element) for element in f.readline().split(' ')]
        print(pper(n, k))
