import twitchio
from twitchio.ext import commands

# Replace *** by your infos


# CREATE AN APPLICATION IN: https://dev.twitch.tv/console
# AND GET THE CLIENT ID
bot_client = '***'

# oath YOU CAN GET HERE: https://twitchapps.com/tmi/
twitch_oath = '***'

# the channel where you want to get the chat
channel_name = '***'

# Créez une classe de bot Twitch
class TwitchBot(commands.Bot):

    def __init__(self):
        super().__init__(token=twitch_oath, prefix='!', initial_channels=[channel_name])

    # Événement appelé lorsque le bot est prêt à être utilisé
    async def event_ready(self):
        print(f'Bot connecté à Twitch en tant que {self.nick}')

    # Événement appelé lorsqu'un message est reçu dans le chat
    async def event_message(self, message):
        # N'afficher que les messages du chat (pas les commandes du bot)
        if message.author.name.lower() != bot_client.lower():
            print(f'{message.author.name}: {message.content}')

        # Passez le message à d'autres événements/commandes
        await self.handle_commands(message)

    # Commande personnalisée pour afficher un message dans le chat
    @commands.command()
    async def sayhello(self, ctx):
        await ctx.send(f"Hello, {ctx.author.name}!")

# Créez une instance du bot Twitch
bot = TwitchBot()

# Lancez le bot
try:
    bot.run()
except twitchio.AuthenticationError as e:
    print(f'Erreur d\'authentification Twitch: {e}')