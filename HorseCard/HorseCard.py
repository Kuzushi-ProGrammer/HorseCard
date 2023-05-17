
import pygame





class Card():
    pass

class BoostCard(Card):
    pass

class StallCard(Card):
    pass

class SprintCard(Card):
    pass

class NullCard(Card):
    pass



class TestCard(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()

        self.x = posX
        self.y = posY

        self.image = testimage
        self.imageSize = self.image.get_rect().size
        self.image = pygame.transform.scale(self.image, (self.imageSize[0]/4, self.imageSize[1]/4))
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def moveCard(self, distance):
        self.y += distance
        self.rect = self.image.get_rect(center=(self.x, self.y))

        # if the center thing is giving too much trouble
        #self.rect = self.image.get_rect()
        #self.rect.x = x
        #self.rect.y = y

    def cardHighlight(self, mousePos):
        self.rect = self.image.get_rect(center=(mousePos[0], mousePos[1]))


        

#Initializing Pygame and objects
pygame.init()
window = pygame.display.set_mode((500, 500))

testimage = pygame.image.load(".\\Images\\cardtemp.png").convert_alpha() #last bit improves performance

cardHeight = 400

card1 = TestCard(150, cardHeight)
card2 = TestCard(200, cardHeight)
card3 = TestCard(250, cardHeight)
card4 = TestCard(300, cardHeight)

spriteGroup1 = pygame.sprite.Group()

spriteGroup1.add(card1)
spriteGroup1.add(card2)
spriteGroup1.add(card3)
spriteGroup1.add(card4)


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((255, 255, 255))

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        card1.moveCard(10)
        print("pressed")
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        mousePos = event.pos
        print(mousePos)
        card1.cardHighlight(mousePos)
        print("clicked")


    spriteGroup1.update()
    spriteGroup1.draw(window)

    pygame.display.flip()

pygame.quit()

