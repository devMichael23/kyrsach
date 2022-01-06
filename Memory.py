from SiliconWorld import SiliconWorld
from Electronic import Electronic


class Memory:
    def __init__(self, w, h):
        self.silicon_world = SiliconWorld(w, h)
        self.electronic = Electronic()
        self.silicon_world.set_params_to_map(self.electronic.location.x, self.electronic.location.y, 5)

    def move_electronic(self, y, x):
        if self.electronic.fuel.need:
            if self.electronic.fuel.bank > 0:
                self.electronic.fuel.bank = self.electronic.fuel.bank - 1
            else:
                exit(0)
        self.silicon_world.set_params_to_map(self.electronic.location.x, self.electronic.location.y, 1)
        self.electronic.location.x = x
        self.electronic.location.y = y
        self.update_electronic_pos()

    def update_electronic_pos(self):
        self.silicon_world.set_params_to_map(self.electronic.location.x, self.electronic.location.y, 5)

    def get_silicon_world(self):
        return self.silicon_world

    def get_electronic(self):
        return self.electronic
