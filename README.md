# AXOS

 CircuitPython script to measure temperature from a DS18B20 One Wire Temp Sensor (connected by Grove QWIIC Hub and Display on Pimoroni Badger 2040). I personally use this for monitoring the water temperature in my Axolotl tank.

## Hardware

Building this project is super easy, barely an inconvenience. 

You just need the following:
 
* DS18B20 One Wire Temp Sensor (with Grove Connector)
* Grove Quiic Hub
* Pimoroni Badger 2040

Connect up the devices (plug and play, no soldering required)

## Software

Flash the Badger 2040 with the latest [https://circuitpython.org/board/pimoroni_badger2040/](CircuitPython UF2)

Copy everything from this repo (except `LICENSE` and `README.md`) to your CIRCUITPY drive

By default the display updates every 15 minutes, but you can change the `delay` variable in `code.py` if you want it to update more frequently

????

PROFIT!