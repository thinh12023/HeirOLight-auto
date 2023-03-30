

from common import EVENT, GAME_RESOUCES, MAX_RESOURCES, OCR_READER, REPEAT_BATTLE
from typing import List, Tuple

from get_image import get_image_from_app
from global_variables import global_state
from handle_movements import click, handle_move_after_end_repeat_battle

#*********************************************************************************************

def get_middle_position(coords: List[Tuple[List[int], str, float]]):
    x_values = [c[0] for c in coords]  # get all x values
    y_values = [c[1] for c in coords]  # get all y values
    middle_x = sum(x_values) / len(x_values)  # calculate the average of x values
    middle_y = sum(y_values) / len(y_values)  # calculate the average of y values
    middle_coords = [middle_x, middle_y]
    return middle_coords

#*********************************************************************************************

def resolve_game_resources(txt, temp_resources):
    values = txt.split('/')  # get the part after the '/' character

    if len(values) != 2:
        return temp_resources

    tmp_mx_res = values[1].split(" ")[0]
    current_res = values[0]

    if tmp_mx_res not in MAX_RESOURCES:
        return temp_resources

    mx_res = MAX_RESOURCES[tmp_mx_res].value
    temp_resources[mx_res] = int(current_res)

    return temp_resources

#*********************************************************************************************

def resolve_purify(temp_resources, coords):
    tmp_complete_char = []

    purify_complete_char_val = GAME_RESOUCES.PURIFY_COMPLETE_CHAR.value
    if purify_complete_char_val in temp_resources:
        tmp_complete_char = temp_resources[purify_complete_char_val]
        
    tmp_complete_char.append(get_middle_position(coords))

    temp_resources[purify_complete_char_val] = tmp_complete_char

    return temp_resources

#*********************************************************************************************

def resolve_confirm_btn(coords):
    middle_pos = get_middle_position(coords)
    click(middle_pos[0], middle_pos[1])

#*********************************************************************************************

def handle_network_error(temp_resources, txt, coords):
    if "Unable to find the network" in txt:
        temp_resources["network_error"] = True

    if "network_error" in temp_resources and ("Confirm" in txt or "Retry" in txt):
        global_state["in_battle"] = False
        resolve_confirm_btn(coords)
        raise Exception("Network error")
    return temp_resources

#*********************************************************************************************

def handle_end_repeat_battle(temp_resources, txt, coords):
    if "Repeat Battle count has reached 0" in txt:
        temp_resources["end_repeat_battle"] = True
        
    if "end_repeat_battle" in temp_resources and "Confirm" in txt:
        global_state["in_battle"] = False
        resolve_confirm_btn(coords)
        handle_move_after_end_repeat_battle()

    return temp_resources


#*********************************************************************************************

def get_curr_resouces_value():
    get_image_from_app()
    result = OCR_READER.readtext('screenshot.png')

    temp_resources = {} 

    for coords, txt, score in result:
        #Handle network errors
        temp_resources = handle_network_error(temp_resources, txt, coords)
        
        #Handle end repeat battle
        temp_resources = handle_end_repeat_battle(temp_resources, txt, coords)
        
        # Get energy, valor, ticket
        if '/' in txt:
            temp_resources = resolve_game_resources(txt, temp_resources)
        # Handle purify
        if "Complete" in txt:
            temp_resources[GAME_RESOUCES.PURIFY_COMPLETE.value] = get_middle_position(coords)
        if "150/150" in txt:
            temp_resources[GAME_RESOUCES.PURIFY_COORDS.value] = resolve_purify(temp_resources, coords)
        if"Event" in txt:
            temp_resources[EVENT.EVENT_BTN.value] = get_middle_position(coords)

        
    return temp_resources