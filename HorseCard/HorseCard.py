
from turtle import window_height
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
        self.halfrect = self.image.get_rect(center=(self.x - 500, self.y))

    def moveCard(self, distance):
        self.y += distance
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def cardReplace(self, distance):
        pass


        

#Initializing Pygame and objects
pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

testimage = pygame.image.load(".\\Images\\cardtemp.png").convert_alpha() #last bit improves performance

cardHeight = 500

card1 = TestCard(100, cardHeight)
card2 = TestCard(200, cardHeight)
card3 = TestCard(300, cardHeight)
card4 = TestCard(400, cardHeight)

spriteGroup1 = pygame.sprite.Group()

spriteGroup1.add(card1)
spriteGroup1.add(card2)
spriteGroup1.add(card3)
spriteGroup1.add(card4)

cardSpeed = 15
defaultCardHeight = 500
selectedCardHeight = 400
submittedCardSpeed = 20
gameWindowHeight = 650
# Game loop
running = True
cardMoving = False
while running:
    key = pygame.key.get_pressed()
    mousePosition = pygame.mouse.get_pos()
    mouseRect = pygame.Rect(mousePosition[0], mousePosition[1], 1, 1)

    #---
    if not cardMoving:
        if card1.rect.collidepoint(mousePosition):
            cardHovered = 1
            if card1.y > selectedCardHeight:
                card1.moveCard(-cardSpeed)

            if card2.y < defaultCardHeight:
                card2.moveCard(cardSpeed)

            if card3.y < defaultCardHeight:
                card3.moveCard(cardSpeed)

            if card4.y < defaultCardHeight:
                card4.moveCard(cardSpeed)

        elif card2.rect.collidepoint(mousePosition):
            cardHovered = 2
            if card2.y > selectedCardHeight:
                card2.moveCard(-cardSpeed)

            if card1.y < defaultCardHeight:
                card1.moveCard(cardSpeed)

            if card3.y < defaultCardHeight:
                card3.moveCard(cardSpeed)

            if card4.y < defaultCardHeight:
                card4.moveCard(cardSpeed)

        elif card3.rect.collidepoint(mousePosition):
            cardHovered = 3
            if card3.y > selectedCardHeight:
                card3.moveCard(-cardSpeed)

            if card1.y < defaultCardHeight:
                card1.moveCard(cardSpeed)

            if card2.y < defaultCardHeight:
                card2.moveCard(cardSpeed)

            if card4.y < defaultCardHeight:
                card4.moveCard(cardSpeed)

        elif card4.rect.collidepoint(mousePosition):
            cardHovered = 4
            if card4.y > selectedCardHeight:
                card4.moveCard(-cardSpeed)

            if card1.y < defaultCardHeight:
                card1.moveCard(cardSpeed)

            if card2.y < defaultCardHeight:
                card2.moveCard(cardSpeed)

            if card3.y < defaultCardHeight:
                card3.moveCard(cardSpeed)
        else:
            cardHovered = 0
            if card1.y < defaultCardHeight:
                card1.moveCard(cardSpeed)

            if card2.y < defaultCardHeight:
                card2.moveCard(cardSpeed)

            if card3.y < defaultCardHeight:
                card3.moveCard(cardSpeed)

            if card4.y < defaultCardHeight:
                card4.moveCard(cardSpeed)

    if cardMoving:
        if cardHovered == 1:
            if card1.y < gameWindowHeight:
                card1.moveCard(submittedCardSpeed)
            cardHovered = 0
        cardMoving = False
                # change vars after card goes off screen
                


    '''
    Potential ideas
        -flip over card have it go through top of screen
        -need a conditional that determines when cards can be selected

    Issues
        -All cards get stuck after click, probably due to the fact that the variable isnt being unset anywhere
        -if statement,,

    '''


    #---

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif key[pygame.K_SPACE]:
            card1.moveCard(10)
            print("pressed")
    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = event.pos
            print(cardHovered)
            if cardHovered != 0: 
                cardMoving = True


        elif event.type == pygame.MOUSEBUTTONUP:
            mousebuttondown = False

    window.fill((255, 255, 255))

  

    spriteGroup1.update()
    spriteGroup1.draw(window)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

