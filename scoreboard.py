from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
       super().__init__()
       self.score = 0
       with open("C:\\Users\\benbi\\OneDrive\\שולחן העבודה\\files\\files_to_snake\\data.txt","r") as data:
         self.high_score = int(data.read())
       self.color("white")
       self.penup()
       self.goto(0,265)
       self.hideturtle()
       self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self. write(f"Score: {self.score} High score: {self.high_score}",align="center",font=("Ariel",24,"normal"))
        
        

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("C:\\Users\\benbi\\OneDrive\\שולחן העבודה\\files\\files_to_snake\\data.txt","w")as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()

       

