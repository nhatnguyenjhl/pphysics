
class Friction:
    '''The friction is the manager to control the moving.'''

    def __init__(self, coefficient=0.1) -> None:
        self._coefficient = coefficient

    @ property
    def coefficient(self):
        return self._coefficient

    def __add__(self, other):
        if type(other) is Friction:
            return Friction(self.coefficient + other.coefficient)

    def apply_on(self, obj):
        obj.add_friction(self)
