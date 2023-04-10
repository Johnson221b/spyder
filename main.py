# 这个是调用的爬虫主函数

import link

# 头
headers = {
        "referer": "https://www.baidu.com.com/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }



# 爬取长沙天气部分
url= 'http://www.tianqihoubao.com/lishi/nanchang/month/202001.html'
timeouts = 60
filename = "nanchang_weather_1"

# 这个部分是记录表头的
soup_link_changsha = link.first(headers,url,timeouts)
link_changsha = link.link_obtain(soup_link_changsha)[0]
other_name_changsha = link.link_obtain(soup_link_changsha)[1]
tem_list_changsha = link.key_obtain(soup_link_changsha)
link.table_tag_write(tem_list_changsha,filename)



local = 0
# 开始循环写入表的具体内容
try:
    for kk in range(len(link_changsha)):
    #for kk in range(3):
        print(kk)
        url_kk = 'http://www.tianqihoubao.com' + link_changsha[kk]
        soup_changsha_kk = link.first(headers,url_kk,timeouts)
        tem_list_changsha_kk = link.key_obtain(soup_changsha_kk)


        local = link.table_body_write(tem_list_changsha_kk,local,filename)
except Exception as e:
    print('http://www.tianqihoubao.com' + link_changsha[kk])
    print(e)
    lim = kk +1
    for kk in range(lim,len(link_changsha)):
        #for kk in range(3):
        print(kk)
        url_kk = 'http://www.tianqihoubao.com' + link_changsha[kk]
        soup_changsha_kk = link.first(headers,url_kk,timeouts)
        tem_list_changsha_kk = link.key_obtain(soup_changsha_kk)


        local = link.table_body_write(tem_list_changsha_kk,local,filename)




