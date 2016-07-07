import urllib.request
import urllib.parse
import json
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=fanyi.logo'
#添加header
userAgent = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
wordList = open('./ComputerScience.txt','a')
while True:
    content = input("请输入要翻译的内容：")
    if content in ['q','Q']:
        break
    data ={
    'type':'AUTO',
    'i':content,
    'doctype':'json',
    'xmlVersion':'1.8',
    'keyfrom':'fanyi.web',
    'ue':'UTF-8',
    'action':'FY_BY_CLICKBUTTON',
    'typoResult':'true'
    }
    data = urllib.parse.urlencode(data)#得到的是一个字符串，需要将其转换成二进制形式
    data = urllib.parse.unquote_to_bytes(data)
    require = urllib.request.Request(url,data,userAgent)
    response = urllib.request.urlopen(require)
    #response = urllib.request.urlopen('http://fanyi.youdao.com/?keyfrom=fanyi.logo')#需要完整的网页地址
    html = response.read()
    #print(html) 以二进制码的形式打印
    html = html.decode("utf-8")#以utf-8形式解码,得到的是一个字符串
    #使用json模块将字符串还原成字典
    html = json.loads(html)#'translateResult': [[{'tgt': '好好学习', 'src': 'good good study'}]]
    result = html['translateResult'][0][0]['tgt']#dict->list->list->dict->result
    print('翻译结果(来自有道)：%s'%result)
    wordList.write(content+'  '+result+'\n')
wordList.close()
