_author__ = 'Hanna'


class EntradaUsuario():
    def __init__(self):
        self.set()

    def set(self):
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.quit_pressed = False
        self.up_pressed = False
        self.space_pressed = False
        self.enter_pressed = False

    def reset(self):
        self.set()
