#!/usr/bin/env python

###################
# IMPORTS
###################

import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from formatted_output import *
import json


options = Options()
options.add_argument("window-size=700,700")
driver = webdriver.Chrome(options=options)

driver.get("https://diep.io")

p_instruct("Please navigate to http://diep.io and begin a sandbox session.")
p_warn("DO NOT RESIZE THE WINDOW.")
akc()

js="""
let _rScore = "0";
CanvasRenderingContext2D.prototype.fillText = new Proxy(CanvasRenderingContext2D.prototype.fillText, {
    apply(fillRect, ctx, [text, x, y, ...blah]) {

        if (text.startsWith('Score: ')) _rScore = text

        alert(_rScore)

        fillRect.call(ctx, text, x, y, ...blah);
    }
})
"""
driver.execute_script(js)

akc()

driver.quit()