# This module serves as the primary interface with PyOpenGL.
# Written by Calvin Weaver.

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Painter:

	# Constructor initializes the window and starts the GLUT main loop
	def __init__(self, updateRef, wSize, wTitle):
		# Initialize the display window through GLUT
		glutInit()
		glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
		glutInitWindowSize(wSize[0], wSize[1])
		glutCreateWindow(wTitle)
		glutDisplayFunc(self.render)
		glutIdleFunc(self.render)
	
		# OpenGL clear values
		glClearColor(0.0, 0.0, 0.0, 1.0)
		glClearDepth(1.0)
		
		# OpenGL configure depth testing for polygon intersections
		glEnable(GL_DEPTH_TEST)
		glDepthMask(GL_TRUE)
		glDepthFunc(GL_LEQUAL)
		glDepthRange(0.0, 1.0)
		
		# OpenGL projections
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective(45.0, wSize[0] / wSize[1], 1.0, 100.0)
		glMatrixMode(GL_MODELVIEW)
		
		# Attach update function reference
		self.updateRef = updateRef
		
		# Start the GLUT main loop
		glutMainLoop()

	def render(self):
		# Clear old OpenGL scene
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()
		
		# Call update function for painter user
		self.updateRef()
		
		# GLUT display rendered content to window
		glutSwapBuffers()

# Static utility method for drawing a quad in 3D space	
def painterDrawQuad(color, vertices):
	glBegin(GL_QUADS)
	glColor3f(color[0], color[1], color[2])
	glVertex3f(vertices[0][0], vertices[0][1], vertices[0][2])
	glVertex3f(vertices[1][0], vertices[1][1], vertices[1][2])
	glVertex3f(vertices[2][0], vertices[2][1], vertices[2][2])
	glVertex3f(vertices[3][0], vertices[3][1], vertices[3][2])
	glEnd()
	