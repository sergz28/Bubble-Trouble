import pyglet


# window = pyglet.window.Window()

# label = pyglet.text.Label('Hello, world!', font_name='Times New Roman', font_size=36,
#                           x=window.width/2, y=window.height/2, anchor_x='center',anchor_y='center')

# @window.event
# def on_draw():
#     window.clear()
#     label.draw()


# pyglet.app.run()


# window = pyglet.window.Window()
# image = pyglet.resource.image('assets/kitten.jpg')

# @window.event
# def on_draw():
#     window.clear()
#     image.blit(window.width/2, window.height/2,)

# pyglet.app.run()



# from pyglet.window import key
# from pyglet.window import mouse
# window = pyglet.window.Window()

# @window.event
# def on_key_press(symbol, modifiers):
#     if symbol == key.A:
#         print('The A symbol was pressed')
#     elif symbol == key.LEFT:
#         print('The left arrow was pressed')

# @window.event
# def on_mouse_press(x, y, button, modifiers):
#     if button == mouse.LEFT:
#         print('The left button was pressed at {}'.format((x,y)))

# @window.event
# def on_draw():
#     window.clear()

# pyglet.app.run()




window = pyglet.window.Window(style=pyglet.window.Window.WINDOW_STYLE_TRANSPARENT)
music = pyglet.resource.media('assets/music.mp3')

label = pyglet.text.Label('Hello, world!', font_name='Times New Roman', font_size=36,
                          x=window.width/2, y=window.height/2, anchor_x='center',anchor_y='center')

@window.event
def on_draw():
    window.clear()
    label.draw()

music.play()



pyglet.app.run()