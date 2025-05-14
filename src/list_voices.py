import edge_tts

async def main():
    voices = await edge_tts.list_voices()
    for voice in voices:
        if voice["Locale"].startswith("sv-SE"):
            print(f"{voice['ShortName']} - {voice['Gender']}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main()) 