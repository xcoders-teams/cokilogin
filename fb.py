import requests
import random
import re

# buka file randua.txt dan baca isi file
with open('ua/randua.txt', 'r') as f:
    ua_list = f.readlines()

# hapus karakter newline pada setiap elemen dalam list
ua_list = [ua.strip() for ua in ua_list]

# pilih user-agent secara acak dari list
ua = random.choice(ua_list)

# buat header dengan user-agent yang dipilih
headers = {'User-Agent': ua}

# fungsi untuk login ke Facebook dan mendapatkan token
def get_fb_token(email, password):
    # url untuk mengirimkan permintaan login
    login_url = 'https://m.facebook.com/login.php'
    # url untuk mengirimkan permintaan mendapatkan token
    token_url = 'https://m.facebook.com/v2.8/dialog/oauth/confirm'

    # ambil halaman login Facebook
    session = requests.Session()
    resp = session.get(login_url, headers=headers)

    # dapatkan inputan yang diperlukan untuk login
    form_data = {}
    try:
        action_url = re.search(r'action="(.*?)"', resp.text).group(1)
        inputs = re.findall(r'<input.*?name="(.*?)".*?value="(.*?)".*?>', resp.text)
        for name, value in inputs:
            form_data[name] = value
    except Exception as e:
        print('Tidak dapat menemukan inputan untuk login')
        print(str(e))
        return None

    # tambahkan email dan password ke form data
    form_data['email'] = email
    form_data['pass'] = password

    # kirim permintaan login
    resp = session.post(action_url, data=form_data, headers=headers)

    # cari url untuk mendapatkan token
    try:
        token_url = re.search(r'action="(.*?)"', resp.text).group(1)
    except Exception as e:
        print('Tidak dapat menemukan url untuk mendapatkan token')
        print(str(e))
        return None

    # kirim permintaan untuk mendapatkan token
    resp = session.get(token_url, headers=headers)

    # dapatkan token dari cookie yang diterima
    try:
        cookie = resp.cookies.get_dict()
        token = cookie['access_token']
        return token
    except Exception as e:
        print('Tidak dapat mendapatkan token')
        print(str(e))
        return None


# contoh penggunaan fungsi get_fb_token
email = 'your_email@example.com'
password = 'your_password'
token = get_fb_token(email, password)
if token:
    with open('result/fb_token.txt', 'w') as f:
        f.write(token)
    print('Token berhasil didapatkan dan disimpan di result/fb_token.txt')
else:
    print('Gagal mendapatkan token')
