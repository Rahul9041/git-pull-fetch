print("Its working")
print("Rahul made change in it")
print(3 + 5)

def get_api_test():
    import requests 
    demo_url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url=demo_url)
    print(dir(response))     #it show its information
    return response.json()   #it shows all data of url
get_api_test()
