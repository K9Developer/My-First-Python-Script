import re
import wrs
from colored import Text

def string_len(string, show_string=False):
    string1 = str(string)
    uni_list = []
    str_list = []
    """ indexes = []
    indexes = [i for i in range(len(string1)) if string1.startswith(' ', i)]
    #print(indexes)"""
    uni_list = split_and_keep_delimiter(string1, " ")
    uni_list_decoded = split_and_keep_delimiter(string1, " ")
    str_list = split_and_keep_delimiter(string1, " ")

    for ii,value in enumerate(uni_list):
        if value.find('\u205f') == -1:
            char_list = list(value)
            for i,char in enumerate(value):

                char_list[i] = "Ø"

            value1 = ""
            for char in char_list:
                value1 = value1 + char
            uni_list[ii] = value1


    for ii, value in enumerate(str_list):
        for ii, value in enumerate(str_list):
            if value.find('\u205f') != -1:
                char_list = list(value)
                for i, char in enumerate(value):
                    char_list[i] = "Ø"

                value1 = ""
                for char in char_list:
                    value1 = value1 + char
                str_list[ii] = value1


    for value in str_list:
        num = 0
        for char in value:
            if char == "Ø":
                num  = num + 1

        if show_string == False:
            if num == len(value):
                num = 0
                continue
            else:

                return len(value)
        elif show_string == True:
            if num == len(value):
                num = 0
                continue
            else:
                string1 = ""

                string1 = ' '.join(uni_list_decoded)
                string1.replace("\u205f", "")

                string1 = list(string1)
                for i,val in enumerate(string1):
                    if val == "\u205f":
                        for b, j in enumerate(string1):
                            if j == ' ':
                                string1[b] = ""
                                break
                for i,val in enumerate(string1):
                    if " " in val or "\u205f" in val:
                        string1[i] = ""
                string1 = ''.join(string1)

                return string1




def split_and_keep_delimiter(input, delimiter):
    result      = list()
    idx         = 0
    while delimiter in input:
        idx     = input.index(delimiter);
        result.append(input[0:idx+len(delimiter)])
        input = input[idx+len(delimiter):]
    result.append(input)
    return result
