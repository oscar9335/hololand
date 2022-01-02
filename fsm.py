from transitions.extensions import GraphMachine

from utils import send_text_message, send_image_url, send_flex_message , send_video_url
from layout import flex_msg_menu,a_recommand,c_recommand,g_recommand,h_recommand,i_recommand,k_recommand,l_recommand,m_recommand,n_recommand,o_recommand,p_recommand,r_recommand,s_recommand,t_recommand,u_recommand,w_recommand,y_recommand,notfound,info,gura,pekora,miko,noel,nene
import random

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_home(self, event):
        text = event.message.text
        return text.lower() == "home"

    def is_going_to_fsm(self, event):
        text = event.message.text
        return text.lower() == "fsm"
    
    def is_going_to_information(self, event):
        text = event.message.text
        return text.lower() == "what is this"
    
    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "menu"

    #def is_going_to_all(self, event):
        #text = event.message.text
        #return text.lower() == "all"

    def is_going_to_peko(self, event):
        text = event.message.text
        return text.lower() == "peko"

    def is_going_to_search(self, event):
        text = event.message.text
        return text.lower() == "search"

    def is_going_to_recommand(self, event):
        text = event.message.text
        return text.lower() == "recommand"

    def is_going_to_a(self, event):
        text = event.message.text
        return text.lower() == "a"
    
    def is_going_to_b(self, event):
        text = event.message.text
        return text.lower() == "b" 

    def is_going_to_c(self, event):
        text = event.message.text
        return text.lower() == "c"

    def is_going_to_d(self, event):
        text = event.message.text
        return text.lower() == "d"
    
    def is_going_to_e(self, event):
        text = event.message.text
        return text.lower() == "e"
    
    def is_going_to_f(self, event):
        text = event.message.text
        return text.lower() == "f"

    def is_going_to_g(self, event):
        text = event.message.text
        return text.lower() == "g"

    def is_going_to_h(self, event):
        text = event.message.text
        return text.lower() == "h"

    def is_going_to_i(self, event):
        text = event.message.text
        return text.lower() == "i"

    def is_going_to_j(self, event):
        text = event.message.text
        return text.lower() == "j"

    def is_going_to_k(self, event):
        text = event.message.text
        return text.lower() == "k"

    def is_going_to_l(self, event):
        text = event.message.text
        return text.lower() == "l"

    def is_going_to_m(self, event):
        text = event.message.text
        return text.lower() == "m"

    def is_going_to_n(self, event):
        text = event.message.text
        return text.lower() == "n"

    def is_going_to_o(self, event):
        text = event.message.text
        return text.lower() == "o"

    def is_going_to_p(self, event):
        text = event.message.text
        return text.lower() == "p"

    def is_going_to_q(self, event):
        text = event.message.text
        return text.lower() == "q"

    def is_going_to_f(self, event):
        text = event.message.text
        return text.lower() == "r"
    
    def is_going_to_s(self, event):
        text = event.message.text
        return text.lower() == "s"

    def is_going_to_t(self, event):
        text = event.message.text
        return text.lower() == "t"

    def is_going_to_u(self, event):
        text = event.message.text
        return text.lower() == "u"

    def is_going_to_v(self, event):
        text = event.message.text
        return text.lower() == "v"

    def is_going_to_w(self, event):
        text = event.message.text
        return text.lower() == "w"

    def is_going_to_x(self, event):
        text = event.message.text
        return text.lower() == "x"

    def is_going_to_y(self, event):
        text = event.message.text
        return text.lower() == "y"

    def is_going_to_z(self, event):
        text = event.message.text
        return text.lower() == "z"

    
    #Home
    def on_enter_home(self, event):
        print("I'm entering home")
        reply_token = event.reply_token
        send_text_message(reply_token, "enter : [what is this] for information or [menu] for next step")
        self.go_back()

    def on_exit_home(self):
        print("Leaving home")

    #information
    def on_enter_information(self, event):
        print("I'm entering information")
        reply_token = event.reply_token
        flex_msg = info
        send_flex_message(reply_token, flex_msg)

    #menu
    def on_enter_menu(self, event):
        reply_token = event.reply_token
        flex_msg = flex_msg_menu
        send_flex_message(reply_token, flex_msg)

    #all
    #def on_enter_all(self, event):
        #self.go_back()


    #peko
    def on_enter_peko(self, event):
        reply_token = event.reply_token
        send_video_url(reply_token, "https://i.imgur.com/IHd1HQ5.mp4")
        self.go_back()
        
    def on_exit_peko(self):
        print("Leaving peko")
    

    #search
    def on_enter_search(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "Enter a character")

    #recommand
    def on_enter_recommand(self, event):
        reply_token = event.reply_token

        a = random.randint(1,5)
        print(a)
        if a == 1:
            print("enter 1")
            flex_msg = gura
            send_flex_message(reply_token, flex_msg)
        elif a == 2:
            print("enter 2")
            flex_msg = miko
            send_flex_message(reply_token, flex_msg)
        elif a == 3:
            print("enter 3")
            flex_msg = pekora
            send_flex_message(reply_token, flex_msg)
        elif a == 4:
            print("enter 4")
            flex_msg = noel
            send_flex_message(reply_token, flex_msg)
        elif a == 5:
            print("enter 5")
            flex_msg = nene
            send_flex_message(reply_token, flex_msg)

        self.go_back()

    def on_exit_recommand(self):
        print("Leaving recommand")
        

    #a
    def on_enter_a(self, event):
        reply_token = event.reply_token
        flex_msg = a_recommand
        send_flex_message(reply_token, flex_msg)
        self.go_back()
        
    def on_exit_a(self):
        print("Leaving a")

    #b
    def on_enter_b(self, event):
        reply_token = event.reply_token
        flex_msg = notfound
        send_flex_message(reply_token, flex_msg)
        

     #c
    def on_enter_c(self, event):
        reply_token = event.reply_token
        flex_msg = c_recommand
        send_flex_message(reply_token, flex_msg)
        self.go_back()
        
    def on_exit_c(self):
        print("Leaving c")


    #d
    def on_enter_d(self, event):
        reply_token = event.reply_token
        flex_msg = notfound
        send_flex_message(reply_token, flex_msg)

    #e
    def on_enter_e(self, event):
        reply_token = event.reply_token
        flex_msg = notfound
        send_flex_message(reply_token, flex_msg)

    #f
    def on_enter_f(self, event):
        reply_token = event.reply_token
        flex_msg = notfound
        send_flex_message(reply_token, flex_msg)

    #g
    def on_enter_g(self, event):
        reply_token = event.reply_token
        flex_msg = g_recommand
        send_flex_message(reply_token, flex_msg)
        self.go_back()
        
    def on_exit_g(self):
        print("Leaving g")

    #h
    def on_enter_h(self, event):
        reply_token = event.reply_token
        flex_msg = h_recommand
        send_flex_message(reply_token, flex_msg)
        self.go_back()
        
    def on_exit_h(self):
        print("Leaving h")
    
    #i
    def on_enter_i(self, event):
        reply_token = event.reply_token
        flex_msg = i_recommand
        send_flex_message(reply_token, flex_msg)
        self.go_back()
        
    def on_exit_i(self):
        print("Leaving i")

    #j
    def on_enter_j(self, event):
        reply_token = event.reply_token
        flex_msg = notfound
        send_flex_message(reply_token, flex_msg)

    #k
    def on_enter_k(self, event):
        reply_token = event.reply_token
        flex_msg = k_recommand
        send_flex_message(reply_token, flex_msg)
        self.go_back()
        
    def on_exit_k(self):
        print("Leaving k")

    #l
    def on_enter_l(self, event):
        reply_token = event.reply_token
        flex_msg = l_recommand
        send_flex_message(reply_token, flex_msg)
        self.go_back()
        
    def on_exit_l(self):
        print("Leaving l")

    #m
    def on_enter_m(self, event):
        reply_token = event.reply_token
        flex_msg = m_recommand
        send_flex_message(reply_token, flex_msg)
        self.go_back()
        
    def on_exit_m(self):
        print("Leaving i")

    #n
    def on_enter_n(self, event):
        reply_token = event.reply_token
        flex_msg = n_recommand
        send_flex_message(reply_token, flex_msg)
        self.go_back()
        
    def on_exit_n(self):
        print("Leaving i")

    #o
    def on_enter_o(self, event):
        reply_token = event.reply_token
        flex_msg = o_recommand
        send_flex_message(reply_token, flex_msg)
        self.go_back()
        
    def on_exit_o(self):
        print("Leaving o")

    #p
    def on_enter_p(self, event):
        reply_token = event.reply_token
        flex_msg = p_recommand
        send_flex_message(reply_token, flex_msg)
        self.go_back()
        
    def on_exit_p(self):
        print("Leaving p")

    
    #q
    def on_enter_q(self, event):
        reply_token = event.reply_token
        flex_msg = notfound
        send_flex_message(reply_token, flex_msg)

    #r
    def on_enter_r(self, event):
        reply_token = event.reply_token
        flex_msg = r_recommand
        send_flex_message(reply_token, flex_msg)
        self.go_back()
        
    def on_exit_r(self):
        print("Leaving r")

    #s
    def on_enter_s(self, event):
        reply_token = event.reply_token
        flex_msg = s_recommand
        send_flex_message(reply_token, flex_msg)
        self.go_back()
        
    def on_exit_s(self):
        print("Leaving s")

    #t
    def on_enter_t(self, event):
        reply_token = event.reply_token
        flex_msg = t_recommand
        send_flex_message(reply_token, flex_msg)
        self.go_back()
        
    def on_exit_t(self):
        print("Leaving t")

    #u
    def on_enter_u(self, event):
        reply_token = event.reply_token
        flex_msg = u_recommand
        send_flex_message(reply_token, flex_msg)
        self.go_back()
        
    def on_exit_u(self):
        print("Leaving u")

    #v
    def on_enter_v(self, event):
        reply_token = event.reply_token
        flex_msg = notfound
        send_flex_message(reply_token, flex_msg)

    #w
    def on_enter_w(self, event):
        reply_token = event.reply_token
        flex_msg = w_recommand
        send_flex_message(reply_token, flex_msg)
        self.go_back()
        
    def on_exit_w(self):
        print("Leaving w")

    #x
    def on_enter_x(self, event):
        reply_token = event.reply_token
        flex_msg = notfound
        send_flex_message(reply_token, flex_msg)

    #y
    def on_enter_y(self, event):
        reply_token = event.reply_token
        flex_msg = y_recommand
        send_flex_message(reply_token, flex_msg)
        self.go_back()
        
    def on_exit_y(self):
        print("Leaving y")
    
    #z
    def on_enter_z(self, event):
        reply_token = event.reply_token
        flex_msg = notfound
        send_flex_message(reply_token, flex_msg)


    #fsm
    def on_enter_fsm(self, event):
        print("I'm entering FSM")
        reply_token = event.reply_token
        send_image_url(reply_token, "https://i.imgur.com/mEpGsr3.png")
        #send_text_message(reply_token, "Trigger FSM")
        self.go_back()

    def on_exit_fsm(self):
        print("Leaving FSM")
