import math
import random
from constants import *

def generate_lumpy_shape_points(center, base_radius, num_points, max_variation):
    cx, cy = center
    points = []
    for i in range(num_points):
        angle = 2 * math.pi * i / num_points
        radius = base_radius + random.uniform(-max_variation, max_variation)
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
        points.append((x, y))
    return points

def is_moving_further_offscreen(pos, new_pos):
    return (
        (new_pos.x < 0 or new_pos.x > SCREEN_WIDTH) and abs(new_pos.x) > abs(pos.x)
    ) or (
        (new_pos.y < 0 or new_pos.y > SCREEN_HEIGHT) and abs(new_pos.y) > abs(pos.y)
    )