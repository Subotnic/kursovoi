import telebot
from telebot import types

f = open('BOSHKY.txt','r', encoding='UTF-8')
boshky = f.read()
f.close()

f = open('HUSKY.txt','r', encoding='UTF-8')
husky = f.read()
f.close()

f = open('BRUSKO20.txt','r', encoding='UTF-8')
brusko20 = f.read()
f.close()

f = open('HQD.txt','r', encoding='UTF-8')
hqd = f.read()
f.close()

f = open('MAD.txt','r', encoding='UTF-8')
mad = f.read()
f.close()

f = open('VooDoo_Salt.txt','r', encoding='UTF-8')
voodoo_salt = f.read()
f.close()

f = open('HotSpot.txt','r', encoding='UTF-8')
hotspot = f.read()
f.close()

f = open('BRUSKO50.txt','r', encoding='UTF-8')
brusko50 = f.read()
f.close()

f = open('SMPL.txt','r', encoding='UTF-8')
smpl = f.read()
f.close()

bot = telebot.TeleBot('5736196885:AAGZRoxfV0zecBIsYEYEtrO4lMUAVRQM-vs')
CHANNEL_NAME = '@your_navigator_bot'
# CHANNEL_NAME = '@https://t.me/your_navigator_bot'
# CHANNEL_NAME = '@t.me\your_navigator_bot'

@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("BOSHKY")
    item2 = types.KeyboardButton("HUSKY")
    item3 = types.KeyboardButton("BRUSKO20")
    item4 = types.KeyboardButton("HQD")
    item5 = types.KeyboardButton("MAD")
    item6 = types.KeyboardButton("VooDoo_Salt")
    item7 = types.KeyboardButton("HotSpot")
    item8 = types.KeyboardButton("BRUSKO50")
    item9 = types.KeyboardButton("SMPL")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)
    markup.add(item5)
    markup.add(item6)
    markup.add(item7)
    markup.add(item8)
    markup.add(item9)
    bot.send_message(m.chat.id, 'Для получения информации выберете одну из кнопок ниже', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.strip() == 'BOSHKY':
        answer = boshky
    if message.text.strip() == 'HUSKY':
        answer = husky
    if message.text.strip() == 'BRUSKO20':
        answer = brusko20
    if message.text.strip() == 'HQD':
        answer = hqd
    if message.text.strip() == 'MAD':
        answer = mad
    if message.text.strip() == 'VooDoo_Salt':
        answer = voodoo_salt
    if message.text.strip() == 'HotSpot':
        answer = hotspot
    if message.text.strip() == 'BRUSKO50':
        answer = brusko50
    elif message.text.strip() == 'SMPL':
        answer = smpl
    bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True, interval = 0)