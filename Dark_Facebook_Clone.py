import threading
from queue import Queue
import requests
import random
import string
import json
import hashlib
from faker import Faker
from colorama import init, Fore, Style
import os
from datetime import date, timedelta
import time

# Initialize colorama
init()

# Clear screen command
CLEAR_COMMAND = 'cls' if os.name == 'nt' else 'clear'

def clear_screen():
    os.system(CLEAR_COMMAND)

Note = Fore.RED+"""
━━━━━━━━━━━━━━━━━━━━Note━━━━━━━━━━━━━━━━━━━━
➔i have no responsibities to any damage made by this tool  
➔Please use this tool responsibly
➙Please Remember to follow us on facebook
➙Make sure you have a strong and secure network connection
➔Use Responsibly
➔ yeah i think that all ×͡×
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# Display logo
logo = Fore.RED + """
++--------------------------------++
||  ██████╗    ███████╗ ██████╗   ||
||  ██╔══██╗   ██╔════╝██╔════╝   ||
||  ██║  ██║   █████╗  ██║        ||
||  ██║  ██║   ██╔══╝  ██║        ||
||  ██████╔╝██╗██║██╗  ╚██████╗   ||
||  ╚═════╝ ╚═╝╚═╝╚═╝   ╚═════╝   ||
++--------------------------------++
➙ 𝕯𝖆𝖗𝖐 𝕱𝖆𝖈𝖊𝖇𝖔𝖔𝖐 𝕮𝖑𝖔𝖓𝖊𝖗
"""
clear_screen()
print(Note)
time.sleep(5)
clear_screen()
print(logo)
print('\x1b[38;5;22m•' * 44)
 
print(Fore.CYAN+"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓           
➣ Github    : @TheRealofClassicHackers
➣ By        : The T.R.C.H chief
➣ Proxy by  : @T.R.C.H
➣ Facebook  : @The Realm of Classic Hackers
➣ Tool Name : Dark Facebook Cloner (DFC)
➤ version   : 2.5
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━             """)
print('\x1b[38;5;208m⇼'*44)
print('\x1b[38;5;22m•'*44)
print('\x1b[38;5;22m•'*44)
print('\x1b[38;5;208m⇼'*44)

def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

def get_mail_domains(proxy=None):
    url = "https://api.mail.tm/domains"
    try:
        response = requests.get(url, proxies=proxy, timeout=10)
        if response.status_code == 200:
            return response.json()['hydra:member']
        else:
            print(f'[×] E-mail Error: {response.text}')
            return None
    except Exception as e:
        print(f'[×] Error fetching mail domains: {e}')
        return None

def create_mail_tm_account(proxy=None):
    fake = Faker()
    mail_domains = get_mail_domains(proxy)
    if mail_domains:
        domain = random.choice(mail_domains)['domain']
        username = generate_random_string(10)
        password = fake.password()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=45)
        first_name = fake.first_name()
        last_name = fake.last_name()
        url = "https://api.mail.tm/accounts"
        headers = {"Content-Type": "application/json"}
        data = {"address": f"{username}@{domain}", "password": password}       
        try:
            response = requests.post(url, headers=headers, json=data, proxies=proxy, timeout=10)
            if response.status_code == 201:
                return f"{username}@{domain}", password, first_name, last_name, birthday
            else:
                print(f'[×] Email creation failed: {response.text}')
                return None, None, None, None, None
        except Exception as e:
            print(f'[×] Error creating email: {e}')
            return None, None, None, None, None
    return None, None, None, None, None

