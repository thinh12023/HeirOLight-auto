from dotenv import load_dotenv
load_dotenv()

import os
import time
from global_variables import global_state

from handle_paricipate_event import handle_participate_event
from handle_purify import handle_purify
from loop_energy_fight import fight_ene
from common import ADB_PATH, ANDROID_PORT
from handle_movements import move_to_dungeon


os.system(f"{ADB_PATH} connect 127.0.0.1:{ANDROID_PORT}")
loop_active = True


while True:
    try:
        print("********************** Start Loop **********************")
        if not loop_active:
            continue

        print(f"Is in Battle {global_state['in_battle']}")

        if not global_state["in_battle"]:
            handle_purify()

            time.sleep(2)
            
            # change logic when change mobs
            move_to_dungeon()

            fight_ene()

        handle_participate_event()

        print("********************** End Loop **********************")
            
    except:
        print("An exception occurred Hehehe")

    # time in seconds
    time.sleep(60)
