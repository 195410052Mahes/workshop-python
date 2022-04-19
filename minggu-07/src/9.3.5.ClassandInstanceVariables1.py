class Dog:

    tricks = []             # kesalahan penggunaan variabel kelas

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

 d = Dog('Fido')
 e = Dog('Buddy')
 d.add_trick('roll over')
 e.add_trick('play dead')
 d.tricks                # secara tak terduga dibagikan oleh semua anjing
# ['roll over', 'play dead'] (Output)