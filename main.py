def on_button_pressed_a():
    basic.show_number(0)
    basic.show_number(90)
    basic.show_number(180)
    basic.pause(500)
    basic.pause(500)
    basic.pause(500)
    servos.P0.set_angle(0)
    servos.P0.set_angle(90)
    servos.P0.set_angle(180)
    servos.P0.stop()
input.on_button_pressed(Button.A, on_button_pressed_a)
65
basic.show_string("SUVER TIME")
basic.show_icon(IconNames.HEART)

def on_forever():
    pass
basic.forever(on_forever)
