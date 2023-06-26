import random

def choose_option():
    options = ("piedra", "papel", "tijera")
    user_option = input("piedra, papel o tijera => ").lower()
    
    if user_option not in options:
        print("Esa opción no es válida.")
        return None
    
    computer_option = random.choice(options)
    print("User_option =>", user_option)
    print("Computer_option =>", computer_option)
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print("¡Es un empate!")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("Piedra le gana a tijera")
            print("¡Ganaste!")
            user_wins += 1
        else:
            print("Papel le gana a piedra")
            print("Perdiste")
            computer_wins += 1
    elif user_option == "papel":
        if computer_option == "piedra":
            print("Papel le gana a la piedra")
            print("¡Ganaste!")
            user_wins += 1
        else:
            print("Tijera le gana a papel")
            print("Perdiste")
            computer_wins += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("Tijera le gana a papel")
            print("Ganaste")
            user_wins += 1
        else:
            print("Piedra le gana a tijera")
            print("Perdiste")
            computer_wins += 1
    
    return user_wins, computer_wins

