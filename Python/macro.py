import sys
import time
import pyautogui
import serial


class Macropad:
    def __init__(self):
        self.port = 'COM4'
        self.baud = 9600
        self.layer = 1
        self.serial = None
        self.layer_toggle = {1: 2, 2: 1}
        self.sleep_time = 0.1
        self.keymap_1 = {
            '0': 'num0', '1': 'num1',
            '2': 'num2', '3': 'num3',
            '4': 'num4', '5': 'num5',
            '6': 'num6', '7': 'num7',
            '8': 'num8', '9': 'num9',
            'S': ['win', 'e'], 'C': ['ctrl', 'c'],
            'P': ['ctrl', 'v'],
            'M': ['ctrl', 'z'], '@': 'f2',
            '$': ['alt', 'f4'], '%': 'f5',
            '+': 'f12', 'E': 'playpause'
        }
        self.keymap_2 = {
            '0': ['ctrl', '/'], '1': '{',
            '2': '}', '3': ['\'', '\''],
            '4': '[', '5': ']',
            '6': ['"', '"'], '7': '(',
            '8': ')', '9': '_',
            'S': ['win', 'e'], 'C': ['ctrl', 'c'],
            'P': ['ctrl', 'v'],
            'M': ['ctrl', 'z'], '@': 'f2',
            '$': ['alt', 'f4'], '%': 'f5',
            '+': 'f12', 'E': ['ctrl', 's']
        }

        self.keymap_opt = {
            1: self.keymap_1,
            2: self.keymap_2
        }
        self.current_keymap = self.keymap_1
        self.layer_mode = {1: 'normal', 2: 'developer'}

    def _connect_serial(self) -> bool:
        try:
            self.serial = serial.Serial(self.port, self.baud)
        except Exception as e:
            print(f'Error connecting to serial: {e}')
            sys.exit(-1)

        print(f'Connected to serial: {self.port}:{self.baud}')
        time.sleep(0.5)
        return True

    def _print_mode(self):
        print(f'Layer: {self.layer_mode[self.layer]}')
        return

    def _set_current_keymap(self):
        self.current_keymap = self.keymap_opt[self.layer]
        return

    def run(self):
        self._connect_serial()
        self._print_mode()

        while True:
            data = str(self.serial.readline())[2]
            if data == 'F':
                self.layer = self.layer_toggle.get(self.layer, self.layer)
                self._set_current_keymap()
                self._print_mode()

            key = self.current_keymap.get(data, None)

            if key:
                pyautogui.press(
                    key
                ) if isinstance(key, str) else pyautogui.hotkey(key[0], key[1])
            else:
                if data != 'F':
                    print(f'Key not found: {data}')

            time.sleep(self.sleep_time)


if __name__ == "__main__":
    macro_pad = Macropad()
    macro_pad.run()
