# This module serves as the main entry point for the program.
# Makes use of the Painter.py helper module for easier interaction
# with OpenGL.
# Written by Calvin Weaver.

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from Painter import *

rotation = 45

# Update function is called by our Painter class once every frame
def update():
	global rotation

	colorGray = [0.6, 0.6, 0.6]
	colorDarkGray = [0.3, 0.3, 0.3]
	
	# OpenGL commands for camera positioning and rotation
	glPushMatrix()
	glTranslatef(0.0, -1.0, -5.0)
	glRotatef(rotation, 0.0, 1.0, 0.0)
	
	# Draw tiled grid on the floor for a frame of reference
	gridSize = 0.2
	for x in range(-5, 6, 1):
		for z in range(-5, 6, 1):
			color = colorGray if (x + z) % 2 == 0 else colorDarkGray
			painterDrawQuad(color, [
				[x * gridSize - gridSize / 2.0, 0, z * gridSize - gridSize / 2.0],
				[x * gridSize + gridSize / 2.0, 0, z * gridSize - gridSize / 2.0],
				[x * gridSize + gridSize / 2.0, 0, z * gridSize + gridSize / 2.0],
				[x * gridSize - gridSize / 2.0, 0, z * gridSize + gridSize / 2.0]
			])
	
	# Draw intersecting shape to demonstrate depth testing
	colorBlue = [0.0, 0.0, 1.0]
	colorGreen = [0.0, 1.0, 0.0]
	painterDrawQuad(colorBlue, [
		[-0.3, 0.0, 0.0],
		[0.3, 0.0, 0.0],
		[0.3, 0.6, 0.0],
		[-0.3, 0.6, 0.0]
	])
	painterDrawQuad(colorGreen, [
		[0.0, 0.0, -0.3],
		[0.0, 0.0, 0.3],
		[0.0, 0.6, 0.3],
		[0.0, 0.6, -0.3]
	])
	
	# OpenGL reset camera transformation
	glPopMatrix()
	
	# Rotate the camera
	rotation = rotation + 0.1

painter = Painter(update, [512, 512], "Calvin Weaver - OpenGL 3D Example - CPE 551 Final Project")