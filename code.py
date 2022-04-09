# putting this together is easy, you just need the following:
# 
#		* DS18B20 One Wire Temp Sensor (with Grove Connector)
#		* Grove Quiic Hub
#		* Pimoroni Badger 2040
#
# Connect up the devices (plug and play, no soldering required)
# Flash the Badger 2040 with the latest CircuitPython UF2
# Install all the libraries mentioned below in the lib folder
# Copy the code below to code.py on the CIRCUITPY drive

import board
import terminalio
import displayio
import vectorio
import time
import adafruit_imageload
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
from adafruit_display_shapes.rect import Rect
from adafruit_onewire.bus import OneWireBus
import adafruit_ds18x20
import gc

# time between refreshes (default 15 mins)
delay = 60 * 15

# setup the DS18B20 one wire temp sensor
ow_bus = OneWireBus(board.SCL)
devices = ow_bus.scan()
ds18b20 = adafruit_ds18x20.DS18X20(ow_bus, devices[0])

# setup the display
display = board.DISPLAY
palette = displayio.Palette(1)
palette[0] = 0xFFFFFF
WHITE = 0xFFFFFF
BLACK = 0x000000

font1 = bitmap_font.load_font("/fonts/Fredoka-75.bdf")
font2 = bitmap_font.load_font("/fonts/Fredoka-32.bdf")



# this is where we put all the stuff we want to display
group = displayio.Group()

# set background
background = Rect(0, 0, display.width, display.height, fill=WHITE, outline=WHITE)

# load an image
image1, palette = adafruit_imageload.load("/images/axolotl1.bmp", bitmap=displayio.Bitmap, palette=displayio.Palette)
image2, palette = adafruit_imageload.load("/images/axolotl2.bmp", bitmap=displayio.Bitmap, palette=displayio.Palette)

print("\n\n\n\n\nLoading AxOS...")

# Loop forever so you can enjoy your message
while True:

	# update temperature	
	temp = '{0:0.0f}'.format(ds18b20.temperature)

	# Set text, font, and color
	text1 = str(temp) + 'ºc'

	if int(temp) > 15 and int(temp) < 20:
		text2 = "Temp OK!"
		pic = displayio.TileGrid(image1, pixel_shader=palette, x=168, y=0)
	else:
		text2 = "Temp BAD!"
		pic = displayio.TileGrid(image2, pixel_shader=palette, x=168, y=0)

	print(text1, text2)

	# Create the title and subtitle labels
	text1 = label.Label(font1, text=text1, color=BLACK, scale=1, x=10, y=40, scale=1)
	text2 = label.Label(font2, text=text2, color=BLACK, scale=1, x=10, y=92, scale=1)

	background = Rect(0, 0, display.width, display.height, fill=WHITE, outline=WHITE)

	# Create the display group and append objects to it

	group.append(background)
	group.append(pic)
	group.append(text1)
	group.append(text2)

	# Show the group and refresh the screen to see the result
	display.show(group)
	display.refresh()

	time.sleep(delay)

	# tidy up (saves memory)
	group.remove(background)
	group.remove(pic)
	group.remove(text1)
	group.remove(text2)
	gc.collect()

	pass
