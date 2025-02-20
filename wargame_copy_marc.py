# WAR !!!

from vikingsClasses_copy_marc import War, Viking, Saxon
import random
import time

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
    print(f"Round {round}... The battle rages on...\n")
    
    # Simulate Viking attack
    result_viking_attack = great_war.vikingAttack()
    print(result_viking_attack)
    
    # Simulate Saxon attack
    result_saxon_attack = great_war.saxonAttack()
    print(result_saxon_attack)
    
    # Print the current army status
    print(f"Viking army: {len(great_war.vikingArmy)} warriors | Saxon army: {len(great_war.saxonArmy)} warriors\n")
    print(great_war.showStatus())
    
    # Add a delay between rounds for suspense
    time.sleep(2)  # Pause for 2 seconds
    
    round += 1