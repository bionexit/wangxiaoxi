import requests
import json
from logger import Logger
import CSVwriter
import aiohttp
import asyncio


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



def query_all():
    URL = 'http://192.168.1.11:8080/block-query'
    result_dic = []
    logger = Logger('BLOCK QUERY')
    
    for i in range (0,6219):
        REQ = {
            "conf":{
                "verf":"6cfd00cefa7c3e56916abf2192aa5c6b77e84bc4a98816f417577b845d46cea1"
                },
            "body":
                {
                    "blockNumber":i
                }
        }
        logger.get_log().info('Block %s starting...' % i)
        print('Block %s starting...' % i)
        result = query_blc(REQ,URL=URL)


        try:
            _block = i

            _create_time = result['data']['createTime']
            height = len(result['data']['txList'])
            for ix in range(0,height):
                core_result = result['data']['txList'][ix]['rwSet']['nsRwSets'][0]['kvRwSet']['writes'][0]['value']
                
                _result = {}
                _result['block']=_block
                _result['block_seq']=ix+1
                _result['create_time']=_create_time
                # print(core_result)
                # print(result['data']['txList'][0]['rwSet']['nsRwSets'][0]['kvRwSet']['writes'][0])
                deep  = json.loads(core_result)
                # print(deep)



                _schemaversion = deep['header']['model']['version']
                _object_id = deep['header']['content']['object_id']
                _type = deep['header']['content']['type']
                _operation = deep['header']['content']['operation']
                _version = deep['header']['content']['version']

                _result['schemaversion']=_schemaversion

                _result['type']=_type
                _result['operation']=_operation
                _result['object_id']=_object_id

                _result['version']=_version
                result_dic.append(_result)
                # print(_result)
        except:
            logger.get_log().error('Data in block %s error' % _block)
            
    return result_dic
        

    #
    # {"createTime": "2022-02-18 20:03:42.179",'block':block,'type':res,'object_id':id,'version':ver,'operation':oper}

CSVwriter.csv_writer(query_all())

