import sys

import random

from string import join

def make_list(corpus):
    word_list = corpus.split()
    return word_list

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
   
    san_list = make_list(corpus)

    chain_dict = {}
    for i in range(len(san_list) -2):
        temp_key = (san_list[i], san_list[i+1]) 
        temp_value = san_list[i+2]

        if chain_dict.get(temp_key) == None:
            chain_dict[temp_key] = [temp_value]
        else:
            chain_dict[temp_key].append(temp_value)
    return chain_dict


def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    curr_key = random.choice(chains.keys())
    curr_list = [curr_key[0], curr_key[1]]
    val_word = curr_key[1]

    while "." not in val_word and "!" not in val_word and "?" not in val_word:
    # look up curr_key and get the value
        val_list = chains.get(curr_key)
    # if the selected value is the end of the text, value will be None type, 
    # and should break
        if val_list == None:
            break
        else:
            index = random.randint(0, len(val_list)-1)
        val_word = val_list[index]
        curr_list.append(val_word)
        curr_key = (curr_key[1], val_word)
    sentence = join(curr_list)
    return sentence 

def main():
     args = sys.argv
     filename = args[1]
     input_text = open(filename).read()

     chain_dict = make_chains(input_text)
     random_text = make_text(chain_dict)
     print random_text

if __name__ == "__main__":
    main()