from web3 import Web3
import json
from urllib.request import urlopen
import os
import sys
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

async def getUrlResponse(url):
    try:
        req = urlopen(url)
    except HTTPError:
        return None
    except URLError:
        return None
    
    if int(req.status) != 504 or int(req.status) != 429:
        print("request status", req.status)
        md_json = json.loads(req.read())
        req.close()
        return md_json
    else: return None   
           
async def getMetaData(md_url):
    
    print("now get response to: ", md_url)
    res = await getUrlResponse(md_url) 
    print(res)
    return res