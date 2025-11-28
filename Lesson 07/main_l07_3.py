# HW 7.3. Пошук підрядка.

from typing import Optional

text = "stress"
def second_index(haystack: str, needle: str) -> Optional[int]:
    if not needle:
        return None  # не шукаємо порожній підрядок
    first = haystack.find(needle)
    if first == -1:
        return None
    second = haystack.find(needle, first + 1)
    return None if second == -1 else second

print(second_index(text, "s"))
print(second_index(text, "e"))