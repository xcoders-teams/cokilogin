import requests
import random
import re

# membaca file randua.txt dan menyimpan user-agent ke dalam sebuah list
with open('ua/randua.txt', 'r') as f:
    ua_list = f.read().split(',')

# memilih user-agent secara acak dari list
ua = random.choice(ua_list)

# membuat header dengan user-agent yang dipilih
headers = {'User-Agent': ua}

# fungsi untuk login ke Facebook dan mendapatkan token
def get_fb_token(email, password):
    # URL untuk mengirimkan permintaan login
    login_url = 'https://m.facebook.com/login.php'
    # URL untuk mengirimkan permintaan mendapatkan token
    token_url = 'https://m.facebook.com/v2.8/dialog/oauth/confirm'

    # mengambil halaman login Facebook
    with requests.Session() as session:
        response = session.get(login_url, headers=headers)

        # mendapatkan inputan yang diperlukan untuk login
        form_data = {}
        try:
            action_url = re.search(r'action="(.*?)"', response.text).group(1)
            inputs = re.findall(r'<input.*?name="(.*?)".*?value="(.*?)".*?>', response.text)
            for name, value in inputs:
                form_data[name] = value
        except Exception as e:
            print('Tidak dapat menemukan inputan untuk login')
            print(str(e))
            return None

        # menambahkan email dan password ke form data
        form_data['email'] = email
        form_data['pass'] = password

        # mengirim permintaan login
        response = session.post(action_url, data=form_data, headers=headers)

        # mencari URL untuk mendapatkan token
        try:
            token_url = re.search(r'action="(.*?)"', response.text).group(1)
        except Exception as e:
            print('Tidak dapat menemukan URL untuk mendapatkan token')
            print(str(e))
            return None

        # mengirim permintaan untuk mendapatkan token
        response = session.get(token_url, headers=headers)

        # mendapatkan token dari cookie yang diterima
        try:
            cookie = response.cookies.get_dict()
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
