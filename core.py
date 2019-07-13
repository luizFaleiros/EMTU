import telegram
import time
from src.conf.Telegram.Settings import TOKEN
from src.conf.EMTU.Response import Response
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater


def getLocation(bot, update):
    message: telegram.Message = update.effective_message
    latitude = message.location.latitude
    longitude = message.location.longitude
    r = Response()
    response = r.ResponsePosition(longitude, latitude)
    for i in range(len(response)):
        bot.send_message(
            chat_id=update.message.chat_id,
            text=response[i]
        )
        time.sleep(0.5)


def start(bot, update):
    response_message = "Bem vindo a onde esta o Onibus"
    response_message += "Aqui você podera rastrear seu onibus"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def ajuda(bot, update):
    response_message = "/ajuda Mostra todos os comandos aceitos pelo bot\n"
    response_message += "/linha enviando o comando mais o numero da linha para receber quantos onibus estao ativos na linha\n"
    response_message += "Para saber os onibus quer passam no ponto em que se encontra, apenas mande sua posição\n"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def getBus(bot, update, args):
    procura = args[0]
    r = Response()
    response = r.ResponseLine(procura)
    bot.send_message(
        chat_id=update.message.chat_id, text=response)


def unknown(bot, update):
    response_message = "Desculpa comando não encontrado"
    bot.send_message(
        chat_id=update.message.chat_id, text=response_message)


def main():
    updater = Updater(token=TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler('start', start)
    )
    dispatcher.add_handler(
        CommandHandler('ajuda', ajuda)
    )
    dispatcher.add_handler(
        CommandHandler('linha', getBus, pass_args=True)
    )
    dispatcher.add_handler(
        MessageHandler(Filters.command, unknown)
    )
    dispatcher.add_handler(
        MessageHandler(Filters.location, getLocation)
    )
    dispatcher.add_handler(
        MessageHandler(Filters.location, getLocation)
    )

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()
