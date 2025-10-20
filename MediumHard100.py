# Q1 Read a text file and count occurrences of each word using regex and Counter.
import re 
from collections import Counter 
def word_count(filepath): 
    with open(filepath, 'r',encoding='utf-8') as f: 
        text = f.read().lower() 
        words = re.findall(r'\b\w+\b', text)
    return Counter(words) 
if __name__ == '__main__': 
    with open('sample.txt','w') as f:
    f.write('Hello hello world test world') 
    print(word_count('sample.txt'))

# Q2  