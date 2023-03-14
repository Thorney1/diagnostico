class CHISTE:
    def __init__(self):
        self.chistes= []

print('La Máquina de Chistes Informáticos')
aux=input('¿Quieres que te muestre un chiste informático? (Si/No): ').upper()
if aux == 'SI':
    #chiste
    aux=input('¿Quieres ver otro chiste informático más? (Ver otro chiste/No)').upper()
    if aux == 'VER OTRO CHISTE':
        ...
if aux == 'NO':
    print('La máquina de chistes informáticos dejó de funcionar...')
    