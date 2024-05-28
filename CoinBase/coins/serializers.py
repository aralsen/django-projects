from .models import Coin
from typing import Iterable, List, Dict, Any


def serialize_apples(coins: Iterable[Coin]) -> List[Dict[str, Any]]:
    data = []
    for coin in coins:
        data.append({
            'name': coin.name,
            'photo_url': coin.photo_url,
        })
    return data
