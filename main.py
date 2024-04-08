import discord
from discord_token import Token
import datetime

class MyClient(discord.Client):
  async def on_ready(self):
    print(f'Logged on as {self.user}!')

  async def on_message(self, message):
    if message.content == "!시험":
      today = datetime.datetime.date(datetime.datetime.now())
      exam_day = datetime.date(2024, 4, 26)
      delta = exam_day - today
      if delta < datetime.timedelta(days=0):
        await message.channel.send("이미 시험이 끝났습니다.")
      else:
        await message.channel.send(f"> 중간고사까지 **{delta.days}**일 남았습니다.")

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(Token)