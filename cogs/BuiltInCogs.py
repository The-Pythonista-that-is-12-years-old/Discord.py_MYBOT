# NOTE: BuiltInCogs.py is the Built In Cog. Pretty self-explanatory.

import random
import time
import math as m
import os
import asyncio
from configparser import ConfigParser
import datetime

from discord.ext import commands
import discord

configure = ConfigParser()
configure.read('community_bot_info.txt')
# debug = configure.get('debug_info', 'debug')

debug = True
shutdown = False
going_to_run_debug = True
beta_mode = False
bot_shutdown_message = 'Sorry! The bot is shut down by the owner! Try again later!'
beta_testing_message = 'Sorry! The bot is only available for selected beta testers! Try again later!'


# TODO: Make all commands following beta mode patterns

# UPDATE: 0.4.0 will include DIFFERENT BOT OWNED BY BRANDON. STATUS: FINISH
# UPDATE: 0.4.0 will also include maybe (BETA MODE). STATUS: CANCELED
# UPDATE: 0.4.0 will include NEW COMMANDS. STATUS: FINISH
# UPDATE: 0.4.0 will include FIX COMMANDS. STATUS: FINISH
# UPDATE: 0.4.0 will include deprecation of cogs.BfbCogs, which will turn into cogs.ExtraFunCommands. STATUS: FINISH
# UPDATE: 0.4.0 will include slight bug fixes and performance improvements. STATUS: FINISH

# UPDATE: 0.4.1 will include COMPLETELY reworked help commands. STATUS: PENDING

