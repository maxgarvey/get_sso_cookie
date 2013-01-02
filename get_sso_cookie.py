import requests
import json

def get_cookies(username, password, outfile="cookies.json",
                   url="https://sso.pdx.edu/cas/login"):
    r = requests.get(url, auth=(username, password))
    cookies = r.cookies
    cookies_dict = cookies.get_dict()

    with open(outfile, "w") as cookie_file:
        cookie_file.write(json.dumps(cookies_dict))
