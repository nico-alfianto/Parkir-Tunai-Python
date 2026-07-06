import datetime
from prettytable import PrettyTable 

# === Database ===
data_kendaraan = []
data_kendaraan_keluar = []
tbl_laporan = []

# === function ===
def time_to_minute(time):
  '''Convert format waktu JAM:MENIT ke menit'''
  list(map(int, time.split(':')))
  # contoh 1:30 -> 1, 30 -> (1 * 60) + 30 -> 90
  hasil = int(time[0] * 60 + time[1])
  return hasil

def minute_to_time(menit):
  '''Convert menit ke format waktu JAM:MENIT'''
  dt = datetime.datetime(1900, 1, 1) + datetime.timedelta(minutes=menit)
  return dt.strftime("%H:%M")

def update_laporan():
  tanggal = datetime.datetime.now().strftime("%Y/%m/%d")
  pendapatan = 0
  total_kendaraan = 0
  total_motor = 0
  total_mobil = 0
  # Membaca list data_kendaraan_keluar satu per satu dengan alias dkk
  for dkk in data_kendaraan_keluar:
    pendapatan = pendapatan + dkk['biaya']
    total_kendaraan+=1 # Total_kendaraan tambah 1
    # Jika kategori == Motor maka total_motor tambah 1 jika tidak total_mobil tambah 1
    if dkk['kategori'] == 'Motor':
      total_motor+=1
    else:
      total_mobil+=1 
    

  laporan = [{
    'tanggal': tanggal,
    'pendapatan': pendapatan,
    'total_kendaraan': total_kendaraan,
    'total_motor': total_motor,
    'total_mobil': total_mobil,
  }]
  tbl_laporan.append(laporan)
  data_kendaraan_keluar.clear()
  print("Laporan berhasil di update.")
  input("\nTekan Enter Untuk Lanjut")
  dashboard()



# === Pages ===
def dashboard():
  '''Halaman menu utama'''
  print()
  print("="*70)
  print("SISTEM INFORMASI MANAJEMEN PARKIR TUNAI".center(70))
  print("="*70)
  print("1 Kendaraan Masuk")
  print("2 Kendaraan Keluar")
  print("3 Daftar Kendaraan")
  print("4 Daftar Kendaraan Keluar")
  print("5 Laporan Parkir")
  print("6 Akhiri Hari")
  print("0 Keluar")
  # Loop untuk mengulangi input jika salah
  while True:
    try:
      pilihan = int(input("Pilih Menu: "))
      if pilihan == 0:
        exit()
        break
      elif pilihan == 1:
        kendaraan_masuk()
        break
      elif pilihan == 2:
        kendaraan_keluar()
        break
      elif pilihan == 3:
        daftar_kendaraan()
        break
      elif pilihan == 4:
        daftar_kendaraan_keluar()
        break
      elif pilihan == 5:
        laporan_parkir()
        break
      elif pilihan == 6:
        if input("Masukkan Password: ") == "Password": # Password yang sangat rahasia, jangan kasih tau siapa-siapa🤫
          update_laporan()
          break
        else:
          print("Password salah")
          continue
      else:
        print("Opsi tidak tersedia, silahkan coba lagi")
    except ValueError:
      print("Input tidak valid, masukkan angka saja.") # Eksepsi data tidak tepat

