import pygame

class Game:
    def __init__(self):
        print('init')
        self.id = -1
        self.CAPTION = "BINGO!"
        self.SCREEN_RESOLUTION = (1280, 720)
        pygame.init()
        pygame.display.set_caption(self.CAPTION)
        self.screen = pygame.display.set_mode(self.SCREEN_RESOLUTION)

        self.GAME_STATE = 1
        self.STATE_WELCOME = 1
        self.STATE_PLAY = 2
        self.STATE_WINNER = 3
        self.count_player = 1
        self.run = True

    def start(self):
        print('start')
        while self.run:
            if self.GAME_STATE == self.STATE_WELCOME:
                self.handle_welcome()
            if self.GAME_STATE == self.STATE_PLAY:
                self.handle_play()
            if self.GAME_STATE == self.STATE_WINNER:
                self.handle_winner()

        pygame.quit()

    def handle_welcome(self):
        welcome_text = "Welcome to BINGO!"
        welcome_font = pygame.font.SysFont('comicsans', 30, True)
        welcome_surface = welcome_font.render(welcome_text, 1, (255,255,255))

        player_text = "player {}...".format(self.count_player)
        player_font = pygame.font.SysFont('comicsans', 50, True)
        player_surface = player_font.render(player_text, 0, (255, 255, 255))

        waiting_text = "waiting player-({}/5)...".format(self.count_player)
        waiting_font = pygame.font.SysFont('comicsans', 50, True)
        waiting_surface = waiting_font.render(waiting_text, 0, (255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
        self.screen.fill((185, 116, 85))
        self.screen.blit(waiting_surface,(640 - waiting_surface.get_width()//2 , 360 - waiting_surface.get_height()//2))
        self.screen.blit(welcome_surface, (640 - welcome_surface.get_width()//2, 0))
        self.screen.blit(player_surface, (0, 0))
        pygame.display.update()



    def handle_play(self):
        pass

    def handle_winner(self):
        pass



if __name__ == "__main__":
    game = Game()
    game.start()