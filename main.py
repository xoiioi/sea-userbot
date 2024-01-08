from pyrogram import Client, filters
from ping3 import ping, verbose_ping
from pyrogram.errors import FloodWait
import time
import random
from logging import *
import logging
from datetime import datetime
import os
import requests
from pyrogram import *
import wikipedia
from phonenumbers.phonenumberutil import NumberParseException
from phonenumbers import parse
from phonenumbers import geocoder
from phonenumbers import timezone
from phonenumbers import carrier
import phonenumbers
import sqlite3
import emoji
from heart import heart_emoji
import pyjokes
from googletrans import Translator

translator = Translator()
api_id = "api id"
api_hash = "api hash"

warnings = {}
prefixe = ['.', '!', 'sea!', '-']
now = datetime.now()
openweathermap_api_key = '28f135a7fc933bddedd6bd891fe407b7'

if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')
wikipedia.set_lang("ru")

app = Client("sea", api_id=api_id, api_hash=api_hash)

logging.basicConfig(
	level=logging.INFO,
	format="[%(levelname)s] %(message)s"
    )
def get_weather(city):
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweathermap_api_key}"
    response = requests.get(api_url)
    weather_data = response.json()

    if response.status_code == 200:
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        return f"🌡️ Температура в городе {city}: {temperature}°C, {description}"
    else:
        return "🕳️ Не удалось получить информацию о погоде."

@app.on_message(filters.command(["type", "ввести", "тайп"], prefixes=prefixe) & filters.me)
def type(client_object, message):
    input_text = message.text.split(".type ", maxsplit=1)[1]
    temp_text = input_text
    edited_text = ""
    typing_symbol = ""

    while edited_text != input_text:
        try:
            message.edit(edited_text + typing_symbol)
            time.sleep(0.05)
            edited_text = edited_text + temp_text[0]
            temp_text = temp_text[1:]
            message.edit(edited_text)
            time.sleep(0.05)
        except FloodWait:
            print("[WARN] Message limit exceeded")


@app.on_message(filters.command(["spam", "спамнуть", "заспам", "спам"], prefixes=".")& filters.me)
def spam(client, message):
	text = message.text
	text.split()[1:]
	text = text[1]
	while True:
		randomint = random.randint(1111, 9999)
		app.send_message(message.chat.id, f'{text} ||' + str(randomint) + '||')
@app.on_message(filters.command("help", prefixes=prefixe)& filters.me)
def helpcommand(client, message):
	messagehelp = """🛟 Помощь по коммандам

- 𝒖𝒏𝒃𝒂𝒏
Разбанивает забаненого юзера (ответом на сообщение)
- 𝒖𝒏𝒎𝒖𝒕𝒆
Размучивает замученного юзера (ответом на сообщение)
- 𝒎𝒖𝒕𝒆
Мутит юзера (ответом на сообщение)
- 𝒃𝒂𝒏
Банит юзера (ответом на сообщение)
- 𝒖𝒏𝒑𝒊𝒏𝒂𝒍𝒍
Открепляет все сообщения
Ставит слоумо в чате
- 𝒕𝒊𝒎𝒆
Ударить юзера
- 𝒇𝒖𝒄𝒌
😨
Спамит сообщениями
- 𝐩𝐨𝐬𝐭 [𝐔𝐑𝐋]
Отправляет ПОСТ запрос на сайт
- 𝐠𝐞𝐭 [𝐔𝐑𝐋]
Отправляет ГЕТ запрос на сайт
- 𝐛𝐨𝐦𝐛𝐞𝐫 [номер]
Кидает легкий спам звонками и сообщениями на номер
- 𝒍𝒊𝒔𝒕𝒆𝒏
Включает режим 𝑳𝒊𝒔𝒕𝒆𝒏 (пишет ваши сообщения в консоль)
- 𝒚 𝒂𝒏𝒅𝒆𝒙
Поиск в Яндексе
- 𝒄𝒓𝒆𝒂𝒕𝒆_𝒈𝒓𝒐𝒖𝒑 [название]
Создать группу
- 𝒄𝒎𝒅 [комманда]
Отправить комманду в консоль
- 𝒘𝒆𝒂𝒕𝒉𝒆𝒓 [город(поддерживает русский язык и английский)]
Показывает погоду в любом городе
- 𝒊𝒅 [@юзернейм]
Показывает юзернейм человека
- 𝒓𝒆𝒃𝒐𝒐𝒕
Перезагрузить бота
- 𝒘𝒊𝒌𝒊𝒑𝒆𝒅𝒊𝒂 [запрос]
Посмотреть в Википедии что либо
- 𝒊𝒏𝒇𝒐
Информация о юзерботе"""
	app.send_message(message.chat.id, messagehelp)	
