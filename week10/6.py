# The first half is just boiler-plate stuff...

import pygame

class SceneBase:
    def __init__(self):
        self.next = self
    
    def ProcessInput(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene
    
    def Terminate(self):
        self.SwitchToScene(None)

def run_game(width, height, fps, starting_scene):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    active_scene = starting_scene

    while active_scene != None:
        pressed_keys = pygame.key.get_pressed()
        
        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True
            
            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)
        
        active_scene.ProcessInput(filtered_events, pressed_keys)
        active_scene.Update()
        active_scene.Render(screen)
        
        active_scene = active_scene.next
        
        pygame.display.flip()
        clock.tick(fps)

# The rest is code where you implement your game using the Scenes model

class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.SwitchToScene(GameScene())
    
    def Update(self):
        pass
    
    def Render(self, screen):
        # For the sake of brevity, the title scene is a blank red screen
        screen.fill((255, 0, 0))

class GameOverScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.font = pygame.font.SysFont("comicsansms", 72)
        self.text = self.font.render("Game over!", True, (0, 128, 0))
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.Terminate()
    
    def Update(self):
        pass
    
    def Render(self, screen):
        screen.fill((255, 255, 255))
        screen.blit(self.text, (320 - self.text.get_width() // 2, 240 - self.text.get_height() // 2))

class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.x = 30
        self.y = 30
        self.color = (0, 128, 255)

    def ProcessInput(self, events, pressed_keys):
        self.pressed = pressed_keys   
        self.events = events

    def Update(self):
        if self.pressed[pygame.K_UP]: self.y -= 3
        if self.pressed[pygame.K_DOWN]: self.y += 3
        if self.pressed[pygame.K_LEFT]: self.x -= 3
        if self.pressed[pygame.K_RIGHT]: self.x += 3

        if(self.x < 0 or self.y < 0):
            self.SwitchToScene(GameOverScene())
    
    def Render(self, screen):
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, 60, 60))

run_game(400, 300, 60, TitleScene())