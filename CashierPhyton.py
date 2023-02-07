import pandas as pd
from tabulate import tabulate

class transaction:
    def __init__(self):

        ''' 
        fungsi inisialisasi dictionary,
        list_order = untuk menyimpan data dictionary  
        check_order = untuk menandai apakah data yang diinput ke dalam dictionary transaksi sudah valid. 
                      nilai awal adalah True dan bisa berubah False setelah di cek validasinya lewat fungsi.
        table = untuk menyimpan table dalam bentuk data frame
        '''
        
        self.list_order = {}
        self.list_valid = True
    
    def add_item(self, nama_item, jumlah_item, harga_per_item):
        '''
        Fungsi untuk menambahkan item ke dalam dictionary.
        nama_barang (str) = nama item yang diorder
        jumlah_barang (int) = jumlah item yang diorder
        harga (int) = harga per item
        '''
        
        if type(jumlah_item) != int:
            print("ERROR: INPUT SALAH. Coba Lagi!")

        elif type(harga_per_item) != int:
            print('ERROR: INPUT SALAH. Coba Lagi!.')

        else:
            # masukkan data dalam bentuk dictionary
            order = {nama_item: [jumlah_item, harga_per_item,jumlah_item*harga_per_item]}
            self.list_order.update(order) 
            print(f'Ditambahakan ke pesanan Anda:  {nama_item}, Qty: {jumlah_item}, Harga: Rp{harga_per_item}')


    def update_nama_item(self, nama_item, nama_baru):
        '''
        Fungsi memperbarui nama item.
        nama_item (str) = nama item yang akan diganti,
        nama_baru(str) = nama item yang menggatikan nama item sebelumnya.
        '''

        update = self.list_order[nama_item]
        self.list_order.pop(nama_item)                 # menghapus item dari list item
        self.list_order.update({nama_baru: update})    # menambah item ke list item

        # menampilkan data pesanan setelah terjadi perubahan
        print(f'{nama_item} berhasil duperbarui menjadi {nama_baru}.')
        print('')
        self.show_order()

    def update_jumlah_item(self, nama_item, jumlah_baru):
        '''
        Fungsi memperbarui jumlah item. 
        jumlah_item (int) = jumlah item yang akan diganti,,
        jumlah_baru(int) = jumlah item yang menggatikan jumlah item sebelumnya.
        '''

        if type(jumlah_baru) != int:
            print("\nERROR: INPUT SALAH. Coba Lagi!")

        else:
            #masukkan data dalam bentuk dictionary
            self.list_order[nama_item][0] = jumlah_baru
            self.list_order[nama_item][2] = jumlah_baru*self.list_order[nama_item][1]

            #menampilkan data pesanan setelah terjadi perubahan
            print(f'Jumlah {nama_item} berhasil diperbarui menjadi {jumlah_baru}.')
            print('')
            self.show_order()
    
    def update_harga_item(self, nama_item, harga_baru):
        ''' 
        Fungsi memperbarui harga item. 
        harga_item (int) = harga item yang akan diganti,,
        harga_baru(int) = harga item yang menggatikan harga item sebelumnya.
        '''

        if type(harga_baru) != int:
            print("\nERROR: INPUT SALAH. Coba Lagi!")
        
        else:
            self.list_order[nama_item][1] = harga_baru
            self.list_order[nama_item][2] = harga_baru*self.list_order[nama_item][0]
            
            #menampilkan data pesanan setelah terjadi perubahan
            print(f'Harga {nama_item} berhasil diperbarui menjadi Rp{harga_baru}.')
            print('')
            self.show_order()

    def delete_item(self, nama_item):
        ''' 
        Fungsi untuk menghapus suatu item.
        '''
        try:
            self.list_order.pop(nama_item)
            print(f'Menghapus item {nama_item}')
            print(f'Daftar belanjaan Anda berhasil diperbarui.')
            print('')
            self.show_order()
        
        except KeyError:
            print(f'{nama_item} tidak ada dalam daftar pesanan.')   

    def reset_transaction(self):
        ''' 
        Fungsi untuk menghapus semua item yang sudah masuk ke list order
        '''

        self.list_order = self.list_order.clear
        print('Semua daftar berlanjaan Anda berhasil dihapus.')

    def show_order(self):
        ''' 
        Fungsi untuk menampilkan semua item yang sudah masuk ke list order'''
        print('Berikut daftar belanjaan Anda:')
        try:
            table_list = pd.DataFrame(self.list_order).T
            headers = ['Nama Item', 'Jumlah Item', 'Harga/Item(Rp)', 'Harga Total(Rp)']
            print(tabulate(table_list, headers, tablefmt='pretty'))

        except:
            print('Belum ada pesanan.')

    def check_order(self):
        ''' Fungsi untuk mengecek dan menampilkan semua item yang sudah masuk ke list order'''

        try:
            #Menampilkan semua pesanan
            table_list = pd.DataFrame(self.list_order).T
            headers = ['Nama Item', 'Jumlah Item', 'Harga/Item(Rp)', 'Harga Total(Rp)']
            print(tabulate(table_list, headers, tablefmt='pretty'))

            #cek jumlah atau harga lebih dari 0
            kolom=0
            while kolom<2:
                for data in table_list[kolom]:
                    if data<=0:
                        self.list_valid = False
                kolom+=1

            if self.list_valid:
                print('Pesanan sudah benar.')
            else:
                print('tedapat kesalahan input nama / jumlah/ harga. Mohon cek ulang pesanan')

        except ValueError:
            print('Belum ada pesanan.')

    def proses_bayar(self):
        ''' Fungsi untuk menampilkan harga total dari list order'''

        # Memastikan pesanan sudah valid sebelum menjalankan method
        self.check_order()
        # Mengitung diskon
        if self.list_valid:

            # Menghitung total belanja
            harga_total = 0
            for item in self.list_order:
                harga_total += self.list_order[item][2]

            #menghitung diskon
            if harga_total > 500_000:
                diskon = int(harga_total*0.1)
                harga_total = int(harga_total - diskon)
                print(f'Anda mendapatkan diskon 10%,sebesar Rp {diskon}.\nTotal belanja Anda menjadi: Rp {harga_total}')
            elif harga_total > 300_000:
                diskon = int(harga_total*0.08)
                harga_total = int(harga_total - diskon)
                print(f'Anda mendapatkan diskon 10%,sebesar Rp {diskon}.\nTotal belanja Anda menjadi: Rp {harga_total}')
            elif harga_total > 200_000:
                diskon = int(harga_total*0.05)
                harga_total = int(harga_total - diskon)
                print(f'Anda mendapatkan diskon 10%,sebesar Rp {diskon}.\nTotal belanja Anda menjadi: Rp {harga_total}')
            else:
                print(f'Total harga belanja Anda adalah Rp {harga_total}.')
        else:
            print('ERROR')
