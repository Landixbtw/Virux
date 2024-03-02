import discord

@bot.event
async def on_voice_state_update(member, before, after):
    # Check if the member joined the "join_for_voice" channel
    if after.channel != None and after.channel.id == "join-for_voice".channel.id:
        #make a new channel 
        # move member to new channel

