import sys
import requests


def send_webhook(wh_url, url):
    requests.post(wh_url, json={"content": url})


def get_page_url(url):
    r = requests.get(url)
    return r.url


if __name__ == '__main__':
    wh_url = sys.argv[0]
    url = sys.argv[1]
    r_url = get_page_url(url)
    if url == r_url:
        send_webhook(wh_url, r_url)
        print("Webhook sent")
    else:
        print("No update")
