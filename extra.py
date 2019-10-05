import xlwings as xw
import os
import pandas as pd
from icecream import ic

# wb = xw.Book()
# sht = wb.sheets["Sheet1"]

data_dump =[]

date = ("8/21/2019", "8/22/2019")
description = ("Store 1", "Store 2")
cat = ("Food", "Refund")
amount = ("-$20.12", "$403.11")

date2 = ("9/21/2019", "9/22/2019")
description2 = ("Store 69", "Noice 2")
cat2 = ("Oh noes", "Woops")
amount2 = ("$20.12", "-$403.11")

temp1 = zip(date, description, cat, amount)
temp2 = zip(date2, description2, cat2, amount2)
labels = ["Date", "Description", "Category", "Amount"]

data_dump.append(temp1)
data_dump.append(temp2)

ic(temp1)
ic(temp2)
ic(data_dump)
# ic(data_dump)
# df = pd.DataFrame(data_dump, columns=labels, index=False)
# ic(df)

# sht.range("A1").value = df
# sht.range("A1").options(pd.DataFrame, expand="table").value

# wb.save()
# wb.close()

with WebDriver(start_webdriver(chromedriver_path)) as wd:
        
class WebDriver:
    """
      Open and closer for the webdriver used in selenium - context manager - allows a resource, in this case the driver, to be used and closed when needed
      gets closed when outside of the with statement scope in main() \n
      TL;DR
      Allows the driver to be opened without having to remember to close it
    """

    # This is the constructor of the class
    def __init__(self, driver):
        self.driver = driver

    # Is asscoiated with the With statement
    def __enter__(self):
        return self.driver

    # Safely quits out of driver
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()
def start_webdriver(chromedriver_path):
    """
        Start up the Chrome Web Driver for Selenium with some preset defaults.
        Otherwise return `Failed`

        :param chromedriver_path: the path to the chromedriver.exe
            - can be relative or the full path

        :return: the driver object or `Failed`
    """
    # Attempts to get the most up to date chromedriver if there is a newer version
    # May fail if chromedriver is open and in use or if driver is not closed properly
    chrome_update = cdu.update_chromedriver(
        chromedriver_path.replace("chromedriver.exe", ""),
        current_exe_path=chromedriver_path,
    )
    if chrome_update == "CDUSuccess":
        print("Successful update for chromedriver")
    else:
        print("Failed to update chrome driver")
        sys.exit()

    # setting up chrome
    CHROME_OPTIONS = webdriver.ChromeOptions()
    # This fixes the issue with chrome complaining about Unpacked extensions being run at the start
    # of each driver startup
    CHROME_OPTIONS.add_experimental_option("useAutomationExtension", False)
    try:
        DRIVER = webdriver.Chrome(
            executable_path=chromedriver_path, options=CHROME_OPTIONS
        )
    except WebDriverException as error:
        thing_to_print = "Error {} | Can not start chrome - perhaps the chromedriver needs to be updated".format(
            error
        )
        logging.error(thing_to_print)
        return "Failed"

    # # Completely Hide the browser after it starts
    # DRIVER.set_window_position(-10000, 0)
    return DRIVER
