# 4.2. for Statements

# Ukur beberapa string:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

print("")

# Buat koleksi sampel
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategi: Ulangi salinan
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategi: Buat koleksi baru
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(users)

print("")