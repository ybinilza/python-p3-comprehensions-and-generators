#!/usr/bin/env python3

def return_evens(num_list):
    even_nos=list();
    for n in num_list:
        if n%2 ==0:
            even_nos.append(n);
    return even_nos;
    

def make_exclamation(sentence_list):
    new_sentance_list=list();
    i=0
    if(len(sentence_list)==0):
        return new_sentance_list;
    for n in sentence_list:
        n=n+"!"
        sentence_list[i]=n;
        i=i+1;
    return sentence_list;

