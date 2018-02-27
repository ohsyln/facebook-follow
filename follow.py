from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import re

PROFILE_NAME = "profile_name_here"
EMAIL = "your_email@example.com"
PASSW = "your_password"

def infiniteScroll(driver):
  SCROLL_PAUSE_TIME = 1
  last_height = driver.execute_script("return document.body.scrollHeight")

  while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
      break
    last_height = new_height

def login(driver):
  username = driver.find_element_by_id("email")
  password = driver.find_element_by_id("pass")
  username.send_keys(EMAIL)
  password.send_keys(PASSW)
  driver.find_element_by_id("loginbutton").click()

def getAllUserLinks(driver):
  links = driver.find_elements_by_xpath("//a[@href]")
  PATTERN = "^https://www\.facebook\.com/.*friends_tab$"
  lst = list(filter(lambda x : re.search(PATTERN,x.get_attribute('href')), links))
  del lst[1::2]
  return lst

def followFriend(driver, friend):
  # open friend in new tab
  actions = ActionChains(driver)
  actions.key_down(Keys.COMMAND).click(friend).key_up(Keys.COMMAND).perform()
  driver.switch_to.window(driver.window_handles[1])

  # find follow link and click
  if isFollowPresent(driver):
    driver.find_element_by_link_text("Follow").click()

  # close tab, return back to friend list
  driver.close()
  driver.switch_to.window(driver.window_handles[0])

def isFollowPresent(driver):
  try:
    driver.find_element_by_link_text("Follow")
  except NoSuchElementException:
    return False
  else:
    return True

def main(): 
  # disables retarded Chrome notifications
  chrome_options = Options()
  chrome_options.add_argument("--disable-notifications")

  # create a new Chrome session
  driver = webdriver.Chrome(chrome_options=chrome_options)
  driver.implicitly_wait(30)

  # login to facebook
  MAIN_URL = "https://www.facebook.com"
  driver.get(MAIN_URL)
  login(driver)

  # navigate to Friends
  FRIEND_URL = "https://www.facebook.com/" + PROFILE_NAME + "/friends"
  driver.get(FRIEND_URL)

  infiniteScroll(driver)

  # follow each friend
  friends = getAllUserLinks(driver)
  for friend in friends:
    followFriend(driver, friend)

  # close the browser window
  driver.quit()

# run main()
main()
