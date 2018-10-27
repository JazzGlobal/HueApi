import hueapi as Hue
import sys


color = sys.argv[1]
light = sys.argv[2]

Hue.ChangeColor(light, color)
