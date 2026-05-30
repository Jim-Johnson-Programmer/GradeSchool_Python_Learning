"""Render a rotating cube in Python using PyOpenGL and GLUT.

Install the package first if needed:
    pip install PyOpenGL PyOpenGL_accelerate
"""

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


# This variable stores the cube's rotation angle.
# We will change it a little every frame so the cube spins.
angle_y = 0.0


def draw_cube():
    """Draw a cube using six colored faces."""

    # glBegin(GL_QUADS) tells OpenGL that we are about to draw
    # four-sided shapes.
    glBegin(GL_QUADS)

    # Front face (red)
    # range of colors 0.0 is no color, 1.0 is full color. You can mix them to get different colors.
    glColor3f(1.0, 0.0, 0.0)      # glColor3f sets the current drawing color (red, green, blue) range 0.0 to 1.0
    # glVertex3f specifies a corner of the shape we are drawing (x, y, z) range -1.0 to 1.0
    glVertex3f(-1.0, -1.0,  1.0)   # front bottom left, x=-1.0 is left, y=-1.0 is bottom, z=1.0 is front
    glVertex3f( 1.0, -1.0,  1.0)   # front bottom right, x=1.0 is right, y=-1.0 is bottom, z=1.0 is front
    glVertex3f( 1.0,  1.0,  1.0)  # front top right, x=1.0 is right, y=1.0 is top, z=1.0 is front
    glVertex3f(-1.0,  1.0,  1.0)  # front top left, x=-1.0 is left, y=1.0 is top, z=1.0 is front

    # Back face (green)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0,  1.0, -1.0)
    glVertex3f( 1.0,  1.0, -1.0)
    glVertex3f( 1.0, -1.0, -1.0)

    # Top face (blue)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-1.0,  1.0, -1.0)
    glVertex3f(-1.0,  1.0,  1.0)
    glVertex3f( 1.0,  1.0,  1.0)
    glVertex3f( 1.0,  1.0, -1.0)

    # Bottom face (yellow)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f( 1.0, -1.0, -1.0)
    glVertex3f( 1.0, -1.0,  1.0)
    glVertex3f(-1.0, -1.0,  1.0)

    # Right face (cyan)
    glColor3f(0.0, 1.0, 1.0)
    glVertex3f( 1.0, -1.0, -1.0)
    glVertex3f( 1.0,  1.0, -1.0)
    glVertex3f( 1.0,  1.0,  1.0)
    glVertex3f( 1.0, -1.0,  1.0)

    # Left face (magenta)
    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0,  1.0)
    glVertex3f(-1.0,  1.0,  1.0)
    glVertex3f(-1.0,  1.0, -1.0)

    glEnd()


def display():
    """This function draws one frame of the scene."""

    # Clear the screen and the depth buffer so we can draw fresh.
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Reset the model-view matrix so the next drawing starts clean.
    glLoadIdentity()

    # Move the cube away from the camera so we can see it.
    glTranslatef(0.0, 0.0, -7.0)

    # Rotate the cube so it looks like it is spinning.
    glRotatef(angle_y, 1.0, 1.0, 0.0)

    # Draw the cube.
    draw_cube()

    # Send the finished image to the screen.
    glutSwapBuffers()


def update(value):
    """Update the animation and ask GLUT to draw again."""

    global angle_y

    # Increase the angle a little each frame.
    angle_y = (angle_y + 1.0) % 360.0

    # Tell GLUT to redraw the window.
    glutPostRedisplay()

    # Ask GLUT to call this function again after 16 milliseconds.
    # That gives us about 60 frames per second.
    glutTimerFunc(16, update, 0)


def reshape(width, height):
    """Adjust the scene when the window changes size."""

    # Prevent division by zero if the window height becomes 0.
    if height == 0:
        height = 1

    # Tell OpenGL that the whole window is the drawing area.
    glViewport(0, 0, width, height)

    # Switch to the projection matrix so we can set the camera view.
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Set a perspective projection so the cube looks 3D.
    gluPerspective(45.0, float(width) / float(height), 0.1, 50.0)

    # Switch back to the model-view matrix for drawing objects.
    glMatrixMode(GL_MODELVIEW)


def init():
    """Set up the OpenGL settings we want to use."""

    # Set the background color to a dark blue-gray.
    glClearColor(0.08, 0.10, 0.16, 1.0)

    # Turn on depth testing so faces in front hide faces behind them.
    glEnable(GL_DEPTH_TEST)


def main():
    """Create the window and start the OpenGL event loop."""

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"PyOpenGL Rotating Cube")

    init()

    # Register the functions GLUT should call.
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutTimerFunc(16, update, 0)

    # Start the program. This keeps the window open.
    glutMainLoop()


if __name__ == "__main__":
    main()
