tts = requests.post(
    "https://api.cartesia.ai/tts/bytes",
    json={
        "model_id": "sonic-turbo",
        "transcript": resposta,
        "voice": {
            "mode": "id",
            "id": "f68ba98a-5a00-4dff-97ca-f7bde17ddf8a"
        },
        "output_format": {
            "container": "wav",
            "encoding": "pcm_s16le",
            "sample_rate": 16000
        }
    },
    headers={
        "X-API-Key": os.getenv("CARTESIA_API_KEY"),
        "Cartesia-Version": "2026-03-01",  # 🔥 ESSENCIAL
        "Content-Type": "application/json"
    }
)
