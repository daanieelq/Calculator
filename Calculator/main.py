def is_valid_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


firstNumb = input("Geben Sie eine Zahl ein: ")
firstOp = input("Geben Sie einen Operator ( + - / * ) ein: ")
secondNumb = input("Geben Sie eine zweite Zahl ein: ")

if not is_valid_number(firstNumb):
    print("Eingabe der ersten Zahl ist ungültig.")
elif not is_valid_number(secondNumb):
    print("Eingabe der zweiten Zahl ist ungültig.")
else:
    firstNumb = float(firstNumb)
    secondNumb = float(secondNumb)

    match firstOp:
        case "+":
            result = firstNumb + secondNumb
            print("Das Ergebnis lautet: ", result)
        case "-":
            result = firstNumb - secondNumb
            print("Das Ergebnis lautet: ", result)
        case ":":
            result = firstNumb / secondNumb
            print("Das Ergebnis lautet: ", result)
        case "/":
            result = firstNumb / secondNumb
            print("Das Ergebnis lautet: ", result)
        case "*":
            result = firstNumb * secondNumb
            print("Das Ergebnis lautet: ", result)
        case _:
            print("Operator ist ungültig")