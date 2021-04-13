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

    # wh_url = "https://discordapp.com/api/webhooks/825451769315459103/94dQ9Bb70AbqRJk_H2t9tfx_lXfv263To5Anc5vUvwhUPxCJhOLiecxP1DIC6gYRHegB"
    # url = "https://www.newbalance.ie/pd/made-in-us-992/ML992V1-29382-M.html"
    # url = "https://www.newbalance.ie/pd/made-in-us-992/ML992V1-31315.html"