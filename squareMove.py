import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np

vertex_src = """
# version 330
layout(location = 0) in vec3 a_position;
layout(location = 1) in vec3 a_color;
out vec3 v_color;
void main()
{
    gl_Position = vec4(a_position, 1.0);
    v_color = a_color;
}
"""

fragment_src = """
# version 330
in vec3 v_color;
out vec4 out_color;
void main ()
{
    out_color = vec4(v_color, 1.0);
}
"""


def window_resize(window, width, height):
    glViewport(0, 0, width, height)


# iniciar a biblioteca
if not glfw.init():
    raise Exception("glfw can not be initialized!")

# criar a janela glfw
window = glfw.create_window(720, 720, "My OpenGL window", None, None)

# checagem se foi de fato criada
if not window:
    glfw.terminate()
    raise Exception("glfw window can not be created!")

# definir a posição da janela em relação ao monitor
glfw.set_window_pos(window, 400, 200)

glfw.set_window_size_callback(window, window_resize)

# definir a janela como contexto atual
glfw.make_context_current(window)

vertices = [-0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
            0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
            -0.5, 0.5, 0.0, 0.0, 0.0, 1.0,
            0.5, 0.5, 0.0, 1.0, 1.0, 1.0]

vertices = np.array(vertices, dtype=np.float32)

shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragment_src, GL_FRAGMENT_SHADER))

VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))

glUseProgram(shader)
glClearColor(0, 0.1, 0.1, 1)

while not glfw.window_should_close(window):
    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT)

    ct = glfw.get_time()
    model = np.identity(4, np.float32)
    model = np.matmul(model, np.array([[abs(np.sin(ct)), 0, 0, 0], [0, abs(np.sin(ct)), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32))
    model = np.matmul(model, np.array([[np.cos(ct), np.sin(ct), 0, 0], [-np.sin(ct), np.cos(ct), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32))
    model_loc = glGetUniformLocation(shader, "u_model")
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)

    glfw.swap_buffers(window)

glfw.terminate()
