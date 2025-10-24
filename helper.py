import pygame as pg
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

def polygons_collide(poly1, poly2):
    def to_int_points(points):
        return [tuple(map(int, (p.x, p.y))) if hasattr(p, "x") else tuple(map(int, p)) for p in points]

    p1 = to_int_points(poly1)
    p2 = to_int_points(poly2)

    all_x = [x for x, _ in p1 + p2]
    all_y = [y for _, y in p1 + p2]
    min_x, max_x = min(all_x), max(all_x)
    min_y, max_y = min(all_y), max(all_y)
    size = (max_x - min_x + 1, max_y - min_y + 1)

    def make_mask(points):
        shifted = [(x - min_x, y - min_y) for x, y in points]
        surf = pg.Surface(size, pg.SRCALPHA)
        pg.draw.polygon(surf, (255, 255, 255, 255), shifted)
        return pg.mask.from_surface(surf)

    return make_mask(p1).overlap(make_mask(p2), (0, 0)) is not None
