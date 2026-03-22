from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

# Step 1 – Open Google
driver.get("https://www.google.com")

# Step 2 – Search your college website
box = wait.until(
    EC.presence_of_element_located((By.NAME, "q"))
)
box.send_keys("Guru Nanak Dev Engineering College, Ludhiana")
box.send_keys(Keys.ENTER)


# Step 3 – Click your college website link from Google results
college_link = wait.until(
    EC.element_to_be_clickable(
        (By.PARTIAL_LINK_TEXT, "Guru Nanak Dev Engineering College")
    )
)
college_link.click()


# ---- Now you are on your college website ----

# Step 4 – Click Departments
departments = wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Departments"))
)
departments.click()


# Step 5 – Click Information Technology
it_dept = wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Information Technology"))
)
it_dept.click()


# Step 6 – Click Time tables
time_tables = wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Time tables"))
)
time_tables.click()


# Step 7 – Click D3 IT A
section = wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT, "D3 IT A"))
)
section.click()


# keep browser open
input("Press Enter to close browser...")
driver.quit()