def kendaraan_masuk():
  '''Halaman memasukkan data kendaraan ke database'''
  print()
  print("-"*70)
  print("KENDARAAN MASUK".center(70))
  print("-"*70)
  # Input gate
  print('''Gate Masuk
    1. Gate 1
    2. Gate 2
    3. Gate 3''')
  while True: # Loop untuk memastikan input kategori tepat
    try:
      inGate = int(input("Masukkan Gate Masuk (1/2/3): "))
      if inGate == 1:
        gate = 'Gate 1'
        break
      elif inGate == 2:
        gate = 'Gate 2'
        break
      elif inGate == 3:
        gate = 'Gate 3'
        break
      else:
        print("Opsi tidak tersedia, silahkan coba lagi.") # jika nomor tidak ada
    except ValueError:
      print("Tipe input tidak valid, masukkan angka saja.") # Eksepsi tipe data tidak tepat
  # Input nopol
  while True:
    nopol = input("Masukkan Nomor Polisi Kendaraan: ")
    if nopol == '':
      print("Nopol tidak boleh kosong.")
    else:
      break
  # Input kategori kendaraan 
  print('''Kategori Kendaraan
    1. Motor
    2. Mobil''')
  while True: # Loop untuk memastikan input kategori tepat
    try:
      inKategori = int(input("Masukkan Kategori Kendaraan (1/2): "))
      if inKategori == 1:
        kategori = 'Motor'
        tarif = 2000
        break
      elif inKategori == 2:
        kategori = 'Mobil'
        tarif = 5000
        break
      else:
        print("Opsi tidak tersedia, silahkan coba lagi.") # jika nomor tidak ada
    except ValueError:
      print("Input tidak valid, masukkan angka saja.") # Jika tipe data tidak tepat
  # Input tipe parkiran reguler atau premium
  print('''Tipe Parkir
    1. Reguler
    2. Premium''')
  while True: # Loop untuk memastikan input tepat
    try:
      tipe_parkir = int(input("Masukkan Tipe Parkir (1/2): "))
      if tipe_parkir == 1:
        tipe_parkir = 'Reguler'
        break
      elif tipe_parkir == 2:
        tipe_parkir = 'Premium'
        tarif = 50000 # Akan mengoverwrite tarif di atas
        break
      else:
        print("Opsi tidak tersedia, silahkan coba lagi.") # jika nomor tidak ada
    except ValueError:
      print("Input tidak valid, masukkan angka saja.") # Jika tipe data tidak tepat
  # Mengambil jam sekarang
  jam_masuk = datetime.datetime.now().strftime("%H:%M")
  # Persiapan data
  kendaraan_info = {
    'gate': gate,
    'nopol': nopol,
    'kategori': kategori,
    'tipe_parkir': tipe_parkir,
    'jam_masuk': jam_masuk,
    'tarif': tarif,
  }
  # Memasukkan data kendaraan_info ke data_kendaraan
  data_kendaraan.append(kendaraan_info)
  print()
  # Meanampilkan data kendaraan
  for ki in kendaraan_info:
    print(ki, ":", kendaraan_info[ki]) 
  print("Kendaraan berhasil ditambahkan.")
  # Mengulangi function lagi jika input bukan N
  if input("\nIsi Lagi?(Y/n): ").upper() == 'N':
    dashboard()
  else:
    kendaraan_masuk()



