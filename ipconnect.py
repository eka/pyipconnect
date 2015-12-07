#!/usr/bin/env python
import os
import requests

from dotenv import load_dotenv


CHECK_LOGIN_URL = 'http://{}/0/wl/cklogin'
LOGIN_URL = 'http://{}/0/wl/'


def is_logged_in():
    r = requests.get(CHECK_LOGIN_URL.format(os.environ.get('ALLIANCE_HOST')))
    return 'yes' in r.content


def login():
    # you should set ALLIANCE_USER and ALLIANCE_PASS in the .config file in the
    # same directory
    data = {
        'login': 1,
        'user': os.environ.get('ALLIANCE_USER'),
        'pass': os.environ.get('ALLIANCE_PASS')
    }
    r = requests.post(
        LOGIN_URL.format(os.environ.get('ALLIANCE_HOST')),
        data=data,
    )
    assert r.status_code == 200


def main():
    load_dotenv(os.path.join(os.path.dirname(__file__), '.config'))
    print "Checking connection"
    if not is_logged_in():
        print "Not logged in, trying to login"
        login()
        assert is_logged_in()
        print "Login successful"
    else:
        print "Already logged in"


if __name__ == "__main__":
    main()
