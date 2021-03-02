import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    PURPLE = '\033[95m'
    BLACK = '\033[98m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:

    def __init__(self, name, hp, mp, atk, df, magic, items, affinity):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 20
        self.atkh = atk + 20
        self.df = df
        self.magic = magic
        self.items = items
        self.affinity = affinity
        self.actions = ["Attack", "Magic", "Items"]


    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def give_damage(self, prop, target, ability = "None"):
        dmg = self.generate_affinity_damage(target, ability)
        dmg += prop
        target.hp -= dmg
        if target.hp < 0:
            target.hp = 0
        return target.hp

    def generate_affinity_damage(self, target, spell = "None"):
        # all_affinities = ["Fire", "Electricity", "Earth", "Wind", "Frost", "Evil", "Holy"]
        """
        frost is countered by fire
        fire is countered by wind
        wind is countered by electricity
        electricity is countered by earth
        earth is countered by frost
        holy and evil balance each other ig
        :param target:
        :return:
        """
        affinities = []
        dmg = 0
        if spell != "None":
            affinities.append(spell.element)
        else:
            affinities = self.affinity
        target_a = target.affinity
        for element in affinities:
            for thing in target_a:
                if (thing == "Frost" and element == "Fire") or (thing == "Fire" and element == "Wind") or (thing == "Wind" and element == "Electricity") or (thing == "Electricity" and element == "Earth") or (thing == "Earth" and element == "Frost"):
                    dmg += 500
                elif (element == "Frost" and thing == "Fire") or (element == "Fire" and thing == "Wind") or (element == "Wind" and thing == "Electricity") or (element == "Electricity" and thing == "Earth") or (element == "Earth" and thing == "Frost"):
                    dmg -= 50
                else:
                    dmg = 0
        return dmg



    def heal(self, prop):
        self.hp += prop
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        return self.hp

    def restore_magic(self, prop):
        self.mp += prop
        if self.mp > self.maxmp:
            self.mp = self.maxmp
        return self.mp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def generate_magic(self, magic_list):
        magic_size = random.randrange(3,5)
        list = magic_list
        random.shuffle(list)
        new_magic = []
        heal = 0
        attack = 0
        for magic in list:
            if magic.type == "Heal" and heal < 2:
                self.magic.append(magic)
                heal += 1
            elif magic.type == "Attack" and attack < 3:
                self.magic.append(magic)
                attack += 1
            elif len(self.magic) >= magic_size:
                break

    def generate_items(self, item_list):
        inventory_size = random.randrange(4, 8)
        list = item_list
        random.shuffle(list)
        new_items = []
        for item in list:
            if len(self.items) < inventory_size:
                self.items.append(item)
            else:
                break
        for item in self.items:
            new_items.append({"item": item, "quantity": 1})
        self.items = new_items

    def get_items(self, items):
        for i in items:
            reference = 0
            for j in self.items:
                if i["item"] == j["item"]:
                    j["quantity"] += 1
                    reference = 1
            if reference == 0:
                self.items.append(i)


    def generate_affinity(self):
        all_affinities = ["Fire", "Electricity", "Earth", "Wind", "Frost", "Evil", "Holy"]
        scrambled = all_affinities
        random.shuffle(scrambled)
        affinity_list = []
        randint = random.randrange(2, 5)
        while randint > 0:
            affinity_list.append(scrambled[randint])
            randint -= 1
        self.affinity = affinity_list


    def choose_action(self):
        i = 1
        print("\n    " + bcolors.OKBLUE + bcolors.BOLD + self.name + "'s ACTIONS: " + bcolors.ENDC)
        for item in self.actions:
            print("        " + str(i) + ":",item)
            i += 1

    def choose_magic(self):
        i = 1
        print("    " + bcolors.OKBLUE + bcolors.BOLD + "MAGIC: " + bcolors.ENDC)
        print("        " + bcolors.OKGREEN + "0: BACK" + bcolors.ENDC)
        for spell in self.magic:
            print("        " + str(i) + ":", spell.name + bcolors.FAIL +
                  " (cost:", str(spell.cost) + ")" + bcolors.OKGREEN +
                  " (effect:", str(spell.prop) + ")" + bcolors.WARNING +
                  " (element:", spell.element + ")" + bcolors.OKBLUE +
                  " (type:", spell.type + ")" + bcolors.ENDC)
            i += 1

    def choose_item(self):
        i = 1
        print("    " + bcolors.OKBLUE + bcolors.BOLD + "ITEMS: " + bcolors.ENDC)
        print("        " + bcolors.OKGREEN + "0: BACK" + bcolors.ENDC)
        for item in self.items:
            if item["quantity"] == 0:
                continue
            else:
                print("        " + bcolors.OKGREEN + str(i) + " -", item["item"].name + bcolors.ENDC + ":", item["item"].description, "(x " + str(item["quantity"]) + ")")
                i += 1

    def generate_stats(self):
        string = self.name + ":"
        while len(string) < 17:
            string += " "
        string += str(self.hp) + "/" + str(self.maxhp)
        while len(string) < 26:
            string += " "
        string += "|"
        proportion = self.hp / self.maxhp
        phloat = (proportion * 100)/ 4
        rounded = round(phloat)
        i = 25
        while rounded > 0:
            string += (bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKGREEN + "█" + bcolors.ENDC)
            rounded -= 1
            i -= 1

        while i > 0:
            string += " "
            i -= 1

        if self.maxmp < 100 and self.mp < 10:
            string += "|   " + str(self.mp) + "/" + str(self.maxmp) + "  |"
        elif self.maxmp < 100 and self.mp < 100:
            string += "|  " + str(self.mp) + "/" + str(self.maxmp) + "  |"
        elif self.maxmp > 99 and self.mp < 100:
            string += "|  " + str(self.mp) + "/" + str(self.maxmp) + " |"
        else:
            string += "| " + str(self.mp) + "/" + str(self.maxmp) + " |"

        proportion = self.mp / self.maxmp
        phloat = (proportion * 100) / 10
        rounded = round(phloat)
        i = 10

        string += bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE
        while rounded > 0:
            string += ("█")
            rounded -= 1
            i -= 1
        string += bcolors.ENDC

        while i > 0:
            string += " "
            i -= 1
        string += "|"
        return string

    def generate_enemy_stats(self):
        string = self.name + ":"
        while len(string) < 17:
            string += " "
        string += str(self.hp) + "/" + str(self.maxhp)
        while len(string) < 26:
            string += " "
        string += "|"
        proportion = self.hp / self.maxhp
        phloat = (proportion * 100) / 4
        rounded = round(phloat)
        i = 25
        while rounded > 0:
            string += (bcolors.BOLD + bcolors.UNDERLINE + bcolors.FAIL + "█" + bcolors.ENDC)
            rounded -= 1
            i -= 1

        while i > 0:
            string += " "
            i -= 1

        if self.maxmp < 100 and self.mp < 10:
            string += "|   " + str(self.mp) + "/" + str(self.maxmp) + "  |"
        elif self.maxmp < 100 and self.mp < 100:
            string += "|  " + str(self.mp) + "/" + str(self.maxmp) + "  |"
        elif self.maxmp > 99 and self.mp < 100:
            string += "|  " + str(self.mp) + "/" + str(self.maxmp) + " |"
        else:
            string += "| " + str(self.mp) + "/" + str(self.maxmp) + " |"

        proportion = self.mp / self.maxmp
        phloat = (proportion * 100) / 10
        rounded = round(phloat)
        i = 10

        string += bcolors.BOLD + bcolors.UNDERLINE + bcolors.PURPLE
        while rounded > 0:
            string += ("█")
            rounded -= 1
            i -= 1
        string += bcolors.ENDC

        while i > 0:
            string += " "
            i -= 1
        string += "|"
        return string