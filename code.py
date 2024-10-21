@bot.tree.command(name="say", description="Fait dire au bot le message que tu veux.")
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.allowed_installs(guilds=True, users=True)
async def say(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(message) 

#commande Discord.PY - Sonarri
