import discogs_client as dc

def login():
    token = input("Paste your token: \n")
    return dc.Client("DiscogsCollector", user_token=token)
