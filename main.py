items = ['gh','fihi','fi']
ra = randint(0, 3)


def ChangeCharacterAni():
    pass
def MainCharacter(speed: number):
    global mySprite
    scene.set_background_color(2)
    mySprite = sprites.create(img("""
            . . . . f f f f . . . . . 
                    . . f f f f f f f f . . . 
                    . f f f f f f c f f f . . 
                    f f f f f f c c f f f c . 
                    f f f c f f f f f f f c . 
                    c c c f f f e e f f c c . 
                    f f f f f e e f f c c f . 
                    f f f b f e e f b f f f . 
                    . f 4 1 f 4 4 f 1 4 f . . 
                    . f e 4 4 4 4 4 4 e f . . 
                    . f f f e e e e f f f . . 
                    f e f b 7 7 7 7 b f e f . 
                    e 4 f 7 7 7 7 7 7 f 4 e . 
                    e e f 6 6 6 6 6 6 f e e . 
                    . . . f f f f f f . . . . 
                    . . . f f . . f f . . . .
        """),
        SpriteKind.player)
    controller.move_sprite(mySprite, 10, 10)
    mySprite.set_position(10, 50)
    if controller.dx() < 1:
        animation.run_image_animation(mySprite,
            [img("""
                    . . . . . . . . . . . . . 
                                . . . f f f f f f . . . . 
                                . f f f f f f f f f . . . 
                                . f f f f f f c f f f . . 
                                f f f f c f f f c f f f . 
                                f c f f c c f f f c c f f 
                                f c c f f f f e f f f f f 
                                f f f f f f f e e f f f . 
                                f f e e f b f e e f f f . 
                                f f e 4 e 1 f 4 4 f f . . 
                                . f f f e 4 4 4 4 f . . . 
                                . 4 4 4 e e e e f f . . . 
                                . e 4 4 e 7 7 7 7 f . . . 
                                . f e e f 6 6 6 6 f f . . 
                                . f f f f f f f f f f . . 
                                . . f f . . . f f f . . .
                """),
                img("""
                    . . . . . . . . . . . . . 
                                . . . f f f f f f . . . . 
                                . f f f f f f f f f . . . 
                                . f f f f f f c f f f . . 
                                f f f f c f f f c f f f . 
                                f c f f c c f f f c c f f 
                                f c c f f f f e f f f f f 
                                f f f f f f f e e f f f . 
                                f f e e f b f e e f f . . 
                                . f e 4 e 1 f 4 4 f f . . 
                                . f f f e e 4 4 4 f . . . 
                                . . f e 4 4 e e f f . . . 
                                . . f e 4 4 e 7 7 f . . . 
                                . f f f e e f 6 6 f f . . 
                                . f f f f f f f f f f . . 
                                . . f f . . . f f f . . .
                """),
                img("""
                    . . . f f f f f . . . . . 
                                . f f f f f f f f f . . . 
                                . f f f f f f c f f f . . 
                                f f f f c f f f c f f . . 
                                f c f f c c f f f c c f f 
                                f c c f f f f e f f f f f 
                                f f f f f f f e e f f f . 
                                f f e e f b f e e f f . . 
                                . f e 4 e 1 f 4 4 f . . . 
                                . f f f e 4 4 4 4 f . . . 
                                . . f e e e e e f f . . . 
                                . . e 4 4 e 7 7 7 f . . . 
                                . . e 4 4 e 7 7 7 f . . . 
                                . . f e e f 6 6 6 f . . . 
                                . . . f f f f f f . . . . 
                                . . . . f f f . . . . . .
                """)],
            500,
            True)
    elif controller.left.is_pressed():
        animation.run_image_animation(mySprite,
            [img("""
                    . . . . . f f f f f . . . 
                                . . . f f f f f f f f f . 
                                . . f f f c f f f f f f . 
                                . . f f c f f f c f f f f 
                                f f c c f f f c c f f c f 
                                f f f f f e f f f f c c f 
                                . f f f e e f f f f f f f 
                                . . f f e e f b f e e f f 
                                . . . f 4 4 f 1 e 4 e f . 
                                . . . f 4 4 4 4 e f f f . 
                                . . . f f e e e e e f . . 
                                . . . f 7 7 7 e 4 4 e . . 
                                . . . f 7 7 7 e 4 4 e . . 
                                . . . f 6 6 6 f e e f . . 
                                . . . . f f f f f f . . . 
                                . . . . . . f f f . . . .
                """),
                img("""
                    . . . . . . . . . . . . . 
                                . . . . f f f f f f . . . 
                                . . . f f f f f f f f f . 
                                . . f f f c f f f f f f . 
                                . f f f c f f f c f f f f 
                                f f c c f f f c c f f c f 
                                f f f f f e f f f f c c f 
                                . f f f e e f f f f f f f 
                                . . f f e e f b f e e f f 
                                . . f f 4 4 f 1 e 4 e f . 
                                . . . f 4 4 4 e e f f f . 
                                . . . f f e e 4 4 e f . . 
                                . . . f 7 7 e 4 4 e f . . 
                                . . f f 6 6 f e e f f f . 
                                . . f f f f f f f f f f . 
                                . . . f f f . . . f f . .
                """),
                img("""
                    . . . . . . . . . . . . . 
                                . . . . f f f f f f . . . 
                                . . . f f f f f f f f f . 
                                . . f f f c f f f f f f . 
                                . f f f c f f f c f f f f 
                                f f c c f f f c c f f c f 
                                f f f f f e f f f f c c f 
                                . f f f e e f f f f f f f 
                                . f f f e e f b f e e f f 
                                . . f f 4 4 f 1 e 4 e f f 
                                . . . f 4 4 4 4 e f f f . 
                                . . . f f e e e e 4 4 4 . 
                                . . . f 7 7 7 7 e 4 4 e . 
                                . . f f 6 6 6 6 f e e f . 
                                . . f f f f f f f f f f . 
                                . . . f f f . . . f f . .
                """)],
            500,
            True)
    if controller.up.is_pressed():
        animation.run_image_animation(mySprite,
            [img("""
                    . . . . . . f f f f 4 4 f . . . 
                                . . . . f f b f 5 4 5 5 4 f . . 
                                . . . f b 3 3 e 4 5 5 5 5 f . . 
                                . . f b 3 3 3 3 e 4 4 4 e f . . 
                                . . f 3 3 3 3 3 3 3 3 3 3 f . . 
                                . . f 3 3 3 3 e b 3 e e 3 3 f . 
                                . . f 3 3 3 3 f f e e e 3 3 f . 
                                . . f b b b b f b f e e e 3 f . 
                                . . f b b b b e 1 f 4 4 e f . . 
                                . f f b b b b f 4 4 4 4 f . . . 
                                . f b b b b f f f e e e f . . . 
                                . . f b b f 4 4 e d d d f . . . 
                                . . . f f e 4 4 e d d d f . . . 
                                . . . . f b e e b d b d b f . . 
                                . . . . f f d 1 d 1 d 1 f f . . 
                                . . . . . . f f b b f f . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . f f f f 4 4 f . . . 
                                . . . . f f b f 5 4 5 5 4 f . . 
                                . . . f b 3 3 e 4 5 5 5 5 f . . 
                                . . f b 3 3 3 3 e 4 4 4 e f . . 
                                . . f 3 3 3 3 3 3 3 3 3 3 3 f . 
                                . . f 3 3 3 3 e b 3 e e 3 3 f . 
                                . . f 3 3 3 3 f f e e e 3 3 f . 
                                . f f b b b b f b f e e e f . . 
                                . f b b b b b e 1 f 4 4 e . . . 
                                . f b b b b b f 4 4 4 4 f . . . 
                                . . f b b b 4 4 e d d d f . . . 
                                . . . f f f 4 4 e d d d f . . . 
                                . . . f b b e e b b d d d f . . 
                                . . . . f b d d 1 d 1 d b f . . 
                                . . . . . f f f b b f f f . . .
                """)],
            500,
            True)
    elif controller.down.is_pressed():
        animation.run_image_animation(mySprite,
            [img("""
                    . . . . f f f f . . . . . 
                                . . f f f f f f f f . . . 
                                . f f f f f f c f f f . . 
                                f f f f f f c c f f f c . 
                                f f f c f f f f f f f c . 
                                c c c f f f e e f f c c . 
                                f f f f f e e f f c c f . 
                                f f f b f e e f b f f f . 
                                . f 4 1 f 4 4 f 1 4 f . . 
                                . f e 4 4 4 4 4 4 e f . . 
                                . f f f e e e e f f f . . 
                                f e f b 7 7 7 7 b f e f . 
                                e 4 f 7 7 7 7 7 7 f 4 e . 
                                e e f 6 6 6 6 6 6 f e e . 
                                . . . f f f f f f . . . . 
                                . . . f f . . f f . . . .
                """),
                img("""
                    . . . . . . . . . . . . . 
                                . . . . . f f f f . . . . 
                                . . . f f f f f f f f . . 
                                . . f f f f f f c f f f . 
                                f f f f f f f c c f f f c 
                                f f f f c f f f f f f f c 
                                . c c c f f f e e f f c c 
                                . f f f f f e e f f c c f 
                                . f f f b f e e f b f f f 
                                . f f 4 1 f 4 4 f 1 4 f f 
                                . . f e 4 4 4 4 4 e e f e 
                                . f e f b 7 7 7 e 4 4 4 e 
                                . e 4 f 7 7 7 7 e 4 4 e . 
                                . . . f 6 6 6 6 6 e e . . 
                                . . . f f f f f f f . . . 
                                . . . f f f . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . 
                                . . . . f f f f . . . . . 
                                . . f f f f f f f f . . . 
                                . f f f c f f f f f f . . 
                                c f f f c c f f f f f f f 
                                c f f f f f f f c f f f f 
                                c c f f e e f f f c c c . 
                                f c c f f e e f f f f f . 
                                f f f b f e e f b f f f . 
                                f f 4 1 f 4 4 f 1 4 f f . 
                                e f e e 4 4 4 4 4 e f . . 
                                e 4 4 4 e 7 7 7 b f e f . 
                                . e 4 4 e 7 7 7 7 f 4 e . 
                                . . e e 6 6 6 6 6 f . . . 
                                . . . f f f f f f f . . . 
                                . . . . . . . f f f . . .
                """)],
            500,
            True)
    else:
        animation.run_image_animation(mySprite,
            [img("""
                . . . . f f f f . . . . . 
                            . . f f f f f f f f . . . 
                            . f f f f f f c f f f . . 
                            f f f f f f c c f f f c . 
                            f f f c f f f f f f f c . 
                            c c c f f f e e f f c c . 
                            f f f f f e e f f c c f . 
                            f f f b f e e f b f f f . 
                            . f 4 1 f 4 4 f 1 4 f . . 
                            . f e 4 4 4 4 4 4 e f . . 
                            . f f f e e e e f f f . . 
                            f e f b 7 7 7 7 b f e f . 
                            e 4 f 7 7 7 7 7 7 f 4 e . 
                            e e f 6 6 6 6 6 6 f e e . 
                            . . . f f f f f f . . . . 
                            . . . f f . . f f . . . .
            """)],
            500,
            True)
        console.log_value("x", controller.dx())
    ChangeCharacterAni()
mySprite: Sprite = None
aniSpeed = 100
MainCharacter(aniSpeed)