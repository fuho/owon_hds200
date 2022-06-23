#! /usr/env/bin python3

# https://www.owon.com.hk/download.asp?category=Digital Oscilloscope&series=HDS200 Series&model=HDS242(S)&SortTag=Latest Firmware
# GET /download.asp?category=Digital%20Oscilloscope&series=HDS200%20Series&model=&SortTag=Latest%20Firmware HTTP/1.1
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
# Accept-Encoding: gzip, deflate, br
# Accept-Language: en-US,en;q=0.9
# Connection: keep-alive
# Cookie: ASPSESSIONIDCEDSCTQT=POPNKPBAOLMLKIPMNGJMBBEA; ASPSESSIONIDSAQCARRT=GLBAIHLBGBHIMELCDFFCAOFL; ASPSESSIONIDSEQCARRT=ENCAIHLBNCJNAOIGBFHJDMDF; ASPSESSIONIDAUQCARSQ=PPIOPGOAFLIDNNBDBILCODGM; ASPSESSIONIDSGTDASQT=JLBBOCLBJMKMIINDBNOCJNGG
# Host: www.owon.com.hk
# Referer: https://www.owon.com.hk/download.asp?category=Digital%20Oscilloscope&series=HDS-N%20Series&model=&SortTag=Latest%20Firmware
# Sec-Fetch-Dest: document
# Sec-Fetch-Mode: navigate
# Sec-Fetch-Site: same-origin
# Sec-Fetch-User: ?1
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.36
# sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="101", "Opera";v="87"
# sec-ch-ua-mobile: ?0
# sec-ch-ua-platform: "macOS"

# https://www.owon.com.hk/download.asp?
# category=Please select product category&series=&model=&SortTag=Latest Firmware

# https://www.owon.com.hk/download.asp?category=Digital%20Oscilloscope&series=HDS200%20Series&model=&SortTag=Latest%20Firmware

import urllib.parse
import urllib.request

url = 'https://www.owon.com.hk/download.asp'
params = {
    'category': 'Digital Oscilloscope',
    'series': 'HDS200',
    'model': '',
    'SortTag': 'Latest Firmware'
}
versions = ('v1.0.0', 'v2.0.0', 'v3.0.0', 'v4.0.0', 'v5.0.0', 'v6.0.0')
url_params = urllib.parse.urlencode(params)
full_url = f"{url}?{url_params}"

for version in versions:
    data = urllib.parse.urlencode({'version': version})
    data = data.encode('ascii')
    req = urllib.request.Request(full_url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
