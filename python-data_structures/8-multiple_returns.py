#!/usr/bin/python3
def multiple_returns(sentence):

    count = 0

    if len(sentence) == 0:
        zero_tuple = (0,None)
        return zero_tuple
    else:
        len_char_tuple = (len(sentence), sentence[0])
        return len_char_tuple
