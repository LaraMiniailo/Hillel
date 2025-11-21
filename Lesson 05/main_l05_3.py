import string

text = input("Введіть рядок: ")

# 1. Прибираємо пунктуацію і пробіли
cleaned = ""
for ch in text:
    if ch not in string.punctuation and not ch.isspace():
        cleaned += ch

# 2. Розбиваємо початковий текст на слова (по пробілах)  і робимо ПершеСловоЗВеликої
words = []
for word in text.split():
    # Прибираємо пунктуацію з кожного слова
    w = "".join(ch for ch in word if ch not in string.punctuation)
    if w:
        words.append(w.capitalize())

# 3. Формуємо hashtag
hashtag = "#" + "".join(words)

# 4. Якщо довше 140 – обрізаємо
if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)
