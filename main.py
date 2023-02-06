# import pyglet as pgl


# window = pgl.window.Window()
# label = pgl.text.Label('Hello, world!', font_name='Times New Roman', font_size=36, 
# x=window.width//2, y=window.width//2, anchor_x='center', anchor_y='center')

# @window.event
# def on_draw():
#     window.clear()
#     label.draw()

# pgl.app.run()



import pyglet


game_window = pyglet.window.Window(visible=False, vsync=False)
game_window.set_caption('Моя игра')
icon1 = pyglet.image.load('16x16.png')
icon2 = pyglet.image.load('32x32.png')
game_window.set_icon(icon1, icon2)


game_window.set_visible()
if __name__ == '__main__':
    pyglet.app.run()