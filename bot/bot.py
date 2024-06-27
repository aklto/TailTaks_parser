import telebot
from telebot import types
from parser.parser import scrape_latest_articles
from model.mistral_api import generate_summary
from keys.key import BOT_TOKEN

temp = 0


def run_bot():
    url = 'https://www.iopet.ru/articles/'
    latest_articles = scrape_latest_articles(url)

    article_list_content = []
    article_list_title = []
    for title, content in latest_articles.items():
        article_list_content.append(content)
        article_list_title.append(title)

    print("увы")

    bot = telebot.TeleBot(BOT_TOKEN)

    @bot.message_handler(commands=['start'])
    def handle_start(message):
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        button1 = types.KeyboardButton("Перезагрузка")
        button2 = types.KeyboardButton("Далее")
        button3 = types.KeyboardButton("Опубликовать")
        keyboard.add(button1, button2, button3)

        bot.send_message(message.chat.id, "Пауки во фритюре", reply_markup=keyboard)

    @bot.message_handler(func=lambda message: message.text == "Перезагрузка")
    def handle_button1(message):
        global temp
        bot.send_message(message.chat.id, "Дождитесь перезагрузки...")
        article_list_content = []
        # article_list_title = []
        for title, content in latest_articles.items():
            article_list_content.append(content)
            # article_list_title.append(title)
        temp = 0
        bot.send_message(message.chat.id, "Перезагрузка завершена")

    @bot.message_handler(func=lambda message: message.text == "Далее")
    def handle_button2(message):
        global temp
        summary = generate_summary(article_list_content[temp])
        temp += 1
        # bot.send_message(message.chat.id, article_list_title[temp])
        bot.send_message(message.chat.id, summary)

    @bot.message_handler(func=lambda message: message.text == "Опубликовать")
    def handle_button3(message):
        bot.send_message(message.chat.id, "В разаботке")

    bot.polling(none_stop=True)