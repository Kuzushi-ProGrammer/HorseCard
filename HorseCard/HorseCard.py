
import pygame
import time
import random





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



class Card(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()

        self.x = posX
        self.y = posY

        self.image = baseImage
        self.imageSize = self.image.get_rect().size
        self.image = pygame.transform.scale(self.image, (self.imageSize[0]/4, self.imageSize[1]/4))
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.halfrect = self.image.get_rect(center=(self.x - 500, self.y))

    def moveCard(self, distance):
        self.y += distance
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def cardReplace(self, distance):
        global cardMoving
        if self.y < gameWindowHeight:
            self.y += distance
            self.rect = self.image.get_rect(center=(self.x, self.y))

        else:
            cardMoving = False
            # change vars after card goes off screen
'''
-------------------------------------------
How could I implement statistics?
-------------------------------------------
 -self.stats = [1, 0, 3] (list based)

 -self.statsDict = {
                    boost: 1,
                    stall: 0,
                    sprint: 3
                   } (dict based)

- self.boost = 1   -> self.boost = deckCard.boost (?)
  self.stall = 0
  self.sprint = 3
  (var based)

  (Null cards are just normal cards with all variables set to 0)

  Problems:
      - Selecting a card from a deck may not work? I'd have to implement extra framework
      - Purely randomly generated cards are no fun
      - Store cards in text file for easy modification?
          - Would need to format it in a way that would accept all data such as:
              - Card Type (Boost, Stall, Sprint, Null)
              - Card Statistics
              - Image Properties and Location


      - Dictionary allows for easiest overwriting of stats and should be pretty flexible in an external text file
      - Load images onto the card object and keep them linked up so the image doesnt stay in place when card goes away
      - When card goes off screen, only change the variables on the object itself, dont change the object(?)
      - Have a global tracker to keep track of your position and enemies position in the race
          - Need to make simple AI (probably just algorithmic like always attacks, only goes left to right, etc.)
      - Turn based or real time?

  Game loop
      - Opens up the game into a menu
          -Settings allows you to choose a deck from the deck folder (not sure if there will be a card limit)
      - Places you randomly along one of 4-6 tracks (idk how many yet)
      - Countdown (3, 2, 1, Go!)



'''        

#Initializing Pygame and objects
pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

baseImage = pygame.image.load(".\\Images\\cardtemp.png").convert_alpha() #last bit improves performance

cardHeight = 500

card1 = Card(100, cardHeight)
card2 = Card(200, cardHeight)
card3 = Card(300, cardHeight)
card4 = Card(400, cardHeight)

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

    #---
    # Do not know how to make this more efficient with less if statments
    if not cardMoving:
        if card1.rect.collidepoint(mousePosition):
            cardHovered = card1
            if card1.y > selectedCardHeight:
                card1.moveCard(-cardSpeed)

            if card2.y < defaultCardHeight:
                card2.moveCard(cardSpeed)

            if card3.y < defaultCardHeight:
                card3.moveCard(cardSpeed)

            if card4.y < defaultCardHeight:
                card4.moveCard(cardSpeed)

        elif card2.rect.collidepoint(mousePosition):
            cardHovered = card2
            if card2.y > selectedCardHeight:
                card2.moveCard(-cardSpeed)

            if card1.y < defaultCardHeight:
                card1.moveCard(cardSpeed)

            if card3.y < defaultCardHeight:
                card3.moveCard(cardSpeed)

            if card4.y < defaultCardHeight:
                card4.moveCard(cardSpeed)

        elif card3.rect.collidepoint(mousePosition):
            cardHovered = card3
            if card3.y > selectedCardHeight:
                card3.moveCard(-cardSpeed)

            if card1.y < defaultCardHeight:
                card1.moveCard(cardSpeed)

            if card2.y < defaultCardHeight:
                card2.moveCard(cardSpeed)

            if card4.y < defaultCardHeight:
                card4.moveCard(cardSpeed)

        elif card4.rect.collidepoint(mousePosition):
            cardHovered = card4
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

    #---

    if cardMoving:
        cardHovered.cardReplace(20)
        pass

    #---

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = event.pos
            if cardHovered != 0: 
                cardMoving = True

    window.fill((255, 255, 255))

    spriteGroup1.update()
    spriteGroup1.draw(window)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

