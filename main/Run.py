__author__ = 'rakshith'

import os
import re
def run():

    #files = [f for f in os.listdir('.')]
    files = [f for f in os.listdir('.') if re.match('.*\.metis', f)]
    for file in files:
        for c in [100, 250, 500, 750, 1000]:
            for b in [0.3, 0.4, 0.5, 0.6, 0.7]:
                for i in [2, 2.5, 3]:
                    os.system("/home/6/chakraba/local/bin/mlrmcl -c "+ str(c) +" -b "+ str(b) +" -i "+ str(i) +" ./"+file)

    files = [f for f in os.listdir('.') if re.match('.*\.metis', f)]
    for file in files:
        for c in [100, 250, 500, 750, 1000]:
            os.system("/home/6/chakraba/local/bin/gpmetis "+ str(c) +" ./"+file)


    files = [f for f in os.listdir('.') if re.match('.*\.txt', f)]
    for file in files:
        os.system("/home/6/chakraba/local/bin/community -i:"+file+" -o:"+file+"_out")

run()