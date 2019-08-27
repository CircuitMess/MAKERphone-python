
# Installation

## 0. Thonny IDE

To start programming your Ringo phone using MicroPython you will need an IDE. Thonny IDE offers a simple interface and tools that you will need to get you started.

Go to the address: https://thonny.org/

Download the installation file according to your OS.
Install Thonny IDE and proceed to the next step.

## 1. Clone CircuitMess-Ringo-python repository

Download the repository from https://github.com/CircuitMess/CircuitMess-Ringo-python.git (Or download manually)

## 2. Flashing Ringo with MicroPython firmware

Follow the guide at: https://learn.adafruit.com/building-and-running-micropython-on-the-esp8266/flash-firmware

**NOTE**: Remember to flash the provided "ESP32_c.bin" custom firmware as it contains all the dependencies required for Ringo phone to work with MicroPython!

## 3. Thonny IDE setup

Before starting you will need to configure the IDE to work with Ringo phone

<img src="https://www.dropbox.com/s/p10v8j5oos71r25/0_.png?raw=1" alt="drawing" width="700"/>

## Interpreter and serial port configuration

1. Tools -> Options -> Interpreter
<img src="https://www.dropbox.com/s/dqv5pj2kfrpym33/1_.png?raw=1 alt="drawing" width="700"/>

2. Dropdown menu -> MicroPython on a generic device
<img src="https://www.dropbox.com/s/z7rwx20pmkt9j6w/2_.png?raw=1" alt="drawing" width="700"/>
	
3. Select your serial port from the second dropdown menu (or select detect manually)
<img src="https://www.dropbox.com/s/2ru2y8saev4webj/3_.png?raw=1" alt="drawing" width="700"/>


## Uploading and running scripts
	
1. File -> Open
2. Open one of the scripts in the /examples folder provided in the repository
3. To run the script you have two options:
		
<b>a) Upload and run a script</b>	
1. Device -> Upload current script with current name
<img src="https://www.dropbox.com/s/lsnd4z74h3rw3ul/4_.png?raw=1" alt="drawing" width="700"/>


2. To run the script from Ringo phone use REPL Shell (Bottom of the IDE screen), type:
	
	import scriptName
	
<img src="https://www.dropbox.com/s/h01voezv2x6gf8m/6_.png?raw=1" alt="drawing" width="700"/>


<b>b) Run script without uploading it</b>  
1. Press the Run current script button and your script will run without uploading to your device
<img src="https://www.dropbox.com/s/1dfotrnozfevgdl/5_.png?raw=1" alt="drawing" width="700"/>