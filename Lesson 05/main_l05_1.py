import string
import keyword
# Список для перевірки
names = ["_","__","___","x","get_value","get value","get!value","some_super_puper_value","Get_value","get_Value","getValue","3m","m3","assert","assert_exception"]
# Пунктуація, яку забороняємо
banned = set(string.punctuation) - {"_"}

for name in names:
    is_valid = True

    if not  name:
        is_valid =  False

    elif name in keyword.kwlist:
        is_valid = False

    elif name[0].isdigit():
        is_valid = False

    elif name.count("_") > 1:
        is_valid = False

    else:
        for ch in name:
            if ch.isupper() or ch.isspace() or ch in banned:
                is_valid = False

            print(name, "=>", is_valid)
            break


