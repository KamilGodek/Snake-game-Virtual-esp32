# Snake Game on MicroPython with ESP32 and OLED Display
This Snake Game project was crafted by Kamil Godek using virtual components simulated on the online platform wokwit.com 
You can use a ready-made simulation link : https://wokwi.com/projects/383020139135163393?fbclid=IwAR1W8fn_RTOpXfMreZjh3cpelEgZoRKmv3J5Ep2DD_EjizM5D5OrWmDZm1c

This project implements a simple Snake Game on MicroPython, designed to run on ESP32 microcontroller with an OLED display. The game utilizes a joystick for controlling the snake's movement. The snake grows by consuming randomly generated food on the display.
![Esp32](https://github.com/KamilGodek/Projekt_SystemyWizyjne/assets/135075598/81162b62-8059-4aeb-8678-912dab3b4a58)


# Hardware Requirements
- ESP32 microcontroller
- SSD1306 OLED Display
- Joystick (analog input)

# Dependencies
- MicroPython machine module
- MicroPython ssd1306 module
- MicroPython utime module

# Usage
1. Connect the OLED display and joystick to the ESP32.
2. Upload the provided MicroPython script to the ESP32.
3. Run the script to start the Snake Game.
4. Control the snake's direction using the joystick.
5. The snake grows by consuming food, randomly placed on the display.

# Code Overview
- `main.py`: Main script containing the Snake Game logic.
- `machine.py`, `ssd1306.py`, `utime.py`: MicroPython modules used for hardware interaction.
