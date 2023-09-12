import asyncio
import websockets
import json


def get_all_keys(json_obj, parent_key=''):
    keys = set()  # Use a set to store unique keys
    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            current_key = f"{parent_key}.{key}" if parent_key else key
            keys.add(current_key)
            keys.update(get_all_keys(value, current_key))
    elif isinstance(json_obj, list):
        for index, item in enumerate(json_obj):
            current_key = f"{parent_key}[{index}]"
            keys.update(get_all_keys(item, current_key))
    return keys

async def client():

    async with websockets.connect("ws://localhost:8080/2579048", max_size=300000000, ping_timeout=20*60) as websocket:
        count =  0
        teams_data = []
        while True:
            count = count + 1
            message = input("Enter a message to send (or 'exit' to quit): ")

            if message.lower() == 'exit':
                break

            await websocket.send("")
            response = await websocket.recv()
            json_data = json.loads(response)

            # with open(f'data_files/event__{count}.json', 'w') as json_file:
            #     json_file.write(response)

            # for event in json_data["events"]:
            #     if event["type"] not in event_types:
            #         event_types.append(event["type"])
            #         print(event["type"])

            # if 'seriesState' in json_data["events"][0]:
            #     count = 0
            #     for game in json_data["events"][0]['seriesState']['games']:
            #         count = count + len(game['segments'])
            #     print(count, json_data["occurredAt"])

                # print(len(json_data["events"][0]['seriesState']['segments']))
            # if json_data["events"][0]['type'] == 'player-killed-player':
            #     event_data = json_data["events"][0]
            #     teams_data = []
                
            #     if 'seriesState' in event_data and 'teams' in event_data['seriesState']:
            #         # print(team['players'])
            #         for team in event_data['seriesState']['teams']:
            #             players = [
            #                 {
            #                     'name': player['name'],
            #                     'id': player['id'],
            #                     'kills': player['kills'],
            #                     'deaths': player['deaths'],
            #                     'headshots': player['headshots']
            #                 }
            #                 for player in team['players']
            #             ]
                        
            #             # players.sort(key=lambda x: x['kills'] / x['deaths'], reverse=True)
                        
            #             teams_data.append({
            #                 'id': team['id'],
            #                 'name': team['name'],
            #                 'score': team['score'],
            #                 'players': players
            #             })
                

asyncio.get_event_loop().run_until_complete(client())
