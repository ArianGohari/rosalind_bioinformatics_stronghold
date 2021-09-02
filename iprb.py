def iprb(k, m, n):
    s = k + m + n
    return k/s + m/s * (k/(s-1) + 0.75*((m-1)/(s-1)) + 0.5*(n/(s-1))) + n/s * (k/(s-1) + 0.5*(m/(s-1)))


if __name__ == '__main__':
    with open('rosalind_iprb.txt', 'r') as f:
        k, m, n = [int(element) for element in f.readline().split(' ')]
        print(iprb(k, m, n))
