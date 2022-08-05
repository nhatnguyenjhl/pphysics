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

    screen = pp.Screen((400, 400))  # Create a screen.

    # Create a game objevt.
    obj = pp.GameObject((40, 40), position=(200, 200), velocity=(10, 7))
    # Draw a red rect on it.
    pp.draw.rect(obj.surface, (255, 0, 0), (0, 0, 40, 40))

    # Setting event.
    screen.set_event(pp.Event(
        on_press=on_press,
        on_release=on_release,
        on_collide=on_collide
    ))

    screen.add(obj)  # Add the object.

    portrait_wall = pp.GameObject(
        (10, 400), position=(-10, 0)).add_tag('portrait_wall')
    portrait_wall2 = pp.GameObject(
        (10, 400), position=(400, 0)).add_tag('portrait_wall')

    screen.add(portrait_wall, portrait_wall2)

    vertical_wall = pp.GameObject(
        (400, 10), position=(0, -10)).add_tag('vertical_wall')
    vertical_wall2 = pp.GameObject(
        (400, 10), position=(0, 400)).add_tag('vertical_wall')

    screen.add(vertical_wall, vertical_wall2)

    pp.start_game(screen)
