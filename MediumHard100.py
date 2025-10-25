# # Q1 Read a text file and count occurrences of each word using regex and Counter.
# import re 
# from collections import Counter 
# def word_count(filepath): 
#     with open(filepath, 'r',encoding='utf-8') as f: 
#         text = f.read().lower() 
#         words = re.findall(r'\b\w+\b', text)
#     return Counter(words) 
# if __name__ == '__main__': 
#     with open('sample.txt','w') as f:
#     f.write('Hello hello world test world') 
#     print(word_count('sample.txt'))

# # Q2  Palindrome Checker
# def is_palindrome(s): 
#     s = ''.join(ch.lower() for ch in s if ch.isalnum()) 
#         return s == s[::-1] 
# if __name__ == '__main__': 
#     print(is_palindrome('A man a plan a canal Panama'))

#Q3 Fibonacci Series
# def fib(n): 
#     if n <= 1: 
#         return n 
#     return fib(n-1) + fib(n-2) 
# if __name__ == '__main__': 
#     n = 10 
#     print([fib(i) for i in range(n)])

# Q4 Email Validator
# import re 
# def valid_email(email): 
#     return bool(re.match(r'^[\w.-]+@[\w.-]+\.\w+$', email)) 

# if __name__ == '__main__': 
#     print(valid_email('test@example.com'))