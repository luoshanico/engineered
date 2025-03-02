import pymunk
import pymunk.pygame_util
import settings

class BuilderEnvironment:
    def __init__(self, game):
        self.game = game
        self.setup_space()

    def setup_space(self):
        self.game.draw_options = pymunk.pygame_util.DrawOptions(self.game.surface)
        self.game.space = pymunk.Space()
        self.game.space.gravity = 0, 2000

    def add_ground(self):
        segment = pymunk.Segment(self.game.space.static_body, (0, settings.HEIGHT), (settings.RES), 20)
        segment.elasticity = settings.world['elasticity']
        segment.friction = settings.world['friction']
        segment.collision_type = settings.WORLD_CAT
        self.game.space.add(segment)
        self.game.segment_shape = segment  # store it if needed

    def create_ball(self, pos):
        mass, radius = 1, 60
        moment = pymunk.moment_for_circle(mass, 0, radius)
        body = pymunk.Body(mass, moment)
        body.position = pos
        shape = pymunk.Circle(body, radius)
        shape.elasticity = 0.9
        shape.friction = 0.3
        shape.collision_type = settings.OBJECT_CAT
        self.game.space.add(body, shape)
        self.game.ball_body = body
        self.game.ball_shape = shape

    def update(self):
        # Use a fixed step time or dt from the game if available
        self.game.space.step(1 / settings.FPS)

    def render(self):
        self.game.space.debug_draw(self.game.draw_options)
