import abc
from math import pi, sqrt, tan, fabs, inf
from turtle import pos, position
import pygame
from pygame.locals import *
import sys
from datetime import datetime


class Vector:
    '''Constructor:
            Constructor 1:
                Vector(comlex_str: str) -> Vector by complex type from input.

            Constructor 2:
                Vector(position: Iterable) -> Vector with two element of iterable.
                    Caution:   The param 'position' can be another vector.

            Constructor 3:
                Vector(start_point, end_point) -> Vector by linking two points.
                    Caution:   Two points must be typed Vector.

            Constructor 4:
                Vector(x, y) -> Vector with position is x, y.
    '''

    def __init__(self, *args) -> None:
        self.x, self.y = 0, 0
        if type(args[0]) is str:
            # Constructor 1
            Vector.get_from_complex(args[0])
        else:
            try:
                # Constructor 2
                self.x, self.y = tuple(args[0])
            except TypeError:
                if type(args[0]) is Vector and type(args[1]) is Vector:
                    # Constructor 3
                    self.x, self.y = args[1] - args[0]
                elif type(args[0]) is not Vector and type(args[1]) is not Vector:
                    # Constructor 4
                    self.x, self.y = args[0], args[1]

    @ property
    def length(self):
        '''Return length of vector.'''
        return Vector.length_of(self)

    @ property
    def position(self):
        '''Return the tuple show position of vector.'''
        return self.x, self.y

    @ position.setter
    def position(self, value):
        '''Can set the position.'''
        self.x, self.y = value

    def __repr__(self):
        '''Call when user call vector object in interactive mode.'''
        return f'Vector at {self.position}'

    def __str__(self):
        '''Call when user print vector object or convert to string'''
        return str(self.position)

    def __getitem__(self, key):
        '''Can access to the elements of vector like a tuple.'''
        return self.position[key]

    def __setitem__(self, key, value):
        '''Can change the elements of vector like a tuple.'''
        self.position[key] = value

    def __add__(self, other):
        '''Can use addition between two vectors.'''
        if type(other) is Vector:
            return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        '''Can use multiplication between two vector or a vector and a number.'''
        if type(other) is Vector:
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    def __rmul__(self, other):
        '''Supported when the number (other) is front of vector.'''
        if type(other) is not Vector:
            return self * other

    def __truediv__(self, other):
        '''Can divide the vector for a number.'''
        # Use __rmul__ to detect if other is not Vector.
        return (1/other) * self

    def __pow__(self, other):
        '''Can pow the vector with a number.'''
        __vector = Vector(self.x, self.y)
        for _ in range(other - 1):
            __vector *= self
        return __vector

    def __neg__(self):
        '''The negative of vector.'''
        return self * (-1)

    def __pos__(self):
        '''The positive of vector.'''
        return self

    def __sub__(self, other):
        '''Can use subtraction between two vector.'''
        return self + (-other)

    def __abs__(self):
        '''Return the length of vector when call abs.'''
        return self.length

    @ staticmethod
    def length_of(vector) -> float:
        '''
            Return the length of vector follow the formula sqrt(x**2 + y**2)
        '''
        return sqrt(vector.x**2 + vector.y**2)

    @ staticmethod
    def get_from_complex(complex_str: str):
        '''
            :param str complex_str:
                :'c' in complex_str: an angle type complex, ex: 10cpi
                :'i' in complex_str: a normal complex, ex: 3i+4
                Caution: Use format string if you want to input a variable.
        '''
        __complex_str = complex_str.replace(' ', '')
        if 'i' in __complex_str:
            index = __complex_str.index('i')
            __x = eval(__complex_str[:index])
            __y = eval('0' + __complex_str[(index + 1):])
        elif 'c' in __complex_str:
            index = __complex_str.index('c')
            __x = eval(__complex_str[:index])
            __y = __x * tan(eval(__complex_str[(index + 1):]))
        else:
            __x, __y = 0, 0
        return Vector(__x, __y)

    def __solve_divariable_equation(self, a1, a2, b1, b2, c1, c2):
        '''
            a1 * x + b1 * y = c1
            a2 * x + b2 * y = c2
        '''
        # Cal y
        __y = c1 * a2 / a1 - c2
        __x = b1 * a2 / a1 - b2
        __y = __y / __x

        # Cal x
        __x = (c1 - b1 * __y)/a1
        return __x, __y

    def analyze(self, i_unit_vector, j_unit_vector):
        '''Return two number m, n: self = m * i_unit_vector + n * j_unit_vector. '''
        return self.__solve_divariable_equation(*self.position, *i_unit_vector.position, *j_unit_vector.position)

    def stem_parallelogram_rule(self, i_same_direction_vector, j_same_direction_vector):
        '''Return two vector has the same direction with i, j and the sum is equal to self.'''
        return tuple(unit_vector * k for unit_vector, k in zip((i_same_direction_vector, j_same_direction_vector), self.analyze(i_same_direction_vector, j_same_direction_vector)))


