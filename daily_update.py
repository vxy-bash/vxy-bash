import datetime
import os

# Erstellt oder aktualisiert die Log-Datei
file_path = "activity_log.txt"

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(file_path, "a") as f:
    f.write(f"Bot Activity Sync: {now}\n")

print(f"Log updated at {now}")