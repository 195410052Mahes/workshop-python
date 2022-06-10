try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # contoh pengecualian
    print(inst.args)     # argumen disimpan di .args
    print(inst)          # __str__ memungkinkan args untuk dicetak secara langsung,
                         # tetapi dapat diganti dalam subkelas pengecualian
    x, y = inst.args     # membongkar argumen
    print('x =', x)
    print('y =', y)

# (Output)
"""
 <class 'Exception'> 
 ('spam', 'eggs') 
 ('spam', 'eggs') 
 x = spam  
 y = eggs  
"""