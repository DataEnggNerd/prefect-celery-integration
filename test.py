import time
import requests

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}


pan_numbers = ["AECPK3808C", "AOLPJ8039B", "AAEHR0506G", "AIYPC4084E", "ABUPF8207D", "ANEPB4686N", "AEYPK1417M", "ALFPK0738D", "AFFPK1765C", "AHQPK0264K", "ALFPK0738D", "AFFPK1765C", "AAACO3916A", "AACPM7770R", "AKUPA0843K", "AAACO3651L", "ARHPM5056E", "AAIPU0281F", "ABIPH9346P", "ABIPH8214Q", "AFLPB2000H", "AFMPB2205F", "AEYPB1895G", "ACEPB2927R", "AFMPB2205F"]

for i in range(25):
    time.sleep(5)
    json_data = {
    'order_id': 'test-order',
    'search_data': {
        'debtor_type': 'Individual',
        'pan_number': pan_numbers[i],
    },
    'payment_method': 'UPI',
    'upi_id': 'gAAAAABmw5WucdgEB3YkRkXatBlAJx5p7BRZ2rydjMeJyYnL3PQJ6XbbpP5XPDcL4v1HhxQplfNMD5e-a4qd267y9SSmKk74FwkGiokXhW_4p9j2JbeGNv4=',
    'user_email_id': 'santhosh@advarisk.com',
    'callback_url': 'https://webhook.site/c4f39b15-5bf0-4aaa-b5f3-5d89df17476c',
    'authentication_token': 'SuSpD0w_iH0HXzv',
}
    response = requests.post('http://stage-scraper-api.advarisk.com:8090/cersai/debtor_search/', headers=headers, json=json_data)
    print(response.json().get("task_id"))
