# HW 10.2. Знайти перше слово

def first_word(text: str) -> str:
    # Забираємо зайві символи на початку
    text = text.lstrip(" .,")

    word = ""
    for ch in text:
        if ch.isalpha() or ch == "'":   # літера або апостроф
            word += ch
        else:
            break   # кінець першого слова
    return word

print (first_word("Hello world"))
print (first_word("greetings, friends"))
print (first_word("don't touch it"))
print (first_word(".., and so on ..."))
print (first_word("hi"))
print (first_word("Hello.World"))