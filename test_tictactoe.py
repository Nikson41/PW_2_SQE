# Підключаємо стандартний модуль тестування Python
import unittest


# Імітація кнопки tkinter
class FakeButton:

    def __init__(self, text=""):
        self.data = {"text": text}

    def __getitem__(self, key):
        return self.data[key]


# Перевірка перемоги
def check_winner(buttons):

    # Перевірка рядків
    for row in buttons:
        if row[0]["text"] == row[1]["text"] == row[2]["text"] != "":
            return True

    # Перевірка стовпців
    for col in range(3):
        if buttons[0][col]["text"] == \
           buttons[1][col]["text"] == \
           buttons[2][col]["text"] != "":
            return True

    # Головна діагональ
    if buttons[0][0]["text"] == \
       buttons[1][1]["text"] == \
       buttons[2][2]["text"] != "":
        return True

    # Побічна діагональ
    if buttons[0][2]["text"] == \
       buttons[1][1]["text"] == \
       buttons[2][0]["text"] != "":
        return True

    return False


# Перевірка нічиєї
def check_draw(buttons):

    for row in buttons:
        for button in row:

            # Якщо знайдена порожня клітинка,
            # нічия ще не настала
            if button["text"] == "":
                return False

    return True


# Клас з набором тестів
class TestTicTacToe(unittest.TestCase):

    # ---------------------------------------------
    # Тест 1
    # Перевірка перемоги по рядку
    # ---------------------------------------------
    def test_row_winner(self):

        board = [

            [FakeButton("X"), FakeButton("X"), FakeButton("X")],

            [FakeButton(""), FakeButton(""), FakeButton("")],
            [FakeButton(""), FakeButton(""), FakeButton("")]
        ]

        # Перевіряємо, що функція повертає True

        self.assertTrue(check_winner(board))

    # ---------------------------------------------
    # Тест 2
    # Перевірка визначення нічиєї
    # ---------------------------------------------
    def test_draw(self):

        board = [

            [FakeButton("X"), FakeButton("O"), FakeButton("X")],
            [FakeButton("O"), FakeButton("X"), FakeButton("O")],
            [FakeButton("O"), FakeButton("X"), FakeButton("O")]
        ]

        # Очікуємо True
        self.assertTrue(check_draw(board))

    # ---------------------------------------------
    # Тест 3
    # Перевірка відсутності переможця
    # ---------------------------------------------
    def test_no_winner(self):

        board = [

            [FakeButton(""), FakeButton(""), FakeButton("")],
            [FakeButton(""), FakeButton(""), FakeButton("")],
            [FakeButton(""), FakeButton(""), FakeButton("")]
        ]

        # Очікуємо False,
        # оскільки поле порожнє
        self.assertFalse(check_winner(board))


# Точка входу в програму
if __name__ == "__main__":

    # Запуск усіх тестів класу TestTicTacToe
    unittest.main()
    