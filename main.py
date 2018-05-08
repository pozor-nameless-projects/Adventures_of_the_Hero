
from ezprint import p
from tkinter import *
import random
import os

user = 'Jana'
age = 0

class hero:

	name = ''
	age = 0
	des = ''
	dam = 0
	den = 0

	def __init__(self, name, age, des, dam, den):
		self.name = name
		self.age = age
		self.des = des
		self.dam = dam
		self.den = den

gnom = hero('Gnom', 120, 'Гномы обитают в подземелье. Они не опасны, пока их не разозлить', 5, 0)
dragon = hero('Dragon', 562, 'Дракон очень сверепое существо. Остерегайтесь его в замке', 14, 1)
elf = hero('Elf', 332, 'Эльфы стреляют своими магическими стрелами.', 10, 1)
trader = hero('Trader', 24, 'Торгует всем что есть в это мире.', 1, 0)
villager = hero('Villager', random.randint(20, 40), 'Простой житель. Ничего не умеет. Ничего не делает.', 0, 0)
old_villager = hero('Old villager', random.randint(50, 85), 'Старый житель. Живет в избушке на пенсии', 0, 0)
young_villager = hero('Young villager', randint(10, 18), 'Молодой житель. Еще учится в школе.'0, 0)

# h = people(user, age, 'Ваш перссонаж бродит по темным уголкам этого средневекового века. Он ищет не только приключения, но и семь тоинственных душ')


def menu():
	menu = Tk()
	
	menu.title('Adventures of the Hero')
	menu.geometry('450x450')
	menu.mainloop()

if __name__ == '__main__':
	menu()
