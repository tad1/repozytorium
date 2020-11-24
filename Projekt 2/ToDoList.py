from os import system, name 

class ListElement:
    def __init__(self, text="", done = False):
        self.done = False
        self.text = text

class List:

    def __init__(self):
        self.elementArr = [];

    def push(self, element):
        self.elementArr.append(element)

    def pop(self, index = 0):
        self.elementArr.pop(index)
 
    def show(self):
        index = 1
        state = {
            True: "wykonano",
            False: "do zrobienia"
           }
        for element in self.elementArr:
            print(str(index) + ".", element.text + ":" , state[element.done])
            index += 1

    def showElement(self, index):
        state = {
            True: "wykonano",
            False: "do zrobienia"
           }
        print(str(index+1) + ".", self.elementArr[index].text + ":", state[self.elementArr[index].done])

    def setText(self, index, text):
        self.elementArr[index].text = text

    def setDone(self, index, done=True):
        self.elementArr[index].done = done

    def addElement(self, text = "", done = False):
        self.push(ListElement(text,done))

    def getLength(self):
        return len(self.elementArr)

lista = List()

def cls():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def create():
    text = input(">>Podaj nazwę zadania: ")
    lista.addElement(text);
    print("Dodano nowy element!")
    input("Naciśnij Enter aby kontnuować...")

def show():
    cls()
    print("---Lista Zadań---")
    lista.show()
    print("")
    print("-----------------")

def delete():
    show()
    print(str(lista.getLength()+1)+". Powrót")
    while True:
        inp = input(">>Wybierz element do usunięcia: ")
        if inp.isdigit():
            index = int(inp)
        else:
            index = -1
        index += -1
        if index >= 0 and index <= lista.getLength():
            break
        print("Brak opcji o numerze",index+1)
    if index == lista.getLength():
        return
        lista.pop(index)
        print("Pomyślnie usunięto", str(index+1), "element!")
        input(">>Naciśnij Enter aby kontynuować...")

def edit():
    if lista.getLength() == 0:
        return
    show()
    print(str(lista.getLength()+1)+". Powrót")
    while True:
        inp = input(">>Wybierz element do modyfikacji: ")
        if inp.isdigit():
            index = int(inp)
        else:
            index = -1
        index += -1
        if index >= 0 and index <= lista.getLength():
            break
        print("Brak elementu o numerze",index+1)
    if index == lista.getLength():
        return
    cls()
    print("Edytowany element:")
    lista.showElement(index);
    editMenu(lista.elementArr[index].done == False)
    choise = input(">>Wybierz akcję: ")
    if choise == '1':
        text = input(">>Nowa nazwa: ")
        lista.setText(index, text)

    elif choise == '2':
        lista.setDone(index, lista.elementArr[index].done == False)

def menu():
    print("Dostępne akcje:")
    print("1. Dodawanie Nowego Elementu")
    print("2. Usuwanie Elementu")
    print("3. Edytuj Element")
    print("4. Zakończ Program")

def editMenu(state):
    print("")
    print("Dostępne modyfikacje:")
    print("1. Edycja nazwy")
    print("2. Zmień stan na \"" + {
        True: "wykonany",
        False: "do zrobienia"}[state == True] + "\"")
    print("3. Powrót")
    

while True:
    show()
    menu()
    choise = input(">>Twój wybór: ")
    if choise == '1':
        create()

    elif choise == '2':
        delete()

    elif choise == '3':
        edit()
    elif choise == '4':
        break



