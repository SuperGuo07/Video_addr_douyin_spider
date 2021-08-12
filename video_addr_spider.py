import json
import csv



def parser_home(parser_home):
    data=[]
    home_data=json.loads(parser_home)
    for item in home_data["aweme_list"]:
        dic = {}
        dic["video_url"]=item["video"]["play_addr"]["url_list"][0] #视频下载链接
        data.append(dic)
    return data
def save_data(data,path):
    header = list(data[0].keys())  # 数据列名
    with open(path, 'a', newline='',encoding="utf-8") as f:
        writer = csv.DictWriter(f,fieldnames=header)
        writer.writerows(data)
def response(flow):
    try:
        if "aweme.snssdk.com/aweme/v1/aweme/post/?" in flow.request.url:
            data=parser_home(flow.response.text)
            save_data(data,"home.csv")
    except:
        print("---"*100,"错误","--"*100)
        pass



