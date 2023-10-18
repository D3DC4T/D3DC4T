import os

def display_directory_contents(directory):
    try:
        # Získání seznamu obsahu složky
        contents = os.listdir(directory)

        # Vypsání obsahu složky
        print(f"Obsah složky '{directory}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"Složka '{directory}' neexistuje.")

def navigate_directories():
    current_directory = "hacks"  # Výchozí složka (upravte podle vašich potřeb)

    # Tutoriál na začátku programu
    os.system('cls' if os.name == 'nt' else 'clear')  # Čištění konzole
    print("Vítejte v programu pro prohlížení složek!")
    print("Použijte tuto konzoli k procházení složek.")
    print("Pokud chcete zobrazit obsah aktuální složky, zadejte '1'.")
    print("Chcete-li přejít do jiné složky, zadejte '2'.")
    print("Pro návrat zpět v hierarchii složek zadejte '3'.")
    print("Pro ukončení programu zadejte '4'.")
    print("nejefektivnější je si to všechno udělat manuálně takže pomocí své hlavy a nepoužívat tento program")
    input("Stiskněte Enter pro pokračování...")

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Čištění konzole

        print("███████         ██████████        ████████            ████████         ████████████████████████        ████████████████████")
        print("███    ██       ███               ███     ██         ████              ██      ██  ██        ██                ██")
        print("███      ██     ███               ███       ██      ████               ██    ██      ██     ██                 ██")
        print("███      ██     ██████████        ███       ██     ████                 ██ ██          ██  ██                  ██")
        print("███      ██     ███               ███       ██     ████                  ██              ██                    ██")
        print("███    ██       ███               ███     ██        ████                  ██            ██                     ██")
        print("███████         ██████████        ████████           ████                  ██          ██                      ██")
        print("                                                       ██████               ██        ██")
        print("                                                                             ██      ██")
        print("                                                                              ████████")

        print(f"Aktuální složka: {current_directory}")
        print("Možnosti:")
        print("1. Zobrazit obsah aktuální složky")
        print("2. Přejít do jiné složky")
        print("3. Vrátit se zpět")
        print("4. Odejít")

        # Přečtení volby od uživatele
        volba = input("Zadejte číslo možnosti (1-4): ")

        if volba == '1':
            display_directory_contents(current_directory)
            input("Stiskněte Enter pro pokračování...")  # Pauza, dokud uživatel nepokračuje

        elif volba == '2':
            new_directory = input("Zadejte cestu k nové složce: ")
            if os.path.isdir(new_directory):
                current_directory = new_directory
            else:
                print(f"Složka '{new_directory}' neexistuje.")

        elif volba == '3':
            current_directory = os.path.dirname(current_directory)

        elif volba == '4':
            print("Rozloučení. Program se ukončuje.")
            break  # Konec programu

# Volání funkce pro navigaci v složkách s tutoriálem na začátku
navigate_directories()
