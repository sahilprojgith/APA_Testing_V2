# APA_Testing_V2
Testing V_2.


Cmd Tests till now :

PS D:\arohan_v1> python --version
Python 3.12.6
PS D:\arohan_v1> python -m venv venv
PS D:\arohan_v1> venv\Scripts\activate
(venv) PS D:\arohan_v1> pip install playwright
  Downloading playwright-1.60.0-py3-none-win_amd64.whl.metadata (3.5 kB)
Collecting pyee<14,>=13 (from playwright)
  Downloading pyee-13.0.1-py3-none-any.whl.metadata (3.0 kB)
Collecting greenlet<4.0.0,>=3.1.1 (from playwright)
  Downloading greenlet-3.5.1-cp312-cp312-win_amd64.whl.metadata (3.9 kB)
Collecting typing-extensions (from pyee<14,>=13->playwright)
  Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 37.9/37.9 MB 4.3 MB/s eta 0:00:
Downloading greenlet-3.5.1-cp312-cp312-win_amd64.whl (238 kB)
Downloading pyee-13.0.1-py3-none-any.whl (15 kB)
Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
Installing collected packages: typing-extensions, greenlet, pyee, playwrigh
Successfully installed greenlet-3.5.1 playwright-1.60.0 pyee-13.0.1 typing-

