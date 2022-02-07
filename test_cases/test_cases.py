import requests

test_payload = {
    "api_url": "http://127.0.0.1:5000/restaurant",
    "restro_id": 4
}

data = [
    {
        "restaurant": "KOME",
        "type_of_food": "Ethnic",
        "cuisine": "Spanish",
        "price": "premium",
        "specialties": "Crab Cakes with Remoulade Sauce"
    },
    {
        "restaurant": "LA CONDESSA_1",
        "type_of_food": "Fast casual_1",
        "cuisine": "Chinese_1",
        "price": "economy_1",
        "specialties": "Frito Pie_1"
    }
]


# Test case to fetch all data
def test_get_all_details():
    response = requests.get(test_payload["api_url"])
    assert response.status_code == 200


# testcase to fetch record by id
def test_get_restro_by_id():
    api_url = test_payload["api_url"] + f'/{str(test_payload["restro_id"])}'
    response = requests.get(api_url)
    assert response.status_code == 200


# test case to insert record
def test_insert_restro():
    import json
    headers = {
        "Content-Type": "application/json"
    }
    payload = json.dumps(data[0])
    response = requests.request("POST", test_payload["api_url"], headers=headers, data=payload)
    assert response.status_code == 201


# testcase to update record
def test_update_restro():
    import json
    headers = {
        "Content-Type": "application/json"
    }
    payload = json.dumps(data[0])
    api_url = test_payload["api_url"] + f'/{str(test_payload["restro_id"])}'
    response = requests.request("PUT", api_url, headers=headers, data=payload)
    assert response.status_code == 200


# testcase to delete record
def test_delete_restro():
    headers = {}
    payload = {}
    api_url = test_payload["api_url"] + f'/{str(test_payload["restro_id"])}'
    response = requests.request("DELETE", api_url, headers=headers, data=payload)
    assert response.status_code == 200
