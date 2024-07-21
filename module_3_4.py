# Самостоятельная работа по уроку "Произвольное число параметров".


def same_root_words(root_word: str, *other_words):
    # current_word = root_word
    same_words = []
    for current_word in other_words:
        # print(root_word.upper() in current_word.upper() or current_word.upper() in root_word.upper(), 'current: ',
        #       current_word)
        if root_word.upper() in current_word.upper() or current_word.upper() in root_word.upper():
            same_words.append(current_word)
    return same_words


result1 = same_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = same_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(f'result1: {result1}')
print(f'result2: {result2}')
