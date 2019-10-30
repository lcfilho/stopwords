import unittest
import stopwords
from os import path
import filecmp
from io import StringIO


class Test_stopword(unittest.TestCase):

    #verifica se o arquivo é criado 
    def test_stopword(self):              
        self.assertTrue(path.exists("/home/luisfilho/semantix/GITS/stopwords/s_stopwords.txt"))

    #verifica o conteudo se o conteudo dos arquivos são os mesmos
    def test_stopword_2(self):
        self.assertFalse(filecmp.cmp("/home/luisfilho/semantix/GITS/stopwords/s_stopwords.txt", "/home/luisfilho/semantix/GITS/stopwords/stopwords.txt"))
    
   
if __name__ == "__main__":
    unittest.main()