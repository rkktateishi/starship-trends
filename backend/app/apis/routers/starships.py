from fastapi import APIRouter

from app.utils import fetch_starships_by_url, fetch_all_films
from app.services.cost_trends import total_average, costs_by_film

router = APIRouter()

# Fetch list of films and relevant starships
# Cache list to improve overall response times and reduce impact reliance on slower system
# In addition cache to avoid hitting rate limits
@router.get("/cost-trends", status_code=200)
def get_starships_trend():
    total_avg = total_average(fetch_starships_by_url(), fetch_all_films())
    # average_by_class = average_by_starship_class(fetch_starships_by_url(), fetch_all_films())

    return [total_avg]

# Fetch list of films and relevant starships
# Cache list to improve overal response times and reduce impact reliance on slower system
# In addition cache to avoid hitting rate limits
@router.get("/cost-by-film", status_code=200)
def get_starships_by_film():
    starship_dict = fetch_starships_by_url()
    films = fetch_all_films()

    return costs_by_film(starship_dict, films)