class DebugAndEvents(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def is_guild_owner():
        def predicate(ctx):
            return ctx.guild is not None and ctx.guild.owner_id == ctx.author.id

        return commands.check(predicate)

    @commands.Cog.listener()
    async def on_ready(self):
        if not shutdown:
            await self.bot.change_presence(status=discord.Status.online, activity=discord.Game('Coding with Brandon'))
        else:
            await self.bot.change_presence(status=discord.Status.online, activity=discord.Game('Shut down'))

        if not shutdown:
            print('The discord bot is now online')
        else:
            print('The discord bot is now online, but it is shutdown')

        if not beta_mode:
            print('The discord bot is available to anyone')
        else:
            print('The discord bot is now in beta mode. This means that only a few people can access it')

    while going_to_run_debug:
        if not debug:
            print('Debug is set to False. Custom syntax will be used.')

            @commands.Cog.listener()
            async def on_command_error(self, ctx, error):
                if isinstance(error, commands.CheckFailure):
                    await ctx.send('Sorry. It looks like you do not have permission to use that command.')
                elif isinstance(error, commands.MissingRequiredArgument):
                    await ctx.send('Sorry. It looks like you forgot an argument')
                elif isinstance(error, commands.CommandNotFound):
                    await ctx.send('Sorry. That command does not exist')
                else:
                    brandon = self.bot.get_user(683852333293109269)
                    await brandon.send('**`ERROR ???:`** OH NO! Unknown Error!')
                    await ctx.send('**`ERROR ???"`** OH NO! Unknown Error!')

        else:
            print('Debug is set to True. Used for debugging stuff.')
            going_to_run_debug = False

        if not shutdown:
            print('Shutdown is set to False. You can use commands freely.')
        else:
            print('Shutdown is set to True. No one can use the commands.')

    @commands.command(help='COMING SOON!', brief='- used for debugging why the bot is acting so slow')
    @commands.has_any_role('MODERATOR', 'Trusted', 'Co-manager', 'Administrator', 'CEO')
    async def ping(self, ctx):
        role = discord.utils.find(lambda r: r.name == 'Trusted', ctx.guild.roles)
        roles = ctx.author.roles
        if not shutdown and not beta_mode:
            await ctx.send(f"Pong! Bot reaction time: {round(self.bot.latency * 1000)} milliseconds")
        else:
            if shutdown and not beta_mode:
                await ctx.send(bot_shutdown_message)
            if beta_mode and not shutdown:
                if role in roles:
                    await ctx.send(f"Pong! Bot reaction time: {round(self.bot.latency * 1000)} milliseconds")
                else:
                    await ctx.send(beta_testing_message)

    @commands.command(help='COMING SOON!', brief='- used to see all errors. WILL BE DM')
    @commands.has_any_role('MODERATOR', 'TRUSTED', 'Co-manager', 'Administrator', 'CEO')
    async def errors(self, ctx):
        # FIXME Complete this
        if not shutdown:
            author_dm = self.bot.get_user(ctx.author.id)
            await author_dm.send('-------------------------------------------------------- **`ALL ERRORS:`** '
                                 '--------------------------------------------------------')
            await author_dm.send('**`ERROR 001:`** for bot shutdown messages')
            await author_dm.send('**`ERROR 002:`** Failure to send messages')
            await author_dm.send('**`ERROR 003:`** Irregular usage of $emergency_lockdown')
            await author_dm.send('**`ERROR ???:`** Unknown error')
            await author_dm.send('**`MISC ERRORS:`**')
            await author_dm.send('**`MISCERROR 001:`** Took too long to respond ')
            time.sleep(0.7)
            # SEPARATOR BETWEEN ERRORS AND WARNINGS
            await author_dm.send('\n-------------------------------------------------------- **`ALL WARNINGS:`** '
                                 '--------------------------------------------------------')
            await author_dm.send('**`WARNING 001:`** Irregular usage of $draw')
            await author_dm.send('**`WARNING 002:`** Notification when Member uses $emergency_lockdown')
            await author_dm.send('**`WARNING 003:`** Author used Incomplete Commands')
            time.sleep(0.7)
            # SEPARATOR BETWEEN WARNINGS AND PYTHON ERRORS
            await author_dm.send('**`PYTHONERROR 1431:`** Speech Recognition Errors')

    @commands.command(help='COMING SOON!', brief='- used for setting debug to True or False')
    @commands.has_any_role('MODERATOR', 'Trusted', 'Co-manager', 'Administrator', 'CEO')
    async def set_debug(self, ctx, boolean):
        # FIXME: Not working. Please fix
        global debug, going_to_run_debug
        role = discord.utils.find(lambda r: r.name == 'Trusted', ctx.guild.roles)
        roles = ctx.author.roles
        if not shutdown and not beta_mode:
            if boolean.lower() == 'true':
                # configure.set('debug info', 'debug', True) <-- not in use
                time.sleep(1)
                debug = True
                going_to_run_debug = True
                await ctx.send('Set debug to True')
                # await ctx.send('Oh No! The bot developer has restricted this command!')
            elif boolean.lower() == 'false':
                # configure.set('debug info' ,'debug', False) <-- not in use
                time.sleep(1)
                debug = False
                going_to_run_debug = True
                await ctx.send('Set debug to False')
                # await ctx.send('Oh No! The bot developer has restricted this command!')
            else:
                await ctx.send('**`Unsuccessful:`** Oh No! Looks like something has gone wrong! Try again later.')
        else:
            if shutdown and not beta_mode:
                await ctx.send(bot_shutdown_message)
            if beta_mode and not shutdown:
                if role in roles:
                    if boolean.lower() == 'true':
                        # configure.set('debug info', 'debug', True) <-- not in use
                        time.sleep(1)
                        debug = True
                        going_to_run_debug = True
                        await ctx.send('Set debug to True')
                        # await ctx.send('Oh No! The bot developer has restricted this command!')
                    elif boolean.lower() == 'false':
                        # configure.set('debug info' ,'debug', False) <-- not in use
                        time.sleep(1)
                        debug = False
                        going_to_run_debug = True
                        await ctx.send('Set debug to False')
                        # await ctx.send('Oh No! The bot developer has restricted this command!')
                    else:
                        await ctx.send(
                            '**`Unsuccessful:`** Oh No! Looks like something has gone wrong! Try again later.')
                else:
                    await ctx.send(beta_testing_message)

    # FIXME: Complete this code
    @commands.command(help='COMING SOON', brief='- copy and paste code. Duh.')
    async def copy_and_paste_code(self, ctx):
        role = discord.utils.find(lambda r: r.name == 'Trusted', ctx.guild.roles)
        roles = ctx.author.roles
        if not shutdown and not beta_mode:
            await ctx.send('**`Copy and paste stuff:`**')
            await ctx.send("@commands.has_any_role('MODERATOR', 'Trusted', 'Co-manager', 'Administrator', 'CEO')")
        else:
            if not shutdown and beta_mode:
                await ctx.send(bot_shutdown_message)
            if beta_mode and not shutdown:
                if role in roles:
                    await ctx.send('**`Copy and paste stuff:`**')
                    await ctx.send(
                        "@commands.has_any_role('MODERATOR', 'Trusted', 'Co-manager', 'Administrator', 'CEO')")
                else:
                    await ctx.send(beta_testing_message)

    @commands.command(help='COMING SOON!', brief='- yay it works')
    @is_guild_owner()
    async def test_remove_role_thingy(self, ctx):
        if not shutdown and not beta_mode:
            roles = ctx.author.roles  # list of roles, lowest role first
            roles.reverse()  # list of roles, highest role first
            top_role = roles[0]  # first entry of list
            await ctx.author.remove_roles(top_role)
            await ctx.send('top role removed')
        else:
            if not shutdown and beta_mode:
                await ctx.send(bot_shutdown_message)
            if beta_mode and not shutdown:
                await ctx.send(beta_testing_message)


class OwnerOnly(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def is_guild_owner():
        def predicate(ctx):
            return ctx.guild is not None and ctx.guild.owner_id == ctx.author.id

        return commands.check(predicate)

    @commands.command(help='COMING SOON!', brief='- draws a person for #random-draw')
    @is_guild_owner()
    async def draw(self, ctx):
        # NOTE: IF I SEE ONE PERSON USING THIS...
        role = discord.utils.find(lambda r: r.name == 'Trusted', ctx.guild.roles)
        roles = ctx.author.roles
        if shutdown or not beta_mode:
            people_enter = ctx.guild.members
            rand_reward = ['access to a secret category', 'a random role', 'Discord Dungeons Money',
                           'Villager Bot Money', 'the ability to be immune to slow mode (temporary)',
                           'owner of the server for ? hours', 'Myuu PKC']
            people_choice = random.choice(people_enter)
            reward_choice = random.choice(rand_reward)

            await ctx.send('Drawing...')
            print(f"WARNING 0001: {ctx.author} has drawn a person! Did you allow them?")
            time.sleep(1.3)
            await ctx.send(f"The lucky winner is {people_choice.mention}!")
            time.sleep(0.8)
            await ctx.send("Choosing random reward...")
            time.sleep(random.randint(1, 3))
            await ctx.send(f"{people_choice.mention} won {reward_choice}!")
        if not shutdown and beta_mode:
            await ctx.send(f" **`ERROR 0001:`** {bot_shutdown_message}")
        else:
            if role in roles:
                people_enter = ctx.guild.members
                rand_reward = ['access to a secret category', 'a random role', 'Discord Dungeons Money',
                               'Villager Bot Money', 'the ability to be immune to slow mode (temporary)',
                               'owner of the server for ? hours', 'Myuu PKC']
                people_choice = random.choice(people_enter)
                reward_choice = random.choice(rand_reward)

                await ctx.send('Drawing...')
                print(f"WARNING 0001: {ctx.author} has drawn a person! Did you allow them?")
                time.sleep(1.3)
                await ctx.send(f"The lucky winner is {people_choice.mention}!")
                time.sleep(0.8)
                await ctx.send("Choosing random reward...")
                time.sleep(random.randint(1, 3))
                await ctx.send(f"{people_choice.mention} won {reward_choice}!")
            else:
                await ctx.send(beta_testing_message)

    @commands.command(help='COMING SOON!', brief='- command which loads a module.')
    @is_guild_owner()
    async def load_cog(self, ctx, *, cog: str):
        role = discord.utils.find(lambda r: r.name == 'Trusted', ctx.guild.roles)
        roles = ctx.author.roles
        if not shutdown and not beta_mode:
            try:
                self.bot.load_extension(cog)
            except Exception as e:
                await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")
            else:
                await ctx.send(f"**`SUCCESS:`** Successfully imported {cog}")
        if not shutdown and beta_mode:
            await ctx.send(f" **`ERROR 0001:`** {bot_shutdown_message}")
        else:
            if role in roles:
                try:
                    self.bot.load_extension(cog)
                except Exception as e:
                    await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")
                else:
                    await ctx.send(f"**`SUCCESS:`** Successfully imported {cog}")
            else:
                await ctx.send(beta_testing_message)

    @commands.command(help='COMING SOON!', brief='- command that unloads a module')
    @is_guild_owner()
    async def unload_cog(self, ctx, *, cog: str):
        if not shutdown:

            try:
                if cog != 'cogs.BuiltInCogs':
                    self.bot.unload_extension(cog)
                else:
                    await ctx.send('**`ERROR:`** You cannot unload BuiltInCogs')
            except Exception as e:
                await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")
            else:
                if cog != 'cogs.BuiltInCogs':
                    await ctx.send(f"**`SUCCESS:`** Successfully unloaded {cog}")
                else:
                    pass
        else:
            await ctx.send(bot_shutdown_message)

    @commands.command(help='COMING SOON!', brief='- command that reloads a module')
    @is_guild_owner()
    async def reload_cog(self, ctx, *, cog: str):
        if not shutdown:

            try:
                self.bot.unload_extension(cog)
                self.bot.load_extension(cog)
            except Exception as e:
                await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
            else:
                await ctx.send(f"**`SUCCESS:`** Successfully reloaded {cog}")
        else:
            await ctx.send(bot_shutdown_message)

    @commands.command(help='COMING SOON!', brief='- command that loads all modules')
    @is_guild_owner()
    async def load_all_cogs(self, ctx):
        # FIXME: Make this better
        if not shutdown:
            for filename in os.listdir('./cogs'):
                if filename.endswith('.py'):
                    try:
                        self.bot.load_extension(f"cogs.{filename[:-3]}")
                    except Exception as e:
                        await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
                    else:
                        await ctx.send(f'**`SUCCESS:`** Successfully loaded cogs.{filename[:-3]}')

    @commands.command(help='COMING SOON!', brief='- command that unloads all modules')
    @is_guild_owner()
    async def unload_all_cogs(self, ctx):
        # FIXME: Make this better
        if not shutdown:
            for filename in os.listdir('./cogs'):
                if filename.endswith('.py'):
                    try:
                        if filename != 'BuiltInCogs.py':
                            self.bot.unload_extension(f"cogs.{filename[:-3]}")
                    except Exception as e:
                        await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
                    else:
                        if filename != 'BuiltInCogs.py':
                            await ctx.send(f'**`SUCCESS:`** Successfully unloaded cogs.{filename[:-3]}')
        else:
            await ctx.send(bot_shutdown_message)

    @commands.command(help='COMING SOON!', brief='- command that reloads all modules')
    @is_guild_owner()
    async def reload_all_cogs(self, ctx):
        # FIXME: Make this better
        if not shutdown:
            for filename in os.listdir('./cogs'):
                if filename.endswith('.py'):
                    try:
                        if filename != 'BuiltInCogs.py':
                            self.bot.unload_extension(f"cogs.{filename[:-3]}")
                            self.bot.load_extension(f"cogs.{filename[:-3]}")
                    except Exception as e:
                        await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
                    else:
                        if filename != 'BuiltInCogs.py':
                            await ctx.send(f'**`SUCCESS:`** Successfully reloaded cogs.{filename[:-3]}')
        else:
            await ctx.send(bot_shutdown_message)


class FunCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['8ball', 'eightball'], help='COMING SOON!', brief='- fun command that possesses the '
                                                                                 'power of 8')
    async def _8ball(self, ctx, *, question):
        """- fun command that possesses the power of 8"""
        if not shutdown:
            answers = ['It is certain.', 'It is decidedly so.',
                       'without a doubt.', 'Yes - definitely.',
                       'You may rely on it.', 'As I see it, yes.',
                       'Most likely.', 'Outlook good.',
                       'Yes.', 'Signs point to yes.',
                       'Reply hazy, try again', 'Ask again later.',
                       'Better not tell you now.', 'Cannot predict now.',
                       'Concentrate and ask again.', 'Don\'t count on it.',
                       'My reply is no.', 'My sources say no.',
                       'Outlook not so good.', 'Very doubtful.',
                       'Signs point to no.', 'The answer is no.']
            time.sleep(0.6)
            await ctx.send(f"Question: {question}\nAnswer: {random.choice(answers)}")
        else:
            await ctx.send(bot_shutdown_message)

    @commands.command(aliases=['roll'], help='COMING SOON!', brief='- fun command that rolls a dice for you')
    async def dice(self, ctx):
        if not shutdown:
            await ctx.send(f"You get {random.randint(1, 6)}.")
        else:
            await ctx.send(bot_shutdown_message)

    @commands.command(help='COMING SOON!', brief='- fu')
    async def randnum(self, ctx, a: int, b: int):
        """- fun command that chooses a random number you specify"""
        if not shutdown:
            await ctx.send(f"The random number is {random.randint(a, b)}")
        else:
            await ctx.send(bot_shutdown_message)

    @commands.command(help='COMING SOON!', brief='- fun command that chooses outcomes that you specify')
    async def choice(self, ctx, *choices):
        if not shutdown:
            await ctx.send(f"The random outcome is {random.choice(choices)}")
        else:
            await ctx.send(bot_shutdown_message)

    @commands.command(help='COMING SOON!', brief='- fun command that flips a coin')
    async def coinflip(self, ctx):
        if not shutdown:
            await ctx.send('Flipping a coin...')
            flip_side = random.randint(0, 1)
            if flip_side == 0:
                await ctx.send('It is...')
                time.sleep(random.random)
                await ctx.send('Heads!')
            else:
                await ctx.send('It is...')
                time.sleep(random.random)
                await ctx.send('Tails!')
        else:
            await ctx.send(bot_shutdown_message)

    @commands.command(help='COMING SOON!', brief='- fun guessing game')
    async def guess(self, ctx):
        # IDEA: Add extra guesses.
        def is_correct(author_check):
            return author_check.author == ctx.author and author_check.content.isdigit()

        answer = random.randint(1, 10)
        await ctx.send('I am guessing a number between 1 and 10. What number is it?')
        try:
            guess = await self.bot.wait_for('message', check=is_correct, timeout=5.0)
        except asyncio.TimeoutError:
            return await ctx.send('Sorry, you took too long. It was {}.'.format(answer))

        if int(guess.content) == answer:
            await ctx.send('You are right!')
        else:
            await ctx.send('You is the worst at guessing. It is actually {}.'.format(answer))


class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help='COMING SOON!', brief='- adds. Pretty self-explanatory')
    async def add(self, ctx, x: int, y: int):
        if not shutdown:
            await ctx.send(f"The answer is {x + y}")
        else:
            await ctx.send(bot_shutdown_message)

    @commands.command(help='COMING SOON!', brief='- subtracts. Pretty self-explanatory')
    async def subtract(self, ctx, x: int, y: int):
        if not shutdown:
            await ctx.send(f"The answer is {x - y}")
        else:
            await ctx.send(bot_shutdown_message)

    @commands.command(help='COMING SOON!', brief='- multiplies. Pretty self-explanatory')
    async def multiply(self, ctx, x: int, y: int):
        if not shutdown:
            await ctx.send(f"The answer is {x * y}")
        else:
            await ctx.send(bot_shutdown_message)

    @commands.command(help='COMING SOON!', brief='- divides. Pretty self-explanatory')
    async def divide(self, ctx, x: int, y: int):
        if not shutdown:
            await ctx.send(f"The answer is {x / y}")
        else:
            await ctx.send(bot_shutdown_message)

    @commands.command(help='COMING SOON!', brief='- takes the exponents of x and y')
    async def exponent(self, ctx, x: int, y: int):
        if not shutdown:
            await ctx.send(f"The answer is {x ** y}")
        else:
            await ctx.send(bot_shutdown_message)

    @commands.command(help='COMING SOON!', brief='- takes the square root of x')
    async def sqrt(self, ctx, x: int):
        if not shutdown:
            await ctx.send(f"The answer is about {round(m.sqrt(x), 3)}")
        else:
            await ctx.send(bot_shutdown_message)

    @commands.command(help='COMING SOON!', brief='- takes the square of x')
    async def square(self, ctx, x: int):
        if not shutdown:
            await ctx.send(f"The answer is about {x ** 2}")
        else:
            await ctx.send(bot_shutdown_message)

    @exponent.error
    async def exponent_handler(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Sorry. This function does not allow decimals")


class ModeratorCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def is_guild_owner():
        def predicate(ctx):
            return ctx.guild is not None and ctx.guild.owner_id == ctx.author.id

        return commands.check(predicate)

    @commands.command(help='COMING SOON!',
                      brief='- DO NOT USE THIS. If we see you doing this, there will be consequences.')
    @is_guild_owner()
    async def emergency_lockdown(self, ctx):

        def check(author_check):
            return author_check.content == 'yes'

        if not shutdown and not beta_mode:
            brandon = self.bot.get_user(683852333293109269)
            author = ctx.author
            await ctx.send()
            await ctx.send(
                "**`WARNING 002:`** Are you SURE you want to lockdown the server? This is a pretty big deal.")
            await brandon.send(f"**`WARNING 002:`** {author} is going to lockdown the server! Did you let him?")
            print(f"WARNING 002: {ctx.author} is going to shutdown the server. Did you let him?")

            try:
                msg = await self.bot.wait_for('message', check=check, timeout=5)
            except asyncio.TimeoutError:
                await ctx.send('**`MISCERROR 001:`** Sorry! You took too long! Come back later.')

            await ctx.send('Locking down server...'.format(msg))
            await brandon.send(f"**`ALERT:`** {author} has shut down the server!")
            guild_members = ctx.guild.members
            guild_members.reverse()
            estimated_time = len(guild_members) * 3
            await ctx.send(f"ESTIMATED TIME: {estimated_time}")
            time.sleep(3)

            """for member in ctx.guild.members:
                await ctx.send(member)
                print(member)
                await ctx.send(member == 'Mr. Code#0194')
                if str(member).strip() == 'Mr. Code#0194':
                    SUPER_ADMIN_role = discord.utils.get(ctx.author.guild.roles, name="SUPER ADMIN")
                    await member.add_roles(SUPER_ADMIN_role)"""

            for member in guild_members:
                # if str(member).split() not in ['Carl-bot#1536', 'Test Bot-Community edition#9493', 'BoxBot#7194',
                # 'Villager Bot#6423', 'Myuu#9942', 'DiscordRPG#0366', 'Statbot#3472', 'TriviaBot#7948']:
                if not member.bot:
                    roles = member.roles
                    roles.reverse()
                    for role in roles:
                        try:
                            await member.remove_roles(role)
                        except:
                            pass
                    banned_role = discord.utils.get(ctx.author.guild.roles, name="BANNED")
                    await member.add_roles(banned_role)

            await ctx.send('Finished banning people!')

        if shutdown and not beta_mode:
            await ctx.send(f" **`ERROR 0001:`** {bot_shutdown_message}")
        else:
            await ctx.send(f"You dare try to use this command, {ctx.author}? I'm telling THE OWNER.")

    # FIXME: FIX THIS DARN THING
    @commands.command(help='COMING SOON!', brief='- give back normal roles to everyone')
    @is_guild_owner()
    async def giverole_lockdown(self, ctx):
        if not shutdown and not beta_mode:
            """daniel_m = await self.bot.get_user(622179028069122068)
            daniel_c = await self.bot.get_user(697487963545927696)
            anna_a = await self.bot.get_user(541402251202134035)
            aidan_c = await self.bot.get_user(683864011959435380)
            robert_b = await self.bot.get_user(724986646382116946)
            garrick_w = await self.bot.get_user(745997390116421679)
            lucas_j = await self.bot.get_user(694667608557092894)
            tom_l = await self.bot.get_user(740682401700774018)
            jason_m = await self.bot.get_user(682717716507000865)
            test_acc = await self.bot.get_user(728361350878855229)
            for member in ctx.guild.members:
                if str(member).strip() == daniel_m.name:
                    await ctx.send('dm')
                if str(member).strip() == daniel_c.name:
                    await ctx.send('dc')"""
            await ctx.send('Sorry! Work in Progress! We\'ll notify you when we fix it!')
            brandon = self.bot.get_user(683852333293109269)
            # TODO: Finish this
            await brandon.send(f"**`WARNING 003:` {ctx.author.name} has used an INCOMPLETE command. Uh Oh!")

    @commands.command(help='COMING SOON!', brief='Notifies everyone in the server with a message')
    @commands.has_role(695312034627059763)  # This is MODERATOR
    async def message_all(self, ctx, *, message):
        brandon = self.bot.get_user(683852333293109269)
        await ctx.send('Sending message...')
        for member in ctx.guild.members:
            if not member.bot and str(member).strip() != 'Mr. Code#0194':
                await member.send(f"--------------- **`INCOMING MESSAGE`** from {ctx.author.name} ---------------")
                time.sleep(1)
                try:
                    await member.send(message)
                    await brandon.send(f"**`SUCCESS:`** Successfully sent message to {member.name}")
                except:
                    await brandon.send(f"**`ERROR 002:`** Failed to send message to {member.name}")

    @emergency_lockdown.error
    async def emergency_lockdown_handler(self, ctx, error):
        if isinstance(error, discord.ext.commands.CheckFailure):
            brandon = self.bot.get_user(683852333293109269)
            await ctx.send(f"You dare try to use this command, {ctx.author.mention}? I'm telling THE OWNER.")
            await brandon.send(f"**`ERROR 003:`**{ctx.author} is trying to use the EMERGENCY LOCKDOWN command.")
            time.sleep(0.9)
            await ctx.send('P.S. You are getting a consequence.')
            roles = ctx.author.roles
            roles.reverse()
            for role in roles:
                try:
                    await ctx.author.remove_roles(role)
                except:
                    pass
            banned_role = discord.utils.get(ctx.author.guild.roles, name="BANNED")
            await ctx.author.add_roles(banned_role)


class MiscellaneousCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def is_guild_owner():
        def predicate(ctx):
            return ctx.guild is not None and ctx.guild.owner_id == ctx.author.id

        return commands.check(predicate)

    @commands.command(help='COMING SOON!', brief='- Shows the rules')
    async def rules(self, ctx):
        if not shutdown:
            await ctx.send("Rules:")
            await ctx.send("1. Do not use inappropriate or vulgar language. Do so and you will be banned.")
            await ctx.send("2. Do not exploit people for resources, such as Discord Dungeons Money, Villager Bot "
                           "Money, etc.")
            await ctx.send("3. Never spam TTS messages. Doing so will bet you banned.")
            await ctx.send("4. Do not spam, period. Exception lies in the #spam channel, but even there, slow mode is "
                           "on.")
            await ctx.send("5. Obey the Moderators. They are moderators for a reason.")
            await ctx.send("6. USE COMMON SENSE.")
            await ctx.send("7. When accessing rewards, do not use the rewards to abuse each other for any reason. "
                           "Doing so will get you banned and possibly reported")
            await ctx.send("8. Do not create a discord raid. We have defenses against it.")
            await ctx.send("9th and last one. This server is for getting to know each other. "
                           "Being rude/imprudent will get you kicked.")
            await ctx.send("Your Welcome!")
        else:
            await ctx.send(bot_shutdown_message)

    @commands.command(help='COMING SOON!', brief='- Clears messages, Require Manage Messages')
    @commands.has_permissions(manage_messages=True)
    @commands.has_any_role('MODERATOR', 'Trusted', 'Co-manager', 'Administrator', 'CEO')
    async def clear(self, ctx, amount: int):
        if not shutdown:
            roles = ctx.author.roles
            roles.reverse()
            # top_role = roles[0]
            # if top_role.id >= 730159564078448660: # this is flawed because discord message id is kinda weird.
            # else:
            # await ctx.send('OOF! You do not have a high enough role!')
            await ctx.channel.purge(limit=amount)
        else:
            await ctx.send(bot_shutdown_message)

    @commands.command(help='COMING SOON!', brief='- shows all the cogs in the cogs folder')
    @is_guild_owner()
    async def cogs(self, ctx):
        await ctx.send('**`Cogs:`**')
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await ctx.send(f"cogs.{filename[:-3]}")

    @clear.error
    async def clear_handler(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You do not have the manage message permission.')


def setup(bot):
    # NOTE: This is VERY important. DO NOT mess with this.
    bot.add_cog(DebugAndEvents(bot))
    bot.add_cog(OwnerOnly(bot))
    bot.add_cog(FunCommands(bot))
    bot.add_cog(Math(bot))
    bot.add_cog(MiscellaneousCommands(bot))
    bot.add_cog(ModeratorCommands(bot))