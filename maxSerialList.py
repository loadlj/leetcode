def max_list(_list):
    _max = _sum = 0
    for i in _list:
        _sum += i
        if _sum > _max:
            _max = _sum
        elif _sum < 0:
            _sum = 0
    return _max


if __name__ == '__main__':
    print max_list([1, 2, -3, 4, -1])
