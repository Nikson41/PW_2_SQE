import pytest


# Імітація кнопки tkinter
class FakeButton:

    def __init__(self, text=""):
        self.data = {"text": text}

    def __getitem__(self, key):
        return self.data[key]


# Функція перевірки переможця
def check_winner(buttons):

    for row in buttons:
        if row[0]["text"] == row[1]["text"] == row[2]["text"] != "":
            return True

    for col in range(3):
        if buttons[0][col]["text"] == \
           buttons[1][col]["text"] == \
           buttons[2][col]["text"] != "":
            return True

    if buttons[0][0]["text"] == \
       buttons[1][1]["text"] == \
       buttons[2][2]["text"] != "":
        return True

    if buttons[0][2]["text"] == \
       buttons[1][1]["text"] == \
       buttons[2][0]["text"] != "":
        return True

    return False


# =====================================================
# ФУНКЦІЯ ДЛЯ ДЕМОНСТРАЦІЇ pytest.raises
# =====================================================

def get_cell(board, row, col):

    # Якщо координати виходять за межі поля
    if row > 2 or col > 2:
        raise IndexError("Координати виходять за межі поля")

    return board[row][col]["text"]


# =====================================================
# FIXTURE
# =====================================================
# Фікстура створює поле з перемогою X по рядку.
# Pytest автоматично передасть це поле у тест.
# =====================================================

@pytest.fixture
def winning_board():

    return [
        [FakeButton("X"), FakeButton("X"), FakeButton("X")],
        [FakeButton(""), FakeButton(""), FakeButton("")],
        [FakeButton(""), FakeButton(""), FakeButton("")]
    ]


# Тест використовує fixture як параметр
def test_winner_fixture(winning_board):

    assert check_winner(winning_board) == True



# =====================================================
# PARAMETRIZE
# =====================================================
# Один тест буде запускатися тричі
# з різними наборами даних.
# =====================================================

@pytest.mark.parametrize(
    "board, expected",
    [

        # Випадок 1:
        # перемога по рядку
        (
            [
                [FakeButton("X"), FakeButton("X"), FakeButton("X")],
                [FakeButton(""), FakeButton(""), FakeButton("")],
                [FakeButton(""), FakeButton(""), FakeButton("")]
            ],
            True
        ),

        # Випадок 2:
        # перемога по діагоналі
        (
            [
                [FakeButton("O"), FakeButton(""), FakeButton("")],
                [FakeButton(""), FakeButton("O"), FakeButton("")],
                [FakeButton(""), FakeButton(""), FakeButton("O")]
            ],
            True
        ),

        # Випадок 3:
        # переможця немає
        (
            [
                [FakeButton(""), FakeButton(""), FakeButton("")],
                [FakeButton(""), FakeButton(""), FakeButton("")],
                [FakeButton(""), FakeButton(""), FakeButton("")]
            ],
            False
        )
    ]
)

def test_winner_parametrized(board, expected):

    assert check_winner(board) == expected



# =====================================================
# ТЕСТ З pytest.raises
# =====================================================

def test_invalid_cell_access():

    board = [
        [FakeButton(""), FakeButton(""), FakeButton("")],
        [FakeButton(""), FakeButton(""), FakeButton("")],
        [FakeButton(""), FakeButton(""), FakeButton("")]
    ]

    # Очікуємо помилку IndexError
    with pytest.raises(IndexError):
        get_cell(board, 5, 5)
    

# =====================================================
# ТЕСТ З @pytest.mark.skip
# =====================================================

@pytest.mark.skip(reason="Функція статистики перемог ще не реалізована")
def test_player_statistics():

    # Майбутня перевірка статистики гравців
    assert True


# =====================================================
# ТЕСТ З @pytest.mark.xfail
# =====================================================

@pytest.mark.xfail(reason="Підтримка поля 4x4 ще не реалізована")
def test_winner_on_4x4_board():

    board = [

        [FakeButton("X"), FakeButton("X"), FakeButton("X"), FakeButton("X")],

        [FakeButton(""), FakeButton(""), FakeButton(""), FakeButton("")],

        [FakeButton(""), FakeButton(""), FakeButton(""), FakeButton("")],

        [FakeButton(""), FakeButton(""), FakeButton(""), FakeButton("")]
    ]

    # Очікуємо перемогу на полі 4x4,
    # але функція check_winner() працює лише для 3x3
    assert check_winner(board) == True



