from classes.magic import Spell
from classes.inventory import Item
from classes.game import bcolors, Person
import random

"""
This code is for initializing all items, spells, and people using the other classes
"""


affinities = ["Fire", "Electricity", "Earth", "Wind", "Frost", "Evil", "Holy"]

# Create Items
holy_water = Item("Holy Water", "full restore", "Fully Restores all HP/MP of the user", 9999)
holy_barrel = Item("Holy Barrel", "full restore", "Fully Restores all HP/MP of all party members", 9999)
totem = Item("Suspicious Totem", "revive", "Revive 1 dead party member", 0)

weak_health_potion = Item("Weak Health Potion", "HP potion", "Heals 50 HP", 50)
health_potion = Item("Health Potion", "HP potion", "Heals 125 HP", 125)
strong_health_potion = Item("Strong Health Potion", "HP potion", "Heals 200 HP", 300)

weak_magic_potion = Item("Weak Magic Potion", "Magic potion", "Restores 20 MP", 20)
magic_potion = Item("Magic Potion", "Magic potion", "Restores 60 MP", 60)
strong_magic_potion = Item("Strong Magic Potion", "Magic potion", "Restores 100 MP", 100)

bomb = Item("Bomb", "damage", "Deals 500 splash damage", 500)
gun = Item("Gun", "damage", "Deals 120 damage at a range", 120)
insta_kill = Item("InstaKill", "damage", "Instantly kills a person", 9999999)

all_items = [holy_water, holy_barrel, weak_health_potion, health_potion, strong_health_potion,
             weak_magic_potion, magic_potion, strong_magic_potion, bomb, gun, insta_kill, totem]

# Attack Spells
fire = Spell("Fire", 10, 100, "Attack", "Fire")
thunder = Spell("Thunder", 10, 100, "Attack", "Electricity")
frost = Spell("Frost", 10 , 100, "Attack", "Frost")
meteor = Spell("Meteor", 20, 200, "Attack", "Earth")
push = Spell("Push", 15, 150, "Attack", "Wind")
cloud = Spell("Cloud", 10, 100, "Attack", "Holy")
curse = Spell("Curse", 15, 100, "Attack", "Evil")

# Heal Spells
angel = Spell("Angel", 20, 120, "Heal", "Holy")
fortitude = Spell("Fortitude", 45, 200, "Heal", "Holy")
supernatural = Spell("Supernatural", 10, 150, "Heal", "Evil")

all_magic = [fire, thunder, frost, meteor, push, cloud, curse, angel, fortitude, supernatural]


# Initialize people
player_magic = [fire, thunder, frost, push, cloud, angel, fortitude]
player_items = [{"item": weak_magic_potion, "quantity": 5}, {"item": weak_health_potion, "quantity": 5},
                {"item": bomb, "quantity": 1}, {"item": gun, "quantity": 7},
                {"item": holy_water, "quantity": 1}, {"item": holy_barrel , "quantity": 1},
                {"item": health_potion, "quantity": 3}, {"item": strong_health_potion, "quantity": 1},
                {"item": magic_potion, "quantity": 3}, {"item": strong_magic_potion, "quantity": 1},
                {"item": insta_kill, "quantity": 5}, {"item": totem, "quantity": 3}]

username = ""
player_1 = Person(username, 500, 100, 80, 70, player_magic, player_items, ["Fire", "Electricity", "Earth", "Wind", "Frost", "Holy"])

party_names = ["Aethelu", "Isabella", "Reina", "Odo", "Drake", "Robin", "Wade", "Wolfgang", "Luther", "Godwin"]

party_1_name = random.choice(party_names)
party_1_hp = random.randrange(300, 700)
party_1_mp = random.randrange(80, 120)
party_1_atk = random.randrange(60, 100)
party_1_df = random.randrange(25, 100)
party_1_magic = []
party_1_items = []
party_1_affinity = []

party_member_1 = Person(party_1_name, party_1_hp, party_1_mp, party_1_atk, party_1_df, party_1_magic, party_1_items, party_1_affinity)