@app.on_message(filters.command(["info", "инфа", "инфо"], prefixes=".")& filters.me)
def info(client, message):
	app.send_photo(message.chat.id,"https://i.postimg.cc/jdBff6Pm/164-20240103194348.png")
	system_name = os.name
	app.send_message(message.chat.id, f"Префиксы: {prefixe}\nСтатус: Developer\n👨‍💻 Разработчик: ||@TimkaLab||\n🌊 Название юзербота: **Sea**\n💬 Чат: Soon\n🛟 Помощь по коммандам: help")
@app.on_message(filters.command(["ban", "бан", "забан", "забанить"], prefixes=prefixe)& filters.me)
def ban(client, message): 
    app.ban_chat_member(message.chat.id,message.reply_to_message.from_user.id) 
    app.send_message(message.chat.id,f"👤 {message.reply_to_message.from_user.mention} **Успешно забанен | Sea**")
@app.on_message(filters.command(["mute", "замут", "мут", "замутить"], prefixes=prefixe)& filters.me)
def mute(client, message):  
    app.restrict_chat_member(message.chat.id,f"🔇 {message.reply_to_message.from_user.mention} **Успешно замучен**")
@app.on_message(filters.command("unpinall", prefixes=prefixe)& filters.me)
def unpinall(client, message):
	app.unpin_all_chat_messages(message.chat.id)
@app.on_message(filters.command(["create_group", "группа_создать", "создать_группу"], prefixes=prefixe)& filters.me)
def creategroup(client, message):
	msg = message.text
	msg = msg.split(" ")
	msg.remove(msg[0])
	msg = " ".join(msg)
	app.create_group(msg, 5506090801)
	app.send_message(message.chat.id, '✅ **Группа создана**')
@app.on_message(filters.command(["unmute", "унмут", "размут"], prefixes=prefixe)& filters.me)
def unmute(client, message):
	app.unmute_chat_member(message.chat.id, message.reply_to_message)
	app.send_message(message.chat.id, f"🔇 {message.reply_to_message.from_user.mention} **Успешно размучен**")
@app.on_message(filters.command(["unban", "разбан", "унбан"], prefixes=prefixe)& filters.me)
def unban(client, message):
	app.unban_chat_member(message.chat.id, message.reply_to_message)
	app.send_message(message.chat.id, f"👤 {message.reply_to_message.from_user.mention} успешно разбанен")
@app.on_message(filters.command(["timer", "таймер"], prefixes=prefixe)& filters.me)
def timer(client, message):
	msg = message.text
	msg = msg.split(" ")
	msg.remove(msg[0])
	msg = " ".join(msg)
	app.send_message(message.chat.id, '⏰ **Поставлен таймер на ' + msg + 'сек**')
	time.sleep(int(msg))
	app.send_message(message.chat.id, '⏰ **Прошло ' + msg + 'сек!**')
@app.on_message(filters.command(["time", "время", "врем"], prefixes=prefixe)& filters.me)
def timemsc(client, message):
	current_time = now.strftime("%H:%M:%S")
	app.send_message(message.chat.id, '⌚ **Текущее время по МСК ' + current_time)
@app.on_message(filters.command(["yandex", "яндекс"], prefixes=prefixe)& filters.me)
def search_on_yandex(client, message):
	msg = message.text
	msg = msg.split(" ")
	msg.remove(msg[0])
	msg = " ".join(msg)
	user_query = msg
	blok_list = user_query.split()
	url_query = '%20'.join(blok_list)
	url = 'https://yandex.ru/search/?text=' + url_query + '&lr=213'
	app.send_message(message.chat.id, url)
@app.on_message(filters.command(["post", "пост"], prefixes=prefixe)& filters.me)
def request(client, message):
	msg = message.text
	msg = msg.split(" ")
	msg.remove(msg[0])
	msg = " ".join(msg)
	response = requests.post(msg)
	app.send_message(message.chat.id, f'🛜 **Отправлен POST запрос на сайт** ||{msg}||\n**Статус запроса: ' + str(response.status_code))
