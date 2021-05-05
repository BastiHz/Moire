from math import ceil, sqrt

import pygame

from src.pattern import Pattern


BACKGROUND_COLOR = pygame.Color(220, 220, 220)
DOT_COLOR = pygame.Color(16, 16, 16)
DOT_RADIUS = 4
DOT_DISTANCE = 12


class DotsHexagonalPattern(Pattern):
    def __init__(self):
        width, height = pygame.display.get_window_size()
        magnification = 1.5
        background = pygame.Surface((width * magnification, height * magnification))
        background.fill(BACKGROUND_COLOR)

        dot_radius_magnified = DOT_RADIUS * magnification
        dot_distance_magnified = DOT_DISTANCE * magnification
        column_spacing = sqrt(3) / 2 * dot_distance_magnified  # height of equilateral triangle
        shifted_column_offset = dot_distance_magnified / 2
        column_is_shifted = False
        n_horizontal = ceil((width * 1.5) / column_spacing) + 1
        n_vertical = ceil(height / DOT_DISTANCE) + 1

        # Make it so that there is a dot at the center of rotation:
        width_half = width * magnification / 2
        height_half = height * magnification / 2
        center_column_index, x_offset = divmod(
            (width_half - dot_radius_magnified),
            column_spacing
        )
        if center_column_index % 2 == 0:
            y_offset = ((height_half - dot_radius_magnified - shifted_column_offset)
                        % dot_distance_magnified)
        else:
            y_offset = (height_half - dot_radius_magnified) % dot_distance_magnified

        for i in range(n_horizontal):
            x = dot_radius_magnified + column_spacing * i + x_offset - column_spacing
            for j in range(n_vertical):
                y = (dot_radius_magnified + dot_distance_magnified * j
                     + y_offset - dot_distance_magnified)
                if column_is_shifted:
                    y += shifted_column_offset
                pygame.draw.circle(
                    background,
                    DOT_COLOR,
                    (x, y),
                    dot_radius_magnified
                )
            column_is_shifted = not column_is_shifted

        foreground = background.copy()
        foreground.set_colorkey(BACKGROUND_COLOR)

        super().__init__(background, foreground, magnification)
