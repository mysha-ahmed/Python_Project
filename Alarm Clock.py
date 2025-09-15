import time

# Get alarm time from user
alarm_time = input("Set the alarm time (HH:MM, 24-hour format): ")

print(f"Alarm set for {alarm_time}. Waiting...")

while True:
    # Get current time
    current_time = time.strftime("%H:%M")

    if current_time == alarm_time:
        print("Wake up! It's time!")
        break

    time.sleep(30)  # Check every 30 seconds to reduce CPU usage