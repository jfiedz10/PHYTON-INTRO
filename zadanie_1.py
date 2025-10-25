# zadanie1.py
# Program demonstracyjny: łączenie list, użycie modułu random i obsługa wyjątku.

# Import modułu random z biblioteki standardowej
# Link do dokumentacji: https://docs.python.org/3/library/random.html

import random

# Tworzenie dwóch list

lista1 = ['jabłko', 'banan', 'gruszka']
lista2 = [1, 2, 3]

# Łączenie list za pomocą funkcji zip() - tworzy pary z elementów obu list
# Link do dokumentacji: https://docs.python.org/3/library/functions.html#zip

polaczone = list(zip(lista1, lista2))
print("Połączone listy:", polaczone)

# Użycie funkcji z modułu random: random.choice() wybiera losowy element z listy
# Link do dokumentacji: https://docs.python.org/3/library/random.html#random.choice

losowy_element = random.choice(lista1)
print("Losowy element z lista1:", losowy_element)

# Obsługa wyjątku: próbujemy skonwertować string na int, co może wywołać ValueError
# Link do dokumentacji ValueError: https://docs.python.org/3/library/exceptions.html#ValueError

try:
    # Symulacja potencjalnego błędu - nieprawidłowy string
    wartosc = int("nie-liczba")  # To wywoła ValueError
    print("Konwersja udana:", wartosc)
    
except ValueError as e:
    print("Błąd ValueError:", e)
    print("Obsługa wyjątku zakończona - program kontynuuje.")
