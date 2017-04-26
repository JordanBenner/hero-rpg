#!/usr/bin/env python3

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""


class Character:
    def __init__(self, health, power):
        self.health = 10
        self.power = 5

    def attack(enemy):
        print(self.attack(enemy))

    def print_status(self):
        print("You have {} health and {} power.".format(self.health, self.power))

    def alive(self):
        if self.health > 0:
            return True


class hero(Character):
    def __init__(self, health, power):
        self.health = 10
        self.power = 5.
        self.name = "Hero"

    def attack(enemy):
        print(hero.attack(enemy))

    def print_status(self):
        print("You have {} health and {} power.".format(hero.health, hero.power))

    def alive(self):
        if self.health > 0:
            return True


class goblin(Character):
    def __init__(self, health, power):
        self.health = 6
        self.power = 2
        self.name = "goblin"

    def attack(hero):
        print(goblin.attack(hero))

    def print_status(self):
        print("The goblin has {} health and {} power.".format(
            goblin.health, goblin.power))

    def alive(self):
        if goblin.health > 0:
            return True


class zombie(Character):
    def __int__(self, health, power):
        self.health = 6
        self.power = 3
        self.name = "zombie"

    def alive(self):
        return True


hero = hero('10', '5')
goblin = zombie('6', '2')


def main():

    while hero.alive() and goblin.alive():
        print()
        print("What do you want to do?")
        print("1. fight zombie")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        inpt = input()

        if inpt == "1":
            # Hero attacks goblin
            goblin.health -= hero.power
            print("You do {} damage to the zombie.".format(hero.power))
        if goblin.alive():
            print("The zombie won't die!")
        elif inpt == "2":
            pass
        elif inpt == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid inpt {}".format(inpt))

        if goblin.alive():
            # Goblin attacks hero
            hero.health -= goblin.power
            print("The zombie does {} damage to you.".format(goblin.power))
        if hero.health <= 0:
            print("You are being eaten.")


if __name__ == "__main__":
    main()
