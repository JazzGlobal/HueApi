import hueapi as Hue
import sys

lightId = sys.argv[1]

Hue.ToggleLight(lightId)
