from ST7735 import TFT
from machine import SPI, Pin, I2C, PWM
from neopixel import NeoPixel
from buttons import buttons
import time
import math

class RINGO(object):
    def __init__(self):
        self.font1 = {
            "Width": 6,
            "Height": 8,
            "Start": 32,
            "End": 127,
            "Data": bytearray([
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x06, 0x5F, 0x06, 0x00,
            0x00, 0x07, 0x03, 0x00, 0x07, 0x03,
            0x00, 0x24, 0x7E, 0x24, 0x7E, 0x24,
            0x00, 0x24, 0x2B, 0x6A, 0x12, 0x00,
            0x00, 0x63, 0x13, 0x08, 0x64, 0x63,
            0x00, 0x36, 0x49, 0x56, 0x20, 0x50,
            0x00, 0x00, 0x07, 0x03, 0x00, 0x00,
            0x00, 0x00, 0x3E, 0x41, 0x00, 0x00,
            0x00, 0x00, 0x41, 0x3E, 0x00, 0x00,
            0x00, 0x08, 0x3E, 0x1C, 0x3E, 0x08,
            0x00, 0x08, 0x08, 0x3E, 0x08, 0x08,
            0x00, 0x00, 0xE0, 0x60, 0x00, 0x00,
            0x00, 0x08, 0x08, 0x08, 0x08, 0x08,
            0x00, 0x00, 0x60, 0x60, 0x00, 0x00,
            0x00, 0x20, 0x10, 0x08, 0x04, 0x02,
            0x00, 0x3E, 0x51, 0x49, 0x45, 0x3E,
            0x00, 0x00, 0x42, 0x7F, 0x40, 0x00,
            0x00, 0x62, 0x51, 0x49, 0x49, 0x46,
            0x00, 0x22, 0x49, 0x49, 0x49, 0x36,
            0x00, 0x18, 0x14, 0x12, 0x7F, 0x10,
            0x00, 0x2F, 0x49, 0x49, 0x49, 0x31,
            0x00, 0x3C, 0x4A, 0x49, 0x49, 0x30,
            0x00, 0x01, 0x71, 0x09, 0x05, 0x03,
            0x00, 0x36, 0x49, 0x49, 0x49, 0x36,
            0x00, 0x06, 0x49, 0x49, 0x29, 0x1E,
            0x00, 0x00, 0x6C, 0x6C, 0x00, 0x00,
            0x00, 0x00, 0xEC, 0x6C, 0x00, 0x00,
            0x00, 0x08, 0x14, 0x22, 0x41, 0x00,
            0x00, 0x24, 0x24, 0x24, 0x24, 0x24,
            0x00, 0x00, 0x41, 0x22, 0x14, 0x08,
            0x00, 0x02, 0x01, 0x59, 0x09, 0x06,
            0x00, 0x3E, 0x41, 0x5D, 0x55, 0x1E,
            0x00, 0x7E, 0x11, 0x11, 0x11, 0x7E,
            0x00, 0x7F, 0x49, 0x49, 0x49, 0x36,
            0x00, 0x3E, 0x41, 0x41, 0x41, 0x22,
            0x00, 0x7F, 0x41, 0x41, 0x41, 0x3E,
            0x00, 0x7F, 0x49, 0x49, 0x49, 0x41,
            0x00, 0x7F, 0x09, 0x09, 0x09, 0x01,
            0x00, 0x3E, 0x41, 0x49, 0x49, 0x7A,
            0x00, 0x7F, 0x08, 0x08, 0x08, 0x7F,
            0x00, 0x00, 0x41, 0x7F, 0x41, 0x00,
            0x00, 0x30, 0x40, 0x40, 0x40, 0x3F,
            0x00, 0x7F, 0x08, 0x14, 0x22, 0x41,
            0x00, 0x7F, 0x40, 0x40, 0x40, 0x40,
            0x00, 0x7F, 0x02, 0x04, 0x02, 0x7F,
            0x00, 0x7F, 0x02, 0x04, 0x08, 0x7F,
            0x00, 0x3E, 0x41, 0x41, 0x41, 0x3E,
            0x00, 0x7F, 0x09, 0x09, 0x09, 0x06,
            0x00, 0x3E, 0x41, 0x51, 0x21, 0x5E,
            0x00, 0x7F, 0x09, 0x09, 0x19, 0x66,
            0x00, 0x26, 0x49, 0x49, 0x49, 0x32,
            0x00, 0x01, 0x01, 0x7F, 0x01, 0x01,
            0x00, 0x3F, 0x40, 0x40, 0x40, 0x3F,
            0x00, 0x1F, 0x20, 0x40, 0x20, 0x1F,
            0x00, 0x3F, 0x40, 0x3C, 0x40, 0x3F,
            0x00, 0x63, 0x14, 0x08, 0x14, 0x63,
            0x00, 0x07, 0x08, 0x70, 0x08, 0x07,
            0x00, 0x71, 0x49, 0x45, 0x43, 0x00,
            0x00, 0x00, 0x7F, 0x41, 0x41, 0x00,
            0x00, 0x02, 0x04, 0x08, 0x10, 0x20,
            0x00, 0x00, 0x41, 0x41, 0x7F, 0x00,
            0x00, 0x04, 0x02, 0x01, 0x02, 0x04,
            0x80, 0x80, 0x80, 0x80, 0x80, 0x80,
            0x00, 0x00, 0x03, 0x07, 0x00, 0x00,
            0x00, 0x20, 0x54, 0x54, 0x54, 0x78,
            0x00, 0x7F, 0x44, 0x44, 0x44, 0x38,
            0x00, 0x38, 0x44, 0x44, 0x44, 0x28,
            0x00, 0x38, 0x44, 0x44, 0x44, 0x7F,
            0x00, 0x38, 0x54, 0x54, 0x54, 0x08,
            0x00, 0x08, 0x7E, 0x09, 0x09, 0x00,
            0x00, 0x18, 0xA4, 0xA4, 0xA4, 0x7C,
            0x00, 0x7F, 0x04, 0x04, 0x78, 0x00,
            0x00, 0x00, 0x00, 0x7D, 0x40, 0x00,
            0x00, 0x40, 0x80, 0x84, 0x7D, 0x00,
            0x00, 0x7F, 0x10, 0x28, 0x44, 0x00,
            0x00, 0x00, 0x00, 0x7F, 0x40, 0x00,
            0x00, 0x7C, 0x04, 0x18, 0x04, 0x78,
            0x00, 0x7C, 0x04, 0x04, 0x78, 0x00,
            0x00, 0x38, 0x44, 0x44, 0x44, 0x38,
            0x00, 0xFC, 0x44, 0x44, 0x44, 0x38,
            0x00, 0x38, 0x44, 0x44, 0x44, 0xFC,
            0x00, 0x44, 0x78, 0x44, 0x04, 0x08,
            0x00, 0x08, 0x54, 0x54, 0x54, 0x20,
            0x00, 0x04, 0x3E, 0x44, 0x24, 0x00,
            0x00, 0x3C, 0x40, 0x20, 0x7C, 0x00,
            0x00, 0x1C, 0x20, 0x40, 0x20, 0x1C,
            0x00, 0x3C, 0x60, 0x30, 0x60, 0x3C,
            0x00, 0x6C, 0x10, 0x10, 0x6C, 0x00,
            0x00, 0x9C, 0xA0, 0x60, 0x3C, 0x00,
            0x00, 0x64, 0x54, 0x54, 0x4C, 0x00,
            0x00, 0x08, 0x3E, 0x41, 0x41, 0x00,
            0x00, 0x00, 0x00, 0x77, 0x00, 0x00,
            0x00, 0x00, 0x41, 0x41, 0x3E, 0x08,
            0x00, 0x02, 0x01, 0x02, 0x01, 0x00,
            0x00, 0x3C, 0x26, 0x23, 0x26, 0x3C
        ])}
        #updated pins/buttons
        self.BTN_1 = 0
        self.BTN_2 = 1
        self.BTN_3 = 2
        self.BTN_4 = 3
        self.BTN_5 = 4
        self.BTN_6 = 5
        self.BTN_7 = 6
        self.BTN_8 = 7
        self.BTN_9 = 8
        self.BTN_ASTERISK = 9
        self.BTN_0 = 10
        self.BTN_HASHTAG = 11
        self.BTN_FUN_RIGHT = 12
        self.BTN_FUN_LEFT = 15
        self.BTN_A = 16
        self.BTN_B = 17
        #obsolete buttons, successor - readJoystickX/Y()
        # self.BTN_UP = 18
        # self.BTN_DOWN = 19
        # self.BTN_LEFT = 20
        # self.BTN_RIGHT = 21

        self._BL_PIN = 21
        self._PIXELS_PIN = 12
        self._SIM_PIXELS_ENABLE_PIN = 26
        self._NUM_PIXELS = 8


        self.i2c = I2C(scl=Pin(27), sda=Pin(14), freq=100000) #ok
        self.buttons = buttons()
        #self.buttons = PCA9539(self.i2c, 0x21) #21 for main buttons, 20 for numerical keypad
        self.spi = SPI(2, baudrate=20000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19)) #ok
        self.display=TFT(self.spi,0,2,4) #ok
        self.display.initr()
        self.display.rgb(True)
        self.display.rotation(1) #rotation changed to 1 (top left)
        self.display.fill(0)
        self.pixels = NeoPixel(Pin(self._PIXELS_PIN, Pin.OUT), self._NUM_PIXELS, timing=True)

        self.BLACK = 0
        self.RED = self.display.RED
        self.MAROON = self.display.MAROON
        self.GREEN = self.display.GREEN
        self.FOREST = self.display.FOREST
        self.BLUE = self.display.BLUE
        self.NAVY = self.display.NAVY
        self.CYAN = self.display.CYAN
        self.YELLOW = self.display.YELLOW
        self.PURPLE = self.display.PURPLE
        self.WHITE = self.display.WHITE
        self.GRAY = self.display.GRAY


        Pin(self._BL_PIN, Pin.OUT).value(0)

    def collideRectRect(self, x1, y1, w1, h1, x2, y2, w2, h2):
        return (x2 < x1 + w1 and x2 + w2 > x1 and y2 < y1 + h1 and y2 + h2 > y1)
    def backlight(self, bl):
        PWM(Pin(self._BL_PIN)).duty(bl)
        return
    def cls(self):
        print("\x1B\x5B2J", end="")
        print("\x1B\x5BH", end="")
        return