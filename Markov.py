"""You are to produce a random text generator using markov chains. We've provided a very bare
freeform manner, just writing code at the 'top level', the same place where we put our global 
variables. This is generally considered bad form. Code should always be contained in functions 
or class methods wherever possible.
The skeleton program we've provided has a recommended set of functions to start with, 
including a very odd if statement at the bottom. You can ignore how this statement works
 for now, all it does is it makes sure your program starts inside the main() function.
The program should accept a filename from the command line, and a sample run should look 
similar to the following""" 


#import
#open/file 


import sys

test_string = """O life of this our spring! why fades the lotus of the water?
Why fade these children of the spring? born but to smile & fall.
Ah! Thel is like a watry bow, and like a parting cloud,
Like a reflection in a glass, like shadows in the water,
Like dreams of infants, like a smile upon an infant's face,
Like the dove's voice, like transient day, like music in the air:
Ah! gentle may I lay me down, and gentle rest my head,
And gentle sleep the sleep of death, and gentle hear the voice
Of him that walketh in the garden in the evening time."""

def make_san_list(corpus):
    word_list = corpus.split()
    san_list = []
    for word in word_list:
        san_list.append(word.strip('.,"[]'))
    return san_list

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    #use a for loop
    #make dict
    # look at word 1 and word 2 
    # if word 1 and 2 does not exist in the {} already, then add a key with a value of word three 
    #in the list

    # Here's the general syntax that the loop over the text_list will take:
    # for i in range(len(list) - 2):
        # key = (a_list[i], a_list[i + 1])
        # value = list[i + 2]
    san_list = make_san_list(corpus)

    chain_dict = {}
    for i in range(len(san_list) -2):
        temp_key = (san_list[i], san_list[i+1]) 
        temp_value = san_list[i+2]

        if chain_dict.get(temp_key) == None:
            chain_dict[temp_key] = [temp_value]
        else:
            chain_dict[temp_key].append(temp_value)
    return chain_dict

#TODO punctuation 


def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    # grab a random key... or something, and assign it to curr_key
    # initialize a list with two elements, curr_key[0] and curr_key[1]
    # NOW THE LOOP BEGINS!
    # look up curr_key and get the value
    # the value is a list. We need to select a random element from that list.
    # we will call this random value rand_val
    # we append rand_val to our starter list
    # we reassign curr_key to (curr_key[1], value)
    # in effect we're shifting our focus over one word, every iteration of the loop
    # NOW THE LOOP ENDS!
    # we join the list to make a giant, wonderful, fluffy text string.
    # TODO figure out how the fuck random works
    # TODO figure out how the fuck where we end the loop (probably punctuation)
    return "Here's some random text."






# def main():
#     args = sys.argv

#     # Change this to read input_text from a file
#     input_text = "Some text"

#     chain_dict = make_chains(input_text)
#     random_text = make_text(chain_dict)
#     print random_text

# if __name__ == "__main__":
#     main()