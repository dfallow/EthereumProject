import ipfsApi
api = ipfsApi.Client('127.0.0.1', 5001)

res = api.add("./White.svg")
print(res)
ipfs_hash = "https://ipfs.io/ipfs/" + res["Hash"]
print(ipfs_hash)