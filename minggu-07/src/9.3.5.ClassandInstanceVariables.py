class Dog:

    kind = 'canine'         # variabel kelas yang dibagikan oleh semua instance

    def __init__(self, name):
        self.name = name    # variabel instance unik untuk setiap instance

d = Dog('Fido')
e = Dog('Buddy')
d.kind                  # dibagikan oleh semua anjing
# 'canine' (Output)
e.kind                  # dibagikan oleh semua anjing
# 'canine' (Output)
d.name                  # untuk d
# 'Fido' (Output)
e.name                  # untuk e
# 'Buddy' (Output)