up = Vector(0, -1)
left = Vector(-1, 0)
down = Vector(0, 1)
right = Vector(1, 0)
zero = Vector(0, 0)
unit = Vector(1, 1)
objects = []
tags = ['_object']


class Object(abc.ABC):
    '''
        Constructor:
            Object() -> Object
        The unit caution: 1 square metres = 1 pixel (1m2 = 1px)
        Properties:
            surface: The showing of object.
            size: The size, unit metres (m) for each element.
            mass: The mass, unit kilogram (kg).
            force: The force, unit Newton (N), showing under type Vector.
            velocity: The velocity, unit metres/second (m/s), showing under type Vector.
            acceleration: The acceleration, unit metres/second**2 (m/s2), showing under type Vector.
            position: The position of object, showing under type Vector.
            name: The name of object, can't be same at other object.
            tag: The tag of object.
    '''

    @ property
    def surface(self):
        '''The showing of object.'''
        return self._surface

    @ property
    def size(self):
        '''Unit: Metres (m) in each element.'''
        return self._size

    @ property
    def mass(self):
        '''Unit: Kilogram (kg).'''
        return self._mass

    @ property
    def force(self):
        '''Unit: Newton (N).
            Show by a vector.
        '''
        return self._force

    @ property
    def velocity(self):
        '''Unit: Metres/second (m/s).'''
        return self._velocity

    @ property
    def acceleration(self):
        '''Unit: Metres/second**2 (m/s2)'''
        if self._mass == 0:
            self._acceleration = self._force * 1e10
        elif self._mass == Object.INFINITY_MASS:
            self._acceleration = 0
        else:
            self._acceleration = self._force / self._mass
        return self._acceleration

    @ property
    def position(self):
        '''Return the position of object under type vector.'''
        return self._position

    @ property
    def name(self):
        return self._name

    @ property
    def friction(self):
        return self._friction

    @ property
    def tags(self):
        return self._tags

    @ staticmethod
    @ property
    def INFINITY_MASS():
        return inf

    @ property
    def has_collision(self):
        return self._has_collision

    # Fixing problem: Long algorithm.
    #
    # @ has_collision.setter
    # def has_collision(self, value):
    #    self._has_collision = value
    #
    #

    _surface = None  # The showing on screen of object
    _size = tuple()
    _mass = 0
    _force = zero
    _velocity = zero
    _acceleration = zero
    _position = zero
    _friction = None
    _has_collision = False
    running = False  # The status of object

    def __init__(self) -> None:
        # Set the status to True when calling constructor.
        self._tags = list(['_object'])
        self._name = 'Object created at ' + datetime.now().strftime("%y/%m/%d %H:%M:%S")
        self.running = True
        objects.append(self)

    def set_name(self, name):
        '''Change the name of object, use self.name to get the name.'''
        self._name = name

    def add_tag(self, tag):
        '''Add the tag of object, use self.tag to get the tag.'''
        if tag not in tags:
            tags.append(tag)
        if tag not in self._tags:
            self._tags.append(tag)

    def del_tag(self, tag):
        '''Delete a tag on object.'''
        if tag in self._tags:
            self._tags.remove(tag)

    def get_force(self) -> Vector:
        '''Return value of force.'''
        return self._force

    @ abc.abstractmethod
    def Force(self, force: Vector):
        '''
            Create a new force on the object, and add to old force following the vector addition rules.
            For deleting all force in object, use: self.Force(-self.force).
        '''
        self._force += force

    @ staticmethod
    def Force_to(obj, force: Vector):
        obj.Force(force)

    @ abc.abstractmethod
    def force_to(self, obj, force: Vector):
        '''Create a force from self to other and self is also got a reversed force.'''
        obj.Force(force)
        Object.Force_to(self, -force)

    @ abc.abstractmethod
    def update(self, time_load=0.06):
        '''
            Update object after a time which's given by time_load key.
        '''
        self._update()
        self._position += self.velocity * time_load
        self._velocity += self.acceleration * time_load

    def add_friction(self, friction):
        '''Add a friction.'''
        if type(friction) is not NoneType and friction is not None:
            if self._friction is not None:
                self._friction += friction
            else:
                self._friction = friction
            self.Force(-friction._coefficient * self.force)

    def _update(self):
        '''_update is always called in super().update(time_load)'''
        if self.has_collision:
            __dict_objects = self.check_collision(objects)
            for name in __dict_objects:
                obj = get_object_by_name(name)
                if __dict_objects[name] and obj.has_collision:
                    pass

    def check_collision(self, *object_list):
        __list = list(object_list)
        try:
            __list.remove(self)
        except ValueError:
            pass

        for i in range(len(__list)):
            obj = __list[i]
            if -self.size[0] <= (self.position.x - obj.position.x) <= obj.size[0] and -self.size[1] <= (self.position.y - obj.position.y) <= obj.size[1]:
                yield __list[i]


