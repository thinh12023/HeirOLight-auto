import os
import easyocr
from enum import Enum

OCR_READER = easyocr.Reader(['en'], gpu=True)

#for bluestack only
def get_android_port() -> int:
    with open('D:\\BlueStacks_nxt\\bluestacks.conf', 'r') as file:
        contents = file.read()

        for txt in contents.split("\n"):
            if "bst.instance.Pie64.status.adb_port" in txt:
                return int(txt.split("=")[-1][1:-1])
            

ANDROID_PORT= get_android_port()

# Get Env
ADB_PATH = os.getenv('ADB_PATH')
ANDROID_CONFIG_PATH = os.getenv('ANDROID_CONFIG_PATH')
PACKAGE_NAME = os.getenv('PACKAGE_NAME')
ENERGY_TO_FIGHT = int(os.getenv('ENERGY_TO_FIGHT'))

class MENU(Enum):
    MENU = (1555,35)
    WORLD_MAP = (1485,110)

class GAME_RESOUCES(Enum):
    #basic resouces
    VALOR = "valor"
    ENERGY= "energy"
    TICKET= "ticket"

    #purify
    PURIFY_COORDS = "purify_coords"
    PURIFY_COMPLETE = "purify_complete"
    PURIFY_COMPLETE_CHAR = "purify_complete_char"

class EVENT(Enum):
    EVENT_BTN = 'event_btn'
    WATER_ARIA = (1500,590)
    REPEAT_BATTLE_BTN = (1245,815)
    START_REPEAT_BTN = (800,820)

class REPEAT_BATTLE(Enum):
    END_CONFIRM_BTN = (800,750)
    WORLD_MAP_BTN = (1182,768)


MAX_RESOURCES = {
    "880": GAME_RESOUCES["VALOR"],
    "120": GAME_RESOUCES["ENERGY"],
    "20": GAME_RESOUCES["TICKET"]
}

MILDRED_ENE_REPEAT = {
    "world_map": (583,672),
    "entrance": (1481,460),
}

ENE_SKIP_FIGHT = {
    "skip_btn": (1473,818),
    "sell_items_btn": (485,370), 
    "start_skip":(805,825),
    "confirm": (800,750),
    "close_skip_options_btn": (1175,56)
}


WORLD_MAP_CORS = {
    "awake_dungeon": (1338,791),
    "gear_dungeon": (1194,791),
    "raid" :(1037, 787),
    "purifying_ground": (891,791),
    "infinity_pvp": (1511,483)
}

class PURIFYING_GROUND(Enum):
    start_purify = (1080,650)
    confirm_start = (625,565)
    confirm_complete = (800, 690)



# PURIFYING_GROUND = {
#     "servant_1": (372,665),
#     "servant_2": (946,621),
#     "start_stop": (1048,648),
#     "confirm_start_stop": (625,567),
#     "confirm_complete": (800, 690),
# }


GEAR_DUNGEON = {
    "drag_15f": (1213,586,1222,770),
}


back_from = {
    "purifying_ground": (45,41)
}
