
# команда для кика участника
@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} был кикнут из сервера.')
    
# команда для бана участника
@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} был забанен на сервере.')
    
# команда для разбана участника
@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} был разбанен на сервере.')
            return
        
# команда для очистки сообщений в канале
@client.command()
async def clear(ctx, amount=20):
    await ctx.channel.purge(limit=amount + 1)

# команда для изменения имени участника
@client.command()
async def rename(ctx, member: discord.Member, *, new_name):
    await member.edit(nick=new_name)
    await ctx.send(f'Имя участника {member.mention} изменено на {new_name}.')

# команда для создания нового текстового канала
@client.command()
async def create_text_channel(ctx, name):
    guild = ctx.guild
    await guild.create_text_channel(name)
    await ctx.send(f'Новый текстовый канал {name} создан на сервере.')

# команда для создания нового голосового канала
@client.command()
async def create_voice_channel(ctx, name):
    guild = ctx.guild
    await guild.create_voice_channel(name)
    await ctx.send(f'Новый голосовой канал {name} создан на сервере.')

# команда для выдачи роли участнику
@client.command()
async def add_role(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    await ctx.send(f'Роль {role.name} выдана участнику {member.mention}.')

# команда для снятия роли у участника
@client.command()
async def remove_role(ctx, member: discord.Member, role: discord.Role):
    await member.remove_roles(role)
    await ctx.send(f'Роль {role.name} снята у участника {member.mention}.')
	
	

@client.command()
async def remove_role(ctx, member: discord.Member, role: discord.Role):
    await member.remove_roles(role)
    await ctx.send(f'Роль {role.name} снята у участника {member.mention}.')

# команда для перемещения участника в другой голосовой канал
@client.command()
async def move(ctx, member: discord.Member, channel: discord.VoiceChannel):
    await member.move_to(channel)
    await ctx.send(f'Участник {member.mention} перемещен в канал {channel.name}.')

# команда для изменения названия роли
@client.command()
async def rename_role(ctx, role: discord.Role, *, new_name):
    await role.edit(name=new_name)
    await ctx.send(f'Название роли {role.mention} изменено на {new_name}.')

# команда для выдачи мьюта участнику
@client.command()
async def mute(ctx, member: discord.Member, *, reason=None):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.add_roles(role, reason=reason)
    await ctx.send(f'Участник {member.mention} замьючен на сервере.')

# команда для снятия мьюта у участника
@client.command()
async def unmute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.remove_roles(role)
    await ctx.send(f'Участник {member.mention} размьючен на сервере.')

# команда для приглашения бота на сервер
@client.command()
async def invite(ctx):
    invite_link = await ctx.channel.create_invite()
    await ctx.send(f'Пригласительная ссылка на сервер: {invite_link}')
# Конец стандартных команд
