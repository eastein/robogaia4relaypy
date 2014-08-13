import RPi.GPIO as GPIO

PINMAP = {
	1 : {
		1 : 4,
		2 : 17,
		3 : 21,
		4 : 22
	},
	2 : {
		1 : 4,
		2 : 17,
		3 : 27,
		4 : 22
	}
}

class RelayBoard(object) :
	PINMAP = None
	RELAYSTATE = {1: None, 2: None, 3: None, 4: None}

	@classmethod
	def init(cls, version) :
		cls.PINMAP = PINMAP[version]
		GPIO.setmode(GPIO.BCM)
		for pin in cls.PINMAP.values() :
			GPIO.setup(pin, GPIO.OUT)

	@classmethod
	def off(cls, relay) :
		pin = cls.PINMAP[relay]
		cls.RELAYSTATE[relay] = False
		GPIO.output(pin, cls.RELAYSTATE[relay])

	@classmethod
	def on(cls, relay) :
		pin = cls.PINMAP[relay]
		cls.RELAYSTATE[relay] = True
		GPIO.output(pin, cls.RELAYSTATE[relay])

	@classmethod
	def checkstate(cls, relay) :
		pin = cls.PINMAP[relay]
		return cls.RELAYSTATE[relay]
