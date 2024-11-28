import sys,pygame
import snake as Snk

class Game:
    def __init__(self,X,Y):
        success, fail = pygame.init()
        print(f'success {success} , fail : {fail}')
        self.width = X
        self.height = Y
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.gameSpeed = 12
        self.cellSize = 20 #cell size 를 누가 들고있을지 나중에 수정
        

    def run(self):
        """run the game"""
        snake = Snk.Snake()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: self.running = False
            
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        snake.setDirection("up")
                    if event.key == pygame.K_DOWN:
                        snake.setDirection("down")
                    if event.key == pygame.K_LEFT:
                        snake.setDirection("left")
                    if event.key == pygame.K_RIGHT:
                        snake.setDirection("right")

            self.screen.fill((10,0,30))
            snake.move()
            if(snake.checkCollision(self.width,self.height)):
                self.quit() # 죽은 화면을 출력해야 하지만 게임 끄는걸로.



            snake.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(self.gameSpeed)



    def quit(self):
        pygame.quit()
        sys.exit()

    def __del__(self):
        pygame.quit()
