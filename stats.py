letter_num = {}
dict_order = []

def word_count(book):
    count = len(book.split())
    return count

def letter_count(book):
    lower = book.lower()
    letter_list = [
        letter 
        for word in lower 
        for letter in word
    ]
    for i in letter_list:
        letter_num[i] = letter_num.get(i, 0) + 1
    return letter_num

def sort_on(count):
    return count["num"]

def order_letters(letter_dict):
    dict_order = [
        {"char": alpha, "num": value} 
        for alpha, value in letter_dict.items() 
        if alpha.isalpha()
    ]
    dict_order.sort(key=sort_on, reverse=True)
    return dict_order