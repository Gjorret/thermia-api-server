from ThermiaOnlineAPI import Thermia
from src.credentials import USERNAME, PASSWORD

thermia = None


def init_thermia():
    global thermia
    if thermia is None:
        thermia = Thermia(USERNAME, PASSWORD)


def reauthenticate():
    global thermia
    thermia = Thermia(USERNAME, PASSWORD)


def get_heat_pumps():
    init_thermia()
    return thermia.fetch_heat_pumps()
