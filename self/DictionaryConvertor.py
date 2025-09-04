def dictconvertor(lst1,lst2):
    dict = {}
    for key , value in zip(lst1,lst2):
        dict[key] = value
    return dict