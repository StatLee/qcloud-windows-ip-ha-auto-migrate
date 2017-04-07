#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块
from src.QcloudApi.qcloudapi import QcloudApi

import sys,os
import json
'''
module 设置需要加载的模块
已有的模块列表：
cvm      对应   cvm.api.qcloud.com
cdb      对应   cdb.api.qcloud.com
lb       对应   lb.api.qcloud.com
trade    对应   trade.api.qcloud.com
sec      对应   csec.api.qcloud.com
image    对应   image.api.qcloud.com
monitor  对应   monitor.api.qcloud.com
cdn      对应   cdn.api.qcloud.com
wenzhi   对应   wenzhi.api.qcloud.com
'''
module = 'vpc'

'''
action 对应接口的接口名，请参考产品文档上对应接口的接口名
'''
action = 'DescribeNetworkInterfaces'

config = {
    'Region': 'gz',
    'secretId': 'XXXXX',
    'secretKey': 'XXXXX',
    'method': 'get'
}

'''
params 请求参数，请参考产品文档上对应接口的说明
'''

nwifsring = sys.argv[1]

params = {
    'networkInterfaceId': nwifsring,
}
try:
    service = QcloudApi(module, config)

    # 请求前可以通过下面四个方法重新设置请求的secretId/secretKey/region/method参数
    # 重新设置请求的secretId
    secretId = 'XXXX'
    service.setSecretId(secretId)
    # 重新设置请求的secretKey
    secretKey = 'XXXXX'
    service.setSecretKey(secretKey)
    # 重新设置请求的region
    region = 'gz'
    service.setRegion(region)
    # 重新设置请求的method
    method = 'post'
    service.setRequestMethod(method)

    # 生成请求的URL，不发起请求
#    print service.generateUrl(action, params)
    # 调用接口，发起请求
    rs=(json.loads(service.call(action, params)))
#    print service.call(action, params)
    for item in rs['data']['data'][0]['privateIpAddressesSet']:
        print item['privateIpAddress']
    
except Exception, e:
    import traceback
    print traceback.format_exc()
    print 'exception:', e
