import random
import ITE
from classes.game import Person, bcolors
from classes.inventory import Item
from classes.magic import Spell

"""

You need to change the death sequence to accommodate for all party members
You also need to spice up the attack choice with maybe different weapons
Add an elemental part of the game where spells and elemental weapons/armor matters!
You should add a bank of enemies where you fight one and then move on to the next one
You should add a reward sequence at the end of a fight if the party wins
BALANCE THE GAME

"""

def get_stats():
    global party
    print(bcolors.BOLD + bcolors.FAIL + "ENEMY:" + bcolors.ENDC)
    print(enemy.generate_enemy_stats() + "\n")
    print(bcolors.BOLD + bcolors.OKBLUE + "PARTY:" + bcolors.ENDC)
    for member in party:
        print(member.generate_stats())


while True:
    user_name = input("What will your name be?: ")
    if len(user_name) > 15:
        print("That name is too long... Try Again!")
    else:
        break


# Attack Spells
fire = ITE.fire
thunder = ITE.thunder
frost = ITE.frost
meteor = ITE.meteor
push = ITE.push
cloud = ITE.cloud
curse = ITE.curse

# Heal Spells
angel = ITE.angel
fortitude = ITE.fortitude
supernatural = ITE.supernatural

all_magic = [fire, thunder, frost, meteor, push, cloud, curse, angel, fortitude, supernatural]

# Create Items
holy_water = ITE.holy_water
holy_barrel = ITE.holy_barrel

weak_health_potion = ITE.weak_health_potion
health_potion = ITE.health_potion
strong_health_potion = ITE.strong_health_potion

weak_magic_potion = ITE.weak_magic_potion
magic_potion = ITE.magic_potion
strong_magic_potion = ITE.strong_magic_potion

bomb = ITE.bomb
gun = ITE.gun

all_items = [holy_water, holy_barrel, weak_health_potion, health_potion, strong_health_potion,
             weak_magic_potion, magic_potion, strong_magic_potion, bomb, gun]
# sword = Item


# Set player and enemy variables
player_magic = ITE.player_magic
enemy_magic = ITE.enemy_0_magic

# , {"item": , "quantity": }
player_items = ITE.player_items

enemy_items = ITE.enemy_0_items


player_1 = ITE.player_1
player_1.name = user_name
enemy_0 = ITE.enemy_0
enemy_1 = ITE.enemy_1
enemy_2 = ITE.enemy_2
enemy_3 = ITE.enemy_3
enemy_4 = ITE.enemy_4
enemy_5 = ITE.enemy_5
enemies = ITE.enemies
previous_enemies = []
# to make the game continuous and fight multiple enemies, create the enemies in the same way as party members
# if a name that has already been used before shows up, code it so that it adds a roman numeral to the end that
# increases by 1 with each occurrence


# create party members
party_member_1 = ITE.party_member_1
party_member_2 = ITE.party_member_2
party_member_3 = ITE.party_member_3

party = [player_1, party_member_1, party_member_2, party_member_3]
dead_party = []

game = True
running = True
i = 0

