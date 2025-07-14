from datetime import datetime

timestamp = datetime.now().timestamp()
print("Seconds since January 1, 1970: {:,} or {:.2e} in scientific notation"
      .format(timestamp, timestamp))
print(datetime.now().strftime("%b %d %Y"))
