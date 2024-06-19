import numpy as np


def convert_hue(hue):
    ratio = 361 / 180
    return np.round(hue / ratio, 2)


def hue_match_pct(img, hue_low, hue_high):
    match_pixels = 0
    no_match_pixels = 0
    for pixel in img:
        for h, s, v in pixel:
            # if convert_hue(hue_low) <= h <= convert_hue(hue_high):  # убрать convert_hue
            if 114 <= h <= 145 and 30 <= s <= 57 and 27 <= v <= 57:
                match_pixels += 1
            else:
                no_match_pixels += 1

    total_pixels = match_pixels + no_match_pixels
    return np.round(match_pixels / total_pixels, 2) * 100