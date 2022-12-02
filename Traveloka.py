import requests

# class Traveloka:
#     def getTravelokaReview():
#         url = 'https://www.traveloka.com/api/v2/hotel/getHotelReviews'
#         body = {
#             'hotelId': '100000000000',
#             'page': 1,
#             'pageSize': 10,
#             'sort': 'RECOMMENDED'
#         }

#         headers = {
#             'authority': 'www.traveloka.com',
#             'accept': 'application/json, text/plain, */*',
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
#             'content-type': 'application/json;charset=UTF-8',
#             'origin': 'https://www.traveloka.com',
#             'x-domain': 'accomContent'
#         }

#         response = requests.post(url, body=body, headers=headers)


def getTravelokaReview():
        url = 'https://www.traveloka.com/api/v2/hotel/getHotelReviews'
        body = {
    "fields": [],
    "data": {
        "filterSortSpec": {
            "travelTheme": None,
            "travelType": None,
            "sortType": "RATING",
            "tagIds": []
        },
        "hotelReviewFilterClientSpec": {
            "hasPhotos": False
        },
        "hotelReviewSortClientSpec": {
            "sortType": "RATING"
        },
        "ascending": True,
        "reviewLanguage": "ENGLISH",
        "hotelId": "3000010001127",
        "skip": 1510,
        "top": 10
    },
    "clientInterface": "desktop"
}

        headers = {
            'content-type': 'application/json',
            'origin': 'https://www.traveloka.com',
            'x-domain': 'accomContent',
            'cookie': 'PHPSESSID=ne5n4bs5af36100tatlu8hpf94; tv-repeat-visit=true; tvs=qgdHX7GvehrD9XH5a3S4PWL3Nd74xArIuT+JzcRMbKddQHovERAJ9HWRLrAaZ0jPhWj5HSxm0ZKiRbldET1ham2PeYg1sQr2h/wIBjIyPQ1JQfOnq9PrXiJXCb7pG+Gum+yqmdzW2IkzPWY4oG7BSNNoWAryX5oePC5p0NmYxLojp/BAW71T6pjl6MsiCbn/3jW7f6f85zK7XA1xLrLbn3wpMY91AYFzJ6h8za/vSrng40uUoDT+qJIv0oQGNB1A; tvl=qgdHX7GvehrD9XH5a3S4PdE8AYpuF3hYPaT5bxhY7ZZovcaQgYHH/BWZAEmffYBkxyxx6RDwZFkKXR8djKqYhQ/Pu7qK/OBUAFQTs/csyiC72isthBBf5oZQ7iEdgzxWwqhciaxLFbhL1CQPuDkZk/psYKrJOanCKPAJhdR5uwXvlyHfFnPptZUxAgMVwRNSCMYWUJplNNMY2P4/83O9X+8GNrPf8Ng75ZieUaJama8='
        }

        response = requests.post(url, json=body, headers=headers)
        datas = response.json()
        print (datas['data']['reviewList'][0]['reviewText'])
        return print (response.status_code)


getTravelokaReview()


        


