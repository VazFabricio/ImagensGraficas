# Importações necessárias
import glfw
from OpenGL.GL import *
import numpy as np

# Verifica se glfw pode ser inicializado
if not glfw.init():
    raise Exception("glfw can not be initialized")

# Cria uma janela GLFW de 600x400 pixels
window = glfw.create_window(600, 400, "Dois quadrados", None, None)

# Verifica se a janela foi criada com sucesso
if not window:
    glfw.terminate()
    raise Exception("glfw can not be created")

# Define a posição da janela na tela
glfw.set_window_pos(window, 400, 200)

# Torna a janela o contexto atual
glfw.make_context_current(window)

# Define as coordenadas dos vértices dos dois quadrados
vertices = [-0.2, -0.2, 0.0,  # vértices do primeiro quadrado
            0.2, -0.2, 0.0,
            0.2, 0.2, 0.0,
            -0.2, 0.2, 0.0,
            0.3, -0.2, 0.0,  # vértices do segundo quadrado
            0.7, -0.2, 0.0,
            0.7, 0.2, 0.0,
            0.3, 0.2, 0.0]

# Define as cores dos vértices dos dois quadrados
colors = [1.0, 0.0, 0.0,  # cores do primeiro quadrado
          1.0, 0.0, 0.0,
          1.0, 0.0, 0.0,
          1.0, 0.0, 0.0,
          0.0, 1.0, 0.0,  # cores do segundo quadrado
          0.0, 1.0, 0.0,
          0.0, 1.0, 0.0,
          0.0, 1.0, 0.0]

# Converte as listas de vértices e cores para arrays do NumPy com tipo de dados float32
vertices = np.array(vertices, dtype=np.float32)
colors = np.array(colors, dtype=np.float32)

# Habilita o uso de arrays de vértices
glEnableClientState(GL_VERTEX_ARRAY)

# Define o array de vértices a ser utilizado
glVertexPointer(3, GL_FLOAT, 0, vertices)

# Habilita o uso de arrays de cores
glEnableClientState(GL_COLOR_ARRAY)

# Define o array de cores a ser utilizado
glColorPointer(3, GL_FLOAT, 0, colors)

# Define a cor de fundo da janela
glClearColor(0, 0, 0, 1)

# Loop principal do programa
while not glfw.window_should_close(window):
    # Verifica eventos de entrada
    glfw.poll_events()

    # Limpa o buffer de cor
    glClear(GL_COLOR_BUFFER_BIT)

    # Desenha o primeiro QUADRADO
    glDrawArrays(GL_QUADS, 0, 4)

    # Desenha o segundo QUADRADO
    glDrawArrays(GL_QUADS, 4, 4)

    # Troca os buffers da janela
    glfw.swap_buffers(window)

# Termina o GLFW
glfw.terminate()
