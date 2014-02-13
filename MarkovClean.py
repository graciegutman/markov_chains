import sys

import random

from string import join

import auth

import twitter 

def make_list(corpus):
    word_list = corpus.split()
    san_list = []
    for word in word_list:
        san_list.append(word.strip('_--+=[]{}<>()'))
    return san_list

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

def select_starter(chains):
    """loop infinitely until we get to a key that starts with a capital letter"""
    while True:
        curr_key = random.choice(chains.keys())
        if curr_key[0].istitle():
            return curr_key

def char_len_check(sentence):
    """Returns True if sentence is under 140 characters"""
    count = 0
    for letter in sentence:
        count += 1
    if count < 141:
        return True
    return False

def has_punctuation(word):
    """If last character of a value matches ?, !, ., return False"""
    if word[-1] in ["?", "!", "."]:
        return False
    return True

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    curr_key = select_starter(chains)
    curr_list = [curr_key[0], curr_key[1]]
    val_word = curr_key[1]

    while has_punctuation(val_word):
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
    """Runs main control flow"""
    args = sys.argv
    filename = args[1]
    input_text = open(filename).read()

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    while not char_len_check(random_text):
       random_text = make_text(chain_dict)
    return random_text

if __name__ == "__main__":
    main()


def tweet():  
    api = twitter.Api(consumer_key=auth.twitter_key,
                     consumer_secret=auth.api_secret,
                     access_token_key=auth.access_token,
                     access_token_secret=auth.access_token_secret)
    
    while True:
        potential_tweet = main()
        print potential_tweet
        print "Do you want to tweet this?"
        answer = raw_input("y/n? \n")
        if answer == "y":
            api.PostUpdates(potential_tweet)
        elif answer == "q":
            print "quitting"
            return

tweet()