class Event:
    '''
        Constructor:
            Event(on_press, on_release) -> Event.
        When creating a child extend it, call self.load() in __init__ to set two overriding press() and release() to on_press and on_release event.
    '''

    @ abc.abstractclassmethod
    def press(self, key):
        '''Override this method and call load in __init__ of child to set the on_press event to it.'''
        pass

    @ abc.abstractclassmethod
    def release(self, key):
        '''Override this method and call load in __init__ of child to set the on_release event to it.'''
        pass

    @ abc.abstractclassmethod
    def collide(self, objects_list):
        '''Override this method and call load in __init__ of child to set the on_collide event to it.'''
        pass

    def __init__(self, on_press, on_release, on_collide=None):
        self.on_press = on_press
        self.on_release = on_release
        self.on_collide = on_collide

    def load(self):
        '''Call when creating a child to set two overriding method press() and release() at on_press and on_release event.'''
        self.on_press = self.press
        self.on_release = self.release
        self.on_collide = self.collide


class World(Object):
    '''
        Constructor:
            World(gravity) -> World with gravity (default is (0, 10))
        Properties:
            objects: Return list of objects added in self.
            gravity: Return value of gravity of World, can set it.
    '''

    @ property
    def objects(self):
        '''Return list of objects added in self.'''
        return self._objects

    @ property
    def gravity(self):
        '''Return the value of gravity.'''
        return self._gravity

    @ gravity.setter
    def gravity(self, value):
        '''While setting gravity, all objects will be got new gravity.'''
        for i in range(len(self)):
            self[i].Force(self[i].mass * (value - self._gravity))
        self._gravity = value

    @ property
    def friction(self):
        '''Return friction of world.'''
        return self._friction

    _gravity = zero
    _objects = []

    def __init__(self, gravity=Vector(0, 10)):
        self._gravity = gravity
        super().__init__()
        self._tags.append('_world')
        self._mass = Object.INFINITY_MASS

    def Force(self, force: Vector):
        for i in range(len(self)):
            self[i].Force(force)
        super().Force(force)

    def update(self, time_load=0.06):
        for i in range(len(self)):
            self[i].update(time_load)

    @ abc.abstractclassmethod
    def force_to(self, obj, force: Vector):
        return super().force_to(obj, force)

    @ staticmethod
    def _get_collision_list(world):
        __list_collision = set()
        for obj in world:
            __temp = obj.check_collision(*world._objects)
            for _obj in world:
                if _obj in __temp:
                    __result = [obj, _obj]
                    __list_collision.add(tuple(__result))
                    __list_collision.add(tuple([_obj, obj]))
                    __list_collision.remove(tuple([_obj, obj]))
        return list(__list_collision)

    @ abc.abstractclassmethod
    def add(self, obj: Object) -> None:
        '''
            Add new child object to this object.
        '''
        __obj = obj
        __obj.Force(__obj.mass * self._gravity + self._force)
        # Fixing problem: The Force can't release self.
        #
        # self.Force(__obj.mass * (-self._gravity) - self._force)
        #
        #
        obj.add_friction(self._friction)
        self._objects.append(__obj)

    def add_friction(self, friction):
        if friction is not None and type(friction) is not None:
            for i in range(len(self)):
                self[i].add_friction(friction)
            return super().add_friction(friction)
        else:
            return None

    def __getitem__(self, key):
        '''ALlows accessing world's objects like a list of objects.'''
        return self._objects[key]

    def __len__(self):
        '''Return the len of objects list.'''
        return len(self._objects)

    def __setitem__(self, key, value):
        '''Allows setting the objects in world.'''
        self._objects[key] = value


