def backtrace_dp_list(pi, dp_list):
    result = []
    for max_length in reversed(range(1, max(dp_list) + 1)):
        k = len(dp_list) - list(reversed(dp_list)).index(max_length) - 1
        result.append(pi[k])
        dp_list = dp_list[0:k]

    return reversed(result)


def lgis_dp(n, pi):
    dp_list = [1] * n

    for i in range(1, n):
        dp_list[i] = 1 + max(
            (dp_list[j] for j in range(i) if pi[i] > pi[j]), default=0)

    return backtrace_dp_list(pi, dp_list)


def lgds_dp(n, pi):
    dp_list = [1] * n

    for i in range(1, n):
        dp_list[i] = 1 + max(
            (dp_list[j] for j in range(i) if pi[i] < pi[j]), default=0)

    return backtrace_dp_list(pi, dp_list)


def lgis(n, pi):
    # get longest increasing subsequence
    longest_increasing_subsequence = lgis_dp(n, pi)

    # get longest decreasing subsequence
    longest_decreasing_subsequence = lgds_dp(n, pi)

    # write result formatted as required
    result = ''
    result += '{}\n'.format(' '.join([str(element) for element in longest_increasing_subsequence]))
    result += '{}\n'.format(' '.join([str(element) for element in longest_decreasing_subsequence]))

    return result


if __name__ == '__main__':
    with open('rosalind_lgis.txt', 'r') as f:
        _n = int(f.readline())
        _pi = [int(i) for i in f.readline().split(' ')]
        print(lgis(_n, _pi))
