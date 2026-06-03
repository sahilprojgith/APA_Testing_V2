from playwright.sync_api import sync_playwright

from tests.cart_tests import (
    test_add_backpack_to_cart,
    test_remove_backpack_from_cart,
    test_add_multiple_products
)

from tests.login_tests import (
    test_valid_login,
    test_invalid_password,
    test_empty_password,
    test_empty_username,
    test_locked_user
)


def run_test(test_function, page):

    try:

        print(f"\nRunning: {test_function.__name__}")

        passed, name = test_function(page)

        if passed:
            print(f"PASS : {name}")
        else:
            print(f"FAIL : {name}")

        return passed

    except Exception as e:

        print(f"ERROR : {test_function.__name__}")
        print(e)

        return False


with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )

    tests = [
        test_valid_login,
        test_invalid_password,
        test_empty_password,
        test_empty_username,
        test_locked_user,
        test_add_backpack_to_cart,
        test_remove_backpack_from_cart,
        test_add_multiple_products
    ]

    passed = 0

    print("\n========================================")
    print("STARTING TEST EXECUTION")
    print("========================================")

    for test in tests:

        print("\n----------------------------------------")

        # Fresh page for every test
        page = browser.new_page()

        if run_test(test, page):
            passed += 1

        page.close()

    print("\n========================================")
    print("TEST EXECUTION COMPLETED")
    print("========================================")

    print(f"TOTAL TESTS : {len(tests)}")
    print(f"PASSED      : {passed}")
    print(f"FAILED      : {len(tests) - passed}")

    print("========================================")

    input("\nPress Enter to close browser...")

    browser.close()

#try 4
# from playwright.sync_api import sync_playwright



# from tests.cart_tests import (
#     test_add_backpack_to_cart,
#     test_remove_backpack_from_cart
# )

# from tests.login_tests import (
#     test_valid_login,
#     test_invalid_password,
#     test_empty_password,
#     test_empty_username,
#     test_locked_user
# )


# def run_test(test_function, page):

#     try:

#         passed, name = test_function(page)

#         if passed:
#             print(f"PASS : {name}")
#         else:
#             print(f"FAIL : {name}")

#         return passed

#     except Exception as e:

#         print(f"ERROR : {test_function.__name__}")
#         print(e)

#         return False


# with sync_playwright() as p:

#     browser = p.chromium.launch(
#         headless=False
#     )

#     page = browser.new_page()

#     tests = [
#         test_valid_login,
#         test_invalid_password,
#         test_empty_password,
#         test_empty_username,
#         test_locked_user,
#         test_add_backpack_to_cart,
#         test_remove_backpack_from_cart
#     ]

#     passed = 0

#     for test in tests:

#         if run_test(test, page):
#             passed += 1

#     print("\n====================")
#     print(f"TOTAL TESTS : {len(tests)}")
#     print(f"PASSED      : {passed}")
#     print(f"FAILED      : {len(tests) - passed}")
#     print("====================")

#     input("\nPress Enter to close browser...")

#     browser.close()






# Try 3 for invalid password:
# from playwright.sync_api import sync_playwright


# def test_invalid_login(page):

#     page.goto("https://www.saucedemo.com")

#     page.fill("#user-name", "standard_user")
#     # page.fill("#password", "wrong_password")
#   --was testing empty one.  page.fill("#password", "")

#     page.click("#login-button")

#     error_text = page.locator("[data-test='error']").inner_text()

#     if "Username and password do not match" in error_text:
#         print("TC002 PASS : Invalid login rejected correctly")
#     else:
#         print("TC002 FAIL : Unexpected behavior")


# with sync_playwright() as p:

#     browser = p.chromium.launch(
#         headless=False
#     )

#     page = browser.new_page()

#     test_invalid_login(page)

#     input("Press Enter to close browser...")

#     browser.close()



# login one #2
# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:

#     browser = p.chromium.launch(
#         headless=False
#     )

#     page = browser.new_page()

#     page.goto("https://www.saucedemo.com")

#     page.fill("#user-name", "standard_user")
#     page.fill("#password", "secret_sauce")

#     page.click("#login-button")

#     page.wait_for_url("**/inventory.html")

#     if "inventory.html" in page.url:
#         print("PASS : Login successful")
#     else:
#         print("FAIL : Login failed")

#     input("Press Enter to close browser...")

#     browser.close()



#first code 

# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:

#     browser = p.chromium.launch(
#         headless=False
#     )

#     page = browser.new_page()

#     page.goto("https://www.saucedemo.com")

#     print("Website opened successfully!")

#     input("Press Enter to close browser...")

#     browser.close()