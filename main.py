from src.gui.login.form_login import App
from src.gui.master.form_master import MasterPanel
from src.persistence.conect import Conectar

if __name__ == "__main__":
    #App()
    Conectar()
    MasterPanel(usu="Gregory")
