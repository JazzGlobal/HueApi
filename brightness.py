import hueapi as Hue
import sys


brightness = int(sys.argv[1])
lightId = sys.argv[2]

light = Hue.GetLightByNum(lightId)
currentBrightness = int(light['state']['bri'])

Hue.UserRequest('PUT', f'lights/{lightId}/state', f'{{"bri":{currentBrightness + brightness}}}')
