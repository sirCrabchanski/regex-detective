from passes import get_rounds as get_pass_rounds
from archive import get_rounds as get_archive_rounds

rounds = get_pass_rounds() + get_archive_rounds()
correct_patterns = [
    r"SEC/[A-Z]{2}\.[0-9]{4}-[KR]",
    r"VIP-[0-9]{2}#[AB]",
    r"(?<!\w)CASE-[0-9]{4}(?![\w-])",
    r"(?<!\w)LOG#[A-Z]{2}/[0-9]{3}(?![\w-])"
]
for number, game_round in enumerate(rounds):
    success, message = game_round.check(correct_patterns[number])
    assert success, message
    success, message = game_round.check(".*")
    assert not success
    success, message = game_round.check("[")
    assert not success
    assert "Синтаксическая ошибка" in message
    print(f"Раунд {number + 1}: все тесты пройдены")
print("Все автоматические проверки успешны!")
