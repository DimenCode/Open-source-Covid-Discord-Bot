import discord
from discord.ext import commands
from covid import Covid
import time

Token = '' #insert token here

description = '''Covid Bot'''
bot = commands.Bot(command_prefix="-", description=description)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = "Covid data"))
    print("************")
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("************")



@bot.command()
async def covid(ctx,pays):

    pays = int(pays)
    covid = Covid()
    country = covid.get_status_by_country_id(pays)

    #you can replace by "covid.get_status_by_country_name" but there is errors if there is spaces in the name
    #you can't get United kingdom'data for exemple

    # translating json to str then splitting it with ", "
    data = str(country)
    data = data.split(", ")
    # I make the result looks better and I delete all the '
    data[1] = data[1].replace("'country':", "Country :")
    data[2] = data[2].replace("'confirmed':", "Confirmed cases :")
    data[3] = data[3].replace("'active':", "Active :")
    data[4] = data[4].replace("'deaths':", "Deaths :")
    data[5] = data[5].replace("'recovered':", "Recovered :")

    # ordering all the data (\n means "go to the next line")
    texte = (
            "Covid data : \n" +
            data[1] + "\n" +
            data[2] + "\n" +
            data[3] + "\n" +
            data[4] + "\n" +
            data[5] + "\n" +
            "Date : " + (str(time.localtime().tm_mday) + "/" + str(time.localtime().tm_mon) + "/" + str(
        time.localtime().tm_year))
    )

    await ctx.send(str(texte))


 # api and basics of the code : https://www.geeksforgeeks.org/how-to-get-covid-19-update-using-covid-module-in-python/
bot.run(Token)
