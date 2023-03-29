# Importações necessárias
import glfw
from OpenGL.GL import *
import numpy as np
from math import sin, cos

# Verifica se glfw pode ser inicializado
if not glfw.init():
    raise Exception("glfw can not be initialized")

# Cria uma janela GLFW de 600x400 pixels
window = glfw.create_window(600, 400, "uma janela para o seu bruxo", None, None)

# Verifica se a janela foi criada com sucesso
if not window:
    glfw.terminate()
    raise Exception("glfw can not be created")

# Define a posição da janela na tela
glfw.set_window_pos(window, 400, 100)

# Torna a janela o contexto atual
glfw.make_context_current(window)

# Define a janela como o contexto atual novamente
glfw.make_context_current(window)

# Define as coordenadas dos vértices do triângulo
vertices = [-0.5, -0.5, 0.0,
             0.5, -0.5, 0.0,
             -0.5, 0.5, 0.0]

# Define as cores dos vértices do triângulo
colors = [1.0, 0.0, 0.0,
          1.0, 0.0, 0.0,
          0.0, 0.0, 1.0]

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
glClearColor(0, 0.1, 0.1, 1)

# Loop principal do programa
while not glfw.window_should_close(window):
    # Verifica eventos de entrada
    glfw.poll_events()

    # Limpa o buffer de cor
    glClear(GL_COLOR_BUFFER_BIT)

    # Obtém o tempo atual
    ct = glfw.get_time()

    # Define a matriz de transformação atual como identidade
    glLoadIdentity()

    # Escala a matriz de transformação pelos valores de seno e cosseno do tempo atual
    glScale(abs(sin(ct)), abs(sin(ct)), 1)

    # Rotaciona a matriz de transformação em torno do eixo Z pelo valor de seno do tempo atual vezes 45 graus
    glRotatef(sin(ct) * 45, 0, 0, 1)

    # Translada a matriz de transformação pelos valores de seno e cosseno do tempo atual
    glTranslatef(sin(ct), cos(ct), 0)

    # Desenha o triângulo
    glDrawArrays(GL_TRIANGLES, 0, 3)

    # Troca os buffers da janela
    glfw.swap_buffers(window)

# Termina o GLFW
glfw.terminate()
