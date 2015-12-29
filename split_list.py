def split_list(lists, nums):
    return [lists[i:i+nums] for i in xrange(0, len(lists), nums)]

if __name__ == '__main__':
    print split_list([1,2,3,4], 2)
