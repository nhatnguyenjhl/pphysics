import sys

sys.path.append('../src/')


def on_press(key):
    pass


def on_release(key):
    pass


def on_collide(obj1, obj2):
    if 'portrait_wall' in obj1.tags:
        obj2.velocity = pp.Vector(-obj2.velocity.x, obj2.velocity.y)
    elif 'portrait_wall' in obj2.tags:
        obj1.velocity = pp.Vector(-obj1.velocity.x, obj2.velocity.y)
    elif 'vertical_wall' in obj1.tags:
        obj2.velocity = pp.Vector(obj2.velocity.x, -obj2.velocity.y)
    elif 'vertical_wall' in obj2.tags:
        obj1.velocity = pp.Vector(obj1.velocity.x, -obj1.velocity.y)


if __name__ == '__main__':
    import pphysics as pp

    screen = pp.Screen((400, 400))

    obj = pp.GameObject((40, 40))
    obj.position = pp.Vector((200, 200))
    obj.velocity = pp.Vector((10, 7))
    pp.draw.rect(obj.surface, (255, 0, 0), (0, 0, 40, 40))

    screen.set_event(pp.Event(
        on_press=on_press,
        on_release=on_release,
        on_collide=on_collide
    ))
    screen.add(obj)

    portrait_wall = pp.GameObject((10, 400))
    portrait_wall2 = pp.GameObject((10, 400))
    portrait_wall.position = pp.Vector(-10, 0)
    portrait_wall2.position = pp.Vector(400, 0)
    portrait_wall.add_tag('portrait_wall')
    portrait_wall2.add_tag('portrait_wall')

    screen.add(portrait_wall)
    screen.add(portrait_wall2)

    vertical_wall = pp.GameObject((400, 10))
    vertical_wall2 = pp.GameObject((400, 10))
    vertical_wall.position = pp.Vector((0, -10))
    vertical_wall2.position = pp.Vector((0, 400))
    vertical_wall.add_tag('vertical_wall')
    vertical_wall2.add_tag('vertical_wall')

    screen.add(vertical_wall)
    screen.add(vertical_wall2)

    pp.start_game(screen)
