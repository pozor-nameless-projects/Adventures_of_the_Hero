
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


#heroes
gnom = hero('Гном', 120, 'Гномы обитают в подземелье. Они не опасны, пока их не разозлить', 5, 0)
dragon = hero('Дракон', 562, 'Дракон очень сверепое существо. Остерегайтесь его в замке', 14, 1)
elf = hero('Эльф', 332, 'Эльфы стреляют своими магическими стрелами.', 10, 1)
trader = hero('Торговец', 24, 'Торгует всем что есть в это мире.', 1, 0)
villager = hero('Житель', random.randint(20, 40), 'Простой житель. Ничего не умеет. Ничего не делает.', 0, 0)
old_villager = hero('Старый житель', random.randint(50, 85), 'Старый житель. Живет в избушке на пенсии', 0, 0)
young_villager = hero('Молодой житель', random.randint(10, 18), 'Молодой житель. Еще учится в школе.', 0, 0)
#items
wooden_stick = item('Палка', 'Палка из дерева. Проще её сжечь чем кого-нибудь ей убить', 1, 15)
torch = item('Факел', 'Факел для освещения дороги.', 2, 35)
small_sword = item('Маленький меч', 'Простой меч. Наносит мало урона.', 3, 100)


# h = people(user, age, 'Ваш перссонаж бродит по темным уголкам этого средневекового века. Он ищет не только приключения, но и семь тоинственных душ')

menu = None
create_person = None


def menu():
	global menu
	menu = Tk()

	menu.title('Adventures of the Hero')
	menu.geometry('450x450')
	menu.config(bg = '#1FA7E1')
	menu.resizable(0, 0)

	label = Label(menu, text = 'Menu', bg='#1FA7E1', fg='white')
	label.config(font = ('Arial', 25, 'bold'))
	label.place(x=180, y=30)
	
	button = Button(menu, text = 'START', width=15, command=create_person)
	button.config(font = ('Arial', 15, 'bold'))
	button.place(x=130, y=100)

	button = Button(menu, text = 'SETTINGS', width=15)
	button.config(font = ('Arial', 15, 'bold'))
	button.place(x=130, y=170)

	button = Button(menu, text = 'EXIT', width=15, command=menu.destroy)
	button.config(font = ('Arial', 15, 'bold'))
	button.place(x=130, y=240)

	menu.mainloop()
	
 
def create_person():
	global create_person
	menu.destroy()
	create_person = Tk()
	create_person.resizable(0, 0)

	create_person.title('Adventures of the Hero')
	create_person.geometry('450x450')
	create_person.config(bg = '#1FA7E1')

	label = Label(create_person, text = 'Input name: ', bg='#1FA7E1', fg='white')
	label.config(font = ('Arial', 20, 'bold'))
	label.place(x=130, y=30)

	entry = Entry(create_person, width = 20)
	entry.config(font = ('Arial', 15, 'bold'))
	entry.place(x=130, y=70)

	label = Label(create_person, text = 'Input Age: ', bg='#1FA7E1', fg='white')
	label.config(font = ('Arial', 20, 'bold'))
	label.place(x=130, y=110)

	entry = Entry(create_person, width = 20)
	entry.config(font = ('Arial', 15, 'bold'))
	entry.place(x=130, y=150)

	button = Button(create_person, text = 'Create person', width=15, command=game)
	button.config(font = ('Arial', 15, 'bold'))
	button.place(x=130, y=190)

	create_person.mainloop()


def game():
	global game
	create_person.destroy()
	game = Tk()

	game.title('Adventures of the Hero')
	game.geometry('450x450')
	game.config(bg = '#1FA7E1')
	game.resizable(0, 0)

	game.mainloop()


if __name__ == '__main__':
	menu()

