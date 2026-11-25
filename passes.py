from round import Round


def check_codes(regex, tests):
    for code, expected in tests:
        actual = regex.fullmatch(code) is not None
        if actual != expected:
            if expected:
                return False, f"Действительный код {code} отклонён."
            return False, f"Поддельный код {code} принят."
    return True, "Все проверки пройдены!"


def check_pass_1(regex):
    tests = [
        # Видимые примеры
        ("SEC/AB.0472-K", True),
        ("SEC/ZX.9183-R", True),
        ("SEC/MT.0007-K", True),
        ("sec/AB.0472-K", False),
        ("SEC/A.0472-K", False),
        ("SEC/AB-0472-K", False),
        ("SEC/AB.472-K", False),
        ("SEC/AB.0472-X", False),

        # Скрытые: действительные пропуска
        ("SEC/AA.0000-K", True),
        ("SEC/ZZ.9999-R", True),
        ("SEC/QW.1020-K", True),
        ("SEC/LP.5601-R", True),
        ("SEC/BB.0001-K", True),
        ("SEC/XD.8080-R", True),
        ("SEC/RT.4321-K", True),
        ("SEC/NN.7777-R", True),
        ("SEC/JK.2006-K", True),
        ("SEC/UV.3095-R", True),

        # Скрытые: неправильный префикс
        ("SEC/AB.0472-KK", False),
        ("SE/AB.0472-K", False),
        ("SECRET/AB.0472-K", False),
        ("SEC-AB.0472-K", False),
        ("SEC//AB.0472-K", False),

        # Скрытые: неправильные буквы
        ("SEC/abc.0472-K", False),
        ("SEC/A1.0472-K", False),
        ("SEC/ABC.0472-K", False),
        ("SEC/aB.0472-K", False),
        ("SEC/АB.0472-K", False),

        # Скрытые: неправильные цифры
        ("SEC/AB.000-K", False),
        ("SEC/AB.12345-K", False),
        ("SEC/AB.12A4-K", False),
        ("SEC/AB.１２３４-K", False),
        ("SEC/AB..1234-K", False),

        # Скрытые: неправильные разделители
        ("SEC/ABX0472-K", False),
        ("SEC/AB/0472-K", False),
        ("SEC/AB.0472#K", False),
        ("SEC/AB.0472K", False),
        ("SEC/AB.0472-K\n", False),
    ]
    return check_codes(regex, tests)


def check_pass_2(regex):
    tests = [
        # Открытые примеры
        ("VIP-07#A", True),
        ("VIP-99#B", True),
        ("vip-07#A", False),
        ("VIP-7#A", False),
        ("VIP-07#C", False),

        # Скрытые: действительные пропуска
        ("VIP-00#A", True),
        ("VIP-00#B", True),
        ("VIP-01#A", True),
        ("VIP-10#B", True),
        ("VIP-25#A", True),
        ("VIP-38#B", True),
        ("VIP-47#A", True),
        ("VIP-56#B", True),
        ("VIP-80#A", True),
        ("VIP-98#B", True),

        # Скрытые: неправильный префикс
        ("VIPS-07#A", False),
        ("VI-07#A", False),
        ("VIP/07#A", False),
        ("Vip-07#A", False),
        ("VIP--07#A", False),

        # Скрытые: неправильные цифры
        ("VIP-123#A", False),
        ("VIP-0#B", False),
        ("VIP-AA#A", False),
        ("VIP-1A#B", False),
        ("VIP-１２#A", False),

        # Скрытые: неправильное окончание
        ("VIP-07#AB", False),
        ("VIP-07#K", False),
        ("VIP-07#a", False),
        ("VIP-07#", False),
        ("VIP-07##A", False),

        # Скрытые: лишние и неправильные символы
        ("VIP-07-A", False),
        ("VIP-07/A", False),
        ("VIP-07#A ", False),
        (" VIP-07#A", False),
        ("VIP-07#A\n", False),
    ]
    return check_codes(regex, tests)


def get_rounds():
    return [
        Round(
            title="Пропуск в закрытый сектор",
            description=(
                "Преступник проник на секретный объект.\n"
                "Восстановите формат настоящего пропуска.\n\n"
                "Правила:\n"
                "1. Код начинается строго с SEC/\n"
                "2. Далее ровно две заглавные латинские буквы\n"
                "3. Затем точка и четыре цифры от 0 до 9\n"
                "4. В конце дефис и буква K или R"
            ),
            examples=(
                "\nДействительные:\n"
                "SEC/AB.0472-K\n"
                "SEC/ZX.9183-R\n"
                "SEC/MT.0007-K\n\n"
                "Поддельные:\n"
                "sec/AB.0472-K\n"
                "SEC/A.0472-K\n"
                "SEC/AB-0472-K\n"
                "SEC/AB.472-K\n"
                "SEC/AB.0472-X"
            ),
            hint=(
                "Используйте [A-Z] для букв и [0-9] для цифр.\n"
                "Количество символов задаётся через {n}.\n"
                "Точку нужно экранировать обратным слешем."
            ),
            clue="Журнал проходов в закрытый сектор",
            checker=check_pass_1
        ),

        Round(
            title="Пропуск особого доступа",
            description=(
                "Найден пропуск в секретную лабораторию.\n"
                "Его код начинается строго с VIP-,\n"
                "затем идут ровно две цифры от 0 до 9,\n"
                "символ # и одна заглавная буква A или B."
            ),
            examples=(
                "\nДействительные:\n"
                "VIP-07#A\n"
                "VIP-99#B\n\n"
                "Поддельные:\n"
                "vip-07#A\n"
                "VIP-7#A\n"
                "VIP-07#C"
            ),
            hint=(
                "Используйте [0-9]{2} для двух цифр.\n"
                "Для выбора между A и B используйте [AB]."
            ),
            clue="Адрес секретной лаборатории",
            checker=check_pass_2
        )
    ]
