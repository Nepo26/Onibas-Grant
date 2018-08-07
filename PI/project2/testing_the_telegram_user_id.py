import telepot
import pprint from 
bot = telepot.Bot('466963914:AAGJpIKVBG4Nc-tZagqDNeZ6g5U_lvAu50w')

#for i in range(0,5):
print(bot.getUpdates()[0])

print(bot.getUpdates()[0]['message']['from']['id'])

#    print("\n")
