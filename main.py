import os
import openai
import telebot


API_TOKEN = os.getenv("OPENAI_API_KEY")
openai.api_key = API_TOKEN

bot = telebot.TeleBot(os.getenv("QUIN_API_KEY"))


@bot.message_handler(func=lambda _: True)
def handle_message(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=1200,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )


    bot.send_message(chat_id=message.from_user.id, text=response.choices[0].text)



bot.polling()
