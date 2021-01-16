from urllib import request


url = "http://i.baidu.com/"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) App\
    leWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",

    "Cookie":"BAIDUID=F1676F6D91D12CF987A81C35B5683EF5:FG=1; PSTM=1543068715; BIDUPSID=F1676F6D91D12CF987A81C35B5683EF5; BDUSS=k4VllQdW9-ZDR6fmo1LWxIeEo5LWd1OTMxLUhCQkY5eUZlZXY0OEtKSzdVSEZjQVFBQUFBJCQAAAAAAAAAAAEAAABATb2F1~OwttK76ti0s8zs0cQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALvDSVy7w0lca3; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PHPSESSID=e1sso19h9qnjugdq974cpofk50; __guid=62687476.678578182179940700.1550386788528.5847; Hm_lvt_4010fd5075fcfe46a16ec4cb65e02f04=1550386790; monitor_count=4; Hm_lpvt_4010fd5075fcfe46a16ec4cb65e02f04=1550387997"
}

req = request.Request(url, headers = headers)

response = request.urlopen(req)

print(response.read().decode())

	
