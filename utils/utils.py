import numpy as np

from constants.default_values import DefaultValues
from constants.scale_units import ScaleUnits


def convert_hue(hue):
    default_ratio = 361
    opencv_ratio = 180

    ratio = default_ratio / opencv_ratio
    return np.round(hue / ratio, ScaleUnits.TWO)


def hue_match(img, hue_low, hue_high):
    match_pixels = DefaultValues.DEFAULT_VALUE
    no_match_pixels = DefaultValues.DEFAULT_VALUE
    for pixel in img:
        for h, s, v in pixel:
            if convert_hue(hue_low) <= h <= convert_hue(hue_high):
                match_pixels += ScaleUnits.ONE
            else:
                no_match_pixels += ScaleUnits.ONE

    total_pixels = match_pixels + no_match_pixels
    return np.round(match_pixels / total_pixels, ScaleUnits.TWO) * ScaleUnits.HUNDRED


def rgb_match(img, rgb_model):
    match_pixels = DefaultValues.DEFAULT_VALUE
    no_match_pixels = DefaultValues.DEFAULT_VALUE
    for pixel in img:
        for r, g, b in pixel:
            if rgb_model.r_low <= r <= rgb_model.r_high and rgb_model.g_low <= g <= rgb_model.g_high and rgb_model.b_low <= b <= rgb_model.b_high:
                match_pixels += ScaleUnits.ONE
            else:
                no_match_pixels += ScaleUnits.ONE

    total_pixels = match_pixels + no_match_pixels
    return np.round(match_pixels / total_pixels, ScaleUnits.TWO) * ScaleUnits.HUNDRED
