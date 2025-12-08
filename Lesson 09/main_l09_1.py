# HW 9.1. Визначити популярність певних слів у тексті


def popular_words(text: str, words: list) -> dict:
    # привести текст до нижнього регістру
    text_lower = text.lower().split()

    # рахуємо входження слів
    result = {}
    for w in words:
        result[w] = text_lower.count(w)
    return result

text = """When I was One I had just begun When I was Two I was nearly new"""

words = ['i', 'was', 'three', 'near']

print(popular_words(text, words))





