import sys
import math
import string


def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    # Implementing vectors e,s as lists (arrays) of length 26
    # with p[0] being the probability of 'A' and so on
    e = [0] * 26
    s = [0] * 26

    with open('e.txt', encoding='utf-8') as f:
        for line in f:
            # strip: removes the newline character
            # split: split the string on space character
            char, prob = line.strip().split(" ")
            # ord('E') gives the ASCII (integer) value of character 'E'
            # we then subtract it from 'A' to give array index
            # This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char) - ord('A')] = float(prob)
    f.close()

    with open('s.txt', encoding='utf-8') as f:
        for line in f:
            char, prob = line.strip().split(" ")
            s[ord(char) - ord('A')] = float(prob)
    f.close()

    return (e, s)


def shred(filename):
    # Using a dictionary here. You may change this to any data structure of
    # your choice such as lists (X=[]) etc. for the assignment
    X = dict.fromkeys(string.ascii_uppercase, 0)
    with open(filename, encoding='utf-8') as f:
        for line in f:
            for letter in line:
                if letter.isalpha():
                    X[letter.upper()] += 1

    return X


def x_log_p(i,p):
    return round(letter_dict[chr(i+65)] * math.log(p[i]),4)


# Q1
print("Q1")
letter_dict = shred("samples/letter1.txt") # TODO: Change this to letter.txt when submit
for key in letter_dict.keys():
    print(f"{key} {letter_dict[key]}")

# Q2
print("Q2")
vec = get_parameter_vectors()
e_list = vec[0]
s_list = vec[1]
print(f"{x_log_p(0,e_list)}")
print(f"{x_log_p(0,s_list)}")
