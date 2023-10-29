#!/usr/bin/env python

###################
# IMPORTS
###################

import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from formatted_output import *


options = Options()
options.add_argument("window-size=700,700")
driver = webdriver.Chrome(options=options)

driver.get("https://google.com")

p_instruct("Please navigate to http://diep.io and begin a sandbox session.")
p_warn("DO NOT RESIZE THE WINDOW.")
akc()

driver.quit()