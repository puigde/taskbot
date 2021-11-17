from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import csv
from datetime import date
import math as m

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
days= int(d1[:2])
months= int(d1[3:5])
years= int(d1[6:10])
weeknumber= 4*(months-1)+ m.ceil((days+2)/7) #+2 so weekcount starts on sundays 



with open("taskbotpis_read.csv", newline='') as csvfile:
    reader= csv.reader(csvfile)
    #reader is a list of lists each one containing the tasks for the 
    #user with the following syntax ['id', task1, ..., taskn, 'extrainfo']
    #extrainfo for example being the shoppinglist or the menus in our case
    tasklist= []
    for row in reader:
        tasklist.append(row)

TOKEN = (
    open("token.txt").read().strip()
)  # constant which uses telegram to recognize the bot

def startingmessage(update, context):
    """Sends a message introducing the bot."""

    text_send = "Bones, soc el taskbot del pis de les corts. Selecciona usuari: /crossfit, /puigde, /pitus"
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text_send,
    )

def tasks_crossfit(update, context):
    tasks(update, context, 0)
def tasks_pitus(update, context):
    tasks(update, context, 1)
def tasks_puigde(update, context):
    tasks(update, context, 2)

#id 0 for crossfit, 1 for pitus 2 for puigde
def tasks(update, context, id):
    """Sends a message of the tasks each person has assigned for the week."""
    text_send=''
    if (id==0): 
        text_send += "Bones Crossfit, les teves tasques d'aquesta setmana son:"
        for i in range(len(tasklist[0])-1):
            text_send+= '->'+ tasklist[0][i] + '\n'
        text_send+= '\n'
        text_send += 'Recorda que la llista de la compra actual és:\n'
        text_send += tasklist[0][-1] +'\n'*2

        if (weeknumber%3==2):
            text_send+= 'Recorda que aquesta setmana les aigues et toquen a tu ;)'

    if (id==1):
        text_send+= "Bones Pitus, les teves tasques d'aquesta setmana son: \n ->"
        if (weeknumber%2==1):
            text_send+= tasklist[1][3] + '\n'
        else:
            text_send+= tasklist[1][2] + '\n'
        text_send+= '->'+ tasklist[1][1] + '\n'
        for i in range(4,len(tasklist[1])):
            text_send+= '->' +tasklist[1][i] + '\n'
        text_send+= '\n'
        
        if (weeknumber%3==2):
            text_send+= 'Recorda que aquesta setmana les aigues et toquen a tu ;)'

    if (id==2):
        text_send+= "Bones Puigde, les teves tasques d'aquesta setmana son: \n ->"
        if (weeknumber%2==0):
            text_send+= tasklist[2][3] + '\n'
        else:
            text_send+= tasklist[2][2] + '\n'    
        text_send+= '->'+ tasklist[2][1] + '\n'
        for i in range(4,len(tasklist[2])-1):
            text_send+= '->' +tasklist[2][i] + '\n'
        text_send+= '\n'
        text_send+= "Recorda que els menús actuals son: " + tasklist[2][len(tasklist[2])-1] + '. \n\n'
        if (weeknumber%3==1):
            text_send+= "Recorda que aquesta setmana les aigues et toquen a tu ;)"
        

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text_send,
    )

# creates objects to work with Telegram
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# When bot recieves the command (eg: start), function /start is executed
dispatcher.add_handler(CommandHandler("i", startingmessage))
dispatcher.add_handler(CommandHandler("ii", startingmessage))
dispatcher.add_handler(CommandHandler("iii", startingmessage))
dispatcher.add_handler(CommandHandler("iiii", startingmessage))
dispatcher.add_handler(CommandHandler("iiiii", startingmessage))
dispatcher.add_handler(CommandHandler("iiiiii", startingmessage))
dispatcher.add_handler(CommandHandler("iiiiiii", startingmessage))
dispatcher.add_handler(CommandHandler("iiiiiiiii", startingmessage))
dispatcher.add_handler(CommandHandler("crossfit", tasks_crossfit))
dispatcher.add_handler(CommandHandler("pitus", tasks_pitus))
dispatcher.add_handler(CommandHandler("puigde", tasks_puigde))


# bot is started
updater.start_polling()

# command necessary if MacOS is used
updater.idle()