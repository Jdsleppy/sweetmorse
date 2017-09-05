#!/usr/bin/env python3

import datetime as dt
import time

from sweetmorse.morse import Morse
from gpiozero import DigitalOutputDevice, DigitalInputDevice

speed = 100  # bits per second
cycle_time = 1/speed  # seconds per bit
end_of_file = "1010101010101010101"

print("Obtaining pin 21 for output...")
gpio_out = DigitalOutputDevice(21)  # voltage generated here

print("Obtaining pin 16 for input...")
print()
gpio_in = DigitalInputDevice(16)  # voltage read here
edges = []  # rising or falling voltage transitions
gpio_in.when_activated = lambda: edges.append((dt.datetime.now(), "1"))
gpio_in.when_deactivated = lambda: edges.append((dt.datetime.now(), "0"))

try:
    message = Morse.from_plain_text("sos")
    binary_outgoing = message.binary
    
    print("Sending message: " + message.plain_text)
    print("Converted to binary: " + binary_outgoing)
    print()
    print("Sending message at {} bits per second...".format(speed))
    print()
    
    for value in binary_outgoing + end_of_file:
        if value == '0':
            gpio_out.off()
        else:
            gpio_out.on()
        time.sleep(cycle_time)
    
    # Interpret all the 0s and 1s we've collected
    binary_incoming = []
    current_edge = edges[0]
    current_time = edges[0][0] + dt.timedelta(seconds=(cycle_time/2))
    
    while edges:
        if edges[0][0] < current_time:
            current_edge = edges.pop(0)
            # This is far from a realtime system, we'll just correct any
            # timing drift sync every time we see an edge.
            current_time = current_edge[0] + dt.timedelta(seconds=(cycle_time/2))
        binary_incoming.append(current_edge[1])
        current_time += dt.timedelta(seconds=cycle_time)
    
    binary_received = ''.join(binary_incoming[:-len(end_of_file)])
    print("Received binary: " + binary_received)

    message_received = Morse.from_binary(binary_received)
    print("Received message: " + message_received.plain_text)

finally:
    gpio_in.close()
    gpio_out.close()
