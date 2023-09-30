import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self,color):
        super().__init__()
        self._cycle_color = color
        self._segments = []
        if color == constants.GREEN:
            self._prepare_body()
        else:
            self._prepare_body2()

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        self._segments[0].move_next()
        # update velocities
        tail = Actor()
        tail.set_color(self._segments[0].get_color())
        tail.set_text("#")
        tail.set_position(self._segments[0].get_position())
        self._segments.append(tail)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(self._cycle_color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)

        position = Point(x  * constants.CELL_SIZE, y)
        velocity = Point(1 * constants.CELL_SIZE, 0)
        text = "8"
        color = constants.YELLOW 
        
        segment = Actor()
        segment.set_position(position)
        segment.set_velocity(velocity)
        segment.set_text(text)
        segment.set_color(color)
        self._segments.append(segment)

    def _prepare_body2 (self):
        x = int(constants.MAX_X / 1.1)
        y = int(constants.MAX_Y / 2)

        position = Point(x  * constants.CELL_SIZE, y)
        velocity = Point(1 * constants.CELL_SIZE, 0)
        text = "8"
        color = constants.GREEN 
        
        segment = Actor()
        segment.set_position(position)
        segment.set_velocity(velocity)
        segment.set_text(text)
        segment.set_color(color)
        self._segments.append(segment)


 
