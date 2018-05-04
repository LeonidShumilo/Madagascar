import os
url='https://datapool.asf.alaska.edu/GRD_HD/SA/'
names_list=['S1A_IW_GRDH_1SDV_20180430T021820_20180430T021845_021690_025699_0723','S1A_IW_GRDH_1SDV_20180418T021820_20180418T021845_021515_025121_E433','S1A_IW_GRDH_1SDV_20180406T021819_20180406T021844_021340_024BA2_03DF','S1A_IW_GRDH_1SDV_20180325T021819_20180325T021844_021165_024627_5366','S1A_IW_GRDH_1SDV_20180313T021819_20180313T021844_020990_024098_F9C1','S1A_IW_GRDH_1SDV_20180301T021819_20180301T021844_020815_023B0F_1D7F','S1A_IW_GRDH_1SDV_20180217T021819_20180217T021844_020640_023580_B794','S1A_IW_GRDH_1SDV_20180205T021819_20180205T021844_020465_022FEC_6DED','S1A_IW_GRDH_1SDV_20180124T021819_20180124T021844_020290_022A56_60ED','S1A_IW_GRDH_1SDV_20180112T021828_20180112T021853_020115_0224C7_ECDC']
def download_data(link,user='shumilo.leonid@gmail.com',password='Research1'):
    com='wget -c --http-user='+user+' --http-password='+password+' "'+link+'"'
    print(com)
    os.system(com)
def process(name):
    com='/usr/local/snap/bin/gpt '+os.path.join(os.path.realpath(''),'graph.xml')+' -Pinput1='+os.path.join(os.path.realpath(''),name+'.zip')+' -Ptarget1='+os.path.join(os.path.realpath(''),name)
    os.system(com)
    com='gdal_merge.py -separate -o '+os.path.join(os.path.realpath(''),name+'.data.tif ')+' '+os.path.join(os.path.realpath(''),name)+'.data/Sigma0_VV_db.img '+os.path.join(os.path.realpath(''),name)+'.data/Sigma0_VH_db.img'
    os.system(com)
    com='python '+os.path.join(os.path.realpath(''),'clean.py')+' '+os.path.join(os.path.realpath(''),name+'.data.tif ')
for link in names_list:
    download_data(url+link+'.zip')
for name in names_list:
    process(name)
