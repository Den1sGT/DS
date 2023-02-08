class SuperHero:
    people = 'people'


    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase


    def get_name(self):
        return self.name

    def multiply_hp(self):
        self.health_points *= 2
        print('Здоровье увеличилось в 2 раза')

    def __str__(self):
        return f'Прозвище: {self.nickname}, Суперспособность: {self.superpower}, Здоровье: {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)


Hero = SuperHero('Ben', 'Halk', 'Strong', 80, 'HAAALK')
name = Hero.get_name()
Hero.multiply_hp()
hero_parameters = Hero.__str__()
phrase_len = Hero.__len__()
print(f'Имя: {name}\n{hero_parameters}\nДлина прозвища: {phrase_len}')



class SuperHero2(SuperHero):

    def __init__(self,name,nickname,superpower,health_points,catchphrase,sila, damage = False, fly = False):
        super().__init__(name,nickname,superpower,health_points,catchphrase)
        self.sila = sila
        self.damage = damage
        self.fly = fly

    def multiply_hp(self):
        self.health_points **= 2
        print('Здоровье увеличилось в 2 раза')
        self.fly = True


    def phrase(self):
        print( 'fly in the True_phrase')

hero =  SuperHero2('Batman','bat', 'money', '100', 'bat' )

hero.multiply_hp()
hero.phrase()


class Villain(SuperHero2):
    people = 'monster'


    def gen_x(self):
        pass

    def crit(self):
        self.damage *= self.damage

hero3 = Villain('zzz', 'zeen', 'strong', 50, 'ZZZ' )
Villain.crit(hero.damage)
