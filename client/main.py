import pygame

class Game:
    def __init__(self):
        print('init')
        self.CAPTION = "BINGO!"
        self.SCREEN_RESOLUTION = (1280, 720)
        pygame.init()
        pygame.display.set_caption(self.CAPTION)
        pygame.display.set_mode(self.SCREEN_RESOLUTION)

        self.GAME_STATE = 1
        self.WELCOME_STATE = 1
        self.PLAY_STATE = 2
        self.WINNER_STATE = 3

    def start(self):
        print('start')
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            if self.GAME_STATE == self.WELCOME_STATE:
                self.handle_welcome()
            if self.GAME_STATE == self.PLAY_STATE:
                self.handle_play()
            if self.GAME_STATE == self.WINNER_STATE:
                self.handle_winner()

    def handle_welcome(self):
        pass

    def handle_play(self):
        pass

    def handle_winner(self):
        pass



if __name__ == "__main__":
    game = Game()
    game.start()