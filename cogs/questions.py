from discord.ext import commands, tasks
import discord
import json



class Questions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open("data/config.json") as cf:
            config = json.load(cf)
            self.break_time = config["break_time"]
            self.true_phrase = config["true_phrase"]
            self.false_phrase = config["false_phrase"]

        self.list_channel = []

        with open("data/questions.json") as qf:
            self.questions = json.load(qf)
            print(self.questions)

    
    def isAlreadyInQuizz(self, member):
        for channel in self.list_channel:
            if (member == channel[1]):
                return True
        return False
    
    def isQuizzChannel(self, chan):
        for channel in self.list_channel:
            if (chan == channel[0]):
                return True
        return False

    @commands.Cog.listener()
    async def on_ready(self):
        print ('Logged in as {0.user}'.format(self.bot))

    
    @commands.command()
    async def salut(self, ctx):
        await ctx.send("Coucou, je suis nouveau sur le serveur !")


    @commands.is_owner()
    @commands.command()
    async def dq(self, ctx):
        """Déconnecte le bot."""
        await ctx.send("Chers amis, je vous laisse !")
        await self.bot.close()
    

    @commands.command(aliases=["smash_quizz"])
    async def smashquizz(self, ctx):
        if (not discord.utils.find(lambda x : x.name=="Héros", ctx.author.roles)):
            await ctx.send("Désolé, mais tu n'as pas le droit de participer ! :speak_no_evil:")
            return
        
        if self.isAlreadyInQuizz(ctx.author):
            await ctx.send(":interrobang: Tu es déjà en session de quizz avec moi !")
            return
        
        category = discord.utils.get(ctx.guild.categories, name="Quizz")
        channel = await ctx.guild.create_text_channel(name, overwrites={
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.author: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }, category=category, topic="Salon de Quizz Smash pour {0.name}.".format(ctx.author))

        self.list_channel.append((channel, ctx.author))

        channel.send("Bonjour ! Je vais t'interroger sur un ensemble de {0} questions ! Bon courage !".format(len(self.questions)))

    @commands.is_owner()
    @commands.command()
    async def close(self, ctx):
        if (self.isQuizzChannel(ctx.channel)):
            await self.list_ringchannels.removeChannel(ctx.channel)
        else:
            await ctx.send("Désolé, mais ça ne fonctionne pas ici !")

    @commands.command(aliases=["ans"])
    async def answer(self, ctx, args):
        await ctx.send(args)




def setup(bot):
    bot.add_cog(Questions(bot))