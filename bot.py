import os
import discord


roles = {
        'me' : 'ME Team',
        'me team' : 'ME Team',
        'mechanical' : 'ME Team',
        'mechanical team' : 'ME Team',

        'electrical team' : 'EE Team',
        'ee team' : 'EE Team',
        'ee' : 'EE Team',

        'sw' : 'Software Team',
        'software' : 'Software Team',
        'software team' : 'Software Team',

        'atlo' : 'ATLO Team',
        'atlo team' : 'ATLO Team',


        'aero' : 'My Dudes',
        'aero team' : 'Aero Team',
        'aerospace team' : 'Aero Team'}

with open("token") as f:
    token = f.readline().strip('\n')

client = discord.Client()


@client.event
async def on_message(message):
    member = message.author
    #ignore self messages, or messages that mention the bot
    if member == client.user or client.user not in message.mentions:
        return
    # remove discord username in message
    content = message.content[22:].strip().lower()
    # escape null
    if content is not None:
        role_to_add = roles.get(content)
        if not role_to_add:
            await message.channel.send('role must be one of: me, sw, atlo, aero, ee')
            return
        # get role object
        role = discord.utils.get(message.guild.roles, name=role_to_add)
        await member.add_roles(role)
        await message.channel.send(f'you have been added to {role}')

    else:
        await message.channel.send('role must be one of: me, sw, atlo, aero, ee')


#@client.event
#async def on_member_join(member):
#    await member.create_dm()
#    await member.dm_channel.send(
#        f'Hi {member.name}, reply with "me, sw, atlo, aero, or ee" to be added to your respective team'
#    )


client.run(token)
