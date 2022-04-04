import time

def countdown(seconds):
  print("Countdown to launch commencing...")
  while (seconds > 0):
    print(f"{seconds}...")
    seconds -= 1
    time.sleep(1)
  print("LAUNCH!")

def main():
  countdown(3)

if __name__ == "__main__":
  main()
