import time
from common import EVENT
from handle_current_resources import get_curr_resouces_value
from handle_movements import click
from global_variables import global_state

#*********************************************************************************************

def handle_participate_event():
    res = get_curr_resouces_value()

    print("event_res", res)

    event_btn_enum = EVENT.EVENT_BTN.value
    if event_btn_enum not in res:
        return
    

    print("Set in battle")
    global_state["in_battle"] = True
    
    #enter event area
    click(res[event_btn_enum][0], res[event_btn_enum][1] - 60)

    time.sleep(1)

    #select mobs
    servant_coords = EVENT.WATER_ARIA.value
    click(servant_coords[0], servant_coords[1])

    time.sleep(1)

    #repeat battle btn
    repeat_battle_btn = EVENT.REPEAT_BATTLE_BTN.value
    click(repeat_battle_btn[0],repeat_battle_btn[1])

    time.sleep(1)

    #start repeat
    start_repeat_btn = EVENT.START_REPEAT_BTN.value
    click(start_repeat_btn[0], start_repeat_btn[1])