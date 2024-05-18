import asyncio
import websockets
from textblob import TextBlob

async def server(ws, path):
    while True:
        resp = await ws.recv()
        text = TextBlob(resp).sentiment
        #polarity (-1, 1), subjectivity (0, 1)
        polar = text.polarity
        subj = text.subjectivity

        if polar >= -1 and polar < -0.5:
            if subj < 0.2 and subj >= 0:
                print("You have a negative sentiment fact")
            elif subj >= 0.2 and subj < 0.5:
                print("Your sentence has negative sentiment")
            else:
                print("You have a negative sentiment opinion")
        elif polar >= -0.5 and polar < 0.5:
            if subj < 0.2 and subj >= 0:
                print("You have a neutral sentiment fact")
            elif subj >= 0.2 and subj < 0.5:
                print("Your sentence has neutral sentiment")
            else:
                print("You have a neutral sentiment opinion")
        else:
            if subj < 0.2 and subj >= 0:
                print("You have a positive sentiment fact")
            elif subj >= 0.2 and subj < 0.5:
                print("Your sentence has positive sentiment")
            else:
                print("You have a positive sentiment opinion")


loop = asyncio.get_event_loop()
loop.run_until_complete(websockets.serve(server, 'localhost', 8080))
loop.run_forever()