@app.on_message(filters.command(["get", "гет"], prefixes=prefixe)& filters.me)
def request(client, message):
	msg = message.text
	msg = msg.split(" ")
	msg.remove(msg[0])
	msg = " ".join(msg)
	response = requests.get(msg)
	app.send_message(message.chat.id, f'🛜 **Отправлен GET запрос на сайт** ||{msg}||\n**Статус запроса: ' + str(response.status_code))
@app.on_message(filters.command(["bomber", "бомбер", "бомб"], prefixes=prefixe)& filters.me)
def bomber(client, message):
	msg = message.text
	msg = msg.split(" ")
	msg.remove(msg[0])
	msg = " ".join(msg)
	app.send_message('ryyddbot', '📲 Спам')
	time.sleep(1)
	app.send_message('ryyddbot', msg)
	time.sleep(1)
	app.send_message('ryyddbot', '2')
	app.send_message(message.chat.id, '📲 **Бомбер запущен**')
@app.on_message(filters.command(["heart", "сердце"], prefixes=prefixe)& filters.me)
def heart(client, message):
	app.send_message(message.chat.id, "⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣶⣶⣦⠀⠀\n⠀⠀⣠⣤⣤⣄⣀⣾⣿⠟⠛⠻⢿⣷⠀\n⢰⣿⡿⠛⠙⠻⣿⣿⠁⠀⠀⠀⢸⣿⡇\n⢿⣿⣇⠀⠀⠀⠈⠏⠀⠀⠀⠀⣼⣿⠀\n⠀⠻⣿⣷⣮⣤⣀⠀⠀⠀⠀⣾⡿⠃⠀\n⠀⠀⠀⠀⠉⠉⠻⣿⣄⣴⣿⠟⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣿⡿⠟⠁⠀⠀⠀⠀")
@app.on_message(filters.command(["cmd", "кмд"], prefixes=prefixe)& filters.me)
def cmdshku(client, message):
	msg = message.text
	msg = msg.split(" ")
	msg.remove(msg[0])
	msg = " ".join(msg)
	ponpon = os.system(msg)
	app.send_message(message.chat.id, f"✅ ** Комманда {msg} отправлена в терминал**")
@app.on_message(filters.command(["weather", "погода"], prefixes=prefixe)&filters.me)
def weather_command(client, message):
    # Извлекаем название города из текста сообщения
    city = message.text.split(" ", 1)[1].strip() if len(message.text.split(" ", 1)) > 1 else None

    if city:
        weather_info = get_weather(city)
        app.send_message(message.chat.id, weather_info)
    else:
        weather_info = "❌ Укажите название города после команды weather."
    
@app.on_message(filters.command(["id", "айди"], prefixes=prefixe)& filters.me)
def getid(client, message):
    msg = message.text
    msg = msg.split(" ")
    msg.remove(msg[0])
    msg = " ".join(msg)
    try:
    	chat = app.get_chat(msg)
    	chat_id = chat.id
    	app.send_message(message.chat.id, f"🆔 **Telegram ID: {chat_id}**")
    except:
    	print('[ERROR] Username not found')
    	app.send_message(message.chat.id, '⛔ **Ошибка отправлена в логи**')
@app.on_message(filters.command(["restart", "рестарт", "перезапуск"], prefixes=prefixe))
def restart(client, message):
	app.send_message(message.chat.id, '🔃 **Бот перезапускается...**')
	os.system('cd core')
	os.system('python reboot.py')
@app.on_message(filters.command(["пинг", "ping", "хост"], prefixes=prefixe)& filters.me)
def checkpingg(client, message):
    start_time = time.time()
    # Отправляем запрос на сервер
    client.send_message(message.chat.id, "Получение пинга...")
    end_time = time.time()
    # Вычисляем время обработки запроса
    response_time = end_time - start_time
    # Отправляем сообщение со временем обработки
    client.send_message(message.chat.id, f"🏓 **Pong! Время обработки запроса: {str(response_time)[:4]} секунд**")
