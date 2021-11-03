# Wakfu Automatización de Tareas
Automatización de tareas para el MMORPG Wakfu mediante la utilización de Python, la librería PyAutoGui y Time, para una implementación básica.

## Fin
El juego cuenta con un sistema de recolección de recursos, en este caso particular se utiliza un entorno llamado MerkaSaco el cual consiste en un panel 2.5D de 70*70 celdas en las cuales se pueden distribuir zonas para distintos usos; cultivos, creación de objetos, etc.

El propósito es automatizar la recolección y planta de recursos en un plano de 10*10 para así dejar el programa corriendo y el personaje recolectando automáticamente sin intervención del usuario.

## Uso
Para este caso particular se utiliza un panel 10*10 para cultivos en la esquina inferior del mapa, con la que basta entrar al MerkaSaco y abrir el archivo wakfu_bot.py.

# ToDo
Implementar una interfaz GUI en conjunto a personalizaciones del conjunto; permitir elegir el número de casillas, qué tipo de recurso plantar, en qué hotkey conectar tal recurso, etc.

# ForFun
Clarificacion
: El uso de esta aplicación es meramente recreativo y no se busca nada más que aprendizaje.


# Archivo
```python
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
```