party_1_items = party_member_1.generate_items(all_items)
party_1_magic = party_member_1.generate_magic(all_magic)
party_1_affinity = party_member_1.generate_affinity()

party_2_name = random.choice(party_names)
party_2_hp = random.randrange(300, 700)
party_2_mp = random.randrange(80, 120)
party_2_atk = random.randrange(60, 100)
party_2_df = random.randrange(25, 100)
party_2_magic = []
party_2_items = []
party_2_affinity = []

party_member_2 = Person(party_2_name, party_2_hp, party_2_mp, party_2_atk, party_2_df, party_2_magic, party_2_items, party_2_affinity)

party_2_items = party_member_2.generate_items(all_items)
party_2_magic = party_member_2.generate_magic(all_magic)
party_2_affinity = party_member_2.generate_affinity()

party_3_name = random.choice(party_names)
party_3_hp = random.randrange(300, 700)
party_3_mp = random.randrange(80, 120)
party_3_atk = random.randrange(60, 100)
party_3_df = random.randrange(25, 100)
party_3_magic = []
party_3_items = []
party_3_affinity = []

party_member_3 = Person(party_3_name, party_3_hp, party_3_mp, party_3_atk, party_3_df, party_3_magic, party_3_items, party_3_affinity)

party_3_items = party_member_3.generate_items(all_items)
party_3_magic = party_member_3.generate_magic(all_magic)
party_3_affinity = party_member_3.generate_affinity()

"""*******************************"""


"""*******************************"""

#enemies
enemy_0_magic = [thunder, meteor, curse, supernatural]
enemy_0_items = [{"item": bomb, "quantity": 2},{"item": holy_water, "quantity": 1}, {"item": totem, "quantity": 1}]

enemy_1_magic = [push, meteor, cloud, curse, supernatural]
enemy_1_items = [{"item": gun, "quantity": 3},{"item": holy_water, "quantity": 1}, {"item": totem, "quantity": 1}]

enemy_2_magic = [fire, thunder, curse, supernatural]
enemy_2_items = [{"item": bomb, "quantity": 2},{"item": holy_water, "quantity": 1}, {"item": totem, "quantity": 1}]

enemy_3_magic = [frost, cloud, curse, supernatural]
enemy_3_items = [{"item": strong_health_potion, "quantity": 5},{"item": gun, "quantity": 3},{"item": holy_water, "quantity": 2}, {"item": totem, "quantity": 1}]

enemy_4_magic = [thunder, meteor, fortitude, cloud, push, curse, supernatural]
enemy_4_items = [{"item": strong_magic_potion, "quantity": 5},{"item": gun, "quantity": 4},{"item": holy_water, "quantity": 1}, {"item": totem, "quantity": 1}]

enemy_5_magic = [fire, push, curse, supernatural]
enemy_5_items = [{"item": gun, "quantity": 3},{"item": bomb, "quantity": 2},{"item": holy_water, "quantity": 1}, {"item": totem, "quantity": 1}]

enemy_0 = Person("Gragnar ", 3000, 400, 400, 25, enemy_0_magic, enemy_0_items, ["Electricity", "Earth", "Evil"])
enemy_1 = Person("Opal ", 6000, 500, 200, 25, enemy_1_magic, enemy_1_items, ["Wind", "Electricity", "Evil"])
enemy_2 = Person("Dragos ", 4500, 300, 350, 25, enemy_2_magic, enemy_2_items, ["Fire", 'Electricity', "Evil"])
enemy_3 = Person("Heptus ", 2500, 400, 1000, 25, enemy_3_magic, enemy_3_items, ["Water", "Wind", "Evil"])
enemy_4 = Person("Aristotle ", 10000, 1000, 50, 25, enemy_4_magic, enemy_4_items, ["Electricity", "Earth", "Wind", "Holy", "Evil"])
enemy_5 = Person("Muckle ", 5000, 500, 500, 25, enemy_5_magic, enemy_5_items, ["Fire", "Wind", "Physical"])

enemies = [enemy_0, enemy_1, enemy_2, enemy_3, enemy_4, enemy_5]