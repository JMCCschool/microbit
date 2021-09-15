def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pass
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_touched():
    pins.digital_write_pin(DigitalPin.P1, 1)
    pins.digital_write_pin(DigitalPin.P0, 1)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_logo_released():
    basic.pause(20000)
    pins.digital_write_pin(DigitalPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P0, 0)
input.on_logo_event(TouchButtonEvent.RELEASED, on_logo_released)

def on_every_interval():
    basic.show_leds("""
        . . . . .
                # . # . #
                # # # . #
                # . # . #
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                # . # . #
                # # # . #
                # . # . #
    """)
    basic.show_leds("""
        # . # . #
                . . . . .
                . . . . .
                # . # . #
                # # # . #
    """)
    basic.show_leds("""
        # # # . #
                # . # . #
                . . . . .
                . . . . .
                # . # . #
    """)
    basic.show_leds("""
        # . # . #
                # # # . #
                # . # . #
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                # . # . #
                # # # . #
                # . # . #
                . . . . .
    """)
loops.every_interval(1000, on_every_interval)