def kendaraan_keluar():
  '''Halaman mengeluarkan data kendaraan ke database'''
  print()
  print("-"*70)
  print("KENDARAAN KELUAR".center(70))
  print("-"*70)
  # Input nopol
  nopol = input("Masukkan Nomor Polisi Kendaraan: ")
  # Mengambil data kendaraan dari data_kendaraan dengan alias kk
  for kk in data_kendaraan:
    if kk['nopol'] == nopol:
      # Mengambil waktu sekarang
      jam_keluar = datetime.datetime.now().strftime("%H:%M")
      # jam_keluar = input("Masukkan Jam Keluar (HH:MM): ") # Input manual
      kk['jam_keluar'] = jam_keluar # Menambahkan data ke database
      # Menggunakan function di section === function === di atas
      jam_masuk = time_to_minute(kk['jam_masuk'])
      jam_keluar = time_to_minute(jam_keluar)
      lama_parkir = jam_keluar - jam_masuk
      kk['lama_parkir'] = minute_to_time(lama_parkir) # Menambahkan data ke database
      # Menghitung biaya parkir berdasarkan jam parkir
      jam = lama_parkir // 60 + 1
      if jam <= 1:
        kk['biaya'] = kk['tarif']
      else:
        kk['biaya'] = kk['tarif'] + (jam - 1) * kk['tarif']
      

      # Output tiket
      print("="*30)
      print("TIKET PARKIR".center(30))
      print("="*30)
      print("Nopol              :", kk['nopol'])
      print("Kategori           :", kk['kategori'])
      print("Tipe Parkir        :", kk['tipe_parkir'])
      print("Jam Masuk          :", kk['jam_masuk'])
      print("Jam Keluar         :", kk['jam_keluar'])
      print("Lama Jam Parkir    :", jam)
      print("-"*30)
      print("Tarif              :", kk['tarif'])
      print("Total Biaya Parkir :", kk['biaya'])
      print("="*30)
      
      # Menyiapkan data untuk di append
      kendaraan_info = {
        'gate': kk['gate'],
        'nopol': kk['nopol'],
        'kategori': kk['kategori'],
        'tipe_parkir': kk['tipe_parkir'],
        'jam_masuk': kk['jam_masuk'],
        'jam_keluar': kk['jam_keluar'],
        'lama_parkir': kk['lama_parkir'],
        'tarif': kk['tarif'],
        'biaya': kk['biaya']
      }

      # Memindahkan data dari data_kendaraan ke data_kendaraan_keluar
      data_kendaraan_keluar.append(kendaraan_info)
      data_kendaraan.remove(kk)

      # Mengulangi function lagi jika input bukan N
      if input("\nKendaraan Keluar?(Y/n): ").upper() == 'N':
        dashboard()
      else:
        kendaraan_keluar()
  print("Kendaraan tidak ditemukan atau sudah keluar.")
  # Mengulangi function lagi jika input bukan N
  if input("\nIsi Lagi?(Y/n): ").upper() == "N":
    dashboard()
  else: 
    kendaraan_keluar()


def daftar_kendaraan():
  '''Halaman daftar data kendaraan'''
  print()
  print("-"*73)
  print("DAFTAR KENDARAAN".center(73))
  print(datetime.datetime.now().strftime("%d %B %Y").center(73))
  print("-"*73)
  # Header tabel
  list_kendaraan = PrettyTable(['Gate','Nopol','Kategori Kendaraan','Tipe Parkir', 'Jam Masuk','Tarif'])
  # List table
  for i in data_kendaraan:
    list_kendaraan.add_row([i['gate'],i['nopol'],i['kategori'],i['tipe_parkir'],i['jam_masuk'],i['tarif']])
  print(list_kendaraan)
  input("\nTekan Enter Untuk Lanjut")
  dashboard()

def daftar_kendaraan_keluar():
  '''Halaman daftar data kendaraan'''
  print()
  print("-"*121)
  print("DAFTAR KENDARAAN KELUAR".center(121))
  print(datetime.datetime.now().strftime("%d %B %Y").center(121))
  print("-"*121)
  # Header tabel
  list_keluar = PrettyTable(['Gate','Nopol','Kategori Kendaraan','Tipe Parkir', 'Jam Masuk','Jam Keluar','Lama Parkir','Tarif','Total Biaya Parkir'])
  # List table
  for i in data_kendaraan_keluar:
    list_keluar.add_row([i['gate'],i['nopol'],i['kategori'],i['tipe_parkir'],i['jam_masuk'],i['jam_keluar'],i['lama_parkir'],i['tarif'],i['biaya']])
  print(list_keluar)
  input("\nTekan Enter Untuk Lanjut")
  dashboard()

def laporan_parkir():
  print()
  print("-"*121)
  print("LAPORAN PARKIR".center(121))
  print(datetime.datetime.now().strftime("%d %B %Y").center(121))
  print("-"*121)
  # Header tabel
  laporan = PrettyTable(['Tanggal','Pendapatan','Total Motor','Total Mobil','Total Kendaraan'])
  # List table
  for l in tbl_laporan:
    laporan.add_row([l[0]['tanggal'],l[0]['pendapatan'],l[0]['total_motor'],l[0]['total_mobil'],l[0]['total_kendaraan']])
  print(laporan)
  input("\nTekan Enter Untuk Lanjut")
  dashboard()
  

dashboard()