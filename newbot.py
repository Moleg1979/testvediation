import telebot
TOKEN = '407659995:AAGhgKR2cIMSEArPkKXKKbvA_8uUHzShHJo'
testmediationbot = telebot.TeleBot(TOKEN)
@testmediationbot.message_handler(content_types=["text"]) 
def repeat_all_messages(message): 
    testmediationbot.send_message(message.chat.id, message.text)
if __name__ == '__main__':
     testmediationbot.polling(none_stop=True)
