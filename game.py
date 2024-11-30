import sys,pygame,random
import snake as snk
import food as fd

class Game:
    def __init__(self,X,Y):
        success, fail = pygame.init()
        print(f'success {success} , fail : {fail}')
        self.width = X
        self.height = Y
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.gameOver = False
        self.gameSpeed = 10.5
        self.cellSize = 20 # cell size 를 누가 들고있을지 나중에 수정
        self.food = None
        self.score = 0

    def getDisplay(self):
        return (self.width,self.hegiht)
    
    def getCellsize(self):
        return self.cellSize
    
    def run(self):
        """run the game"""

        self.showStartScreen()
        self.snake = snk.Snake()
        self.generateFood()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: self.running = False
            
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.setDirection("up")
                    if event.key == pygame.K_DOWN:
                        self.snake.setDirection("down")
                    if event.key == pygame.K_LEFT:
                        self.snake.setDirection("left")
                    if event.key == pygame.K_RIGHT:
                        self.snake.setDirection("right")
                    
                    if event.key == pygame.K_a: # 디버깅용 
                        self.snake.addLength(3)


            
            self.snake.move()
            
            if(self.snake.checkCollision(self.width,self.height)):
                self.gameOver = True

            if(self.gameOver):
                self.showGameOver()

            if(self.snake.checkEatFood(self.food)):
                self.score += self.food.getPoint()
                self.snake.addLength(self.food.getPoint())
                self.generateFood()
            



            self.screen.fill((10,0,30))
            self.food.draw(self.screen)
            self.snake.draw(self.screen)
            self.drawScore()

            pygame.display.flip()
            self.clock.tick(self.gameSpeed)
            

    def generateFood(self):
        while True:
            new_food = random.choice([fd.Item1, fd.Item2, fd.Item3])()
            new_food.setPosition(self.width, self.height, self.cellSize)
            if new_food.getPosition() not in self.snake.body:
                self.food = new_food
                break

    def drawScore(self):
        font = pygame.font.Font(None,48)
        scoreText = font.render(f"Score : {self.score}", True, (255,255,255))
        self.screen.blit(scoreText,(24,24))



    def showStartScreen(self):
        self.screen.fill((0,0,0))
        title = pygame.font.Font(None,128).render("Snake Game",True,(230,230,33))
        pressText = pygame.font.Font(None,48).render("Press any key to start",True,(230,230,33))
        self.screen.blit(title,(self.width // 2 - title.get_width() // 2, self.height // 3))
        self.screen.blit(pressText,(self.width // 2 - pressText.get_width() // 2, self.height // 3 * 2))
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    exit(1)
                elif event.type == pygame.KEYDOWN:
                    waiting = False
        
    def showGameOver(self):
        text = pygame.font.Font(None, 74).render("Game Over! Press R to Restart", True, (255, 255, 255))
        self.screen.blit(text, (self.width // 2 - text.get_width() // 2, self.height // 2))
        pygame.display.flip()

        while self.gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset()  # 게임 재시작
                        self.gameOver = False


    def reset(self):
        self.snake = snk.Snake()
        self.generateFood()
        self.score = 0


    def quit(self):
        pygame.quit()
        sys.exit()

    def __del__(self):
        pygame.quit()



