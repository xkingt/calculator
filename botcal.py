import telebot

bot = telebot.TeleBot("1136511305:AAFft9BdMuHsZ-vc1o1KqcfIY79JeQjNROE")

@bot.message_handler(commands=['startcal'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Привет " + message.from_user.first_name + ", ты решил что-то посчитать \nВведите число", )
	cifra1 = str(message.text)

@bot.message_handler(content_types=['text'])
def send_cifra(message):
	bot.send_message(message.chat.id, 'второе число')
	cifra2 = str(message.text)
	True
@bot.message_handler(content_types=['text'])
def send_znak(message):
	bot.send_message(message.chat.id, 'выберете знак')
	znak = str(message.text)

@bot.message_handler(content_types=['text'])
def send_rezult(message):
	if znak == '+':
		bot.send_message(message.chat.id, int(cifra1) + int(cifra2))
	elif znak == '-':
		bot.send_message(message.chat.id, int(cifra1) - int(cifra2))
	elif znak == '/':
		bot.send_message(message.chat.id, int(cifra1) / int(cifra2))
	elif znak == '*':
		bot.send_message(message.chat.id, int(cifra1) * int(cifra2))
	else:
		bot.send_message(message.chat.id, 'Выбрана другая операция')

bot.polling()
