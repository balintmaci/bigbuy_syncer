

def read_api_key():
    with open("api_key") as f:
        return f.readline()


api_key = read_api_key()
print(api_key)