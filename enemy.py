class Enemy():
    def __init__(self, name = "Enemy", hp = 10, damage = 1):
        self.name = name
        self.hp = hp
        self.damage = damage

    def get_info(self):
        print(self.hp)
        print(self.name)

    def attack(self, enemy):
        enemy.hp -= self.damage 

class Zombie(Enemy):
    def __init__(self, name = "Zombie", hp = 100, damage = 10):
        self.hp = hp
        self.name = name
        self.damage = damage

class Creeper(Enemy):
    def __init__(self, name = "Creeper", hp = 20, damage = 5):
        self.hp = hp
        self.name = name
        self.damage = damage

zom = Zombie()
zom.get_info()


crep = Creeper()
crep.get_info()

for i in range(4):
    crep.attack(zom)
zom.get_info()
