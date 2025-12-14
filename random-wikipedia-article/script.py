import requests
import sys

def main():
    request = requests.get("https://en.wikipedia.org/wiki/Special:Random", timeout=10, headers={"User-Agent": "python requests library"}, allow_redirects=False)
    print(request.headers["Location"])
    article_url = request.headers["Location"]
    data = {"todo": f"Read {article_url}"}
    result = requests.post("http://todo-backend-svc:3000/todos", data=data, timeout=15, allow_redirects=False)
    if result.status_code == 301:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
