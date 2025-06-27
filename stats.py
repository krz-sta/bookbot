def get_num_words(text):
    return len(text.split())

def count_characters(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    dicts_list = []
    new_dict= {}
    for key in dict:
        if not key.isalpha():
            continue
        new_dict = {"char": key, "num":dict[key]}
        dicts_list.append(new_dict)
    dicts_list.sort(reverse=True, key=sort_on)
    return dicts_list