masses = {
    71.03711: 'A',
    103.00919: 'C',
    115.02694: 'D',
    129.04259: 'E',
    147.06841: 'F',
    57.02146: 'G',
    137.05891: 'H',
    113.08406: 'I',
    128.09496: 'K',
    131.04049: 'M',
    114.04293: 'N',
    97.05276: 'P',
    128.05858: 'Q',
    156.10111: 'R',
    87.03203: 'S',
    101.04768: 'T',
    99.06841: 'V',
    186.07931: 'W',
    163.06333: 'Y',
}


def spec(weigths):
    n = len(weigths)
    s = ''

    for i in range(n-1):
        delta = float('%.5f' % (weigths[i+1] - weigths[i]))
        s = s + masses[delta]

    return s


if __name__ == '__main__':
    with open('rosalind_spec.txt', 'r') as f:
        _weights = [float(line) for line in f.readlines()]
        print(spec(_weights))
