from concurrent.futures import Executor, ThreadPoolExecutor
from faulthandler import is_enabled
from pickle import FALSE, PicklingError
import websockets
import asyncio
import pyaudio
import wave
import os
from queue import Queue
import logging

logging.basicConfig(level=logging.DEBUG)

os.environ['PYTHONASYNCIODEBUG'] = '1'
os.environ['PYTHONDEVMODE'] = '1'

q = Queue()
playing = -1

HOST = "192.168.90.250"
PORT = 8484
CHUNK = 1024
MIN_MSG = 0
MAX_MSG = 25
INIT_MSG = MIN_MSG-1
AUDIO_DIR = "C:\\Users\\Dante\\Desktop\\WebSocket\\server\\audio\\"
audio = [AUDIO_DIR + "1_ADDUARSI.wav",
        AUDIO_DIR + "2_INSEMPRARSI.wav",
        AUDIO_DIR + "3_INMIARSI_INTUARSI.wav",
        AUDIO_DIR + "4_SITIRE.wav",
        AUDIO_DIR + "5_INDRACARSI.wav",
        AUDIO_DIR + "6_ADDENTARE.wav",
        AUDIO_DIR + "7_MUSO.wav",
        AUDIO_DIR + "8_CIGOLARE.wav",
        AUDIO_DIR + "9_MENSOLA.wav",
        AUDIO_DIR + "10_FERTILE.wav",
        AUDIO_DIR + "11_MUFFA.wav",
        AUDIO_DIR + "12_ALTO.wav",
        AUDIO_DIR + "13_BELLO.wav",
        AUDIO_DIR + "14_BOCCA.wav",
        AUDIO_DIR + "15_CASA.wav",
        AUDIO_DIR + "16_RINGHIARE.wav",
        AUDIO_DIR + "17_SBADIGLIARE.wav",
        AUDIO_DIR + "18_SPUTARE.wav",
        AUDIO_DIR + "19_TESCHIO.wav",
        AUDIO_DIR + "20_UNO.wav",
        AUDIO_DIR + "21_MILLE.wav",
        AUDIO_DIR + "22_INMILLARSI.wav",
        AUDIO_DIR + "23_PUNTO.wav",
        AUDIO_DIR + "24_CERCHIO.wav",
        AUDIO_DIR + "25_STELLE.wav"]

class Server():

    def ServerInfo():
        print("Server listening on Port " + str(PORT) + " ip: " + HOST)


    def play(i):
        global playing        
        global stream
        global p
        
        if playing==INIT_MSG:
            print("Playing " + str(i))
            playing = i

            global wf
            global data

            if(int(i) <= 24):
                wf = wave.open(audio[int(i)], 'rb')

            # instantiate PyAudio
            p = pyaudio.PyAudio()

            # open stream
            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)

            # read data
            data = wf.readframes(CHUNK)

            # play stream
            while (len(data) > 0) and (stream.is_active()):
                stream.write(data)
                data = wf.readframes(CHUNK)

            # stop stream
            if stream.is_active():
                stream.stop_stream()
                stream.close()
                # close PyAudio
                p.terminate()
               
            #q.get()
            playing=INIT_MSG

        elif playing!=i:  # already playing this audio, ignore it!
            print("Already playing " + str(playing))
            try:
                print("Stop playing " + str(playing))
                # stop stream
                stream.stop_stream()
                stream.close()
                
                # close PyAudio
                p.terminate()
                playing=INIT_MSG
                if i != MAX_MSG: #ignore STOP message?
                    Server.play(i)

            except Exception:
                print("Errore PyAudio: " + str(Exception))                




    async def socket(websocket):

        print("A client just connected to the Socket")

        async for message in websocket:
            print("Received message from client: " + message)
            msg = int(message)
            
            if msg >= MIN_MSG and msg <= MAX_MSG:
                try:
                    asyncio.get_event_loop().run_in_executor(None, Server.play, msg)
                except Exception:
                    print("Errore ThreadPoolExecutor: ", Exception)

if __name__ == "__main__":
    Server.ServerInfo()

    start_server = websockets.serve(Server.socket, HOST, PORT)
    asyncio.get_event_loop().set_default_executor(ThreadPoolExecutor())
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()