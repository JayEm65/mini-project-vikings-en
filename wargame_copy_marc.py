# WAR !!!
from vikingsClasses_copy_marc import War, Viking, Saxon
import random
import time
from colorama import Fore, Style, init
import pygame

# Colorama
init(autoreset=True)

# Pygame mixer
pygame.mixer.init()

# Load sound files
victory_sound = pygame.mixer.Sound("sounds/victory_sound.wav")
death_sound = pygame.mixer.Sound("sounds/death_sound.wav")
viking_attack_sound = pygame.mixer.Sound("sounds/Viking_attack_sound.wav")
saxon_attack_sound = pygame.mixer.Sound("sounds/Saxon_attack_sound.wav")

soldier_names = ["albert", "andres", "archie", "dani", "david", "gerard", "german", "graham", "imanol", "laura"]
great_war = War()

# Create 5 Vikings
for i in range(0, 5):
    if i:
        great_war.addViking(Viking(soldier_names[random.randint(0, 9)].capitalize(), 100, random.randint(20, 50)))

# Create 5 Saxons
for i in range(0, 5):
    if i:
        great_war.addSaxon(Saxon(100, random.randint(20, 50)))

round = 0
while great_war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    print(Fore.WHITE + f"Round {round}... The battle rages on...\n")

    # Simulate Viking attack
    result_viking_attack = great_war.vikingAttack()
    if "died" in result_viking_attack:
        print(Fore.RED + result_viking_attack)
        death_sound.play()
    elif "received" in result_viking_attack:
        print(Fore.MAGENTA + result_viking_attack)
    else:
        print(Fore.YELLOW + result_viking_attack)
        viking_attack_sound.play()

    # Simulate Saxon attack
    result_saxon_attack = great_war.saxonAttack()
    if "died" in result_saxon_attack:
        print(Fore.RED + result_saxon_attack)
        death_sound.play()
    elif "received" in result_saxon_attack:
        print(Fore.MAGENTA + result_saxon_attack)
    else:
        print(Fore.CYAN + result_saxon_attack)
        saxon_attack_sound.play()

    # Army status
    print(Fore.CYAN + f"Viking army: {len(great_war.vikingArmy)} warriors" + Fore.WHITE + " | " + 
          Fore.YELLOW + f"Saxon army: {len(great_war.saxonArmy)} warriors\n")

    # Final message and victory sound
    final_status = great_war.showStatus()
    if "Vikings have won" in final_status:
        print(Fore.GREEN + final_status)
        victory_sound.play()
    elif "Saxons have fought" in final_status:
        print(Fore.GREEN + final_status)
        victory_sound.play()
    else:
        print(Fore.WHITE + final_status)

    # Delay between rounds
    time.sleep(3)
    
    round += 1
