import pygame
from network import Network
from button import Button

class App:
    def __init__(self):
        print('init')
        self.btns = [Button("Rock", 50, 500, (0, 0, 0)), Button("Scissors", 250, 500, (255, 0, 0)), Button("Paper", 450, 500, (0, 255, 0))]
        self.player = None
        self.game = None
        self.n = None
        self.width = 1000
        self.height = 700

        self.id = -1
        self.CAPTION = "BINGO!"
        self.SCREEN_RESOLUTION = (1000, 700)
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
            elif self.GAME_STATE == self.STATE_PLAY:
                self.handle_play()
            elif self.GAME_STATE == self.STATE_WINNER:
                self.handle_winner()
        pygame.quit()

    def handle_welcome(self):
        self.screen.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Klik untuk Mulai Bermain!", 1, (255, 0, 0))
        self.screen.blit(text, (600, 400))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.GAME_STATE = self.STATE_PLAY
                self.handle_play()
        pygame.display.update()

    def handle_play(self):
        print('play')
        clock = pygame.time.Clock()
        clock.tick(60)
        self.n = Network()
        self.player = int(self.n.getP())
        while self.run:
            try:
                self.game = self.n.send("get")
            except:
                self.run = False
                print("Couldn't get game")
                break

            if self.game.bothWent():
                self.redrawWindow()
                pygame.time.delay(500)
                try:
                    self.game = self.n.send("reset")
                except:
                    self.run = False
                    print("Couldn't get game")
                    break

                font = pygame.font.SysFont("comicsans", 90)
                if (self.game.winner() == 1 and self.player == 1) or (self.game.winner() == 0 and self.player == 0):
                    text = font.render("You Won!", 1, (255, 0, 0))
                elif self.game.winner() == -1:
                    text = font.render("Tie Game!", 1, (255, 0, 0))
                else:
                    text = font.render("You Lost...", 1, (255, 0, 0))

                self.screen.blit(text, (self.width / 2 - text.get_width() / 2, self.height / 2 - text.get_height() / 2))
                pygame.display.update()
                pygame.time.delay(2000)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for btn in self.btns:
                        if btn.click(pos) and self.game.connected():
                            if self.player == 0:
                                if not self.game.p1Went:
                                    self.n.send(btn.text)
                            else:
                                if not self.game.p2Went:
                                    self.n.send(btn.text)

            self.redrawWindow()
        # self.screen.fill((128, 128, 128))
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         self.run = False
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         self.GAME_STATE = self.STATE_WELCOME
        # pygame.display.update()

    def handle_winner(self):
        pass

    def redrawWindow(self):
        self.screen.fill((128, 128, 128))

        if not (self.game.connected()):
            font = pygame.font.SysFont("comicsans", 80)
            text = font.render("Waiting for Player...", 1, (255, 0, 0), True)
            self.screen.blit(text, (self.width / 2 - text.get_width() / 2, self.height / 2 - text.get_height() / 2))
        else:
            font = pygame.font.SysFont("comicsans", 60)
            text = font.render("Your Move", 1, (0, 255, 255))
            self.screen.blit(text, (80, 200))

            text = font.render("Opponents", 1, (0, 255, 255))
            self.screen.blit(text, (380, 200))

            move1 = self.game.get_player_move(0)
            move2 = self.game.get_player_move(1)
            if self.game.bothWent():
                text1 = font.render(move1, 1, (0, 0, 0))
                text2 = font.render(move2, 1, (0, 0, 0))
            else:
                if self.game.p1Went and self.player == 0:
                    text1 = font.render(move1, 1, (0, 0, 0))
                elif self.game.p1Went:
                    text1 = font.render("Locked In", 1, (0, 0, 0))
                else:
                    text1 = font.render("Waiting...", 1, (0, 0, 0))

                if self.game.p2Went and self.player == 1:
                    text2 = font.render(move2, 1, (0, 0, 0))
                elif self.game.p2Went:
                    text2 = font.render("Locked In", 1, (0, 0, 0))
                else:
                    text2 = font.render("Waiting...", 1, (0, 0, 0))

            if self.player == 1:
                self.screen.blit(text2, (100, 350))
                self.screen.blit(text1, (400, 350))
            else:
                self.screen.blit(text1, (100, 350))
                self.screen.blit(text2, (400, 350))

            for btn in self.btns:
                btn.draw(self.screen)

        pygame.display.update()


if __name__ == "__main__":
    app = App()
    app.start()