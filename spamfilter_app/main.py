from pygame_app.application import Application
from model.model_manager import ModelManager
from model.model import LM

model = ModelManager()
app = Application(model)
app.start()