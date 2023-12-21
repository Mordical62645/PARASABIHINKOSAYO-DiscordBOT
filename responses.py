async def send_hello_messages(channel):
    for _ in range(10):
        await channel.send("MESSAGE DUPLICATE")

async def handle_response(message):
    p_message = message.content.lower()

    if p_message == "MESSAGE":
        await send_hello_messages(message.channel)