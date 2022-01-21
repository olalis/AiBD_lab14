from textblob import TextBlob
from typing import List
from copy import deepcopy

def hello(name):
    output = f'Hello {name}'
    return output


def extract_sentiment(text):
    text = TextBlob(text)

    return text.sentiment.polarity


def text_contain_word(word: str, text: str):
    
    return word in text


def bubble_sort(tab: List):
    n = len(tab)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]

    return tab


print(bubble_sort([4, 3, 2, 1, 3, 0]))