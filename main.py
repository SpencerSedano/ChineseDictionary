with open('cedict_ts.u8', encoding="utf8") as file:
    text = file.read()
    lines = text.split('\n')
    dict_blocks = list(lines)

print(dict_blocks[468])

def dictionary(word):
    user_input = input("Write a word: ")
    pass