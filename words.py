"""
To get and filter words for decoding
"""

def load_words(file_name):
    in_file = open(file_name, 'r')
    line = in_file.readline()
    word_list = line.split()
    in_file.close()
    return word_list


def filter_len(words, max_len=4, min_len=4):
    return list(filter(lambda x: min_len <= len(x) <= max_len, words))
