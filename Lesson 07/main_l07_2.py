#HW 7.2 Модифікація рядка

text = "greetings, friends."
def correct_sentence(text: str) -> str:
    text = text[:1].upper() + text[1:]
    return text if text.endswith('.') else text + '.'

print(correct_sentence(text))

text = "hello"
def correct_sentence(text: str) -> str:
    text = text[:1].upper() + text[1:]
    return text if text.endswith('.') else text + '.'

print(correct_sentence(text))

text = "greetings, Friends"
def correct_sentence(text: str) -> str:
    text = text[:1].upper() + text[1:]
    return text if text.endswith('.') else text + '.'

print(correct_sentence(text))

text = "Greetings, friends"
def correct_sentence(text: str) -> str:
    text = text[:1].upper() + text[1:]
    return text if text.endswith('.') else text + '.'

print(correct_sentence(text))

ext = "greetings, friends"
def correct_sentence(text: str) -> str:
    text = text[:1].upper() + text[1:]
    return text if text.endswith('.') else text + '.'

print(correct_sentence(text))

print('==========================================================')
print('Ok')