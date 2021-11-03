import pyautogui as p 
import time as t 

arriba = (725,362)
izquierda = (639,361)
abajo = (638,404)
derecha = (726,404)

class esqueje:

	def algatrenza():
		p.keyDown('alt')
		p.press('4')
		p.keyUp('alt')
	def carya():
		p.keyDown('alt')
		p.press('3')
		p.keyUp('alt')
	def zarza():
		p.keyDown('alt')
		p.press('2')
		p.keyUp('alt')
	def maracaju():
		p.keyDown('alt')
		p.press('1')
		p.keyUp('alt')
	def kokotero():
		p.keyDown('ctrl')
		p.press('8')
		p.keyUp('ctrl')
	def divi():
		p.keyDown('ctrl')
		p.press('7')
		p.keyUp('ctrl')

class direccion:

	def up():
		p.moveTo(arriba[0],arriba[1])
	def up_click():
		direccion.up()
		p.click()
	def up_right_click():
		direccion.up()
		p.click(button='right')

	def left():
		p.moveTo(izquierda[0],izquierda[1])
	def left_click():
		direccion.left()
		p.click()
	def left_right_click():
		direccion.left()
		p.click(button='right')

	def right():
		p.moveTo(derecha[0],derecha[1])
	def right_click():
		direccion.right()
		p.click()
	def right_right_click():
		direccion.right()
		p.click(button='right')

	def down():
		p.moveTo(abajo[0],abajo[1])
	def down_click():
		direccion.down()
		p.click()
	def down_right_click():
		direccion.down()
		p.click(button='right')

class reposiciona:

	def reposition():
		#Lo vuelve a la esquina superior del jardin
		for ciclo in range(10):
			direccion.left_click()
			direccion.up_click()
		#Lo reposiciona una casilla atras para poder plantar
		direccion.down_click()

class planta:
	def plantar():
		reposiciona.reposition()
		for alto_jardin in range(10):
			for largo_jardin in range(10):
                                #Se puede utilizar cualquiera
				esqueje.algatrenza()
				direccion.up()
				for iteration in range(5): #Se itera porque tiene un 60% de exito
					p.click()
					#Tiempo que dura cada plantacion
					t.sleep(5)
				p.click(button='right')
				direccion.right_click()
			direccion.right_click()
			direccion.down_click()
			for iteration in range(10):
				direccion.left_click()
				t.sleep(1)
t.sleep(2)
planta.plantar()

