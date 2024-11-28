import sys,pygame,obj
import snake as Snk
speed = [2,2]
black = 0,0,0
class Game:
    def __init__(self,X,Y):
        pygame.init()
        self.width = X
        self.height = Y
        self.screen = pygame.display.set_mode((X,Y))
        self.clock = pygame.time.Clock()
        self.running = True
        self.board = [[0 for _ in range(64)] for _ in range(36)] # board 를 초기화.
        obj.GameObject.cellSize = 20
        

    def run(self):
        """run the game"""
        snake = Snk.Snake()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            
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
            snake.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(10)



    def quit(self):
        pygame.quit()
        sys.exit()

    def __del__(self):
        pygame.quit()



pg = Game(1280,720) # 64 36
pg.run() # 이벤트 루프 돌기 시작.

