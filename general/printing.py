import datetime
import inspect
import os

from colorama import Fore, Style, init

init(autoreset=True)


def debugPrint(anyString: str, colorCode: int = -1):
    """
    Custom printing function to keep the formatting the same everywhere

    # Args:
        - anyString: String to be printed.
        - colorCode: Optional, changes the color.

    # ColorCodes:
        - `1` =  Red
        - `2` =  Blue
        - `3` =  Green
        - `4` =  Magenta
        - `5` =  Black
    """
    defaultColor = ["", ""]
    format = {
        1: [Fore.RED, Fore.LIGHTRED_EX],
        2: [Fore.BLUE, Fore.LIGHTBLUE_EX],
        3: [Fore.GREEN, Fore.LIGHTGREEN_EX],
        4: [Fore.MAGENTA, Fore.LIGHTMAGENTA_EX],
        5: [Fore.BLACK, Fore.LIGHTBLACK_EX],
    }
    fetchedFormat = format.get(colorCode, defaultColor)

    logTime: datetime.datetime = datetime.datetime.now()

    # INFO: Gets the path of the file running this function externally.
    callerPath = inspect.currentframe().f_back.f_code.co_filename  # type: ignore
    fileName: str = os.path.splitext(os.path.basename(callerPath))[0].upper()

    print(
        "{col1}[{time}]{colReset} {col2}[{name}]{colReset} >> {msg}".format(
            col1=fetchedFormat[0],
            col2=fetchedFormat[1],
            time=logTime,
            name=fileName,
            msg=anyString,
            colReset=Style.RESET_ALL,
        )
    )
