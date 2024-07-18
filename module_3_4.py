#Самостоятельная работа по уроку "Произвольное число параметров".
def single_root_words(root_word, *other_words):
    global same_words
    same_words=[]
    for n_word in other_words:
        if root_word.upper() in n_word.upper() or n_word.upper() in root_word.upper():
            same_words.append(n_word)
    print(same_words)
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')