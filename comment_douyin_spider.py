# import openpyxl
import json
import csv
# import xlrd
# import xlwt


def parser_comments(parser_comments):
    data=[]
    print("*"*100)
    print("解析评论数据")
    print("*" * 100)
    comment=json.loads(parser_comments)
    for item in comment["comments"]:
        dic={}
        dic["cid"]=item["cid"] #cid
        dic["aweme_id"]=item["aweme_id"] #aweme_id可能是视频id
        dic["nickname"]=item["user"]["nickname"] #评论者名字
        dic["gender"]=item["user"]["gender"] #评论者性别
        dic["unique_id"]=item["user"]["unique_id"] #评论者抖音号
        dic["signature"]=item["user"]["signature"] #评论者主页简介
        dic["birthday"]=item["user"]["birthday"] #评论者生日
        dic["region"]=item["user"]["region"]  # 评论者所属地区
        dic["custom_verify"]=item["user"]["custom_verify"] #评论者的认证
        dic["sec_uid"]=item["user"]["sec_uid"] #可通过此拼接url访问得到评论者主页json数据
        dic["text"]=item["text"] #评论内容
        dic["time"]=item["create_time"] #评论时间戳
        dic["digg_count"]=item["digg_count"] #评论获赞数
        dic["reply_comment_total"]=item["reply_comment_total"]#评论回复数
        data.append(dic)
    return data
        # print(data)

def save_data(data,path):
    header = list(data[0].keys())  # 数据列名
    with open(path, 'a', newline='',encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f,fieldnames=header)
        writer.writerows(data)  # 写入数据
'''
def save_data_openpyxl(data, path):
    header = list(data[0].keys())  # 数据列名
    wb = openpyxl.load_workbook(path)
    ws = wb.active
    ws.title = "comment_list"
    ws.append(header)
    ws.append(data)
    wb.save(path)

def save_data_xlrd(data, path):
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('Sheet1')
    for i in data:
        sheet1.write(i)
    workbook.save(path)
'''



def response(flow):
    try:
        if "aweme.snssdk.com/aweme/v2/comment/list/?" in flow.request.url:
            data=parser_comments(flow.response.content)
            save_data(data,"comment_qiangxiaocao.csv")
            # save_data_openpyxl(data, "comment_test1.xlsx")
            # save_data_xlrd(data,"comment_test.xls")
    except:
        print("---"*100,"错误","--"*100)
        pass





