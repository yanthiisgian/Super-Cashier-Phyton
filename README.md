# Super-Cashier-Phyton

## Latar Belakang
Super casier ini merupakan system pembayaran metode self-service yang bertujuan untuk memberikan kenyamanan dan user friendly bagi pelanggan untuk dapat meningkatkan proses bisnis sebuah supermarket. System pembayaran ini akan dibuat dengan program Phyton.

## Requirements atau objectives
1. Customer membuat transaksi ID.
2. Custumer memasukkan nama, jummlah, dan harga item yang akan dibeli.
3. Customer dapat melakukan update dengan:
   - Mengubah nama item
   - Mengubah jumlah item
   - Mengubah harga item
   - Atau menghapus semua orderan / reset transaksi
4. Customer dapat menampilkan ouput pesanan, berupa nama, jumlah, harga/item, harga total, dan diskon.
5. Dilengkapi dengna fitur pesan error jika terjadi kesalahan input data.

## Flow Chart Program
![Flowchart - Super cashier (1)_page-0001](https://user-images.githubusercontent.com/123178154/217258751-0ef29331-8c0a-4b6a-89c9-04a1a759a4cb.jpg)

## Penjelasan Flow Chart
1. Start
2. Membuat ID sebagai awal transaksi.
3. Kemudian customer lanjut ke Langkah add item untuk input data berupa nama, jumlah, dan harga item.
4. Setelah itu customer dapat menampilkan daftar pembelian, pada proses ini tidak ada proses cek data yang diiput sudah sesuai atau tidak.
5. Check order untuk memastikan data yang diinput valid atau tidak. Jika data benar maka proses dapat dilanjut ke proses pembayaran. Jika data masih salah maka customer bisa ubah nama atau jumlah atau harga barang, atau dapat reset untuk mengulang dari awal iput data. 
6. Proses bayar akan berisi info harga total dan diskon yang diperoleh.
7. Selesai

## Penjelasan Fungsi Code
1. init() , untuk mendeklarasikan variable utama dalam sebuah class.
   - list_order = dictionary untuk menyimpan data pesanan.
   - list_valid = berupa booelan untuk menandai apakah data yang diinput ke dalam dictionary transaksi sudah valid. Nilai awal adalah True dan bisa berubah False setelah dicek validitasnya lewat fungsi.
2. add_item (self, nama_item, jumlah_item, harga_per_item)
   Fungsi untuk input data ke dalam dictionary.
   - Nama_item = nama item yang dibeli tipe string, sebagai key dalam dictionary
   - Jumlah_item = jumlah item, tipe integer
   - Harga_item = harga per item, tipe integer
3. update_nama_item(self, nama_item, nama_baru)
   Fungsi memperbarui nama item.
   - nama_item (str) = nama item yang akan diganti,
   - nama_baru(str) = nama item yang menggatikan nama item sebelumnya.
4. update_jumlah_item(self, nama_item, jumlah_baru)
   Fungsi memperbarui jumlah item. 
   - jumlah_item (int) = jumlah item yang akan diganti,,
   - jumlah_baru(int) = jumlah item yang menggatikan jumlah item sebelumnya.
5. update_harga_item(self, nama_item, harga_baru)
   Fungsi memperbarui harga item. 
   - harga_item (int) = harga item yang akan diganti,,
   - harga_baru(int) = harga item yang menggatikan harga item sebelumnya.
6. delete_item(self, nama_item)
   Fungsi untuk menghapus suatu item dari daftar pesanan.
7. reset_transaction(self)
   Fungsi untuk menghapus semua item yang sudah masuk ke list order, Kembali ke awal untuk input data orderan.
8. show_order(self)
   Fungsi untuk menampilkan semua item yang sudah masuk ke daftar order.
9. check_order(self)
   Berbeda dengan fungsi show_order(self), fungsi ini bertujuan untuk cek data sudah benar atau tidak. Jika benar maka dapat lanjut ke proses pembaran, jika tidak benar maka customer diarahkan untuk ganti nama/harga/harga yang tidak sesuai.
10. proses_bayar(self)
    Fungsi untuk menampilkan harga total dan diskon.
Pada proses ini juga akan diinfo data sudah benar atau tidak. Jika benar maka akan diberi info total harga dan/ diskon, jika data belum benar maka total harga tidak dapat ditampilkan.

## Conclusion
Fitur menambahkan barang, mengedit barang (nama, quantity, harga per item), menghapus barang, dan perhitungan total harga serta diskon pada di execute dengan baik pada program ini.

