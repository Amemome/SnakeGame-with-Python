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
        self.gameSpeed = 10.5
        self.cellSize = 20 #cell size 를 누가 들고있을지 나중에 수정
        self.food = None
        self.score = 0
    def getDisplay(self):
        return (self.width,self.hegiht)
    
    def getCellsize(self):
        return self.cellSize
    def run(self):
        """run the game"""
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
                    
                    if event.key == pygame.K_a:
                        self.snake.addLength(3)


            self.screen.fill((10,0,30))
            self.snake.move()
            
            if(self.snake.checkCollision(self.width,self.height)):
                self.quit() # 죽은 화면을 출력해야 하지만 게임 끄는걸로.
            if(self.snake.checkEatFood(self.food)):
                self.score += self.food.getPoint()
                self.snake.addLength(self.food.getPoint())
                self.generateFood()

            self.food.draw(self.screen)
            self.snake.draw(self.screen)
            self.drawScore()
            pygame.display.flip()
            self.clock.tick(self.gameSpeed)

    def generateFood(self):
        self.food = random.choice([fd.Item1,fd.Item2,fd.Item3])()
        self.food.setPosition(self.width,self.height,self.cellSize)


    def drawScore(self):
        font = pygame.font.Font(None,20)
        scoreText = font.render(f"Score : {self.score}", True, (255,255,255))
        self.screen.blit(scoreText,(24,24))

    def quit(self):
        pygame.quit()
        sys.exit()

    def __del__(self):
        pygame.quit()
