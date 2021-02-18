import requests
from lxml import etree
import re
import sys
import time

path = sys.path[0]
requests.packages.urllib3.disable_warnings()
# 为了反爬虫只能这样
header = {
    "authority": "www.juzikong.com",
    "method": "GET",
    "path": "/",
    "scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "cookie": "__gads=ID=ffbebf21d251f3aa-2250a36d92c40097:T=1604675722:RT=1604675722:S=ALNI_Ma6wTlUzyVCO-WepIEjEll7m44mVw; _ga=GA1.2.1871593187.1604675675; Hm_lvt_bdf284068ceac91d2241963e43550528=1604675676,1604678535,1604678648,1604818388; _gid=GA1.2.1598551397.1604818388; Hm_lpvt_bdf284068ceac91d2241963e43550528=1604818516",
    "if-none-match": "12f01-HwnW+MaVA0M4mb7nbVQoUubh5Sw",
    "referer": "https://www.juzikong.com/works/f1527de5-d1b0-4cb3-b2e2-c47dc71e186f",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    # UA换成电脑更方便数据清洗
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
}

se = requests.session()


def get_start(start_url):
    resp = se.get(start_url, headers=header, verify=False).text
    # print(resp)
    html = etree.HTML(resp)

    # 获取总页数和话题
    title = html.xpath(r"//*[@id='__layout']/div/div[3]/div[1]/div[2]/div[1]/span/b")
    title = title[0].text.replace("\n", "").replace(" ", "")
    # / html / body / div[1] / div / div / div[3] / div[1] / div[2] / div[3] / ul / li[3] / a
    # 2020.11.14 发现 bug 获取总页数 有些话题的总页数比较少 需要遍历咯 最多显示8页
    # 还是不获取总页数了 直接获取句子数反推总页数
    pat = re.compile(r"共收录(.*?)条")
    juzhi_all = pat.findall(resp.replace("\n", "").replace(" ", ""))[0]
    page_all = int(int(juzhi_all) / 10)
    if int(juzhi_all) % 10 != 0:
        page_all = page_all + 1
    print("当前{}话题共:{}页".format(title, page_all))
    return page_all, title


# get_start("https://www.juzikong.com/works/f0daf978-c00c-4d4d-bbaa-9e56cbb1040e")


# 获取每页句子(10/页)
def get_page(url_page, page):
    url_page = url_page + "?page={}".format(page)
    resp = se.get(url_page, headers=header, verify=False).text
    html = etree.HTML(resp)
    # 每一页的句子转进列表里面
    content_list = []
    # 每页句子内容的规律 1-10
    # //*[@id="__layout"]/div/div[3]/div[1]/div[2]/div[2]/section[1]/div[2]/a/span/span/span
    # //*[@id="__layout"]/div/div[3]/div[1]/div[2]/div[2]/section[2]/div[2]/a/span/span/span
    # //*[@id="__layout"]/div/div[3]/div[1]/div[2]/div[2]/section[3]/div[2]/a/span/span/span
    # //*[@id="__layout"]/div/div[3]/div[1]/div[2]/div[2]/section[4]/div[2]/a/span/span/span
    # 获取一页的句子 到最后一页可能没有10句 要处理异常
    for t in range(1, 11):
        # 针对一个句子有换行符如何解决呢? (已解决)
        # ../a/span[1]/span/span
        # ../a/span[2]/span/span
        # ../a/span[4]/span/span

        try:
            content = html.xpath(
                r"//*[@id='__layout']/div/div[3]/div[1]/div[2]/div[2]/section[{}]/div[2]/a/span[1]/span/span".format(t))

            # 检查span[2]是否有内容
            check = html.xpath(
                r"//*[@id='__layout']/div/div[3]/div[1]/div[2]/div[2]/section[{}]/div[2]/a/span[2]/span/span".format(t))
            if check == []:
                content = content[0].text
                content_list.append(content)
                # print(content)
            else:
                # 开始遍历获取换行内容
                content_tt = ""
                try:
                    for tt in range(1, 99999):
                        content_tt_c = html.xpath(
                            r"//*[@id='__layout']/div/div[3]/div[1]/div[2]/div[2]/section[{}]/div[2]/a/span[{}]/span/span".format(
                                t, tt))
                        content_tt = content_tt + "/" + content_tt_c[0].text
                except Exception as tte:
                    # print(content_tt)
                    content_list.append(content_tt)
                    # 获取完就跳出
                    continue

        except Exception as e:
            print("获取{}页第{}条句子出现异常:{}".format(page, t, e))
            break

    print("获取到{}页的{}条句子".format(page, str(len(content_list))), content_list)
    return content_list


# get_page("https://www.juzikong.com/works/2cb94e93-049f-4082-85b1-c344485d6d76", 64)


if __name__ == "__main__":
    # 获取句子写入文件
    # 话题链接
    start_url = input("请输入句子迷话题链接~:")
    sleep_time = float(input("设置爬取速度(单位:s):"))

    # start_url = "https://www.juzikong.com/works/f1527de5-d1b0-4cb3-b2e2-c47dc71e186f"
    # 总页数
    try:
        page_all, title = get_start(start_url)
    except Exception as e:
        print("获取话题失败!")
        print("网站有严格的反爬虫机制,请尝试访问url,若可访问,请截图以下错误信息 联系作者修改bug,若确实不可以访问请更换ip后重试! 谢谢您")
        print("错误信息", e)
    for i in range(1, int(page_all) + 1):
        content_list = get_page(start_url, i)
        # 遍历列表写入
        for content in content_list:
            with open(r"{}//{}句子.txt".format(path, title), "a", encoding="utf8") as f:
                f.write(content + "\n")
        time.sleep(sleep_time)  # 防止速度过快

    # 获取句子json写入文件(功能2)
    # 话题链接
    # start_url = "https://www.juzikong.com/works/2cb94e93-049f-4082-85b1-c344485d6d76"
    # 总页数
    # page_all = get_start(start_url)
    # # 构造
    # arr = []
    # for i in range(1, int(page_all) + 1):
    #     content_list = get_page(start_url, i)
    #     # 遍历列表写入
    #     for content in content_list:
    #         arr.append(content)
    #     time.sleep(0.1)  # 防止速度过快
    #
    # with open(r"{}//《抖音文案馆》json.txt".format(path), "a", encoding="utf8") as f:
    #     f.write(str(arr))
