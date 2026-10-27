import aiohttp
import asyncio
import json
from datetime import datetime

WEATHER_API_URL = "https://api.weather.yandex.ru/graphql/query"
CURRENCY_API_URL = "https://www.cbr-xml-daily.ru/daily_json.js"
CAR_API_URL = "https://api.cars-base.ru/full"

semaphore = asyncio.Semaphore(3)

async def fetch_data(url, session): 
    async with semaphore:
        try:
            async with session.get(url, timeout=5) as response:
                if response.status == 200:
                    data = await response.json()
                    return data
                else:
                    print(f"Ошибка {response.status} при запросе {url}")
                    return None
        except asyncio.TimeoutError:
            print(f"Таймаут при запросе {url}")
            return None
        except Exception as e:
            print(f"Ошибка {e} при запросе {url}")
            return None

async def get_all_data():
    async with aiohttp.ClientSession() as session:
        weather_task = fetch_data(WEATHER_API_URL, session)
        currency_task = fetch_data(CURRENCY_API_URL, session)
        car_task = fetch_data(CAR_API_URL, session)
        
        weather_data, currency_data, car_data = await asyncio.gather(
            weather_task, currency_task, car_task
        )
        
        return {
            "weather": weather_data,
            "currency": currency_data,
            "car": car_data,
            "timestamp": datetime.now().isoformat()
        }

def save_data(data, filename="data.json"):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(json.dumps(data, ensure_ascii=False) + "\n")

async def main():
    while True:
        data = await get_all_data()
        if data:
            save_data(data)
            print(f"Данные сохранены: {data['timestamp']}")
        await asyncio.sleep(600)

if __name__ == "__main__":
    asyncio.run(main())