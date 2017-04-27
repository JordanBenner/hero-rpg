#!/usr/bin/env python3
from random import randint


class Character:
    def __init__(self):
        self.health = 10
        self.power = 5

    def attack(self, enemy):
        enemy.health -= self.power

    def print_status(self):
        print("You have {} health and {} power.".format(self.health, self.power))

    def alive(self):
        if self.health > 0:
            return True


class Hero(Character):
    def __init__(self):
        super().__init__()
        self.health = 10
        self.power = 5
        self.name = "Hero"

    def attack(self, enemy):
        damage = self.power
        if randint(0, 4) == 4:
            damage = damage * 2
            enemy.health -= damage


class Goblin(Character):
    def __init__(self):
        super().__init__()
        self.health = 6
        self.power = 2
        self.name = "goblin"


class Zombie(Character):
    def __int__(self):
        super().__init__()
        self.health = 6
        self.power = 1
        self.name = "zombie"

    def alive(self):
        return True


class Medic(Character):
    def __init__(self):
        super().__init__()
        self.health = 10
        self.power = 3
        self.name = "medic"

    def health_status(self):
        if randomint(0, 4) == 4:
            medic.health += 2


class Shadow(Character):
    def __init__(self):
        super().__init__()
        self.health = 1
        self.power = 6
        self.name = 'shadow'
        self.evasion = 10

    def damage(self):
        heahlth = self.health
        if randomint(0, 9) == 9:
            shadow.health += 1

    def when_attacked(self):
        damage = self.power
        if self.evasion > 10:
            if randomint(0, 9) == 9:
                self.health -= damage

    def Wizard(Character):
        def __init__(self):
            super().__init__()
            self.health = 7
            self.power = 10
            self.name = 'wizard'


hero = Hero()
goblin = Zombie()


def main():

    while hero.alive() and goblin.alive():
        hero.print_status()
        print()
        print("What do you want to do?")
        print("1. fight zombie")
        print("2. run in circles")
        print("3. book it")
        print("> ", end=' ')
        inpt = input()
        print()
        if inpt == "1":
            hero.attack(goblin)
            print("You do {} damage to the zombie.".format(hero.power))
        elif inpt == "2":
            print("Dont look")
            pass
        elif inpt == "3":
            print("Goodbye.")
            exit(0)
        else:
            print("Invalid inpt {}".format(inpt))

        if goblin.alive():
            goblin.attack(hero)
            print("The zombie does {} damage to you.".format(goblin.power))
        if hero.health <= 0:
            print("You are being eaten.")


if __name__ == "__main__":
    main()
