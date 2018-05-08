
from ezprint import p
from tkinter import *
import threading
import random
import time
import os


user = ''
age = ''


screen_saver_thread = None


def cls():
	os.system('cls')


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


def printkrasivo(s):
	strtoprint = ''
	for i in s:
		strtoprint = strtoprint + str(i)
		sys.stdout.write('\r\r' + (strtoprint) + '')
		time.sleep(0.01)


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
class windows:
	global user
	global age
	menu = None
	create_person = None


	def menu(self):
		global menu
		menu = Tk()

		menu.title('Adventures of the Hero')
		menu.geometry('450x450')
		menu.config(bg = '#1FA7E1')
		menu.resizable(0, 0)

		label = Label(menu, text = 'Menu', bg='#1FA7E1', fg='white')
		label.config(font = ('Arial', 25, 'bold'))
		label.place(x=180, y=30)
		
		button = Button(menu, text = 'START', width=15, command=self.create_person)
		button.config(font = ('Arial', 15, 'bold'))
		button.place(x=130, y=100)

		button = Button(menu, text = 'CONTINUE', width=15, command=self.create_person)
		button.config(font = ('Arial', 15, 'bold'))
		button.place(x=130, y=170)

		button = Button(menu, text = 'SETTINGS', width=15)
		button.config(font = ('Arial', 15, 'bold'))
		button.place(x=130, y=240)

		button = Button(menu, text = 'EXIT', width=15, command=menu.destroy)
		button.config(font = ('Arial', 15, 'bold'))
		button.place(x=130, y=310)

		menu.mainloop()
		
	 
	def create_person(self):
		global create_person

		def con():
			set_user_data(entry, entry1)
			game_windows.game()

		menu.destroy()
		create_person = Tk()
		create_person.resizable(0, 0)

		create_person.title('Adventures of the Hero')
		create_person.geometry('450x450')
		create_person.config(bg = '#1FA7E1')

		label = Label(create_person, text = 'Input name: ', bg='#1FA7E1', fg='white')
		label.config(font = ('Arial', 20, 'bold'))
		label.place(x=130, y=30)

		entry = Entry(create_person, width = 20, )
		entry.config(font = ('Arial', 15, 'bold'))
		entry.place(x=130, y=70)

		label = Label(create_person, text = 'Input Age: ', bg='#1FA7E1', fg='white')
		label.config(font = ('Arial', 20, 'bold'))
		label.place(x=130, y=110)

		entry1 = Entry(create_person, width = 20)
		entry1.config(font = ('Arial', 15, 'bold'))
		entry1.place(x=130, y=150)

		button = Button(create_person, text = 'Create person', width=15, command=con)
		button.config(font = ('Arial', 15, 'bold'))
		button.place(x=130, y=190)

		create_person.mainloop()
		try:
			screen_saver_thread.join()
		except:
			pass

	def inv(self):
		global inv
		
		inv = Tk()

		inv.title('Adventures of the Hero')
		inv.geometry('450x450')
		inv.config(bg = '#1FA7E1')
		inv.resizable(0, 0)

		game.mainloop()


def set_user_data(entry1, entry2):
	global user
	global age
	user = entry1.get()
	age = entry2.get()


def screen_saver():
	strs = []
	strs.append(' ▄▄▄      ▓█████▄  ██▒   █▓▓█████  ███▄    █ ▄▄▄█████▓ █    ██  ██▀███  ▓█████   ██████ ') 
	strs.append('▒████▄    ▒██▀ ██▌▓██░   █▒▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒ ██  ▓██▒▓██ ▒ ██▒▓█   ▀ ▒██    ▒ ') 
	strs.append('▒██  ▀█▄  ░██   █▌ ▓██  █▒░▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░▓██  ▒██░▓██ ░▄█ ▒▒███   ░ ▓██▄   ') 
	strs.append('░██▄▄▄▄██ ░▓█▄   ▌  ▒██ █░░▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░ ▓▓█  ░██░▒██▀▀█▄  ▒▓█  ▄   ▒   ██▒') 
	strs.append(' ▓█   ▓██▒░▒████▓    ▒▀█░  ░▒████▒▒██░   ▓██░  ▒██▒ ░ ▒▒█████▓ ░██▓ ▒██▒░▒████▒▒██████▒▒') 
	strs.append(' ▒▒   ▓▒█░ ▒▒▓  ▒    ░ ▐░  ░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░   ░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░░ ▒░ ░▒ ▒▓▒ ▒ ░') 
	strs.append('  ▒   ▒▒ ░ ░ ▒  ▒    ░ ░░   ░ ░  ░░ ░░   ░ ▒░    ░    ░░▒░ ░ ░   ░▒ ░ ▒░ ░ ░  ░░ ░▒  ░ ░') 
	strs.append('  ░   ▒    ░ ░  ░      ░░     ░      ░   ░ ░   ░       ░░░ ░ ░   ░░   ░    ░   ░  ░  ░  ') 
	strs.append('      ░  ░   ░          ░     ░  ░         ░             ░        ░        ░  ░      ░  ') 
	strs.append('           ░           ░                                                                ') 
	strs.append(' ▒█████    █████▒')
	strs.append('▒██▒  ██▒▓██   ▒ ')
	strs.append('▒██░  ██▒▒████ ░ ')
	strs.append('▒██   ██░░▓█▒  ░ ')
	strs.append('░ ████▓▒░░▒█░    ')
	strs.append('░ ▒░▒░▒░  ▒ ░    ')
	strs.append('  ░ ▒ ▒░  ░      ')
	strs.append('░ ░ ░ ▒   ░ ░    ')
	strs.append('    ░ ░          ')
	strs.append('▄▄▄█████▓ ██░ ██ ▓█████     ██░ ██ ▓█████  ██▀███   ▒█████  ')
	strs.append('▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒▒██▒  ██▒')
	strs.append('▒ ▓██░ ▒░▒██▀▀██░▒███      ▒██▀▀██░▒███   ▓██ ░▄█ ▒▒██░  ██▒')
	strs.append('░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄  ▒██   ██░')
	strs.append('  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░▓█▒░██▓░▒████▒░██▓ ▒██▒░ ████▓▒░')
	strs.append('  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░    ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ')
	strs.append('    ░     ▒ ░▒░ ░ ░ ░  ░    ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░  ░ ▒ ▒░ ')
	strs.append('  ░       ░  ░░ ░   ░       ░  ░░ ░   ░     ░░   ░ ░ ░ ░ ▒  ')
	strs.append('          ░  ░  ░   ░  ░    ░  ░  ░   ░  ░   ░         ░ ░  ')

	for i in strs:
		printkrasivo(i + '\n')
                                                                                 

def game():
	pass


if __name__ == '__main__':
	cls()
	screen_saver_thread = threading.Thread(target = screen_saver)
	screen_saver_thread.start()
	game_windows = windows()
	game_windows.menu()

