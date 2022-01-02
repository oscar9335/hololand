from fsm import TocMachine

machine = TocMachine(
    states=["user", "home", "fsm","information","peko","menu","search","recommand","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "home",
            "conditions": "is_going_to_home",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "fsm",
            "conditions": "is_going_to_fsm",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "information",
            "conditions": "is_going_to_information",
        },
        {
            "trigger": "advance",
            "source": "information",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        
        {
            "trigger": "advance",
            "source": "information",
            "dest": "home",
            "conditions": "is_going_to_home",
        },
        {
            "trigger": "advance",
            "source": "information",
            "dest": "peko",
            "conditions": "is_going_to_peko",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "search",
            "conditions": "is_going_to_search",
        },
        
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "recommand",
            "conditions": "is_going_to_recommand",
        },
        
        {
            "trigger": "advance",
            "source": "search",
            "dest": "a",
            "conditions": "is_going_to_a",
        },
        {
            "trigger": "advance",
            "source": "search",
            "dest": "b",
            "conditions": "is_going_to_b",
        },
        {
            "trigger": "advance",
            "source": "b",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "b",
            "dest": "home",
            "conditions": "is_going_to_home",
        },
        {
            "trigger": "advance",
            "source": "search",
            "dest": "c",
            "conditions": "is_going_to_c",
        },
        {
            "trigger": "advance",
            "source": "search",
            "dest": "d",
            "conditions": "is_going_to_d",
        },
        {
            "trigger": "advance",
            "source": "d",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "d",
            "dest": "home",
            "conditions": "is_going_to_home",
        },
        {
            "trigger": "advance",
            "source": "search",
            "dest": "e",
            "conditions": "is_going_to_e",
        },
        {
            "trigger": "advance",
            "source": "e",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "e",
            "dest": "home",
            "conditions": "is_going_to_home",
        },
        {
            "trigger": "advance",
            "source": "search",
            "dest": "f",
            "conditions": "is_going_to_f",
        },
        {
            "trigger": "advance",
            "source": "f",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "f",
            "dest": "home",
            "conditions": "is_going_to_home",
        },
        {
            "trigger": "advance",
            "source": "search",
            "dest": "g",
            "conditions": "is_going_to_g",
        },
        {
            "trigger": "advance",
            "source": "search",
            "dest": "h",
            "conditions": "is_going_to_h",
        },
        {
            "trigger": "advance",
            "source": "search",
            "dest": "i",
            "conditions": "is_going_to_i",
        },
        {
            "trigger": "advance",
            "source": "search",
            "dest": "j",
            "conditions": "is_going_to_j",
        },
        {
            "trigger": "advance",
            "source": "j",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "j",
            "dest": "home",
            "conditions": "is_going_to_home",
        },
        {
            "trigger": "advance",
            "source": "search",
            "dest": "k",
            "conditions": "is_going_to_k",
        },
        {
            "trigger": "advance",
            "source": "search",
            "dest": "l",
            "conditions": "is_going_to_l",
        },
        {
            "trigger": "advance",
            "source": "search",
            "dest": "m",
            "conditions": "is_going_to_m",
        },
        {
            "trigger": "advance",
            "source": "search",
            "dest": "n",
            "conditions": "is_going_to_n",
        },
        {
            "trigger": "advance",
            "source": "search",
            "dest": "o",
            "conditions": "is_going_to_o",
        },
        {
            "trigger": "advance",
            "source": "search",
            "dest": "p",
            "conditions": "is_going_to_p",
        },
        {
            "trigger": "advance",
            "source": "search",
            "dest": "q",
            "conditions": "is_going_to_q",
        },
        {
            "trigger": "advance",
            "source": "q",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "q",
            "dest": "home",
            "conditions": "is_going_to_home",
        },
        {
            "trigger": "advance",
            "source": "search",
            "dest": "r",
            "conditions": "is_going_to_r",
        },
        {
            "trigger": "advance",
            "source": "search",
            "dest": "s",
            "conditions": "is_going_to_s",
        },
        {
            "trigger": "advance",
            "source": "search",
            "dest": "t",
            "conditions": "is_going_to_t",
        },
        {
            "trigger": "advance",
            "source": "search",
            "dest": "u",
            "conditions": "is_going_to_u",
        },
        {
            "trigger": "advance",
            "source": "search",
            "dest": "v",
            "conditions": "is_going_to_v",
        },
        {
            "trigger": "advance",
            "source": "v",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "v",
            "dest": "home",
            "conditions": "is_going_to_home",
        },
        {
            "trigger": "advance",
            "source": "search",
            "dest": "w",
            "conditions": "is_going_to_w",
        },
        {
            "trigger": "advance",
            "source": "search",
            "dest": "x",
            "conditions": "is_going_to_x",
        },
        {
            "trigger": "advance",
            "source": "x",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "x",
            "dest": "home",
            "conditions": "is_going_to_home",
        },
        {
            "trigger": "advance",
            "source": "search",
            "dest": "y",
            "conditions": "is_going_to_y",
        },
        {
            "trigger": "advance",
            "source": "search",
            "dest": "z",
            "conditions": "is_going_to_z",
        },
        {
            "trigger": "advance",
            "source": "z",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "z",
            "dest": "home",
            "conditions": "is_going_to_home",
        },
        {"trigger": "go_back", "source": ["home","fsm","peko","recommand","a","c","g","h","i","k","l","m","n","o","p","r","s","t","u","w","y"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)
machine.get_graph().draw("fsm.png", prog="dot", format="png")
