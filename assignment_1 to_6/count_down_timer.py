import time

seconds = int(input("Enter the countdown time in seconds: "))

while seconds > 0:
    mins, secs = divmod(seconds, 60)
    timer = f'{mins:02d}:{secs:02d}'
    print(f'Time left: {timer}', end='\r')  # overwrite the line
    time.sleep(1)
    seconds -= 1

print("\nTime's up! ⏰")
