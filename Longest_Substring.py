#!usr/bin/env python
# -*- coding:utf-8 -*-

"""
Given a string, find the length of the longest substring without repeating characters.
For example, the longest substring without repeating letters for "abcabcbb" is "abc",
which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

"""
def test(s):
    start = end = 0
    s_dict = {}
    max_length = 0
    while end < len(s):
        if s[end] in s_dict and s_dict[s[end]] >= start:
            start = s_dict[s[end]] + 1
        s_dict[s[end]] = end
        end += 1
        max_length = max(max_length, end-start)
    return max_length

if __name__ == '__main__':
    print test('abba')
