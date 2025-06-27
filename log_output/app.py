import time, uuid
from datetime import datetime, timezone

def main() -> None:
    while True:
        now = datetime.now(timezone.utc)
        now = now.strftime('%Y-%m-%dT%H:%M:%S.%fZ: ' + str(uuid.uuid4()))
        with open("/app/share/file.txt", "w", encoding="utf-8") as f:
            f.write(now)
        time.sleep(5)

if __name__ == "__main__":
    main()
