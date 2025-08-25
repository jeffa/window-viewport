#!/usr/bin/env python

import sys
import argparse
from window.viewport import viewport
from PIL import Image, ImageDraw, ImageFont

def main():
    parser = argparse.ArgumentParser(description='Process data and produce a bar chart in PNG format.')
    parser.add_argument('--data', nargs='+', type=str, help='data to chart, e.g., --data=5 --data=10 --data=3 or use a comma delimited string: --data=21,45,30,67,10')
    parser.add_argument('--height', type=int, default=150, help='height of PNG output')
    parser.add_argument('--width', type=int, default=200, help='width of PNG output')
    args = parser.parse_args()

    if args.data:
        # Parse the data
        data = []
        for item in args.data:
            if ',' in item:
                data.extend(map(int, item.split(',')))
            else:
                data.append(int(item))
    else:
        data = [4, 3, 10, 7, 2]  # Default data if none provided

    img = create_bar_chart(data, args.width, args.height)
    img.save("bar-chart.png", format='PNG')  # Output to stdout as PNG

def create_bar_chart(data, width, height):
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)

    mapper = viewport( world_bounds=(0, max(data), 0, len(data)), view_bounds=(height, 0, 0, width))

    # Draw the lines and labels
    for i, value in enumerate(data):
        x = mapper.Dx(i + 0.5)
        y_start = mapper.Dy(1)
        y_end = mapper.Dy(value - 0.5)

        draw.line((x, y_start, x, y_end), fill='black')
        # Draw the string label
        draw.text((mapper.Dx(i + 0.45), mapper.Dy(0)), str(value), fill='black')

    # Draw title
    draw.text((10, 20), "bar chart", fill='blue')

    return img

# python bar-charts.py --data=5 --data=10 --data=3 --width=300 --height=200
if __name__ == "__main__":
    main()
