import time

def countdown(seconds):
  print("Countdown to launch commencing...")
  while (seconds > 0):
    print(f"{seconds}...")
    seconds -= 1
    time.sleep(1)
  print("LAUNCH!")

def is_successful(success):
  if success:
    print("Congratulations! Launch was a success!")
  else:
    print("Oh no! Something went wrong, launch failed!")

def main():
  countdown(3)
  is_successful(True)

if __name__ == "__main__":
  main()
