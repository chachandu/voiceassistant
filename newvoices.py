import os 
import pygame

def speak(text):
    voice = 'en-US-MichelleNeural'
    chunks = text.split()
    chunks_size = 100
    chunks = [chunks[i:i + chunks_size]for i in range (0,len(chunks),chunks_size)]

    for chunks in chunks: 
        text = ' '.join(chunks)
        data = f'python -m edge_tts --voice "{voice}" --text "{text}" --write-media "data.mp3"'
        os.system(data)
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("data.mp3")

        try:
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

        except Exception as e:
            print(e)

        finally:
            pygame.mixer.music.stop()
            pygame.mixer.quit()          

    return True       

# Name: en-AU-NatashaNeural
# Gender: Female

# Name: en-AU-WilliamNeural
# Gender: Male

# Name: en-CA-ClaraNeural
# Gender: Female

# Name: en-CA-LiamNeural
# Gender: Male

# Name: en-GB-LibbyNeural
# Gender: Female

# Name: en-GB-MaisieNeural
# Gender: Female

# Name: en-GB-RyanNeural
# Gender: Male

# Name: en-GB-SoniaNeural
# Gender: Female

# Name: en-GB-ThomasNeural
# Gender: Male

# Name: en-HK-SamNeural
# Gender: Male

# Name: en-HK-YanNeural
# Gender: Female

# Name: en-IE-ConnorNeural
# Gender: Male

# Name: en-IE-EmilyNeural
# Gender: Female

# Name: en-IN-NeerjaExpressiveNeural
# Gender: Female

# Name: en-IN-NeerjaNeural
# Gender: Female

# Name: en-IN-PrabhatNeural
# Gender: Male

# Name: en-KE-AsiliaNeural
# Gender: Female

# Name: en-KE-ChilembaNeural
# Gender: Male

# Name: en-NG-AbeoNeural
# Gender: Male

# Name: en-NG-EzinneNeural
# Gender: Female

# Name: en-NZ-MitchellNeural
# Gender: Male

# Name: en-NZ-MollyNeural
# Gender: Female

# Name: en-PH-JamesNeural
# Gender: Male

# Name: en-PH-RosaNeural
# Gender: Female

# Name: en-SG-LunaNeural
# Gender: Female

# Name: en-SG-WayneNeural
# Gender: Male

# Name: en-TZ-ElimuNeural
# Gender: Male

# Name: en-TZ-ImaniNeural
# Gender: Female

# Name: en-US-AnaNeural
# Gender: Female

# Name: en-US-AriaNeural
# Gender: Female

# Name: en-US-ChristopherNeural
# Gender: Male

# Name: en-US-EricNeural
# Gender: Male

# Name: en-US-GuyNeural
# Gender: Male

# Name: en-US-JennyNeural
# Gender: Female

# Name: en-US-MichelleNeural
# Gender: Female

# Name: en-US-RogerNeural
# Gender: Male

# Name: en-US-SteffanNeural
# Gender: Male



