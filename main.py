from passes import get_rounds as get_pass_rounds
from archive import get_rounds as get_archive_rounds

rounds = get_pass_rounds() + get_archive_rounds()
clues = []
print("=" * 50)
print("                 REGEX-ДЕТЕКТИВ")
print("       Расследование секретного дела")
print("=" * 50)
for number, game_round in enumerate(rounds, start=1):
    print(f"\nДело №{number}: {game_round.title}")
    print("-" * 50)
    print(game_round.description)
    print(game_round.examples)
    while True:
        print("\nВведите регулярное выражение.")
        print("? — подсказка, exit — выход")
        pattern = input("> ")
        if pattern.lower() == "exit":
            print("Расследование прервано.")
            exit()
        if pattern == "?":
            print("\nПодсказка:", game_round.hint)
            continue
        success, message = game_round.check(pattern)
        print("\n" + message)
        if success:
            clues.append(game_round.clue)
            print("Улика получена:", game_round.clue)
            break
    if number < len(rounds):
        input("\nНажмите Enter для следующего дела...")
print("\n" + "=" * 50)
print("РАССЛЕДОВАНИЕ ЗАВЕРШЕНО!")
print("=" * 50)
print("\nСобранные улики:")
for number, clue in enumerate(clues, start=1):
    print(f"{number}. {clue}")
print("\nПреступник найден. Дело закрыто!")