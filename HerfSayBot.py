from telebot import util
import telebot
Mytooken = "5573127605:AAEQ4VndSjqw9eKnkPVqBmnCzMCzt9Vhsp0"
MyBot = telebot.TeleBot(Mytooken)
MyChatID = 633283743
#large_text = open('D:\Bot\large_text.txt','rb').read()
@MyBot.message_handler(commands=['start'])
def CommandLine(message):
    MyBot.reply_to(message,"Bu bot daxil etdiyiniz ifadədəki sait və samit hərflərin sayını təyin edir.\nBir ifadə daxil edin:")
@MyBot.message_handler(func=lambda message: True)
def echo_message(message):
    print(message.chat.id)
    Saitler = ['a','ı','o','u','e','ə','i','ö','ü']
    ExtraSigns = [',','.','!','(',')',"'",'"',':',';',' ','?','-']
    SaitList = []
    Extras = 0
    Mesaj = str((message.text)).lower()
    for i in Mesaj:
        if i in ExtraSigns:
            Extras+=1
        if i in Saitler:
            SaitList.append(i)
    MyBot.reply_to(message, '{} ifadəsində {} sait, {} samit var.'.format(Mesaj, str(len(SaitList)), len(Mesaj)-(Extras+len(SaitList))))
MyBot.infinity_polling()
