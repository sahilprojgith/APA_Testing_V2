def test_valid_login(page):

    page.goto("https://www.saucedemo.com")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")

    page.click("#login-button")

    page.wait_for_url("**/inventory.html")

    if "inventory.html" in page.url:
        return True, "TC001 Valid Login"
    
    return False, "TC001 Valid Login"


def test_invalid_password(page):

    page.goto("https://www.saucedemo.com")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "wrong_password")

    page.click("#login-button")

    error_text = page.locator("[data-test='error']").inner_text()

    if "Username and password do not match" in error_text:
        return True, "TC002 Invalid Password"

    return False, "TC002 Invalid Password"


def test_empty_password(page):

    page.goto("https://www.saucedemo.com")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "")

    page.click("#login-button")

    error_text = page.locator("[data-test='error']").inner_text()

    if "Password is required" in error_text:
        return True, "TC003 Empty Password"

    return False, "TC003 Empty Password"


def test_empty_username(page):

    page.goto("https://www.saucedemo.com")

    page.fill("#user-name", "")
    page.fill("#password", "secret_sauce")

    page.click("#login-button")

    error_text = page.locator("[data-test='error']").inner_text()

    if "Username is required" in error_text:
        return True, "TC004 Empty Username"

    return False, "TC004 Empty Username"


def test_locked_user(page):

    page.goto("https://www.saucedemo.com")

    page.fill("#user-name", "locked_out_user")
    page.fill("#password", "secret_sauce")

    page.click("#login-button")

    error_text = page.locator("[data-test='error']").inner_text()

    if "Sorry, this user has been locked out" in error_text:
        return True, "TC005 Locked User"

    return False, "TC005 Locked User"