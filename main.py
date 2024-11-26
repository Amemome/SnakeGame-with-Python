import sys,pygame
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
        

    def run(self):
        ballrect = pygame.Rect(100,100,50,50)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            ballrect = ballrect.move(speed)
            if ballrect.left < 0 or ballrect.right > self.width:
                speed[0] = -speed[0]
            if ballrect.top < 0 or ballrect.bottom > self.height:
                speed[1] = -speed[1]

            self.screen.fill(black)
            pygame.draw.rect(self.screen,(255,0,0),ballrect)
            pygame.display.flip()
            self.clock.tick(60)



    def quit(self):
        pygame.quit()
        sys.exit()

    def __del__(self):
        pygame.quit()


pg = Game(1280,720)

pg.run()