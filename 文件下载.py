import types
import requests
import os
from logger import Logger
import time
import json
from CSVtypewriter import dic_csv_typewriter


def download_file(download_dic,company,name,types, content_type='visitor', object_id='test'):
    """
    :param download_dic: {
                            "file_id": "c90118df-d5a9-4370-9ced-cd5bc0906b87",
                            "file_name": "天津OTC区块链项目 周会4.26-4.30 会议记录.pdf",
                            "DownloadUrl": "https://ecsp.tjotc.com.cn:443/file/mdoc/doc/202105/kEFtAIxNLtGjSRW_446934116.pdf?e=1620900388&token=AFP2WJ8WAM4QKF8046L4:GJ7wvP4NBLhgf9Z_GDlBtiDYhG4=",
                            "is_delete": "false"
                         }
    :param content_type: BLC content_type
    :param object_id: BLC Object_id
    :return:  {"file_path": download_file_addr, "file_name": download_file_name, "code": 200, "message": "文件下载成功"}
    """
    logger = Logger('FILE_DOWNLOAD')
    if download_dic['is_delete'] != False:
        logger.get_log().warning('%s为已删除的无效文件', json.dumps(
            download_dic['file_name'], ensure_ascii=False))
        logger.shutdown()
        return {"message": "deleted_file", "status": 400}

    base_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(base_dir, 'FileDownload',
                             time.strftime("%F"), content_type, object_id)
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    download_file_name = company+'-'+name+'-'+types+'.png'
    download_file_addr = os.path.join(file_path, download_file_name)

    url = download_dic['preview_url']
    r = requests.get(url)
    with open(download_file_addr, 'wb') as f:
        f.write(r.content)
    r.close()
    logger.get_log().info('文件下载成功: \n  文件下载请求JSON: %s\n 文件下载路径: %s', json.dumps(download_dic, ensure_ascii=False),
                          download_file_addr)
    logger.shutdown()
    return {"file_path": download_file_addr, "file_name": download_file_name, "code": 200, "message": "文件下载成功"}

def query_blc(data, URL):
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    logger = Logger('QUERY_BLC')
    post_json = json.dumps(data)
    req = requests.post(url=URL,headers=headers,data=post_json)
    logger.get_log().info(req.content)
    logger.get_log().info(req.text)
    logger.shutdown()
    result = req.text
    req.close()
    return json.loads(result)


REQ = {
    "appKey": "fbf862989461b38b",
    "sign": "MTE0ZWNmNzMyZWViYTQ5YjRlZTZlOGMzMDk0N2Q0MmYyYWI2MzkwZTdkMWFlMmNkMjZhZmVjYzI5ZmNmYmU1OQ==",
    "worksheetId": "6110d1bc3a1ee9302e4f6a59",
    "viewId": "621edc7b2a402fd74245ac3d",
    "pageSize": 50,
    "pageIndex": 1
}

csvpath  = os.path.abspath(os.path.dirname(__file__))
csvfile = dic_csv_typewriter('contact',csvpath)

URL = 'https://ecsp.tjotc.com.cn:443/api/v2/open/worksheet/getFilterRows'

header = {'name':'','title':'','company':'','contact':''}

csvfile.write_headline(header)

result = query_blc(REQ,URL=URL)

i = len(result['data']['rows'])
for i in range (0,i):
    
    query_result = result['data']['rows'][i]


    name = query_result['name']
    title = query_result['title']
    compnay = query_result['company']
    mobile=query_result['mobile']
    jkm=query_result['jkm']
    xcm=query_result['xck']

    jkm_json = json.loads(jkm)
    xcm_json = json.loads(xcm)
    # print(jkm_json[0])
    # download_file(jkm_json[0],company=compnay,name=name,types='健康码',object_id='“中国信创谷”之行，探“国之重器”')
    # download_file(xcm_json[0],company=compnay,name=name,types='行程码',object_id='“中国信创谷”之行，探“国之重器”')
    csvfile.write_content({'name':name,'title':title,'company':compnay,'contact':mobile})
# csvfile.close()

# print(result['data']['rows'][0]['xck'])
# result_dic={'name':result['data']['rows'][0]['name'],'title':result['data']['rows'][0]['title'],'company':result['data']['rows'][0]['company']}



# print(result_dic)
