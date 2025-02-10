s1 = "here-come-the-dots-followed-by-dashes"
def convert(x):
    s = [x for x in s1.split('-')]
    print(s)
    b = s.sort()
    d = '-'.join(s)
    print(d)

a = convert(s1)