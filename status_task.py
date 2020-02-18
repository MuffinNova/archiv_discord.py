##########################################

@bot.event
async def on_ready():
    print('Wir sind eingeloggt als User {}'.format(bot.user.name))
    bot.loop.create_task(status_task())


##########################################
async def status_task():
    while True:
        servers = list(bot.guilds) #counts the bot guilds
        await bot.change_presence(
            activity=discord.Activity(name='', type=discord.ActivityType.listening))
        await asyncio.sleep(15)
        await bot.change_presence(activity=discord.Activity(name='', type=discord.ActivityType.watching))
        await asyncio.sleep(30)
        await bot.change_presence(
            activity=discord.Activity(name='', type=discord.ActivityType.listening))
        await asyncio.sleep(15)
        await bot.change_presence(activity=discord.Activity(name='to {0} server'.format(str(len(servers))),    #This, Ladies and Gentlemen
                                                            type=discord.ActivityType.watching))               #told you on how many servers
        await asyncio.sleep(15)                                                                                #is possible to find the Bot.