import glfw
from OpenGL.GL import *
from OpenGL.GL import shaders
from pyrr import matrix44
from pyrr import Vector3
import numpy as np

VERTEX_SHADER = """
#version 330 core 
layout (location = 0) in vec3 position;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

void main()
{
    gl_Position = projection * view * model * vec4(position, 1.0f);
}
"""

FRAGMENT_SHADER = """
#version 330 core 
out vec4 color;

void main()
{
    color = vec4(1.0f, 1.0f, 1.0f, 1.0f);
}
"""


class VECTOR3:

    def __init__(
            self,
            x,
            y,
            z,
    ):
        self.x = x
        self.y = y
        self.z = z


class MATRIX44:

    def __init__(self, m=None):
        if m is None:
            self.m = np.identity(4, dtype=np.float32)
        else:
            self.m = np.array(m, dtype=np.float32)

    def __mul__(self, other):
        return MATRIX44(np.dot(self.m, other.m))

    def translate(self, x, y, z):
        m = np.identity(4, dtype=np.float32)
        m[0, 3] = x
        m[1, 3] = y
        m[2, 3] = z
        self.m = np.dot(self.m, m)

    def rotate(self, angle, x, y, z):
        c = np.cos(angle)
        s = np.sin(angle)
        norm = np.sqrt(x * x + y * y + z * z)
        x /= norm
        y /= norm
        z /= norm
        m = np.identity(4, dtype=np.float32)
        m[0, 0] = x * x * (1 - c) + c
        m[0, 1] = x * y * (1 - c) - z * s
        m[0, 2] = x * z * (1 - c) - y * s
        m[1, 0] = y * x * (1 - c) + z * s
        m[1, 1] = y * y * (1 - c) + c
        m[1, 2] = y * z * (1 - c) - x * s
        m[2, 0] = x * z * (1 - c) - y * s
        m[2, 1] = y * z * (1 - c) + x * s
        m[2, 2] = z * z * (1 - c) + c
        self.m = np.dot(self.m, m)

    def scale(self, x, y, z):
        m = np.identity(4, dtype=np.float32)
        m[0, 0] = x
        m[1, 1] = y
        m[2, 2] = z
        self.m = np.dot(self.m, m)


class Cube:
    def __init__(self, size):
        self.shader = None
        self.vertices = np.array([
            [-1, -1, 0],
            [1, -1, 0],
            [1, 1, 0],
            [-1, 1, 0],
        ], dtype=np.float32) * size / 2

        self.indices = np.array([
            [0, 1, 2],
            [2, 3, 0],
        ], dtype=np.uint32)

        self.colors = np.array([
            [1, 0, 0],
            [1, 0, 0],
            [1, 0, 0],
            [1, 0, 0],
        ], dtype=np.float32)

        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)

        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(0)

        self.ebo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.indices.nbytes, self.indices, GL_STATIC_DRAW)

        glBindVertexArray(0)

    def draw(
            self,
            model,
            view,
            projection,
    ):
        glUseProgram(self.shader)

        glUniformMatrix4fv(glGetUniformLocation(self.shader, "model"), 1, GL_FALSE, model)
        glUniformMatrix4fv(glGetUniformLocation(self.shader, "view"), 1, GL_FALSE, view)
        glUniformMatrix4fv(glGetUniformLocation(self.shader, "projection"), 1, GL_FALSE, projection)

        glBindVertexArray(self.vao)
        glDrawElements(GL_TRIANGLES, len(self.indices) * 3, GL_UNSIGNED_INT, None)
        glBindVertexArray(0)

    def set_shader(self, shader):
        self.shader = shader


def main():
    if not glfw.init():
        return

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    window = glfw.create_window(900, 600, 'Cubo parametric', None, None)
    if not window:
        glfw.terminate()
        return

    glfw.set_window_pos(window, 560, 250)
    glfw.make_context_current(window)

    glClearColor(1.0, 1.0, 0.3, 1.0)

    cube = Cube(1.0)

    shader = shaders.compileProgram(
        shaders.compileShader(VERTEX_SHADER, GL_VERTEX_SHADER),
        shaders.compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
    )
    cube.set_shader(shader)

    glEnable(GL_DEPTH_TEST)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        view = matrix44.create_from_translation(Vector3([0.0, 0.0, -5.0]))
        projection = matrix44.create_perspective_projection_matrix(45.0, 800 / 600, 0.1, 100.0)

        model = matrix44.create_from_axis_rotation(Vector3([0.5, 1.0, 0.0]), glfw.get_time())

        cube.draw(model, view, projection)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == '__main__':
    main()
