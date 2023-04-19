import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np


def main():
    vertex_shader = """
        #version 330 core 
        layout (location = 0) in vec2 a_position;
        void main(){
            gl_Position = vec4(a_position, 0.0, 1.0);
        }
    """

    fragment_shader = """
        #version 330 core 
        out vec4 FragColor;
        void main(){
            FragColor = vec4(1.0, 1.0, 1.0, 1.0);
        }
    """

    if not glfw.init():
        return

    window = glfw.create_window(800, 600, "My OpenGL window", None, None)

    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)

    vertices = np.array([
        -0.5, -0.5,
        0.5, -0.5,
        0.5, 0.5,
        -0.5, 0.5
    ], dtype=np.float32)

    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, None)
    glEnableVertexAttribArray(0)

    shader_program = compileProgram(
        compileShader(vertex_shader, GL_VERTEX_SHADER),
        compileShader(fragment_shader, GL_FRAGMENT_SHADER)
    )

    # loop principal
    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT)
        glUseProgram(shader_program)
        glDrawArrays(GL_QUADS, 0, 4)

        glfw.swap_buffers(window)

    glDeleteVertexArrays(1, [vao])
    glDeleteBuffers(1, [vao])
    # encerra glfw
    glfw.terminate()


if __name__ == '__main__':
    main()
