import asyncio
import websockets
import glob
import json
import time
import ssl

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain('/<path-to->/fullchain.pem', '/<path-to->/privkey.pem')


async def handle_connection(ws, path):
    async def send_line(line):
        await ws.send(json.dumps(line))
    await ws.ping()

    try:
        files = f'../data_files/csgo/CCT-Online-Finals-1{path}_events.jsonl'
        if files:
            with open(files, 'r') as events_file:
                count = 0
                for line in events_file:
                    count = count + 1
                    await send_line(json.loads(line.strip()))
        else:
            print(f"No matching files found for path: {path}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await ws.close()

async def main():
    server = await websockets.serve(handle_connection, "0.0.0.0", 8080, ssl=ssl_context)
    print("WebSocket server is running on port 8080")
    await server.wait_closed()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()
