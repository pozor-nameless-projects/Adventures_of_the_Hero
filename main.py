
from ezprint import pприкул
import random
import os

user = 'Jana'
age = 0

class people:

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

gnom = people('Gnom', 120, 'Гномы обитают в подземелье. Они не опасны, пока их не разозлить', 5, 0)
dragon = people('Dragon', 562, 'Дракон очень сверепое существо. Остерегайтесь его в замке', 14, 1)
# h = people(user, age, 'Ваш перссонаж бродит по темным уголкам этого средневекового века. Он ищет не только приключения, но и семь тоинственных душ')