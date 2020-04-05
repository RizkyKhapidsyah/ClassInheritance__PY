class Ojek():
    def __init__(self, nama, transmisi, daerah):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah = daerah

    def cek_id(self):
        print('Nama : ', self.nama, '\nMotor : ', self.transmisi, '\nDaerah : ', self.daerah)

class Gojek(Ojek): #Inheritance
    pass

class Gojok(Ojek): #Override
    def cek_id(self):
        print('Cek Aplikasinya!')

ojek1 = Ojek('Zulfikar', 'Manual', 'Medan')
ojek2 = Gojek('Indadari', 'Automatic', 'Jakarta')
ojek3 = Gojok('Siapa Ya', 'Automatic', 'Surabaya')

ojek1.cek_id()
ojek2.cek_id()
ojek3.cek_id()