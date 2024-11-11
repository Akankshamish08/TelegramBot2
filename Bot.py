from Config import *
import telebot
import openai
BOT_API="7639261615:AAHBl-NRcr-yqWUxRFWkFQN0DynfC98BTiw"
OPENAI_KEY="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"
my_id=""
chatStr = ''
def ChatModal(prompt):
    global chatStr
    openai.api_key=OPENAI_KEY
    chatStr += f"Demo: {prompt}\nSmartAI: "
    response = openai.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[chatStr],
                    temperature=1,
                    max_tokens=2048,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0,
                    response_format={
                    "type": "text"
  }
)
    print(response)
    chatStr += f"{response['choices'][0]['text']}"
    return response['choices'][0]['text']
bot = telebot.TeleBot(BOT_API)

@bot.message_handler(["start"])
def start(message):
    bot.reply_to(message,"Hello to Demobot")
@bot.message_handler()
def chat(message):
   try:
       reply = ChatModal(message.text)
       bot.reply_to(message,reply)
   except Exception as e:
       print(e)
       bot.reply_to(message,e)   
print("bot starting..")
bot.polling()