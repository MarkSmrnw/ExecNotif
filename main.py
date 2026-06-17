import time

import ui.tempUi as tempui
from general.printing import debugPrint

examplePrint = "Print example print example 123456789!"

debugPrint(examplePrint, 1)
debugPrint(examplePrint, 2)
debugPrint(examplePrint, 3)
debugPrint(examplePrint, 4)
debugPrint(examplePrint, 5)
tempui.startMainUi()

time.sleep(10)
