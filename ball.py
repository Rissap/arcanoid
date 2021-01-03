import random

class Ball:
    def __init__(self, canvas, paddle, score, color):
        self.canvas = canvas
        self.platform = platform
        self.score = score
        self.color = color

        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        
        start_from = [-2, -1, 1, 1]
        random.shuffle(start_from)
        self.x = start_from[0]
        self.y = -2

        self.canvas_height = canvas.winfo_height()
        self.canvas_width = canvas.winfo_width()

        self.hit_bottom = False

    def hit_platform(self, pos):
        platform_pos = self.canvas.coords(self.platform.id)
        if pos[2] >= platform_pos[0] and pos[0] <= platform_pos[2]:
            if pos[3] >= platform_pos[1] and pos[3] <= platform_pos[3]:
                self.score.hit()
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.y = 2

        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            canvas.create_text(250, 120, text="You loose!", font("Courier", 30), fill="orange")

        if self.hit_platform(pos):
            self.y = -2

        if pos[0] <= 0:
            self.x = 2

        if pos[2] >= self.canvas_width:
            self.x = -2
