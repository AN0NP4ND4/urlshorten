import telegram.ext
import pyshorteners

api_key = "5012058543:AAHxlkVUud3NHdu-zJ31RSpkOO03ahn16AA"

def start(update , context):
  first_name = update.message.chat.first_name
  update.message.reply_text(f"""Hello {first_name} , Welcome To Bright link Shortener Bot Type /help For additional info.""")
	
def help(update , context):
	update.message.reply_text("""
	Use The Following Commands.
	
	/start -> To Start The Bot
	/help  -> For This message
	/howto -> How to use The Bot
	/about  -> To Know about us""")
	
		
def howto(update , context):
			update.message.reply_text("""
			Send Link That Starts With (http:// or https://) Only
			EXAMPLE : (https://www.google.com )
			And Wait For a Few Seconds Until
			Shorten The Link.""")
			
		
	
def about(update , context):
		update.message.reply_text("""This Bot Is Created For Shorten Links.
	
Creator --> An0np4nd4

Channels :
BRIGHT TECH(@brightt_tech)
Python Tutorial(@pyth0n_tutorial)

Subscribe Our YouTube Channel 
https://youtube.com/channel/UCAuis-A1ocYOEWZe3ecnToQ

THANKS FOR USING !

This Is First Version & Will Update Soon...""")


def handel_message(update , context):
	user_input = update.message.text
	update.message.reply_text(f"You Send : {user_input} \n SHORTENING .....")
	
	if user_input.startswith("http"):
		url_shortener = pyshorteners.Shortener()
		short_url = url_shortener.tinyurl.short(user_input)
		
		update.message.reply_text(f"DONE!,Here Is The Link Shorten : {short_url}")
	else:
		update.message.reply_text("Unacceptable Link!")
		
	
	
updater = telegram.ext.Updater(api_key , use_context = True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("howto", howto))
disp.add_handler(telegram.ext.CommandHandler("about", about))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text,handel_message))

updater.start_polling()
updater.idle()
