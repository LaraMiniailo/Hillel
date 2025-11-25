example_hw62 = [0, 224930, 466289, 950400, 1209600, 1900800, 8639999, 22493, 7948799]

# Рахуємо кількість секунд у днях, годинах, хвилинах
for total_seconds in example_hw62:
    days, rem = divmod(total_seconds, 24 * 60 * 60)  # 86400
    hours, rem = divmod(rem, 60 * 60)                # 3600
    minutes, seconds = divmod(rem, 60)

    # Підбір правильної форми "день"
    last_two = days % 100
    last_one = days % 10

    if 11 <= last_two <= 14:
        day_word = "днів"
    elif last_one == 1:
        day_word = "день"
    elif last_one in (2, 3, 4):
        day_word = "дні"
    else:
        day_word = "днів"

    print(f"{total_seconds} -> {days} {day_word}, "
          f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
