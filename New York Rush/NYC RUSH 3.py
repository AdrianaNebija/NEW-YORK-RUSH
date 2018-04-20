#Gamers2303
#New York Rush
#Adriana,Briget,Rosario,Jozka
#In our game our main player is a FBI agent which#is dressed as a'
#businessman so he would be able to blend in.
#He needs to stay undercover and is assigned to reach a specific area
#in order to save the citizens from a national threat.'


from gamelib import*#import game library
game = Game(800,800,"New York Rush")

#title
title = Image("title.png",game)
title.y -= 288
#bk
bk = Image("Backup Cover.jpg",game)#Image Object
bk.resizeTo(800,800)
game.setBackground(bk)

#BK- Level 1
bk1 = Image("NYC.jpg",game)
bk1.resizeTo(800,600)

#tc
tc = Image("TC.png",game)
tc.resizeTo(50,40)
tc.moveTo(300,550)
tc.resizeBy(1000

#bm
bm = Image("BM1.gif",game)
bm.resizeTo(50,40)
bm.moveTo(50,513)
bm.resizeBy(330)

#elderly
elderly = Image("elderly.png",game)
elderly.resizeTo(30,40)
elderly.moveTo(470,513)
elderly.resizeBy(330)

#play
play = Image("play.png",game)
play.moveTo(550,20)
play.resizeBy(-40)
play.y += 200

jumping = False #Used to check to see if you are jumping
landed = False  #Used to check to see if you have landed on the "ground" (platform)
factor = 1  #Used for a slowing effect of the jumping

#Title Screen - first game loop
while not game.over:
    game.processInput()

    bk.draw()
    play.draw()
    title.draw()
    

    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over = True

    game.update(30)

game.over = False
#Level 1
while not game.over:
    game.processInput()

    bk1.draw()
    bm.draw()
    tc.draw()
    elderly.draw()

    if bm.collidedWith(tc):
        game.time -=1


#jumping
    if bm.y< 400:
        landed = False#not landed
        #if bm.collidedWith(platform,"rectangle"):
            #landed = True
    else:
        landed = True

    if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
        jumping = True

    if jumping:
        bm.y -=40*factor
        #Make the character go up.  Factor creates a slowing effect to the jump
        factor*=.95#fall slowly
        landed = False
        #Since you are jumping you are no longer staying on land
        if factor < .12:
            jumping = False
            #Stop jumping once the slowing effect finishes
            factor = 1

               
    if not landed:
        bm.y +=17#adjust as needed

    if keys.Pressed[K_RIGHT]:
        bm.x += 6
    if keys.Pressed[K_LEFT]:
        bm.x -= 6


    
    

    

    game.update(30)





    game.displayTime()
    
    game.update(60)
game.quit()

