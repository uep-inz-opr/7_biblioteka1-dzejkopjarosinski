#New approach to the problem 

class Biblioteka:


    # Define a class with list instead of variables
    def __init__(self):
        self.tytul = []
        self.autor = []
        self.rok_wydania = []


  


    def add_book(self, book):
        self.rok_wydania.append(book)

      # Define egzemplarz as a list and add append title, author to it
    def egzemplarz(self, egzemplarz):
        egzemplarz_list = list(egzemplarz)


        if egzemplarz_list[0:2] in self.rok_wydania:
         self.autor.append(egzemplarz_list[0:2])
         self.tytul.append(egzemplarz_list[0])
        else: 
            liblary.add_book(egzemplarz_list[0:2])
            self.autor.append(egzemplarz_list[0:2])
            self.tytul.append(egzemplarz_list[0])


    # Create counter 
    def policz(self):

        counter = []
        sortowanie = []

        for book in self.rok_wydania:
            x = self.autor.count(book)
            book = [book[0], book[1], x]
            counter.append(book)
            sortowanie = sorted(counter, key = lambda x: x[0])

        for el in sortowanie:
            elx = (el[0], el[1], el[2])
            print(elx)



#Create instance o fthe liblary class 

liblary =  Biblioteka()
inp = int(input())
for j in range(0,inp):
    user_input = eval(input()) #Turns string into int
    liblary.egzemplarz(user_input)
    
liblary.policz()


