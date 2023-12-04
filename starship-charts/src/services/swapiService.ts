import axios from 'axios';

export async function fetchStarshipCostTrends() {
    const response = await axios.get("http://localhost:8000/starships/cost-trends");
    return response.data;
}

export async function fetchStarshipCostsByFilm() {
    const response = await axios.get("http://localhost:8000/starships/cost-by-film");
    return response.data;
}