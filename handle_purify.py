

import time
from handle_current_resources import get_curr_resouces_value
from handle_movements import click, return_to_world_map, return_to_world_map_with_opened_menu
from common import GAME_RESOUCES, MENU, PURIFYING_GROUND

#*********************************************************************************************

def handle_loop_purifying(char):
    char_coords = (char[0] - 70, char[1] - 150)

    click(char_coords[0], char_coords[1])
    time.sleep(1.5)

    tmp_confirm_complete = PURIFYING_GROUND.confirm_complete.value
    click(tmp_confirm_complete[0], tmp_confirm_complete[1])
    time.sleep(1)
    print("purify completed, start purify again")

    click(char_coords[0], char_coords[1])
    time.sleep(1)

    tmp_start_purify = PURIFYING_GROUND.start_purify.value
    click(tmp_start_purify[0], tmp_start_purify[1])
    time.sleep(1)

    tmp_confirm_purify = PURIFYING_GROUND.confirm_start.value
    click(tmp_confirm_purify[0], tmp_confirm_purify[1])

    time.sleep(1)

#*********************************************************************************************

def handle_purify():

    #Open menu
    menu = MENU.MENU.value
    click(menu[0], menu[1])

    time.sleep(0.5)

    res = get_curr_resouces_value()
    
    purify_enum = GAME_RESOUCES.PURIFY_COMPLETE.value
    if purify_enum not in res:
        return return_to_world_map_with_opened_menu()
    
    click(res[purify_enum][0], res[purify_enum][1])

    time.sleep(3)

    res = get_curr_resouces_value()

    purify_comp_char = GAME_RESOUCES.PURIFY_COMPLETE_CHAR.value
    if purify_comp_char not in res:
        return return_to_world_map_with_opened_menu()
    
    for char in res[purify_comp_char]:
        handle_loop_purifying(char)
    
    return return_to_world_map()