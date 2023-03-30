from common import ENERGY_TO_FIGHT, GAME_RESOUCES
from handle_current_resources import get_curr_resouces_value
from handle_movements import repeat_fight_w_ene_movement, return_to_world_map
import time
from global_variables import global_state

#*********************************************************************************************

def handle_repeat_fight_with_energy(energy_to_fight: int):
    curr_res = get_curr_resouces_value()

    if curr_res == False:
        return -1
    
    res_energy = GAME_RESOUCES.ENERGY.value
    if res_energy not in  curr_res:
        return -1
    
    energy = curr_res[res_energy]

    if(energy < energy_to_fight): 
        print(f"Not enough energy: {energy}")
        return energy

    repeat_fight_w_ene_movement()
    
    remain_ene = energy - energy_to_fight
    print(f"Fight success, remain energy: {remain_ene}")
    return remain_ene

#*********************************************************************************************

def fight_ene():
    # optimize to reduce call to the OCR
    time_until_fight = int(time.time()) - global_state["ene_timer"]
    if(time_until_fight < 0):
        print(f"Time until fight with ene: {time_until_fight} seconds")
        return return_to_world_map()

    energy_left = handle_repeat_fight_with_energy(ENERGY_TO_FIGHT)
    if energy_left < 0:
        return return_to_world_map()
    
    ene_condition = ENERGY_TO_FIGHT - energy_left
    if ene_condition > 0:
        global_state["ene_timer"] = int(time.time()) + (ene_condition*60)
    
    return return_to_world_map()
    
