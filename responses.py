async def send_hello_messages(channel):
    for _ in range(10):
        await channel.send("BOBO!")

async def handle_response(message):
    p_message = message.content.lower()

    if p_message == "!bobo":
        await send_hello_messages(message.channel)