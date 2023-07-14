import requests
import json

COUNTRY_CODES = {
    'Japan': 'jp',
    'Brasil': 'br',
    'United States': 'us',
    'China': 'cn',
    'South Korea': 'kr',
    'Spain': 'es',
    'France': 'fr',
    'United Kingdom': 'gb',
    'Germany': 'de',
    'Colombia': 'co',
    'Belgium': 'be',
    'Poland': 'pl',
    'Australia': 'au',
    'Austria': 'at'
}

def get_top_songs():
    result = {}

    for country, country_code in COUNTRY_CODES.items():
        api_url = f'https://api.deezer.com/chart/{country_code}/tracks'

        try:
            response = requests.get(api_url)
            data = response.json()

            songs = []
            for i, entry in enumerate(data['data']):
                if i >= 5:
                    break

                song = {
                    'title': entry['title'],
                    'artist': entry['artist']['name'],
                    'position': entry['position'],
                }
                songs.append(song)

            result[country] = songs

        except requests.exceptions.RequestException as e:
            result[country] = {'error': str(e)}

    return json.dumps(result)

if __name__ == '__main__':
    top_songs = get_top_songs()
    print(top_songs)
