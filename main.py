from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '5927688446:AAGw4Y3tBScHzVn6F4_BNX-XxsabFRLBDxI'
BOT_USERNAME: Final = '@MrCuacBot'


# Comandirris
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('CUAC!, gracias por chatear cuacmigo, soy MrCuacBot! :D')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('CUAC!, soy MrCuac, por favor escribe /cuac para recibir cuacs diarios. Yo responderé cualquier cosa! :)')
    
async def cuac_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('CUAC! :D')


# Manejando respuestas -> RESPUESTAS
def handle_response(text: str) -> str:
    # Añadiendo procesado de texto.
    processed: str = text.lower()
    if 'hola' in processed:
        return 'CUAC (Hola! C:)'
    if 'como estas' in processed:
        return 'Aqui andamos súper cuacs!'
    if 'ayuda' in processed:
        return 'Cuac... escribe /help mi estimade :D'
    if 'cuac' in processed:
        return 'CUAC! , tu si le sabes!'
    if 'te quiero' in processed:
        return 'Pues yo te amo <3'
    
    return 'Cuac?...'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type # Nos informa si hay un chat de grupo, o chat privado
    text: str = update.message.text # Mensaje recibido (el que podemos procesar)

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"') # Imprimiendo el ID del usuario que envia el mensaje en priv/grupo y su mensaje

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text) #Para chats privados

    print('Bot: ', response) #Esto es para el debugging
    await update.message.reply_text(response)

# Para errores de Loggeo
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('CUAC!, iniciando botsito...')
    app = Application.builder().token(TOKEN).build()

    #Comandos
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('cuac',cuac_command))

    # Mensajes
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #Errores
    app.add_error_handler(error)

    # Sondeando el bot
    print('Sondeando...')
    app.run_polling(poll_interval=3)

