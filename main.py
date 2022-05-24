


class Book:

    def __init__(self, tytul, autor):
        self.tytul = tytul
        self.autor = autor

class Egzemplarz:


    def __init__(self, tytul, autor, rok):
        self.tytul = tytul
        self.autor = autor
        self.rok = int(rok)




def dodaj_egzemplarz(tytul, autor, rok):
    egzemplarz = Egzemplarz(tytul, autor, rok)
    egzemplarze.append(egzemplarz)


books = []
egzemplarze = []
book_amount = int(input())
iterate = 0


for book_input in range(book_amount):
    book_input = eval(input())
    tytul = book_input[0]
    autor = book_input[1]
    rok = book_input[2]
    dodaj_egzemplarz(tytul, autor, rok)
    book = Book(tytul, autor)
    if iterate == 0:
        books.append(book)
        iterate += 1
    else:
        for ksiazka in books:
            if (book.tytul != ksiazka.tytul) & (book.autor != ksiazka.autor):
                books.append(ksiazka)
                break
            else:
                continue


for i in range(len(books)-1):
    counter = 1
    for y in range(i + 1, len(books)):
        if books[i].autor == books[y].autor & books[i].tytul == books[y].tytul:
            counter += 1

        else:
            continue
    books[i].counter = counter

books[len(books)-1].counter = 1
no_copy = [None] * len(books)
for i in range(len(books)):
    no_copy[i] = books[i]


for i in range(len(books)-1):
    other = False
    for y in range(i+1, len(books)):
        if books[i].autor == books[y].autor & books[i].tytul == books[y].tytul:
            if books[i].counter > books[y].counter:
                no_copy.remove(books[y])

a = []
for ksiazka in no_copy:
    appender = (ksiazka.tytul, ksiazka.autor, ksiazka.counter)
    a.append(appender)

a = sorted(a, key=lambda x: x[0])
for aappender in a:
    print(appender)