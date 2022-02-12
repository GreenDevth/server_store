import asyncio

from discord.ext import commands
from database.Store import *
from database.Players import *


class StoreButtonEventCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_button_click(self, interaction):
        member = interaction.author
        store_btn = interaction.component.custom_id

        if store_btn == 'atv_blue':
            print(f'{member.name} clicked.')
            check_player = players_exists(member.id)

            if check_player == 1:
                player = players(member.id)
                player_coin = player[5]
                player_exp = player[6]
                player_lelvel = player[7]
                await interaction.respond(content=f'{player_coin}')
            await interaction.respond(content='player not found')
            # package = get_command(store_btn)
            # package_cmd = package.split(",")
            # await interaction.respond(content=f'{member.name} click the button {store_btn}')
            # for pack in package_cmd:
            #     await interaction.channel.send(f'{pack}')
            #     await asyncio.sleep(1)


def setup(bot):
    bot.add_cog(StoreButtonEventCommand(bot))
