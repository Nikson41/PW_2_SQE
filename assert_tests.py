# Клас FakeButton імітує кнопку tkinter.
# Нам він потрібен, щоб тестувати логіку гри без запуску графічного інтерфейсу.
class FakeButton:

    # Конструктор створює кнопку та записує її текст
    # ("X", "O" або "")
    def __init__(self, text=""):
        self.data = {"text": text}

    # Дозволяє звертатися до об'єкта так само,
    # як до справжньої кнопки tkinter:
    # button["text"]
    def __getitem__(self, key):
        return self.data[key]


# Функція перевіряє, чи є на полі переможець
def check_winner(buttons):

    # Перевірка всіх рядків
    for row in buttons:

        # Якщо всі 3 клітинки рядка однакові
        # і вони не порожні - є переможець
        if row[0]["text"] == row[1]["text"] == row[2]["text"] != "":
            return True

    # Перевірка всіх стовпців
    for col in range(3):

        if buttons[0][col]["text"] == \
           buttons[1][col]["text"] == \
           buttons[2][col]["text"] != "":
            return True

    # Перевірка головної діагоналі
    if buttons[0][0]["text"] == \
       buttons[1][1]["text"] == \
       buttons[2][2]["text"] != "":
        return True

    # Перевірка побічної діагоналі
    if buttons[0][2]["text"] == \
       buttons[1][1]["text"] == \
       buttons[2][0]["text"] != "":
        return True

    # Якщо жодна умова не виконалась,
    # то переможця немає
    return False


# Функція перевіряє, чи настала нічия
def check_draw(buttons):

    # Перебираємо всі клітинки поля
    for row in buttons:
        for button in row:

            # Якщо знайдено хоча б одну порожню клітинку,
            # гра ще не завершена
            if button["text"] == "":
                return False

    # Якщо порожніх клітинок немає,
    # вважаємо, що поле повністю заповнене
    return True


# ==================================================
# ТЕСТ 1
# Перевіряємо визначення перемоги по рядку
# ==================================================

board = [

    # Перший рядок повністю складається з X
    [FakeButton("X"), FakeButton("X"), FakeButton("X")],

    [FakeButton(""), FakeButton(""), FakeButton("")],
    [FakeButton(""), FakeButton(""), FakeButton("")]
]

# Очікуємо результат True
assert check_winner(board) == True, \
    "Перемога по рядку не знайдена"


# ==================================================
# ТЕСТ 2
# Перевіряємо визначення нічиї
# ==================================================

board = [

    [FakeButton("X"), FakeButton("O"), FakeButton("X")],
    [FakeButton("O"), FakeButton("X"), FakeButton("O")],
    [FakeButton("O"), FakeButton("X"), FakeButton("O")]
]

# Поле повністю заповнене.
# Очікуємо True.
assert check_draw(board) == True, \
    "Нічия не визначена"


# ==================================================
# ТЕСТ 3
# Перевіряємо відсутність переможця
# ==================================================

board = [

    [FakeButton(""), FakeButton(""), FakeButton("")],
    [FakeButton(""), FakeButton(""), FakeButton("")],
    [FakeButton(""), FakeButton(""), FakeButton("")]
]

# Поле порожнє.
# Переможця бути не повинно.
assert check_winner(board) == False, \
    "Помилково знайдено перемогу"


# Якщо виконання дійшло сюди,
# значить усі assert-тести пройдені
print("Усі assert-тести пройдено успішно!")

