
from intelhex import IntelHex

ih = IntelHex()   
ih.loadhex("./data/test.hex") 
dic=ih.todict()