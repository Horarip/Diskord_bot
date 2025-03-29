import discord
from discord.ext import commands

# ==================== NASTAVENÍ BOTA ====================

intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)

# ==================== EVENTY ====================

@bot.event
async def on_ready():
    print(f'✅ Bot {bot.user} je online!')

# ==================== SPRÁVA TO-DO LISTU ====================

tasks = []  # Seznam úkolů

@bot.command(name="add")
async def add_task(ctx, *, task):
    """Přidání úkolu do seznamu"""
    tasks.append(task)
    await ctx.send(f'✅ Úkol přidán: {task}')

@bot.command(name="list")
async def list_tasks(ctx):
    """Zobrazení všech úkolů"""
    if not tasks:
        await ctx.send("📝 Seznam úkolů je prázdný.")
    else:
        message = "**📋 To-Do List:**\n"
        for i, task in enumerate(tasks, 1):
            message += f"{i}. {task}\n"
        await ctx.send(message)

@bot.command(name="remove")
async def remove_task(ctx, index: int):
    """Odebrání úkolu podle indexu"""
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        await ctx.send(f'🗑 Úkol odstraněn: {removed}')
    else:
        await ctx.send("⚠ Neplatné číslo úkolu.")

@bot.command(name="clear")
async def clear_tasks(ctx):
    """Vyčištění celého seznamu úkolů"""
    tasks.clear()  
    await ctx.send("🧹 Seznam úkolů byl vyčištěn.")

# ==================== SPUŠTĚNÍ BOTA ====================

bot.run("MTM1NDEzMzMwNjAwOTk4MDk1OA.GqEyvl.SAlznMqHGpwLiQUQir5bwxlmoI_x-FIkWe2fbo")
