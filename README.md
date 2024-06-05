# Macropad Project

This repository contains the code and documentation for a 4x5 macropad built using the following components:

- **Arduino Nano**: Microcontroller for handling key presses and communication.
- **20 Mechanical Switches**: Used as the keys for the macropad.
- **20 Diodes (1N4148)**: To prevent ghosting and ensure reliable keypress detection.
- **Python Script**: Reads data from the serial port and triggers key events using the `pyautogui` library.
- **Keymaps**: Two layouts available—normal and developer—switchable using the special `FN` key.

## Features

- **Customizable Layouts**: Define the key layout for your macropad using the Arduino module.
- **Serial Communication**: The Arduino sends key data over the serial port.
- **Python Script**: Reads serial data and simulates keypresses using `pyautogui`.
- **FN Key**: Easily switch between the normal and developer keymaps.

## Usage

1. **Normal Mode**:
   - Use the macropad with the default keymap.
   - Customize the key layout in the Arduino module.

2. **Developer Mode**:
   - Press the `FN` key to switch to developer mode.
   - Use a different key layout for programming.

## Contributing

Feel free to contribute by opening issues or pull requests. Let's make this macropad even better!

## License

This project is licensed under the MIT License. See the LICENSE file for details.