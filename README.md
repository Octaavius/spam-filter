# Spam-filter

## Filtrowanie spamu oparte na modelu językowym

### Opis

W dzisiejszych czasach niemal każdy korzysta z poczty elektronicznej, a marnowanie czasu na nieistotne lub niechciane wiadomości potrafi być naprawdę frustrujące. Właśnie dlatego większość usług e-mailowych posiada specjalny folder na spam. Zainteresowało mnie, jak takie systemy określają, które wiadomości są spamem, a które nie — i to skłoniło mnie do przeprowadzenia projektu, w którym porównałem trzy różne typy sieci neuronowych do tego zadania klasyfikacyjnego.

Mój projekt składa się z dwóch głównych części:

1. **Aplikacja Pygame** , dzięki której można sprawdzić, czy dana wiadomość e-mail zostanie zakwalifikowana jako spam czy jako wiadomość prawidłowa.
2. **Notebook Jupyter**, w którym porównuję skuteczność różnych architektur sieci neuronowych i opisuję cały proces trenowania modeli.

Zachęcam do zapoznania się z projektem i sprawdzenia, czy Wasze wiadomości zostaną sklasyfikowane jako spam czy wiadomości prawidłowe!

## Spis treści

| Sekcja                                                 | Opis                                                           |
| ------------------------------------------------------ | -------------------------------------------------------------- |
| [Uruchamianie aplikacji](#uruchamianie-aplikacji)         | Instrukcje dotyczące uruchomienia aplikacji Pygame            |
| [Zbiory danych treningowych](#zbiory-danych-treningowych) | Informacje o danych użytych do trenowania modeli              |
| [Notebook Jupyter](#notebook-jupyter)                     | Szczegółowy opis notebooka, jego lokalizacja i użyte modele |

## Uruchamianie aplikacji

0. **Zainstaluj interpreter Pythona**
   Jak to zrobić, znajdziesz [tutaj](https://www.python.org/downloads/)
1. **Sklonuj repozytorium**:
   Otwórz terminal i sklonuj repozytorium:
   ```bash
   git clone https://github.com/Octaavius/spam-filter.git
   ```
2. **Przejdź do folderu projektu**:
   Zmień katalog roboczy na folder z projektem:
   ```bash
   cd Spam-filter
   ```
3. **Zainstaluj wymagane biblioteki**:
   Zainstaluj wszystkie niezbędne biblioteki potrzebne do działania aplikacji:
   ```bash
   pip install -r requirements.txt
   ```
4. **Uruchom aplikację**
   ```bash
   python scripts/main.py
   ```

## Zbiory danych treningowych

Do trenowania modeli użyłem następującego zbioru danych:
[Spam Email Classification Dataset](https://www.kaggle.com/datasets/purusinghvi/email-spam-classification-dataset).

Zbiór ten zawiera tylko dwie kolumny: tekst wiadomości oraz etykiety (spam / nie-spam), dlatego nie była potrzebna żadna skomplikowana wstępna obróbka danych przed rozpoczęciem treningu modeli.

## Notebook Jupyter

Notebook znajduje się w folderze research i jest dostępny [tutaj](https://github.com/Octaavius/spam-filter/blob/main/research/Research.ipynb).

W notebooku najpierw tworzę słownik, w którym każdemu słowu przypisywany jest unikalny identyfikator. Jeśli dane słowo nie znajduje się w słowniku, przypisywany jest mu specjalny token oznaczający nieznane słowo.

Następnie zdefiniowałem trzy różne architektury sieci neuronowych, wykorzystując: zwykłe RNN, GRU i LSTM. Wszystkie modele osiągnęły dobre wyniki, jednak najlepiej spisał się model oparty na warstwach GRU. W notebooku znajduje się także wykres przedstawiający proces uczenia się modelu.
