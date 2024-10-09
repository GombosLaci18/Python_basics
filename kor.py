def within_range(num: int, min: int, max: int) -> bool:
    return (min < num and num <= max)


while (True):
    answer: str = input("How old are you?")
    # Megnézi, hogy az input az 0 és 99 között van
    # 1. megnézi, hogy valid szám
    try:
        number = int(answer)
    except ValueError as err:
        print("Give a valid number")
        continue
    # Check if input is between 0 and 99
    valid: bool = within_range(number, 0, 99)
    if not valid:
        print("You gave wrong number (0 - 99)")
        continue

state: str = ""

if 0 < number and number <= 99:
    # OK
    if number < 25:
        state = "young"
    elif number < 50:
        state = "adult"
    elif number < 75:
        state = "elderly"
    elif number < 99:
        state = "ghost"
    pass

match state:
    case "young":
        print("szevasz kisfiam")
    case "adult":
        print("♥")
    case "elderly":
        print("Welcome to the Facebook")
    case "ghost":
        print("skibidi ohio sigma W aura GYATT")
