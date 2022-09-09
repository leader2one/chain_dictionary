def find_chain_end(i: str, d: dict):
    if i not in d:
        return i
    else:
        return find_chain_end(d[i], d)


def solve(string: str, d: dict):
    decoded_string = ''
    for i in string:
        chain_end = find_chain_end(i, d)
        decoded_string += chain_end
    return decoded_string


if __name__ == '__main__':
    s = "abcd"
    # result = zzzl
    d = {
        'a': 'b',
        'b': 'c',
        'c': 'z',
        'd': 'l'
    }
    print(solve(s, d))

