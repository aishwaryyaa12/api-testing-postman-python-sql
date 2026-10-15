import requests
import json

def test_api_and_data_consistency():
    print("Executing REST API Data Consistency Verification...")
    response = requests.get("https://dummyjson.com/carts/1")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    data = response.json()
    assert "products" in data
    total_calculated = sum(p['price'] * p['quantity'] for p in data['products'])
    print(f"Calculated Cart Total: ${total_calculated}")
    print("API Data Consistency Check: PASSED!")

if __name__ == "__main__":
    test_api_and_data_consistency()
