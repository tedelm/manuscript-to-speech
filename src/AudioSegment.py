import asyncio
import edge_tts
import subprocess
import os
import csv

async def generate_speech():
    # Skapa kommunikatorer med olika röster
    # sv-SE-SofieNeural är en kvinnlig svensk röst
    # sv-SE-MattiasNeural är en manlig svensk röst
    nilla_voice = "sv-SE-SofieNeural"
    nils_voice = "sv-SE-MattiasNeural"
    en_jenny_voice = "en-US-JennyNeural"
    en_christopher_voice = "en-US-ChristopherNeural"
    en_aria_voice = "en-US-AriaNeural"
    # Skapa audio-mappen om den inte finns
    os.makedirs("audio", exist_ok=True)
    
    # Lista för att spara alla genererade filer
    generated_files = []
    
    # Läs in dialoger från CSV-filen
    dialogues = []
    with open('dialogues.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            dialogues.append((row['voice'], row['dialog']))
    
    # Loopa genom alla dialoger
    for i, (speaker, text) in enumerate(dialogues, 1):
        # Välj röst baserat på talare
        #voice = nilla_voice if speaker == "nilla" else nils_voice
        if speaker == "nilla":
            voice = nilla_voice
        elif speaker == "nils":
            voice = nils_voice
        elif speaker == "en_jenny":
            voice = en_jenny_voice
        elif speaker == "en_christopher":
            voice = en_christopher_voice
        elif speaker == "en_aria":
            voice = en_aria_voice
        else:
            voice = nils_voice
        

        # Skapa filnamn med nummer
        file_path = f"audio/dialog_{i:02d}_{speaker}.mp3"
        
        # Generera tal
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(file_path)
        
        # Lägg till filen i listan
        generated_files.append(file_path)
        
        # Vänta en kort stund mellan varje generering
        await asyncio.sleep(0.5)
    
    # Kontrollera att alla filer existerar
    for file_path in generated_files:
        if not os.path.exists(file_path):
            raise Exception(f"Ljudfilen {file_path} kunde inte skapas")
    
    return generated_files

# Kör funktionen
generated_files = asyncio.run(generate_speech())
print("Genererade ljudfiler:", generated_files)



