import time

def countdown_timer(seconds):
    print(f"Starting countdown from {seconds} seconds...\n")

    while seconds:
        mins, secs = divmod(seconds, 60)  # Get minutes and seconds
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        print(time_format, end="\r")  # Overwrite the line in the terminal
        time.sleep(1)  # Wait for one second
        seconds -= 1  # Decrease the time by one second

    print("Time's up! ⏰")

def main():
    print("Welcome to the Countdown Timer!")
    
    # Ask user to input countdown time
    try:
        countdown_time = int(input("Enter the countdown time in seconds: "))
        if countdown_time <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    countdown_timer(countdown_time)

if __name__ == "__main__":
    main()
