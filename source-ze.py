import requests,random,os,time
import telebot
from telebot import types
from user_agent import generate_user_agent

def ch_user(user):
    da = requests.post("https://www.instagram.com/accounts/web_create_ajax/attempt/",headers={'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7','content-length': '61','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI','origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/accounts/emailsignup/','sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(),'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI','x-ig-app-id': '936619743392459','x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M','x-instagram-ajax': '72bda6b1d047','x-requested-with': 'XMLHttpRequest'},data={'email' : 'a@gmail.com','username': f'{user}','first_name': 'AA','opt_into_one_tap': 'false'}).text
    if ('{"account_created": false, "errors": {"email": [{"message": "Too many accounts are using a@gmail.com.", "code": "email_sharing_limit"}], "__all__": [{"message": "Create a password at least 6 characters long.", "code": "too_short_password"}]}, "dryrun_passed": false, "username_suggestions": [], "status": "ok", "error_type": "form_validation_error"}') in  da:
        return True
    else:
        return False

def get_user():
    while True:
        get_str1  = "".join(random.choice("qwertyuiopasdfghjklzxcvbnm")for i in range(1))
        get_str2  = "".join(random.choice("qwertyuiopasdfghjklzxcvbnm")for i in range(1))
        get_str3  = "".join(random.choice("qwertyuiopasdfghjklzxcvbnm")for i in range(1))
        get_int  = "".join(random.choice("1234567890")for i in range(1))
        get_  = "".join(random.choice("_.")for i in range(1))
        d = random.randint(1,4)
        if d == 1:
            username = str(get_str1+get_str2+get_+get_int+get_str2)
        elif d == 2:
            username = str(get_str1+get_str2+get_+get_int+get_str3)
        elif d == 3:
            username = str(get_str1+get_str2+get_+get_str3+get_int)
        elif d == 4:
        	username = str(get_str1+get_int+get_+get_str3+get_str2)
        if "_" in str(username) or "." in str(username) :
            return str(username)
            break


s = []
msg = "*مرحبا بك عزيزي المستخدم ❤️🌜\n\nفي بوت صيد يوزرات أنستغرام شبه رباعية صيد ديقيق وسريع ⚡ \n\nمنفضل أضغط على Start لبدء الصيد ▶️\n\nالمبرمج 𝑫𝑨𝑹𝑲 أ *"
token = str(input("Enter Token Bot \n> "))
bot = telebot.TeleBot(token) 
@bot.message_handler(commands=['start'])
def boten(message):
    id = message.from_user.id
    name = message.from_user.first_name
    username = message.from_user.username
    mas = types.InlineKeyboardMarkup(row_width=1)
    A = types.InlineKeyboardButton(text ="بدء ▶️", callback_data="start"+str(id))
    B = types.InlineKeyboardButton('المطور', url="https://t.me/MARKO_TOOLS")
    mas.add(A,B)
    bot.send_message(message.chat.id,msg,reply_markup=mas,parse_mode="markdown")
@bot.callback_query_handler(func=lambda call : True)
def callback(call):
    id = call.message.chat.id
    if call.data == "start"+str(id):
        h = 0
        b = 0
        while True:
            if str(id) in str(s):
                s.remove(id)
                mas = types.InlineKeyboardMarkup(row_width=1)
                A = types.InlineKeyboardButton(text ="بدء ▶️", callback_data="start"+str(id))
                B = types.InlineKeyboardButton('المطور', url="https://t.me/S45_C")
                mas.add(A,B)
                bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=msg,reply_markup=mas)
                break
            
            username  = get_user()
            
            ch = ch_user(username)
            if ch:
                h+=1
                message = f"𖤚  𝑫𝑨𝑹𝑲-𝐓𝐎𝐎𝐋𝐒 ࿐ 🇮🇶.  \n︎ .ꨄ︎ ––––––––––––––––︎ ꨄ︎. \n .𖤛. 𝒖𝒔𝒆𝒓𝒏𝒂𝒎𝒆 : {username} \n .︎ꨄ︎ –––––––––––––––– ꨄ︎.\n 𝐂𝐡 : 𝑫𝑨𝑹𝑲 ☆ @S45_C"
                bot.send_message(call.message.chat.id,message)
            else:
                b+=1
            mas = types.InlineKeyboardMarkup(row_width=2)
            T = types.InlineKeyboardButton(text ="✅ True : "+str(h), callback_data="u")
            F = types.InlineKeyboardButton(text ="❌ False : "+str(b), callback_data="n")
            S = types.InlineKeyboardButton(text ="Stop ⏹️", callback_data="stop"+str(id))
            mas.add(T,F,S)
            bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"*جاري بد الصيد الان ⚡ \n\n Username : {username} 👈 \n\n لأيقاف الصيد أضغط على Stop 👇\n\n\n المبرمج : @S45_C *",parse_mode="markdown",reply_markup=mas)
    elif call.data == "stop"+str(id):
        s.append(id)
bot.polling()