from fastapi import HTTPException
import ujson as json
from requests_cache import CachedSession, RedisCache

from app.core.config import settings

def query(endpoint, query_params):

    querystring = "&".join("{}={}".format(k, v) for k, v in query_params.items())
    headers = {'User-Agent': 'swapi-python'}
    session = CachedSession(
        cache_name="{}{}?{}".format(settings.SWAPI_URL, endpoint, querystring),
        expire_after=settings.DEFAULT_TTL,
        backend=RedisCache(host='redis', port=6379)
    )
    response = session.get("{}{}?{}".format(settings.SWAPI_URL, endpoint, querystring), headers=headers)
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Could not fetch Resource")
    return response

# fetch all starships and key by url
def fetch_all_starships():
    curr_page = 1
    next = True
    starships = []

    while next:
        json_data = json.loads(query('/starships', { "page": curr_page }).content)
        starships += json_data["results"]
        if bool(json_data['next']):
            curr_page += 1
        else:
            next = False

    return starships

def fetch_starships_by_url():
    curr_page = 1
    next = True
    starships = {}

    while next:
        json_data = json.loads(query('/starships', { "page": curr_page }).content)
        starships.update({s["url"]: s for s in json_data["results"]})
        if bool(json_data['next']):
            curr_page += 1
        else:
            next = False

    return starships


def fetch_all_films():
    curr_page = 1
    next = True
    films = []

    while next:
        json_data = json.loads(query('/films', { "page": curr_page }).content)
        films += json_data["results"]
        if bool(json_data['next']):
            curr_page += 1
        else:
            next = False
    films = sorted(films, key=lambda i: i["episode_id"])
    return films