@app.on_message(filters.command(["wikipedia", "вики", "википедия"], prefixes=prefixe)& filters.me)
def wikipedia_command(client, message):
	msg = message.text
	msg = msg.split(" ")
	msg.remove(msg[0])
	msg = " ".join(msg)
	results = wikipedia.search(msg)
	if results:
	   	page = wikipedia.page(results[0])
	   	app.send_message(message.chat.id, page.title + '\n' + page.summary)
	else:
		app.send_message(message.chat.id, '🚫 **Не найдено**')
@app.on_message(filters.command(["hit", "ударить", "вьебать"], prefixes=prefixe)& filters.me)
def ydar(client, message):
	self_username = "@TimkaLab"
	ddks = f'{message.reply_to_message.from_user.mention}'
	app.send_photo(message.chat.id, "https://i.postimg.cc/hPstLW8Z/165-20240104165750.png")
	app.send_message(message.chat.id, f"""
	
	{self_username} ударил {ddks}""")
@app.on_message(filters.command(["fuck", "трах", "выебать"], prefixes=prefixe)& filters.me)
def ydar(client, message):
	self_username = "@TimkaLab"
	ddks = f'{message.reply_to_message.from_user.mention}'
	video = open('assets/fuckmem.mp4', 'rb')
	app.send_video(message.chat.id, video)
	app.send_message(message.chat.id, f"""
	
	{self_username} трахнул {ddks}""")
@app.on_message(filters.command(["hug", "обнять"], prefixes=prefixe)& filters.me)
def shshsuuuiiivan(client, message):
	self_username = "@TimkaLab"
	ddks = f'{message.reply_to_message.from_user.mention}'
	app.send_message(message.chat.id, f"""
	
	{self_username} обнял {ddks}""")
@app.on_message(filters.command(["heartanim", "хеартаним"], prefixes=prefixe)& filters.me)
def heartanim(client, message):
	bumshkd = message.text.split("heartanim", maxsplit=1)[1] + "__"
	end_message = "💛" + "__"
	for i in range(len(heart_emoji)):
	       message.edit(emoji.emojize(emoji.demojize(heart_emoji[i])))
	       time.sleep(0.325)
	message.edit(end_message)
@app.on_message(filters.command("bfgfarm", prefixes=prefixe)& filters.me)
def bfgshka(client, message):
	
	while True:
		app.send_message(message.chat.id, "Ограбить казну")
		time.sleep(0.5)
		app.send_message(message.chat.id, "Купить биткоин 10000000")
		time.sleep(0.5)
		app.send_message(message.chat.id, "Купить биткоин 1000000")
		time.sleep(0.5)
		app.send_message(message.chat.id, "Купить биткоин 100000")
		time.sleep(0.5)
		app.send_message(message.chat.id, "Купить биткоин 10000")
		time.sleep(0.5)
		app.send_message(message.chat.id, "Купить биткоин 1000")
		time.sleep(0.5)
		app.send_message(message.chat.id, "Купить биткоин 100")
		time.sleep(0.5)
		app.send_message(message.chat.id, "Купить биткоин 10")
		time.sleep(0.5)
		app.send_message(message.chat.id, "Мой сад")
		app.send_message(message.chat.id, "Сад полить")
@app.on_message(filters.command(["доброе утро", "bobroe"], prefixes=prefixe)& filters.me)
def hdhdhs(client, message):
	while True:
		try:
			message.edit("🌅 доброе 🌅")
			time.sleep(2)
			message.edit("☀️ утро ☀️")
			time.sleep(2)
		except FloodWait as e:
			pass
@app.on_message(filters.command(["joke", "шутка", "анекдот"], prefixes=prefixe)& filters.me)
def joke_gen(client, message):
     joke = pyjokes.get_joke()
     joke_result = translator.translate(joke, dest='ru')
     app.send_message(message.chat.id, joke_result.text)
@app.on_message(filters.command("python", prefixes=prefixe)& filters.me)
def pythonxhi(client, message):
     msg = message.text
     msg = msg.split(" ")
     msg.remove(msg[0])
     msg = " ".join(msg)
     msg()
print("""
                 
  ___  ___  __ _ 
 / __|/ _ \/ _` |
 \__ \  __/ (_| |
 |___/\___|\__,_|
                 
""")
print('\n')
print('─── ⋆⋅☆⋅⋆ ──')
self_id = 5506090801

app.run()
app.send_message(self_id, "Бот запущен")
