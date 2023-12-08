import tkinter as tk

# Membuat kelas Cafe dengan properti nama dan daftar menu
class Cafe:
    def __init__(self, nama, menu):
        self.nama = nama
        self.menu = menu

# Membuat objek Cafe dengan nama dan daftar menu
#cafe = Cafe("Dikana", {"Espresso":15000, "Americano":15000, "Avocado Coffee":18000})

cafe = Cafe("Dikana", {"Espresso":15000,"Americano":10000,"Kawa daun":15000,"Teh Talua Pinang":18000
                       "Avocado Coffe":18000,"Milk Kawa daun":17000,
                       
})

# Fungsi untuk menghitung total harga
def hitung_total_harga():
    total_harga = 0
    for item in menu_items:
        total_harga += cafe.menu[item[0]] * item[1].get()
    return total_harga

# Fungsi untuk menampilkan struk

def tampilkan_struk():
    nama= "Sobatngop"
    nama
    total_harga = hitung_total_harga()
    uang_customer = int(input_uang_customer.get())
    kembalian = uang_customer - total_harga

    # Membuat window untuk struk
    struk_window = tk.Toplevel(window)
    struk_window.title("Struk")

    # Menampilkan detail pesanan
    pesanan_label = tk.Label(struk_window, text="Pesanan:")
    pesanan_label.pack()

    for item in menu_items:
        if item[1].get() > 0:
            pesanan_label = tk.Label(struk_window, text=f"{item[0]} x{item[1].get()} = {cafe.menu[item[0]] * item[1].get()} IDR")
            pesanan_label.pack()

    # Menampilkan total harga
    total_harga_label = tk.Label(struk_window, text=f"Total Harga: {total_harga} IDR")
    total_harga_label.pack()

    # Menampilkan uang customer dan kembalian
    uang_customer_label = tk.Label(struk_window, text=f"Uang Customer: {uang_customer} IDR")
    uang_customer_label.pack()

    kembalian_label = tk.Label(struk_window, text=f"Kembalian: {kembalian} IDR")
    kembalian_label.pack()

# Membuat window utama
window = tk.Tk()
window.title("CAFE DIKANA")

# Membuat label untuk nama cafe
nama_cafe_label = tk.Label(window, text=f"Selamat datang di Cafe {cafe.nama}")
nama_cafe_label.pack()

# Membuat label untuk daftar menu
menu_label = tk.Label(window, text="Menu:")
menu_label.pack()

# Membuat checkbutton untuk setiap menu
menu_items = []
for item in cafe.menu:
    var = tk.IntVar()
    item_checkbutton = tk.Checkbutton(window, text=f"{item} ({cafe.menu[item]} IDR)", variable=var)
    item_checkbutton.pack()
    menu_items.append((item, var))

# Membuat label untuk input uang customer
input_uang_customer_label = tk.Label(window, text="Masukkan uang customer:")
input_uang_customer_label.pack()

# Membuat input untuk uang customer
input_uang_customer = tk.Entry(window)
input_uang_customer.pack()

# Membuat tombol untuk menampilkan struk
tampilkan_struk_button = tk.Button(window, text="Tampilkan Struk", command=tampilkan_struk)
tampilkan_struk_button.pack()

# Menjalankan program
window.mainloop()
