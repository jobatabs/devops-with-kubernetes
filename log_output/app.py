import time, uuid
from datetime import datetime, timezone

def main() -> None:
    while True:
        now = datetime.now(timezone.utc)
        now = now.strftime('%Y-%m-%dT%H:%M:%S.%fZ: ' + str(uuid.uuid4()))
        print(now)
        time.sleep(5)

if __name__ == "__main__":
    main()
