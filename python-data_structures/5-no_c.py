#!/usr/bin/python3
def no_c(my_string):
    translate_table = str.maketrans('','', 'cC')
    translated_string = my_string.translate(translate_table)
    return translated_string
