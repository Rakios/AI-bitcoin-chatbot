from rasa_core.channels.facebook import FacebookInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import os
from rasa_core.utils import EndpointConfig

# load your trained agent
interpreter = RasaNLUInterpreter("models/nlu/default/bot/")
MODEL_PATH = "models/dialog"
action_endpoint = EndpointConfig(url="https://bitcoin25bot.herokuapp.com/webhook")
agent = Agent.load(MODEL_PATH, interpreter=interpreter)

input_channel = FacebookInput(
        fb_verify="prueba-bot",
        # you need tell facebook this token, to confirm your URL
        fb_secret="0fc4285c08b36c07113b15be9abceefa", # your app secret
        fb_access_token="EAACthrdIUVUBANAz997eKP654fiZC6h99IFiksQmtIPUrkr0Eh5glkLCvh14oAnzAGx6AtOq1MZB3ZBVDztnjwkLE7OdGjoBrbGHLJs4S4RJIXv8pABc1ONSsi2ZCrS5K2ZAM2a0pFTBdNSkMZA8WwZBntSKbVaSTV67pBUtE17ZBwZDZD"
        # token for the page you subscribed to
)
# set serve_forever=False if you want to keep the server running
s = agent.handle_channels([input_channel], int(os.environ.get('PORT',5004)), serve_forever=True)