@bot.command()
async def mute(ctx, member: discord.Member=None):
    role = discord.utils.get(ctx.guild.roles, names='Muted')
    if not member:
        await ctx.send('Please specify a member')
        return
    await member.add_roles(role)
    await ctx.send('Added roles!')
