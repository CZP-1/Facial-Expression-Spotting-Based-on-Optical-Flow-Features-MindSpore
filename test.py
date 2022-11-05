import os
import samm_util as SAMM
import cas_util as CAS
from time import *
import pandas as pd

def detect_expression(path,name,fps):
    fileList = os.listdir(path)
    print(fileList)
    data = pd.DataFrame(columns=["vid","pred_onset","pred_offset","type"])
    j=0
    iou = 0.5
    for vio in fileList:
            if name == "samm":
                pp = SAMM.draw_roiline19(path , vio , 6, -4,7)  
                pp=pp*7
            elif name == "cas":
                pp = CAS.draw_roiline19(path , vio , 0, -4,1)
            pp = pp.tolist()
            pp.sort()
            print(pp)
            for i,interval in enumerate(pp):
                data.loc[i+j,'vid'] = vio
                data.loc[i+j,'pred_onset'] = interval[0]
                data.loc[i+j,'pred_offset'] = interval[1]
                if (interval[1]-interval[0])/fps > iou:
                    data.loc[i+j,'type'] = 'mae'
                else:
                    data.loc[i+j,'type'] = 'me'
            j=i+j+1
    data.to_csv(name+'_pred'+".csv",index=False)

def main():
    path_samm = "/home/data2/CZP/2022MEGC-SPOT/MEGC2022_testSet/SAMM_Test_cropped/"
    detect_expression(path_samm,'samm',200)
    path_cas = "/home/data2/CZP/2022MEGC-SPOT/MEGC2022_testSet/CAS_Test_cropped/"
    detect_expression(path_cas,'cas',30)


if __name__ == '__main__':
    main()
