# HW 12.1. Очистити текст від html-тегів.
def clean_html_file(src_path, dst_path="cleaned.txt"):

# Функція Читає файл src_path, видаляє все між символами '<' і '>' (включно), і записує очищений текст у dst_path.

# Зчитуємо вміст файлу
    with open(src_path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()
# Видаляємо теги простим автоматом (без regex): переходимо в "режим всередині тегу" на '<' і виходимо з нього на '>'
    out_chars = []
    inside_tag = False
    for ch in text:
        if ch == '<':
            inside_tag = True
            continue
        if ch == '>':
            inside_tag = False
            continue
        if not inside_tag:
            out_chars.append(ch)

    cleaned = "".join(out_chars)

# Записуємо результат
    with open(dst_path, "w", encoding="utf-8") as f:
        f.write(cleaned)

if __name__ == "__main__":

# Приклад використання (файл draft.html має лежати поряд зі скриптом):
    clean_html_file("draft.html", "cleaned.txt")