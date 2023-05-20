import requests


def login_as(driver, base_url, user):
    session_cookie = None

    session = requests.Session()

    session.post(
        f"{base_url}/api/auth/login",
        data=user,
        allow_redirects=False,
    )
    session_cookie = session.cookies.get_dict().get("session")

    print(f"{session_cookie}")

    if session_cookie is not None:
        driver.add_cookie({"name": "session", "value": session_cookie})
        print(f"Yoinked session cookie: {session_cookie}")
    else:
        raise Exception("Failed to login")


def logout(driver):
    driver.delete_cookie("session")
    print("Unyoinked session cookie")
