# Copyright 2018 Keval Khara kevalk@bu.edu

import requests
import time
import json


def get_results(params):

	access_token = ""
	header = {'Authorization': 'Bearer %s' % access_token}

	resp = requests.get(url="http://api.yelp.com/v3/businesses/search", params=params, headers=header)

	# Transforms the JSON API response into a Python dictionary
	data = resp.json()
	return data


def get_search_parameters(lati,longi):
	# See the Yelp API for more details
	params = {}
	params["term"] = "restaurant"
	params["latitude"] = str(lati)
	params["longitude"] = str(longi)
	params["radius_filter"] = "2000"
	params["limit"] = "10"
	return params


def main():
	locations = [(39.98,-82.98), (42.24,-83.61), (41.33,-89.13)]
	api_calls = []
	for lati,longi in locations:
		params = get_search_parameters(lati,longi)
		api_calls.append(get_results(params))
		time.sleep(1.0)

	count = 1
	for calls in api_calls:
		print("Location ", count)
		print("=" * 75)
		print(json.dumps(calls, indent=3))
		count += 1
		print()


if __name__=="__main__":
	main()
