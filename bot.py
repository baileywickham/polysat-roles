import os
import discord

ERRMSG = 'role must be one of: me, sw, atlo, aero, ee, alumni, pr'

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

        'ATLO' : 'ATLO Team',
        'atlo' : 'ATLO Team',
        'atlo team' : 'ATLO Team',

        'alumn' : 'Alumni',
        'alum' : 'Alumni',
        'alumni' : 'Alumni',

        'pr' : 'PR Team',
        'pr team' : 'PR Team',

        'aero' : 'Aero Team',
        'aero team' : 'Aero Team',
        'aerospace team' : 'Aero Team'}

with open("/root/polysat-roles/token") as f:
    token = f.readline().strip('\n')

client = discord.Client()


@client.event
async def on_message(message):
    botid = str(client.user.id)
    member = message.author
    #ignore self messages, or messages that mention the bot
    if member == client.user:
        return

    # if bot not mentioned, skip
    if client.user not in message.mentions and '692172262681346140' not in message.content:
        print(message.content)
        return

    # remove discord username in message
    content = message.content[22:].strip().lower()
    #content = message.content.replace(f'<@!{botid}>', '').strip(' ').lower()
    # escape null
    if content is not None:
        role_to_add = roles.get(content)
        if not role_to_add:
            await message.channel.send(ERRMSG)
            return
        # get role object
        role = discord.utils.get(message.guild.roles, name=role_to_add)
        await member.add_roles(role)
        await message.channel.send(f'you have been added to {role}')

    # Sent blank message
    else:
        await message.channel.send(ERRMSG)

client.run(token)