def register_facebook_account(email, password, first_name, last_name, birthday, proxy=None):
    try:
        api_key = '882a8490361da98702bf97a021ddc14d'
        secret = '62f8ce9f74b12f84c123cc23437a4a32'
        gender = random.choice(['M', 'F'])
        req = {
            'api_key': api_key,
            'attempt_login': True,
            'birthday': birthday.strftime('%Y-%m-%d'),
            'client_country_code': 'EN',
            'fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod',
            'fb_api_req_friendly_name': 'registerAccount',
            'firstname': first_name,
            'format': 'json',
            'gender': gender,
            'lastname': last_name,
            'email': email,
            'locale': 'en_US',
            'method': 'user.register',
            'password': password,
            'reg_instance': generate_random_string(32),
            'return_multiple_errors': True
        }
        sorted_req = sorted(req.items(), key=lambda x: x[0])
        sig = ''.join(f'{k}={v}' for k, v in sorted_req)
        ensig = hashlib.md5((sig + secret).encode()).hexdigest()
        req['sig'] = ensig
        api_url = 'https://b-api.facebook.com/method/user.register'
        reg = _call(api_url, req, proxy)
        
        if 'error' in reg:
            print(f'[×] Facebook registration failed: {reg["error"]}')
            return
        
        if 'new_user_id' not in reg or 'session_info' not in reg or 'access_token' not in reg['session_info']:
            print(f'[×] Unexpected response from Facebook API: {reg}')
            return
            
        id = reg['new_user_id']
        token = reg['session_info']['access_token']
        account_info = f'''
-----------GENERATED-----------
EMAIL: {email}
ID: {id}
PASSWORD: {password}
NAME: {first_name} {last_name}
BIRTHDAY: {birthday}
GENDER: {gender}
-----------GENERATED-----------
Token: {token}
-----------GENERATED-----------'''
        print(account_info)
        
        with open('username.txt', 'a') as f:
            f.write(account_info + '\n')
            
    except Exception as e:
        print(f'[×] Error registering Facebook account: {e}')

def _call(url, params, proxy=None, post=True):
    headers = {
        'User-Agent': '[FBAN/FB4A;FBAV/35.0.0.48.273;FBDM/{density=1.33125,width=800,height=1205};FBLC/en_US;FBCR/;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/4.1.1;FBBK/0;]'
    }
    try:
        if post:
            response = requests.post(url, data=params, headers=headers, proxies=proxy, timeout=10)
        else:
            response = requests.get(url, params=params, headers=headers, proxies=proxy, timeout=10)
        return response.json()
    except Exception as e:
        print(f'[×] Error in API call: {e}')
        return {'error': str(e)}

# Proxy-related functions (unchanged as per instructions)
def test_proxy(proxy, q, valid_proxies):
    if test_proxy_helper(proxy):
        valid_proxies.append(proxy)
    q.task_done()

def test_proxy_helper(proxy):
    try:
        response = requests.get('https://api.mail.tm', proxies=proxy, timeout=5)
        return response.status_code == 200
    except:
        return False

def load_proxies():
    with open('proxies.txt', 'r') as file:
        proxies = [line.strip() for line in file]
    return [{'http': f'http://{proxy}'} for proxy in proxies]

def get_working_proxies():
    proxies = load_proxies()
    valid_proxies = []
    q = Queue()
    for proxy in proxies:
        q.put(proxy)
    
    threads = []
    for _ in range(10):  # 10 threads
        worker = threading.Thread(target=worker_test_proxy, args=(q, valid_proxies))
        worker.daemon = True
        worker.start()
        threads.append(worker)
    
    q.join()  # Block until all tasks are done
    return valid_proxies

def worker_test_proxy(q, valid_proxies):
    while not q.empty():
        try:
            proxy = q.get_nowait()
            test_proxy(proxy, q, valid_proxies)
        except Queue.Empty:
            break

# Main execution
working_proxies = get_working_proxies()

if not working_proxies:
    print(Fore.RED + '[×] No working proxies found.')
    print(Fore.RED + 'Check your internet connection.')
    exit()

try:
    num_accounts = int(input(Fore.GREEN + '[+] How Many Accounts You Want: '))
    if num_accounts <= 0:
        print(Fore.RED + '[×] Please enter a positive number.')
        exit()
except ValueError:
    print(Fore.RED + '[×] Invalid input. Please enter a number.')
    exit()

for i in range(num_accounts):
    proxy = random.choice(working_proxies)
    email, password, first_name, last_name, birthday = create_mail_tm_account(proxy)
    if email and password and first_name and last_name and birthday:
        register_facebook_account(email, password, first_name, last_name, birthday, proxy)
    else:
        print(Fore.RED + '[×] Skipping account creation due to email creation failure.')

print('\x1b[38;5;22m•' * 44)