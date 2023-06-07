
import unittest
from modules import manzana
from modules import kiwi
from modules import papa
from modules import zanahoria
from modules import fruta
from modules import verdura
from modules import alimento


class TestAlimento(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_Alimento(self):
        test_manzana=manzana.Manzana.aw_prom_manzana(100)
        test_kiwi=kiwi.Kiwi.aw_prom_kiwi(100)
        test_papa=papa.Papa.aw_prom_papa(100)
        test_zanahoria=zanahoria.Zanahoria.aw_prom_zanahoria(100)

        test_fruta=fruta.Fruta.aw_prom_frutas(test_manzana,test_kiwi)
        test_verdura=verdura.Verdura.aw_prom_verduras(test_papa,test_zanahoria)
        test_alimento=alimento.Alimento.aw_prom_total(test_manzana,test_kiwi,test_papa,test_zanahoria)

    
if __name__ == '__main__':
    unittest.main()