#!/usr/bin/env python

import argparse
import math
from window.viewport import viewport
from PIL import Image, ImageDraw

def main():
    parser = argparse.ArgumentParser(description='Graph waveform generator.')
    parser.add_argument('--wave', type=str, choices=['sine', 'square', 'fsquare', 'sawtooth', 'triangle'], default='sine', help='The waveform to draw.')
    parser.add_argument('--width', type=int, default=200, help='Width of PNG output.')
    parser.add_argument('--height', type=int, default=150, help='Height of PNG output.')
    parser.add_argument('--res', type=float, default=0.01, help='Resolution of the wave.')
    args = parser.parse_args()

    waves = {
        'sine': sine,
        'square': square,
        'fsquare': fsquare,
        'sawtooth': sawtooth,
        'triangle': triangle,
    }

    wave_func = waves[args.wave]
    img = Image.new("RGB", (args.width, args.height), "white")
    img = wave_func(img, args.res, args.wave, args.width, args.height)
    img.save(f"{args.wave}.png", "PNG")

def sine(img, res, wave, width, height):
    mapper = viewport( world_bounds=(0, 1, 0, 4), view_bounds=(height, 0, 0, width))
    return graph_it(mapper, lambda x: math.sin(x), img, res, wave)

def sawtooth(img, res, wave, width, height):
    mapper = viewport( world_bounds=(0, 1, 0, 4), view_bounds=(height, 0, 0, width))

    def sub(x):
        tmp = x / mapper.Wr * 2 * 1.618
        return 1 * (tmp - math.floor(tmp))

    return graph_it(mapper, sub, img, res, wave)

def triangle(img, res, wave, width, height):
    mapper = viewport( world_bounds=(0, 1, 0, 4), view_bounds=(height, 0, 0, width))

    def sub(x):
        return (2 / math.pi) * math.asin(math.sin(x * math.pi))

    return graph_it(mapper, sub, img, res, wave)

def square(img, res, wave, width, height):
    mapper = viewport( world_bounds=(-2, 1, 0, 4), view_bounds=(height, 0, 0, width))

    sign = lambda x: 0 if x == 0 else (1 if x > 0 else -1)

    def sub(x):
        return .9 * sign(math.sin(2 * math.pi * (x - .5) / (mapper.Wr * 2)))

    return graph_it(mapper, sub, img, res, wave)

def fsquare(img, res, wave, width, height):
    mapper = viewport( world_bounds=(-1, 2, 0, 4), view_bounds=(height, 0, 0, width))

    def sub(x):
        y = 0
        for i in range(1, 20, 2):
            y += 1 / i * math.cos(2 * math.pi * i * x - (math.pi / 2))
        return y

    return graph_it(mapper, sub, img, res, wave)

def graph_it(mapper, y_func, img, res, wave):
    draw = ImageDraw.Draw(img)

    prev = {}
    for x in range(mapper.Wl, mapper.Wr + 1, int(res * 100)):
        y = y_func(x)
        curr = {'dx': mapper.Dx(x), 'dy': mapper.Dy(y)}

        if prev:
            draw.line([prev['dx'], prev['dy'], curr['dx'], curr['dy']], fill="black")
        else:
            draw.point((curr['dx'], curr['dy']), fill="black")

        prev = curr

    # Annotate the wave
    draw.text((mapper.Dx(mapper.Wr / 3), mapper.Dy(mapper.Wb)), f"{wave} wave", fill="blue")
    return img

if __name__ == "__main__":
    main()
