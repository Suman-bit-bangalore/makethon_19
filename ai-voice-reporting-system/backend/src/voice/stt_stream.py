from google.cloud import speech_v1p1beta1 as speech
import asyncio
import websockets

async def transcribe_stream(websocket, path):
    client = speech.SpeechClient()

    # Configure the audio stream
    audio_stream = speech.StreamingRecognizeRequest(
        audio_content=await websocket.recv()
    )

    # Configure the recognition settings
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    # Create a streaming request
    requests = (speech.StreamingRecognizeRequest(
        audio_content=audio_content
    ) for audio_content in audio_stream)

    # Start the streaming recognition
    responses = client.streaming_recognize(config=config, requests=requests)

    # Process the responses
    async for response in responses:
        for result in response.results:
            await websocket.send(result.alternatives[0].transcript)

start_server = websockets.serve(transcribe_stream, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()