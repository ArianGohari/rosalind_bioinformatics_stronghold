def subs(s, t):
    n = len(s)
    k = len(t)
    locations = []

    # iterate through s and match s[i: i+k] with p
    for i in range(n-k):
        if s[i:i+k] == t:
            locations.append(i + 1)

    return locations


if __name__ == '__main__':
    with open('rosalind_subs.txt', 'r') as f:
        s = f.readline().strip()
        t = f.readline().strip()
        locs = subs(s, t)
        print(' '.join([str(location) for location in locs]))