while game:
    running = True
    i = random.randrange(0,len(enemies))
    enemy = enemies[i]
    for bad in previous_enemies:
        if bad == enemy.name:
            enemy.name += "I"
            enemy.maxhp += 500
            enemy.hp = enemy.maxhp
            enemy.maxmp += 200
            enemy.mp = enemy.maxmp
            enemy.generate_items(all_items)
    previous_enemies.append(enemy.name)


    print("\n" + bcolors.FAIL + bcolors.BOLD + enemy.name + " ATTACKS!" + bcolors.ENDC)

    while running:
        print("\n===============================\n")

        get_stats()

        for player in party:

            while True:

                player.choose_action()
                choice = input("    Choose action: ")
                index = int(choice) - 1

                print("    You chose", choice,"!\n")

                if index == 0:
                    dmg = player.generate_damage()
                    player.give_damage(dmg, enemy)
                    print(bcolors.OKGREEN + bcolors.BOLD + "You attacked for " + str(dmg) + " points of damage. Enemy HP: " + str(enemy.get_hp()) + bcolors.ENDC)
                    break

                elif index == 1:
                    player.choose_magic()
                    magic_choice = (int(input(" Choose magic: ")) - 1)

                    if magic_choice == -1:
                        continue

                    spell = player.magic[magic_choice]
                    magic_prop = spell.generate_spell_prop()
                    cost = spell.cost

                    current_mp = player.get_mp()

                    if cost > current_mp:
                        print(bcolors.WARNING + "\nNot enough MP\n" + bcolors.ENDC)
                        continue

                    player.reduce_mp(cost)

                    if spell.type == "Heal":
                        player.heal(spell.prop)
                        print(bcolors.OKBLUE + "\n" + spell.name + " heals for " + str(magic_prop) + " points!" + bcolors.ENDC)
                    elif spell.type == "Attack":
                        ehp = enemy.hp
                        player.give_damage(magic_prop, enemy, spell)
                        if enemy.hp == (ehp - magic_prop):
                            print(bcolors.OKBLUE + "\n" + spell.name + " deals " + str(magic_prop) + " points of damage." + bcolors.ENDC)
                        elif enemy.hp != (ehp - magic_prop):
                            print(bcolors.OKBLUE + "\n" + spell.name + " deals " + str(ehp - enemy.hp) + " elemental points of damage." + bcolors.ENDC)
                    break

                elif index == 2:
                    if len(player.items) > 0:
                        player.choose_item()
                        item_choice = (int(input("     Choose item: ")) - 1)

                        if item_choice == -1:
                            continue

                        item = player.items[item_choice]["item"]
                        player.items[item_choice]["quantity"] -= 1

                        # check item type
                        if item.type == "full restore":
                            if item.name == "Holy Water":
                                player.heal(item.prop)
                                player.restore_magic(item.prop)
                                print(bcolors.OKBLUE + "\n" + str(item.name) + " heals for max points!" + bcolors.ENDC)
                            elif item.name == "Holy Barrel":
                                for party_member in party:
                                    party_member.heal(item.prop)
                                    party_member.restore_magic(item.prop)
                                print(bcolors.OKBLUE + "\n" + str(item.name) + " restores and heals for max points!" + bcolors.ENDC)
                        elif item.type == "revive":
                            if item.name == "Suspicious Totem":
                                if len(dead_party) > 0:
                                    print(bcolors.BOLD + bcolors.OKGREEN + "        Choose who you want to revive" + bcolors.ENDC)
                                    i = 1
                                    for member in dead_party:
                                        print("        " + str(i) + ": " + bcolors.OKBLUE + member.name + bcolors.ENDC)
                                        i += 1
                                    choice = input("        Party Member: ")
                                    index = (int(choice) - 1)
                                    party.append(dead_party[index])
                                    print(bcolors.PURPLE + dead_party[index].name + " has been revived and has rejoined the party!" + bcolors.ENDC)
                                    dead_party[index].hp = dead_party[index].maxhp
                                    dead_party[index].mp = dead_party[index].maxmp
                                    dead_party.remove(dead_party[index])
                                else:
                                    print(bcolors.PURPLE + "Everyone is alive! A Suspicious Totem cannot be used!" + bcolors.ENDC)
                                    continue
                        elif item.type == "HP potion":
                            player.heal(item.prop)
                            print(bcolors.OKBLUE + "\n" + str(item.name) + " heals for " + str(item.prop) + " points!" + bcolors.ENDC)
                        elif item.type == "Magic Potion":
                            player.restore_magic(item.prop)
                            print(bcolors.OKBLUE + "\n" + str(item.name) + " restores " + str(item.prop) + " magic points!" + bcolors.ENDC)
                        elif item.type == "damage":
                            player.give_damage(item.prop, enemy)
                            print(bcolors.OKGREEN + bcolors.BOLD + "\nYour", item.name, "attacked for " + str(
                                item.prop) + " points of damage. Enemy HP: " + str(enemy.get_hp()) + bcolors.ENDC)

                        # remove item from inventory if it has no quantity
                        if player.items[item_choice]["quantity"] == 0:
                            temp_item = str(player.items[item_choice]["item"].name)
                            player.items.remove(player.items[item_choice])
                            print(bcolors.FAIL + bcolors.BOLD + "You have run out of", temp_item + "s!" + bcolors.ENDC)
                        break

            if len(party) == 0:
                print(bcolors.FAIL + bcolors.UNDERLINE + "\nYour enemy has defeated you!" + bcolors.ENDC)
                get_stats()
                game = False
                running = False
                break
            elif enemy.get_hp() == 0:
                print(bcolors.OKGREEN + bcolors.UNDERLINE + bcolors.BOLD + "\nYou win!\n" + bcolors.ENDC)
                get_stats()
                print(bcolors.BOLD + bcolors.PURPLE + "\nEvery party member finds new loot among the dead evil!" + bcolors.ENDC)
                print("\n===============================\n")
                for guy in party:
                    guy.get_items(enemy.items)
                running = False
                break

        target_1 = random.randrange(0,len(party))
        target_2 = random.randrange(0,len(party))

        while target_2 == target_1:
            target_2 = random.randrange(0,len(party))

        enemy_dmg = enemy.generate_damage()
        enemy.give_damage(enemy_dmg, party[target_1])
        print(bcolors.FAIL + bcolors.BOLD + enemy.name + " attacked " + bcolors.OKGREEN + party[target_1].name + bcolors.FAIL + " for " + str(enemy_dmg) + " points of damage. " + party[target_1].name + "'s HP: " + str(
            party[target_1].get_hp()) + bcolors.ENDC)

        enemy_dmg = enemy.generate_damage()
        enemy.give_damage(enemy_dmg, party[target_2])
        print(bcolors.FAIL + bcolors.BOLD + enemy.name + " attacked " + bcolors.OKGREEN + party[target_2].name + bcolors.FAIL + " for " + str(enemy_dmg) + " points of damage. " + party[target_2].name + "'s HP: " + str(
            party[target_2].get_hp()) + bcolors.ENDC)

        for person in party:
            if person.hp == 0:
                print(bcolors.BOLD + bcolors.FAIL + person.name + " has died!" + bcolors.ENDC)
                dead_party.append(person)
                party.remove(person)