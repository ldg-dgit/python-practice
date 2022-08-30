from requests import get

websites = [
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com"
]

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    print(website)

# pypi.org 에 많은 외부 라이브러리를 찾을 수 있다.
# pip3 install requests
