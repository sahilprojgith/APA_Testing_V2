def test_add_backpack_to_cart(page):

    page.goto("https://www.saucedemo.com")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")

    page.click("#login-button")

    page.wait_for_url("**/inventory.html")

    page.click(
        "[data-test='add-to-cart-sauce-labs-backpack']"
    )

    badge_text = page.locator(
        ".shopping_cart_badge"
    ).inner_text()

    if badge_text == "1":
        return True, "TC006 Add Backpack To Cart"

    return False, "TC006 Add Backpack To Cart"

def test_remove_backpack_from_cart(page):

    page.goto("https://www.saucedemo.com")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")

    page.click("#login-button")

    page.wait_for_url("**/inventory.html")

    print("Current URL:", page.url)
    print("Inventory page loaded")

    # Add backpack
    page.click(
        "[data-test='add-to-cart-sauce-labs-backpack']"
    )

    # Remove backpack
    page.click(
        "[data-test='remove-sauce-labs-backpack']"
    )

    # Cart badge should disappear
    badge_count = page.locator(
        ".shopping_cart_badge"
    ).count()

    if badge_count == 0:
        return True, "TC007 Remove Backpack From Cart"

    return False, "TC007 Remove Backpack From Cart"

def test_add_multiple_products(page):

    page.goto("https://www.saucedemo.com")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")

    page.click("#login-button")

    page.wait_for_url("**/inventory.html")

    # Add Backpack
    page.click(
        "[data-test='add-to-cart-sauce-labs-backpack']"
    )

    # Add Bike Light
    page.click(
        "[data-test='add-to-cart-sauce-labs-bike-light']"
    )

    badge_text = page.locator(
        ".shopping_cart_badge"
    ).inner_text()

    print(f"Cart Badge Value: {badge_text}")

    if badge_text == "2":
        return True, "TC008 Add Multiple Products"

    return False, "TC008 Add Multiple Products"