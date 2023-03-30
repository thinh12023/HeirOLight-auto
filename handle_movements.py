import os
import time
from common import ADB_PATH, ENE_SKIP_FIGHT, MENU, MILDRED_ENE_REPEAT, REPEAT_BATTLE

#*********************************************************************************************

def click(x,y):
    os.system(f"{ADB_PATH} shell input tap {x} {y}")
    return

#*********************************************************************************************

def move_to_dungeon():
    tmp = MILDRED_ENE_REPEAT["world_map"]
    click(tmp[0], tmp[1])

    time.sleep(0.5)

    tmp2 = MILDRED_ENE_REPEAT["entrance"]
    click(tmp2[0], tmp2[1])

    time.sleep(1)

#*********************************************************************************************

def return_to_world_map():
    # RETURN to worl map
    menu = MENU.MENU.value
    click(menu[0], menu[1])

    time.sleep(0.5)

    wm = MENU.WORLD_MAP.value
    click(wm[0], wm[1])

    time.sleep(3)

#*********************************************************************************************

def return_to_world_map_with_opened_menu():
    wm = MENU.WORLD_MAP.value
    click(wm[0], wm[1])

    time.sleep(3)

#*********************************************************************************************

def skip_and_check_sell_item():
    #skip btn
    skip_btn = ENE_SKIP_FIGHT['skip_btn']
    click(skip_btn[0], skip_btn[1])

    time.sleep(1)

    # Check sell item option
    sell_item_btn = ENE_SKIP_FIGHT["sell_items_btn"]
    click(sell_item_btn[0], sell_item_btn[1])

    time.sleep(1)

#*********************************************************************************************

def repeat_fight_w_ene_movement():
    skip_and_check_sell_item()

    #start skip btn
    start_skip = ENE_SKIP_FIGHT['start_skip']
    click(start_skip[0], start_skip[1])

    time.sleep(3)

    #confirm
    confirm = ENE_SKIP_FIGHT['confirm']
    click(confirm[0], confirm[1])

    time.sleep(1)

    skip_and_check_sell_item()

    time.sleep(1)

    #close skip option
    close_skip_btn = ENE_SKIP_FIGHT["close_skip_options_btn"]
    click(close_skip_btn[0],close_skip_btn[1])

    time.sleep(1)

#*********************************************************************************************

def handle_move_after_end_repeat_battle():
    end_confirm = REPEAT_BATTLE.END_CONFIRM_BTN.value
    click(end_confirm[0], end_confirm[1])

    time.sleep(1)

    world_map_btn = REPEAT_BATTLE.WORLD_MAP_BTN.value
    click(world_map_btn[0], world_map_btn[1])

    #ensure world map has done loading
    time.sleep(3)

#*********************************************************************************************

