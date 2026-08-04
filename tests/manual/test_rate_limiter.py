import requests

URL1 = "http://127.0.0.1:5000/"
URL2 = "http://127.0.0.1:5000/login"
URL3 = "http://127.0.0.1:5000/admin"

NUMBER_OF_REQUESTS =15

print("\nMaking 15 requests to: http://127.0.0.1:5000/")
for i in range(NUMBER_OF_REQUESTS):

    response1 = requests.get(URL1)

    print(
        f"request {i+1}:" f"Status {response1.status_code}"
    )

print("\nMaking 15 requests to: http://127.0.0.1:5000/login")
for i in range(NUMBER_OF_REQUESTS):

    response2 = requests.get(URL2)

    print(
        f"request {i+1}:" f"Status {response2.status_code}"
    )
print("\nMaking 15 requests to: http://127.0.0.1:5000/admin")
for i in range(NUMBER_OF_REQUESTS):

    response3 = requests.get(URL3)

    print(
        f"request {i+1}:" f"Status {response3.status_code}"
    )