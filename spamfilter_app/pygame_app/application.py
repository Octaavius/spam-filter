import pygame
from pygame_app.const import *
from utils.stringInput import String

class Application:
    def __init__(self, language_model_manager):
        pygame.init()
        pygame.display.set_caption('SPAM FILTER')
        self.screen = pygame.display.set_mode(DISPLAY_SIZE)

        self.language_model_manager = language_model_manager

        self.font = pygame.font.Font(None, FONT_SIZE)
        self.start_input_box = pygame.Rect(*INPUT_BOX_START_POS, INPUT_BOX_WIDTH, INPUT_BOX_HEIGHT)
        self.input_box = self.start_input_box.copy()
        self.input_string = String(VISIBLE_LINES_COUNT, INPUT_BOX_HEIGHT, INPUT_BOX_WIDTH - WIDTH_EPS)
        
        self.running = True
        self.showResult = False
        self.isSpam = False

    def start(self):
        while self.running:
            if not self.showResult:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            if self.input_string.pop():
                                self.input_box.height -= INPUT_BOX_HEIGHT

                        elif event.key == pygame.K_RETURN:
                            input_text = self.input_string.submit()
                            self.isSpam = self.language_model_manager.spam_checker(input_text)
                            self.input_box = self.start_input_box.copy()
                            self.showResult = True

                        elif event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
                            self.input_string.copy()

                        elif event.key == pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
                            self.input_box.height += INPUT_BOX_HEIGHT * self.input_string.paste(self.input_box.height, self.font)

                        elif event.key == pygame.K_UP:
                            self.input_string.scroll_up()
                        elif event.key == pygame.K_DOWN:
                            self.input_string.scroll_down()

                        else:
                            if self.input_string.add(event.unicode, self.input_box.height, self.font):
                                self.input_box.height += INPUT_BOX_HEIGHT

                    self.draw_parts()
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            self.showResult = False
                    
                    self.draw_parts()

        pygame.quit()

    def draw_parts(self):
        self.screen.fill(BG_COLOR)
        
        if not self.showResult:
            self.draw_input_box()
            self.draw_title()
        else:
            self.draw_spam_check_result()
            
        pygame.display.flip()

    def draw_input_box(self):
        border_rect = self.input_box.inflate(BORDER_THICKNESS*2, BORDER_THICKNESS*2)
        pygame.draw.rect(self.screen, BORDER_COLOR, border_rect, border_radius=BORDER_RADIUS)
        
        pygame.draw.rect(self.screen, INPUT_BOX_COLOR, self.input_box, border_radius=BORDER_RADIUS)
        for i, line in enumerate(self.input_string.visible_range()):
            line_for_render = line + '|' if self.input_string.lines_len() - 1 == i else line
            text_surface = self.font.render(line_for_render, True, TEXT_COLOR)
            self.screen.blit(text_surface, (self.input_box.x + 10, self.input_box.y + 10 + i * INPUT_BOX_HEIGHT))

    def draw_title(self):
        label_surface_first = self.font.render(TITLE_TEXT[0], True, TEXT_COLOR)
        self.screen.blit(label_surface_first, TITLE_TEXT_COORDINATES[0]) 

        label_surface_second = self.font.render(TITLE_TEXT[1], True, TEXT_COLOR)
        self.screen.blit(label_surface_second, TITLE_TEXT_COORDINATES[1]) 

    def draw_spam_check_result(self):
        label_surface_first = self.font.render(SPAM_CHECKER_TEXT[0][self.isSpam], True, TEXT_COLOR)
        self.screen.blit(label_surface_first, SPAM_CHECKER_TEXT_COORDINATES[0][self.isSpam]) 

        label_surface_second = self.font.render(SPAM_CHECKER_TEXT[1], True, TEXT_COLOR)
        self.screen.blit(label_surface_second, SPAM_CHECKER_TEXT_COORDINATES[1])
