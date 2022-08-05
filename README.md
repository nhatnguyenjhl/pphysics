# PPhysics
 Python module for game's physics library.

## Installation
Run ```pip install pphysics```

For more details, see [Installation](https://nhatnguyenjhl.github.io/pphysics/installation.html).

## Update version 1.1.0
* Added image alias pygame.image

* Added Color alias pygame.Color

* Added cursors alias pygame.cursors

* Added event alias pygame.event

* Added font alias pygame.font

* Added joystick alias pygame.joystick

* Added key alias pygame.key

* Added mixer alias pygame.mixer

* Added mouse alias pygame.mouse

* Added muisc alias pygame.mixer.muisc

* Added PixelArray alias pygame.PixelArray

* Added Rect alias pygame.Rect

* Add scrap alias pygame.scrap

* Added sndarray alias pygame.sndarray

* Added sprite alias pygame.sprite

* Added Surface alias pygame.Surface

* Added surfarray alias pygame.surfarray

* Added time alias pygame.time

* Added transform alias pygame.transform

* Added __doc__ for get_objects_by_tag(), get_object_by_name(), get_objects() and remove_tag()

* Fixed error at get_object_by_name(): No variables named 'object'. Did you mean: 'objects'?

* Update Vector constructor 5: Vector() -> Vector with position (0, 0)

* Update GameObject constructor: Allow setting property in constructor.

* Update Object.__doc__

* Change returned value of Object.Force(), Object.del_tag(), Object.add_tag(), Object.set_name() from None to self.

* Change returned value of World.add() from None to self

* Update World.add() to add many object in once

* Support GameObject.position, GameObject.velocity to be assigned to a tuple, the returned type is automatically converted to Vector.

## DOCUMENTARY
See documentary pages: [PPhyics Documetation](https://nhatnguyenjhl.github.io/pphysics/).

## EXAMPLE
See [Simple game's source code](https://github.com/nhatnguyenjhl/pphysics/blob/main/tests/simple_game.py)
<br>
<br>
<br>



















