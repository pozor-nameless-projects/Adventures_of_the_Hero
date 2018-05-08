
from ezprint import p
from tkinter import *
import random
import os

user = 'Jana'
age = 0


class item:

	def __init__(self, name, desc, damage, cost):
		self.name = name
		self.desc = desc
		self.damage = damage
		self.cost = cost


class hero:


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

young_villager = hero('Young villager', random.randint(10, 18), 'Молодой житель. Еще учится в школе.', 0, 0)
 


# h = people(user, age, 'Ваш перссонаж бродит по темным уголкам этого средневекового века. Он ищет не только приключения, но и семь тоинственных душ')


def menu():
	menu = Tk()

	menu.title('Adventures of the Hero')
	menu.geometry('450x450')
	menu.config(bg = '#1FA7E1')

	label = Label(menu, text = 'Menu', bg='#1FA7E1', fg='white')
	label.config(font = ('Arial', 25, 'bold'))
	label.place(x=180, y=30)
	
	button = Button(menu, text = 'START', width=15)
	button.config(font = ('Arial', 15, 'bold'))
	button.place(x=130, y=100)

	button = Button(menu, text = 'SETTINGS', width=15)
	button.config(font = ('Arial', 15, 'bold'))
	button.place(x=130, y=170)

	button = Button(menu, text = 'EXIT', width=15, command=menu.destroy)
	button.config(font = ('Arial', 15, 'bold'))
	button.place(x=130, y=240)

	menu.mainloop()


if __name__ == '__main__':
	menu()
