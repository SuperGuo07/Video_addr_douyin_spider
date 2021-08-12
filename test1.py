

import requests

requests.packages.urllib3.disable_warnings()

res = requests.get(url="https://www.baidu.com", verify=False)
print(res)