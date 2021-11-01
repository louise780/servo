input.onButtonPressed(Button.A, function () {
    basic.showNumber(0)
    basic.showNumber(90)
    basic.showNumber(180)
    basic.pause(500)
    basic.pause(500)
    basic.pause(500)
    servos.P0.setAngle(0)
    servos.P0.setAngle(90)
    servos.P0.setAngle(180)
    servos.P0.stop()
})
65
basic.showString("SEVER TIME")
basic.showIcon(IconNames.Heart)
basic.forever(function () {
	
})
