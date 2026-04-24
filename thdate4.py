from datetime import datetime, timedelta

bay_gio = datetime.now()
khoang_cho = timedelta(seconds=5)
tuong_lai = bay_gio+khoang_cho
print(f"thoi gian hien tai: {bay_gio.strftime('%H:%M:%S')}")
print(f"thoi gian sau 5s: {tuong_lai.strftime('%H:%M:%S')}")gi