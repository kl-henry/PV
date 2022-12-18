from admin_anrede import Ui_adminAnrede
from admin_potd import Ui_admPOTD

class PV_Menu_calls(object):
    
    @staticmethod
    def admin_potd():
        DiaadmPOTD = Ui_admPOTD()
        DiaadmPOTD.setupUi(DiaadmPOTD)
        DiaadmPOTD.show()
    
    @staticmethod
    def admin_anrede():
        DiaadmAnrede = Ui_adminAnrede()
        DiaadmAnrede.setupUi(DiaadmAnrede)
        DiaadmAnrede.show()
