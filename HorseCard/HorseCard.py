
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

    def cardHighlight(self, mousePos):
        self.rect = self.image.get_rect(center=(mousePos[0], mousePos[1]))


        

#Initializing Pygame and objects
pygame.init()
window = pygame.display.set_mode((500, 500))

testimage = pygame.image.load(".\\Images\\cardtemp.png").convert_alpha() #last bit improves performance

cardHeight = 400

card1 = TestCard(100, cardHeight)
card2 = TestCard(200, cardHeight)
card3 = TestCard(300, cardHeight)
card4 = TestCard(400, cardHeight)

spriteGroup1 = pygame.sprite.Group()

spriteGroup1.add(card1)
spriteGroup1.add(card2)
spriteGroup1.add(card3)
spriteGroup1.add(card4)


# Game loop
running = True
mousebuttondown = False
while running:
    key = pygame.key.get_pressed()
    mousePosition = pygame.mouse.get_pos()
    mouseRect = pygame.Rect(mousePosition[0], mousePosition[1], 5, 5)

    collideList = [card1.rect, card2.rect, card3.rect, card4.rect]
    collision = mouseRect.collideobjects(collideList)
    if collision:
        print("your mom")
        print(collision)

    if card1.rect.collidepoint(mousePosition):
        if card1.y > 300:
            card1.moveCard(-5)

    else:
        if card1.y < 400:
            card1.moveCard(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif key[pygame.K_SPACE]:
            card1.moveCard(10)
            print("pressed")
    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousebuttondown == True
            mousePos = event.pos
            card1.cardHighlight(mousePos)
            print(mousePos)
            print("clicked")

        elif event.type == pygame.MOUSEBUTTONUP:
            mousebuttondown = False

        elif event.type == pygame.MOUSEMOTION:
            if mousebuttondown:
                mousePos = event.pos
                print(mousePos)
                card1.cardHighlight(mousePos)
                print("clicked")

    window.fill((255, 255, 255))

  

    spriteGroup1.update()
    spriteGroup1.draw(window)

    pygame.display.flip()

pygame.quit()

