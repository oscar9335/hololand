import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()


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

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
                
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
        #print(events)
    except InvalidSignatureError:
        abort(400)


    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")

        response = machine.advance(event)

        if response == False:
            send_text_message(event.reply_token, "Enter home or press the button for help ")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
