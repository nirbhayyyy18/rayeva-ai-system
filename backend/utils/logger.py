import os
from datetime import datetime

def log_ai(prompt,response):

    log_dir = "backend/logs"

    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, "ai_logs.txt")

    with open(log_file, "a", encoding="utf-8") as f:

        f.write("\n\n")

        f.write("TIME: "+ str(datetime.now()))

        f.write("\nPROMPT:\n")

        f.write(prompt)

        f.write("\nRESPONSE:")

        f.write(response)

