import disnake
from disnake.ext import commands
from disnake import FFmpegPCMAudio
import aiohttp
import random

bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all())

#event for the bot to give a role to new members
@bot.event
async def on_member_join(member):
    # Получаем объект роли, которую мы хотим выдать
    role = disnake.utils.get(member.guild.roles, name="БОМЖИ")
    if role is not None:
        # Выдача роли пользователю
        await member.add_roles(role)
        print(f"{member} получил(а) роль {role.name}.")


#that kick command for the kick members on discord server without role
@bot.slash_command(name="holokost")
async def kick_users(ctx):
    # Проверяем, является ли автор команды администратором
    if ctx.author.guild_permissions.administrator:
        for member in ctx.guild.members:
            # Проверяем, есть ли у пользователя хотя бы одна роль
            if len(member.roles) == 1:  # Пользователь всегда имеет роль @everyone, поэтому проверяем, что у него есть только одна роль
                try:
                    await member.kick(reason="No roles")
                    print(f"Пользователь {member.name} был выгнан.")
                    await ctx.send(f"Пользователь {member.name} был выгнан.")
                except Exception as e:
                    print(f"Ошибка при выгоне пользователя {member.name}: {e}")
                    await ctx.send(f"Ошибка при выгоне пользователя {member.name}: {e}")
    else:
        await ctx.send("У вас нет прав на выполнение этой команды.")



@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

#that the game for random
@bot.slash_command(name="random1")
async def roll(ctx):
    # Бросаем два кубика
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2

    await ctx.send(f'Первый кубик: {dice1}\nВторой кубик: {dice2}\nОбщая сумма: {total}')

#that the game for random
@bot.slash_command(name="random2")
async def guess(ctx, number: int):
    if number < 2 or number > 12:
        await ctx.send('Пожалуйста, выберите число от 2 до 12')
        return

    # Бросаем два кубика
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2

    if total == number:
        await ctx.send(f'Вы угадали! Сумма: {total}')
    else:
        await ctx.send(f'Вы не угадали. Сумма: {total}')



@bot.slash_command()
async def hello(ctx: disnake.AppCmdInter, target: disnake.Member = None):
    if target is None:
        await ctx.send("Привет! Как дела?")
    else:
        await ctx.send(f"Привет, {target.mention}! Как дела?")


@bot.slash_command(name="pokahohol")
async def ban_users(ctx: disnake.AppCmdInter, target: disnake.Member = None):
    if ctx.author.guild_permissions.administrator:
        try:
            await target.kick(reason="я так захотел")
            print(f"Пользователь {target.mention} был выгнан.")
            await ctx.send(f"Пользователь {target.mention} был ЗАБАНЕН.")
        except Exception as e:
            print(f"Ошибка при выгоне пользователя {target.mention}: {e}")
            await ctx.send(f"Ошибка при выгоне пользователя {target.mention}: {e}")
    else:
        await ctx.send("У вас нет прав на выполнение этой команды.")


@bot.slash_command()
async def goodbye(ctx: disnake.AppCmdInter, target: disnake.Member = None):
    if target is None:
        await ctx.send("До свидания сын тупой шлюхи! Хорошего дня!")
    else:
        await ctx.send(f"{target.mention} Пошел нахуй, сын тупой шлюхи! Хорошего дня!")


@bot.slash_command()
async def nice(ctx: disnake.AppCmdInter, target: disnake.Member = None):
        if target is None:
            await ctx.send("Иди нахуй!")
        else:
            await ctx.send(f"Иди нахуй, {target.mention}! Иди нахуй, {target.mention}! Иди нахуй, {target.mention}! Иди нахуй, {target.mention}! Иди нахуй, {target.mention}! Иди нахуй, {target.mention}!")



bot.run("")