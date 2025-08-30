from requests import get
from pprint import PrettyPrinter

BASE_URL = 'https://api.freecurrencyapi.com/v1'
KEY = 'fca_live_QJgdEF0VEe0u9pi5ImmkooqxC6vuONeoJBAB0H5J'

printer = PrettyPrinter()


def get_currencies():
    url = f'{BASE_URL}/currencies?apikey={KEY}'
    
    try:
        response = get(url)
        response.raise_for_status()
        data = response.json()['data']

        data = list(data.items())
        data.sort()
    except Exception as e:
        print('An error occured:',e)

    return data

def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['name']
        _id = currency['code']
        symbol = currency.get('symbol_native', '')

        print(f'{_id} - {name} - {symbol}')
    
def exchange_rate():
    currency1 = input("Enter base currency: ").upper()
    currency2 = input("Enter target currency: ").upper()
    amount = float(input(f"Enter amount in {currency1}: "))

    url = f"{BASE_URL}/latest?apikey={KEY}&base_currency={currency1}&currencies={currency2}"

    try:
        response = get(url)
        response.raise_for_status()
        rates = response.json()['data']
        if currency2 in rates:
            rate = rates[currency2]
            converted = amount * rate
            print(f"{amount} {currency1} = {converted:.2f} {currency2}")
        else:
            print(f"Exchange rate for {currency2} not found.")
    except Exception as e:
        print("An error occurred:", e)

def main():
    currencies = get_currencies()

    print('Welcome to the currency converter!')
    print()

    exchange_rate()
    print("\nTip: You can find currency codes above or online. Make sure to enter valid codes (e.g., USD, EUR, JPY).")
    print("If you get an error, check your internet connection or the currency codes entered.\n")

    while True:
        again = input("Do you want to convert another currency? (yes/no): ").strip().lower()
        if again in ('yes', 'y'):
            exchange_rate()
        elif again in ('no', 'n'):
            print("Thank you for using the currency converter!")
            break
        else:
            print("Please enter 'yes' or 'no'.")
            
            
if __name__ == '__main__':
    main()