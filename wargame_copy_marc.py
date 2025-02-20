# WAR !!!

from vikingsClasses_copy_marc import War, Viking, Saxon
import random
import time

soldier_names = ["albert", "andres", "archie", "dani", "david", "gerard", "german", "graham", "imanol", "laura"]
great_war = War()

# Create 5 Vikings
for i in range(0, 5):
    if i:
        great_war.addViking(Viking(soldier_names[random.randint(0, 9)].capitalize(), 100, random.randint(0, 100)))

# Create 5 Saxons
for i in range(0, 5):
    if i:
        great_war.addSaxon(Saxon(100, random.randint(0, 100)))

round = 0
while great_war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    print(f"Round {round}... The battle rages on...\n")
    
    result_viking_attack = great_war.vikingAttack()
    print(result_viking_attack)
    
    result_saxon_attack = great_war.saxonAttack()
    print(result_saxon_attack)
    
    print(f"Viking army: {len(great_war.vikingArmy)} warriors | Saxon army: {len(great_war.saxonArmy)} warriors\n")
    print(great_war.showStatus())
    
    time.sleep(2)
    
    round += 1
