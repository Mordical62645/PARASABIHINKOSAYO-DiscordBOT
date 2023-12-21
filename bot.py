import discord
import responses

intents = discord.Intents(messages=True)
intents = discord.Intents.default()
intents = discord.Intents().all()

async def send_message(message, user_message, is_private):
    try:
        await responses.handle_response(message)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTE4NzM0Njc0NjAyNDY2NTA5OA.GHNR1v.62VmDtOFk8mE9y2l0dO7GzvFxpYY9nxhkQ9pE0'
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message and user_message.startswith("?"):
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)