import requests
import os
import pandas as pd
from multiprocessing import *
import random


def Download_video(url):
    requests.packages.urllib3.disable_warnings()
    video = requests.get(url, verify=False).content
    path_vi = (r"D:/Work/data/视频/%s.mp4"%(random.randint(0,100000)))
    with open(path_vi, "wb") as code:
        code.write(video)

if __name__ == "__main__":
    if not os.path.exists(r"D:/Work/data/视频"):
        os.mkdir(r"D:/Work/data/视频")
    df = pd.read_csv("home.csv", names=["url"])
    pool=Pool(5)
    pool.map(Download_video,df.url.tolist())