class Screen(World):
    '''
        Constructor:
            Screen(size, title) -> Screen.
        Constant:
            FULL_SCREEN: size = FULL_SCREEN to set screen to expand computer's screen.
    '''

    @ Object.size.setter
    def size(self, value):
        '''Size of screen.'''
        self._size = value
        self._surface = self._display.set_mode(self._size)

    @ staticmethod
    @ property
    def FULL_SCREEN():
        '''Constant showing the full screen state.'''
        return 256

    _world = None

    def __init__(self, size, title='Physics Game') -> None:
        self._display = pygame.display
        self._clock = pygame.time.Clock()
        self._display.init()
        if size is Screen.FULL_SCREEN:
            self._surface = self._display.set_mode()
            self._size = self._surface.get_size()
        else:
            self.size = size
        self._display.set_caption(title)
        super().__init__(gravity=zero)
        self._tags.append('_screen')

    def Force(self, force: Vector):
        super().Force(force)

    def add(self, obj: Object) -> None:
        return super().add(obj)

    def force_to(self, obj, force: Vector):
        return super().force_to(obj, force)

    def set_event(self, event: Event):
        '''Set the event.'''
        self._event = event

    def set_world(self, world: World):
        '''Set the world, only a world of screen.
            If you wanna add two world, use self.add().
        '''
        self._world = world

    def __on_event(self):
        '''
            Adding event to update.
        '''
        for __event in pygame.event.get():
            if __event.type == KEYDOWN:
                self._event.on_press(__event.key)
            elif __event.type == KEYUP:
                self._event.on_release(__event.key)
            elif __event.type == QUIT:
                self.running = False

    def __on_collide(self):
        if self._event.on_collide is not None:
            self._event.on_collide(World._get_collision_list(self))

    def update(self, time_load=0.06):
        self.__on_event()
        self.__on_collide()
        self._surface.fill((0, 0, 0))
        for i in range(len(self)):
            self[i].update(time_load)
            if self[i].surface is not None:
                self._surface.blit(self[i].surface, self[i].position.position)
        if self._world is not None:
            for i in range(len(self._world)):
                self._world[i].update(time_load)
                if self._world[i].surface is not None:
                    self._surface.blit(
                        self._world[i].surface, self._world[i].position.position)
        if not self.running:
            self._display.quit()
            sys.exit()
        else:
            self._display.flip()
            self._clock.tick(int(time_load * 1000))


class GameObject(Object):
    '''
        Constructor:
            GameObject(size, mass) -> GameObject.
    '''

    @ Object.surface.setter
    def surface(self, value):
        '''Allows setting the surface.'''
        self._surface = value
        self._size = self._surface.get_size()

    @ Object.velocity.setter
    def velocity(self, value):
        '''Allows setting the velocity.'''
        self._velocity = value

    @ Object.position.setter
    def position(self, value):
        self._position = value
        self._x, self._y = self._position

    @ property
    def x(self):
        return self._x

    @ property
    def y(self):
        return self._x

    @ x.setter
    def x(self, value):
        self._x = value
        self._position = Vector(self._x, self._y)

    @ y.setter
    def y(self, value):
        self._y = value
        self._position = Vector(self._x, self._y)

    def __init__(self, size, mass=1):
        super().__init__()
        self._size = size
        self._mass = mass
        self._surface = pygame.Surface(self._size)
        self._tags.append('_game_object')
        self._x, self._y = self._position

    def Force(self, force: Vector):
        super().Force(force)

    def force_to(self, obj, force: Vector):
        return super().force_to(obj, force)

    def update(self, time_load=0.06):
        super().update(time_load)


def start_game(obj: Object):
    '''Start the game on a object (normal is Screen object).
        Call the obj.update() in a loop block with conditional obj.running.
        If you wanna create an owner.
        The code:
            while <the object/screen variable name>.running:
                <the object/screen variable name>.update(time_load)
        The time_load use the unit second.
    '''
    while obj.running:
        obj.update()


def get_objects_by_tag(tag='_object'):
    return [obj for obj in objects if obj.tag is tag]


def get_object_by_name(name):
    try:
        return [obj for obj in object if obj.name is name][0]
    except IndexError:
        return None


def get_objects():
    return objects


def remove_tag(tag):
    if tag in tags:
        tags.remove(tag)
