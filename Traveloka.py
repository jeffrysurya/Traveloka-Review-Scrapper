import requests
import json

def getTravelokaReview(page):
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
        "skip": page,
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
        data = response.json()
        return data['data']['reviewList']
    
def saveReview(data):
    with open('review.json', 'a') as f:
        json.dump(data, f, indent=4)

review_data = []
for i in range(0,1510,10):
    data = getTravelokaReview(i)
    for i in range(len(data)):
        review_data.append({
            'Name': data[i]['reviewerName'],
            'Score': data[i]['overallScore'],
            'Review': data[i]['reviewText'],
        })

with open('review.json', 'w') as f:
    json.dump(review_data, f, indent=4)

