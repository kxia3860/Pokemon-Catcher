from gamelib import *

game = Game(800, 600, "Pokemon Catcher", 60)
bk = Image("images\\pokemonbackground.png", game)
game.setBackground(bk)
bk.resizeTo(800, 600)

rocket = Image("images\\teamrocket.png", game)
rocket.moveTo(400, 50)

Ash = Animation("images\\ash.png",6,game,128/2, 195/3, 5)
Ash.resizeBy(70)
Ash.moveTo(100, 450)

Lightning = Animation("images\\boltlight.png",4,game, 1000/2, 750/2, 10)
Lightning.resizeBy(30)
Lightning.moveTo(450, 210)

Grass = Image("images\\pokemongrass.png", game)
Grass.resizeBy(50)
Grass.moveTo(300, 475)

Tstrike = Sound("sound\\thunder.wav", 1)



eevee = []
for num in range(15):
    eevee.append(  Image("images\\eevee.png", game)  )
for e in eevee:
    x = randint(100, 700)
    y = -randint(100, 5000)
    s = randint(1,2)
    e.moveTo(x, y)
    e.setSpeed(s, 180)
    e.resizeBy(-80)
    

bulbasaur = []
for num in range(15):
    bulbasaur.append(  Image("images\\bulbasaur.png", game)  )
for b in bulbasaur:
    x = randint(100, 700)
    y = -randint(100, 5000)
    s = randint(1,2)
    b.moveTo(x, y)
    b.setSpeed(s, 180)
    b.resizeBy(-85)

charmander = []
for num in range(15):
    charmander.append(  Image("images\\charmander.png", game)  )
for c in charmander:
    x = randint(100,700)
    y = -randint(100,5000)
    s = randint(1,2)
    c.moveTo(x,y)
    c.setSpeed(s,180)
    c.resizeBy(-75)

title = Image("images\\PokemonLogo.png", game)
bk.draw()
title.draw()
game.drawText("PRESS [SPACE] TO PLAY", 320, 400)
game.update(1)
game.wait(K_SPACE)

gameover = Image("images\\gameoverlogo.png", game)
Lightning.visible = False
while not game.over:
    game.processInput()
    game.scrollBackground("left", 2)
  
    
    bk.draw()
    Grass.draw()
    Ash.move()
    rocket.draw()
    Lightning.draw(False)
    for b in bulbasaur:
        b.move()
        if b.collidedWith(Ash):
            b.visible = False
            game.score += 10
        if b.collidedWith(Grass, "rectangle"):
            b.visible = False
            Lightning.visible = True
            Lightning.moveTo(Ash.x + 200, Ash.y - 200)
            Ash.health -= 5
            Tstrike.play(1000)
    for e in eevee:
        e.move()
        if e.collidedWith(Ash):
            e.visible = False
            game.score += 10
        if e.collidedWith(Grass, "rectangle"):
            e.visible = False
            Lightning.visible = True
            Lightning.moveTo(Ash.x + 200, Ash.y - 200)
            Ash.health -= 5
            Tstrike.play(1000)
    for c in charmander:
        c.move()
        if c.collidedWith(Ash):
            c.visible = False
            game.score += 10
        if c.collidedWith(Grass, "rectangle"):
            c.visible = False
            Lightning.visible = True
            Lightning.moveTo(Ash.x + 200, Ash.y - 200)
            Ash.health -= 5
            Tstrike.play(1000)

    
    if keys.Pressed[K_RIGHT]:
        Ash.x += 2
    if keys.Pressed[K_LEFT]:
        Ash.x -= 2
    if Ash.health < 1 or game.score > 99:
        game.over = True 
                            
        

    game.drawText("Health: " + str(Ash.health), 85, 10)
    game.displayScore(5, 10)
    game.update(60)


gameover.draw()
game.drawText("PRESS [SPACE] TO EXIT", 450, 500)
game.update(1)
game.wait(K_SPACE)
game.quit()
    
    
