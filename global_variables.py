from typing import TypedDict

class GlobalState(TypedDict):
    in_battle: bool
    ene_timer: int

global_state: GlobalState = {
    "in_battle": False,
    "ene_timer": 0
}