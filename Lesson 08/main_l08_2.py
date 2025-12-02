# HW 8.2. Паліндром.

# Варіант 1: Перевіряємо паліндромз урахуванням регвстра і знаків.
def is_palindrome_manual_v1(s):
    #   Проверяет, является ли строка палиндромом, посимвольно сравнивая.

    s_str = str(s)
    n = len(s_str)
    for i in range(n // 2):
        if s_str[i] != s_str[n - 1 - i]:
            return False
    return True


# Варіант 2: Перевіряємо паліндромз ігноруя регистр та пробіли і знаки.

def is_palindrome_manual_v2(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


print(is_palindrome_manual_v1('A man, a plan, a canal: Panama'))
print(is_palindrome_manual_v1('0P'))
print(is_palindrome_manual_v1('a.'))
print(is_palindrome_manual_v1('aurora'))

print('')
print('==============================')
print('')

print(is_palindrome_manual_v2('A man, a plan, a canal: Panama'))
print(is_palindrome_manual_v2('0P'))
print(is_palindrome_manual_v2('a.'))
print(is_palindrome_manual_v2('aurora'))
