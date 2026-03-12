# Projekt testowania biblioteki Seaborn

## Cel projektu
Celem projektu jest stworzenie prostego systemu testowania typu "out-of-the-box" dla biblioteki **Seaborn** (Python), dostępnej w repozytorium PyPI.

## Strategia testowa
Projekt skupi się na testowaniu najnowszej stabilnej wersji biblioteki Seaborn. Testy mają weryfikować kluczowe funkcjonalności biblioteki z perspektywy typowego użytkownika, który tworzy wizualizacje danych.

*   **Testy funkcjonalne:** Sprawdzą poprawność działania wybranych funkcji biblioteki, takich jak tworzenie różnych typów wykresów (np. `scatterplot`, `histplot`) i ich podstawowe parametryzowanie. Oczekiwane rezultaty to utworzenie obiektu wykresu lub pliku graficznego bez błędów.
*   **Testy wydajnościowe:** Zmierzą czas generowania wykresów dla zbiorów danych o różnej wielkości. Pozwoli to na wstępną ocenę, jak biblioteka radzi sobie z większymi danymi.
*   **Scenariusze testów akceptacyjnych:** Zdefiniują sytuacje z życia wzięte, w których biblioteka jest używana, wraz z kryteriami sukcesu (np. "użytkownik jest w stanie wygenerować wykres korelacji dla podanego zbioru danych").

Pipeline CI/CD (GitHub Actions) zostanie skonfigurowany do automatycznej instalacji Seaborna i uruchamiania wszystkich przygotowanych testów.

## Podział ról w zespole
*(Tutaj wpiszcie rzeczywiste role i osoby)*
*   **Hubert Miłuch:** Administrator repozytorium, konfiguracja pipeline'u GitHub Actions.
*   **Franciszek Żurawicz:** Projektowanie i implementacja testów funkcjonalnych.
*   **Maciej Radlak.:** Projektowanie i implementacja testów wydajnościowych, dokumentacja

## Kanały komunikacji
*   **GitHub Issues:** Do śledzenia zadań i błędów.
*   **Discord/Messenger:** Do codziennej, bieżącej komunikacji w zespole.
