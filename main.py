import requests
import datetime
import time
import pytz

base_url = 'https://store-manager-backend-eta.vercel.app/store/sales/'

def send_get_request():
	response = requests.get(base_url)
	print(f"Request sent. Status code: {response.status_code}")

def main():
	while True:
		# Get the current time in GMT
		current_time = datetime.datetime.now(pytz.timezone('GMT'))
		
		# Check if it's 6 PM GMT
		if current_time.hour == 18 and current_time.minute == 0:
			send_get_request()
			
			# Wait for 60 seconds to avoid sending multiple requests in the same minute
			time.sleep(60)
		else:
			# Wait for a short period before checking the time again
			time.sleep(10)

if __name__ == "__main__":
	main()