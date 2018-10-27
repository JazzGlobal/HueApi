# HueApi
A small collection of scripts I wrote to access my lights while working at my computer. This only works with Python3.

# Dependencies
[Requests](http://docs.python-requests.org/en/master/)

You also need to make sure you follow the tutorial found [Here](https://developers.meethue.com/documentation/getting-started)
You only need to follow steps 1 - 3. 

Once you've finished following the tutorial, replace the 'apiPrefix' and 'user' values found in the hueapi.py file. This is crucial in being able to use the scripts.

# Examples
This is pretty straight forward. Run the scripts using their proper parameters.

#### Toggle Light ID 1

```$ python3 toggle.py 1```

#### Change Brightness
Increases the brightness of Light ID 1 by 100.

```$ python3 brightness.py 100 1```

Decreases the brightness of Light ID 1 by 100.

```$ python3 brightness.py -100 1```

#### Change Color
Changes Color of Light ID 1 to Red. 

```$ python3 color red 1```

