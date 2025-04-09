from service.input_service import do_tap, do_input_text
from dotenv import load_dotenv
import os

# -    load the .env file   -
load_dotenv()

# -     DEFINE THE MOCK DATA    -
MOCK_USR = os.getenv("MOCK_USER_NAME")
MOCK_PASWD = os.getenv("MOCK_PASSWORD")

""""

   

"""

def login():
    #click on red button
    do_tap(724, 206)
    # type accont
    do_input_text(MOCK_USR)
    # type continue
    do_tap(733, 204)
    # click input password
    do_tap(724, 780)
    # type password
    do_input_text(MOCK_PASWD)
    # click continue button
    do_tap(721, 2230)


