#!/usr/bin/env python

###################
# IMPORTS
###################

import json
import time

###################
# LOCAL IMPORTS
###################

from formatted_output import *
from input_simulation import *

###################
# CODE
###################

p_warn("This script will take control of your mouse and keyboard occasionally.")
enter_to_continue()

p_instruct("Please open a chrome browser window and navigate to http://diep.io/ and then complete the following steps:")
p_instruct("1. Complete the captcha.")
p_instruct("2. Begin a sandbox session.")
p_instruct("3. Enter a name and then enter the sandbox session.")
p_instruct("4. Make sure the browser window is fit to the screen.")
enter_to_continue()

p_instruct("After you press enter, you will have 5 seconds to click into the game window. After that, the bot will begin working.")
enter_to_continue()

time.sleep(5)

p_instruct("The bot will begin working. Please do not touch your mouse or keyboard.")

