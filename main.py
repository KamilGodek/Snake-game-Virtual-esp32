from machine import Pin, I2C, ADC
import ssd1306
import utime

# ESP32 Pin assignment
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Pin assignment for joystick
joystick_x_pin = 34
joystick_y_pin = 35

# Initialize ADC
adc_x = ADC(Pin(joystick_x_pin))
adc_y = ADC(Pin(joystick_y_pin))

# Snake properties
snake_size = 1
snake = [(oled_width // 2, oled_height // 2)]  # Initial position of the snake
snake_direction = (1, 0)  # Initial direction of the snake (right)

# Food properties
food = []

def generate_food():
    global food
    food = [(utime.ticks_us() % oled_width, utime.ticks_us() % oled_height)]

generate_food()  # Generate initial food

def move_snake():
    global snake
    global snake_direction
    global food
    global snake_size

    while True:
        # Read values from joystick
        x_value = adc_x.read()
        y_value = adc_y.read()

        # Determine the new direction based on joystick values
        if x_value < 1000:
            snake_direction = (1, 0)   # Move right
        elif x_value > 3000:
            snake_direction = (-1, 0)  # Move left
        elif y_value < 1000:
            snake_direction = (0, 1)   # Move down
        elif y_value > 3000:
            snake_direction = (0, -1)  # Move up

        # Move the snake by adding a new head in the current direction
        new_head = ((snake[0][0] + snake_direction[0]) % oled_width, (snake[0][1] + snake_direction[1]) % oled_height)
        snake.insert(0, new_head)

        # Check if the snake has collided with food
        if snake[0] in food:
            generate_food()
            snake_size += 1  # Increase the size of the snake

        # Keep the snake size limited
        if len(snake) > snake_size:
            snake.pop()

        utime.sleep(0.1)  # Adjust the speed of the snake

# Start the snake movement in the background
import _thread
_thread.start_new_thread(move_snake, ())

def draw_snake():
    while True:
        oled.fill(0)  # Clear the display

        # Draw the snake on the display
        for segment in snake:
            oled.pixel(segment[0], segment[1], 1)  # 1 indicates white color

        # Draw food on the display
        for pixel in food:
            oled.pixel(pixel[0], pixel[1], 1)

        oled.show()
        utime.sleep(0.1)

# Start drawing the snake in the background
_thread.start_new_thread(draw_snake, ())

# Wait for some time to see the snake animation
utime.sleep(60)
