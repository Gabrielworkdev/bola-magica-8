import os 
notes = []
sair = False 
while not sair :
    resp = input('Fazer anotação ? (s/n)')
    if resp == "s":
        txt = input("Anotação:")
        notes.append(txt)
    print('\n'+ "anotações".center(30, "=") )

#layout 
for note in notes:
    text_size = len(note)
    note_size = text_size+6
    print('-'*note_size)
    print(note.center(note_size))
    print('-'*note_size)
r = input("sair ? (s/n)")
if r == "s":
    sair = True
os.system('cls' if os.name == 'nt' else 'clear') 