[notice] A new release of pip is available: 24.2 -> 26.1.2
[notice] To update, run: python.exe -m pip install --upgrade pip
(venv) PS D:\arohan_v1> pip list
Package           Version
----------------- -------
greenlet          3.5.1
pip               24.2
playwright        1.60.0
pyee              13.0.1
typing_extensions 4.15.0
(venv) PS D:\arohan_v1> python -m playwright install
Downloading Chrome for Testing 148.0.7778.96 (playwright chromium v1223) frght.dev/builds/cft/148.0.7778.96/win64/chrome-win64.zip
181.9 MiB [====================] 100% 0.0s
Chrome for Testing 148.0.7778.96 (playwright chromium v1223) downloaded to \Local\ms-playwright\chromium-1223
Downloading Chrome Headless Shell 148.0.7778.96 (playwright chromium-headlettps://cdn.playwright.dev/builds/cft/148.0.7778.96/win64/chrome-headless-sh
112.4 MiB [====================] 100% 0.0s
Chrome Headless Shell 148.0.7778.96 (playwright chromium-headless-shell v12sers\Admin\AppData\Local\ms-playwright\chromium_headless_shell-1223
Downloading Firefox 150.0.2 (playwright firefox v1522) from https://cdn.plawnload/playwright/builds/firefox/1522/firefox-win64.zip
Firefox 150.0.2 (playwright firefox v1522) downloaded to C:\Users\Admin\Appht\firefox-1522
58.6 MiB [====================] 100% 0.0s
WebKit 26.4 (playwright webkit v2287) downloaded to C:\Users\Admin\AppData\bkit-2287
Downloading FFmpeg (playwright ffmpeg v1011) from https://cdn.playwright.deywright/builds/ffmpeg/1011/ffmpeg-win64.zip
1.3 MiB [====================] 100% 0.0s
FFmpeg (playwright ffmpeg v1011) downloaded to C:\Users\Admin\AppData\Local1011
Downloading Winldd (playwright winldd v1007) from https://cdn.playwright.deywright/builds/winldd/1007/winldd-win64.zip
Winldd (playwright winldd v1007) downloaded to C:\Users\Admin\AppData\Local1007
C:\Python312\python.exe: can't open file 'D:\\arohan_v1\\main.py': [Errno 2ctory
(venv) PS D:\arohan_v1\APA-Testing_Agent> dir


    Directory: D:\arohan_v1\APA-Testing_Agent


Mode                 LastWriteTime         Length Name                     
----                 -------------         ------ ----                     
-a----          6/4/2026   2:58 AM            341 main.py                  


(venv) PS D:\arohan_v1\APA-Testing_Agent> python main.py              
Website opened successfully!
(venv) PS D:\arohan_v1\APA-Testing_Agent> python main.py
PASS : Login successful
(venv) PS D:\arohan_v1\APA-Testing_Agent> python main.py
TC002 PASS : Invalid login rejected correctly
(venv) PS D:\arohan_v1\APA-Testing_Agent> python main.py
TC002 FAIL : Unexpected behavior
Press Enter to close browser...
(venv) PS D:\arohan_v1\APA-Testing_Agent> python main.py
TC002 FAIL : Unexpected behavior
Press Enter to close browser...
(venv) PS D:\arohan_v1\APA-Testing_Agent> python main.py
PASS : TC001 Valid Login
PASS : TC002 Invalid Password
PASS : TC003 Empty Password
PASS : TC004 Empty Username
PASS : TC005 Locked User

====================
TOTAL TESTS : 5
PASSED      : 5
FAILED      : 0
====================

Press Enter to close browser...
(venv) PS D:\arohan_v1\APA-Testing_Agent> python main.py
PASS : TC001 Valid Login
PASS : TC002 Invalid Password
PASS : TC003 Empty Password
PASS : TC004 Empty Username
PASS : TC005 Locked User
PASS : TC006 Add Backpack To Cart
====================
TOTAL TESTS : 6
PASSED      : 6
FAILED      : 0
====================

Press Enter to close browser...
(venv) PS D:\arohan_v1\APA-Testing_Agent> python main.py
PASS : TC001 Valid Login
PASS : TC002 Invalid Password
PASS : TC003 Empty Password
PASS : TC004 Empty Username
PASS : TC005 Locked User
PASS : TC006 Add Backpack To Cart
ERROR : test_remove_backpack_from_cart
Page.click: Timeout 30000ms exceeded.
Call log:
  - waiting for locator("[data-test='add-to-cart-sauce-labs-backpack']")


====================
TOTAL TESTS : 7
PASSED      : 6
====================

Press Enter to close browser...
(venv) PS D:\arohan_v1\APA-Testing_Agent> python main.py
PASS : TC001 Valid Login
PASS : TC002 Invalid Password
PASS : TC003 Empty Password
PASS : TC004 Empty Username
PASS : TC005 Locked User
PASS : TC006 Add Backpack To Cart
Current URL: https://www.saucedemo.com/inventory.html
Inventory page loaded
ERROR : test_remove_backpack_from_cart
Page.click: Timeout 30000ms exceeded.
Call log:
  - waiting for locator("[data-test='add-to-cart-sauce-labs-backpack']")


====================
TOTAL TESTS : 7
PASSED      : 6
FAILED      : 1
====================

Press Enter to close browser...
(venv) PS D:\arohan_v1\APA-Testing_Agent> python main.py

========================================
STARTING TEST EXECUTION
========================================

----------------------------------------

Running: test_valid_login
PASS : TC001 Valid Login

----------------------------------------

Running: test_invalid_password
PASS : TC002 Invalid Password

----------------------------------------

Running: test_empty_password
PASS : TC003 Empty Password

----------------------------------------

Running: test_empty_username
PASS : TC004 Empty Username

----------------------------------------

Running: test_locked_user
PASS : TC005 Locked User

----------------------------------------

Running: test_add_backpack_to_cart
PASS : TC006 Add Backpack To Cart

----------------------------------------

Running: test_remove_backpack_from_cart
Current URL: https://www.saucedemo.com/inventory.html
Inventory page loaded
PASS : TC007 Remove Backpack From Cart

========================================
TEST EXECUTION COMPLETED
========================================
TOTAL TESTS : 7
PASSED      : 7
FAILED      : 0
========================================

Press Enter to close browser...
(venv) PS D:\arohan_v1\APA-Testing_Agent> python main.py

========================================
STARTING TEST EXECUTION
========================================

----------------------------------------

Running: test_valid_login
PASS : TC001 Valid Login

----------------------------------------

Running: test_invalid_password
PASS : TC002 Invalid Password

----------------------------------------

Running: test_empty_password
PASS : TC003 Empty Password

----------------------------------------

Running: test_empty_username
PASS : TC004 Empty Username

----------------------------------------

Running: test_locked_user
PASS : TC005 Locked User

----------------------------------------

Running: test_add_backpack_to_cart
PASS : TC006 Add Backpack To Cart

----------------------------------------

Running: test_remove_backpack_from_cart
Current URL: https://www.saucedemo.com/inventory.html
Inventory page loaded
PASS : TC007 Remove Backpack From Cart

----------------------------------------

Running: test_add_multiple_products
Cart Badge Value: 2
PASS : TC008 Add Multiple Products

========================================
TEST EXECUTION COMPLETED
========================================
TOTAL TESTS : 8
PASSED      : 8
FAILED      : 0
========================================

Press Enter to close browser...
(venv) PS D:\arohan_v1\APA-Testing_Agent> 
