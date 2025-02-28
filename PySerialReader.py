import serial
import time


# Configure the correct COM port and baud rate
SERIAL_PORT = 'COM4'  # Change to match your setup (e.g., COM4, COM5, etc.)
BAUD_RATE = 115200

# ser = serial.Serial('COM4', 115200)  # Adjust port accordingly
# while True:
#     data = ser.readline().decode().strip()
#     print("Received:", data)


try:
    # Open the serial connection
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)

    while True:
        # Send a signal (e.g., "PING")
        message = "PING\n"
        ser.write(message.encode())  # Send message as bytes

        # Wait for a response from the microcontroller
        response = ser.readline().decode().strip()

        if response:
            print(f"Received: {response}")
        else:
            print("No response received.")

        # Wait 1 second before sending the next message
        time.sleep(1)

except serial.SerialException as e:
    print(f"Error: {e}")

finally:
    if ser.is_open:
        ser.close()