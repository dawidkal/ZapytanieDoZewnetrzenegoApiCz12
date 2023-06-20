import requests
import json

while True:
    print("**** MENU ****")
    print("1 - Wyszukaj po kategorii")
    print("2 - Wyszukaj po składniku")
    print("3 - Lista kategorii")
    print("4 - Zakończ program")

    wybor = input("Wybierz pozycję z menu. Wybrano: ")

    if wybor == "1":
        print("--- Wyszukiwanie przepisów po kategorii ---")
        zapytanie = input("Co chcesz wyszukać? (np. nazwa potrawy, składnik, typ potrawy): ")
        response = requests.get(f'https://www.themealdb.com/api/json/v1/1/filter.php?c={zapytanie}')

        if response.status_code != requests.codes.ok:
            print("Wystąpił jakiś problem.")
        else:
            print(json.dumps(response.json(), indent=2))

    elif wybor == "2":
        print("--- Wyszukiwanie przepisów po składniku ---")
        zapytanie = input("Co chcesz wyszukać? (np. nazwa potrawy, składnik, typ potrawy): ")
        response = requests.get(f'https://www.themealdb.com/api/json/v1/1/search.php?s={zapytanie}')

        if response.status_code != requests.codes.ok:
            print("Wystąpił jakiś problem.")
        else:
            print(json.dumps(response.json(), indent=2))

    elif wybor == "3":
        print("-----------------------------------------------------------------------------------------------------")
        print("**** Lista kategorii ****")
        kategorie = requests.get(f'https://www.themealdb.com/api/json/v1/1/categories.php')

        if kategorie.status_code != requests.codes.ok:
            print("Wystąpił jakiś problem.")
        else:
            print(json.dumps(kategorie.json(), indent=2))
            print(
                "-----------------------------------------------------------------------------------------------------")

    elif wybor == "4":
        break  # Zakończ pętlę while i program

    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")