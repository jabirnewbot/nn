import requests
import random
import threading

def send_sms(number, message):
    API = f"https://flask-hello-world-theta-bay.vercel.app/?n={number}&m={message}"
    resp = requests.get(API)
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
    message = "You Get 50,000 Tk From Goverment Of Bangladesh, Grab It From: https://t.me/INVESTEARININGBANGLA |আপনি বাংলাদেশ সরকার থেকে 50,000 টাকা পান, এটি নিন:https://t.me/INVESTEARININGBANGLA !"
    
    # User input for amount and number of phone numbers
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
