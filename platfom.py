from random import shuffle

class Platform:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.color = color
        
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        start = list(range(20, 220, 20))
        shuffle(start)
        self.start_point_x = start[0]

        self.canvas.move(self.id, self.start_point_x, 300)

        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.started = False
        self.canvas.bind_all('<KeyPress-Return>', self.start_game)

    def turn_left(self, event):
        self.x = -2

    def turn_right(self, event):
        self.x = 2

    def start_game(self, event):
        self.started = True

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <=0 or pos[2] >= self.canvas_width:
            self.x = 0
