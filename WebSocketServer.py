from concurrent.futures import Executor, ThreadPoolExecutor
import websockets
import asyncio
import pyaudio
import wave
import os
from queue import Queue
import logging

os.environ['PYTHONASYNCIODEBUG'] = '1'
os.environ['PYTHONDEVMODE'] = '1'

q = Queue()

global IsPlaying
IsPlaying = False
HOST = "192.168.1.196"
PORT = 8484
CHUNK = 1024

audio = ["C:\\PyProjects\\server\\audio\\1_ADDUARSI.wav",
        "C:\\PyProjects\\server\\audio\\2_INSEMPRARSI.wav",
        "C:\\PyProjects\\server\\audio\\3_INMIARSI_INTUARSI.wav",
        "C:\\PyProjects\\server\\audio\\4_SITIRE.wav",
        "C:\\PyProjects\\server\\audio\\5_INDRACARSI.wav",
        "C:\\PyProjects\\server\\audio\\6_ADDENTARE.wav",
        "C:\\PyProjects\\server\\audio\\7_MUSO.wav",
        "C:\\PyProjects\\server\\audio\\8_CIGOLARE.wav",
        "C:\\PyProjects\\server\\audio\\9_MENSOLA.wav",
        "C:\\PyProjects\\server\\audio\\10_FERTILE.wav",
        "C:\\PyProjects\\server\\audio\\11_MUFFA.wav",
        "C:\\PyProjects\\server\\audio\\12_ALTO.wav",
        "C:\\PyProjects\\server\\audio\\13_BELLO.wav",
        "C:\\PyProjects\\server\\audio\\14_BOCCA.wav",
        "C:\\PyProjects\\server\\audio\\15_CASA.wav",
        "C:\\PyProjects\\server\\audio\\16_RINGHIARE.wav",
        "C:\\PyProjects\\server\\audio\\17_SBADIGLIARE.wav",
        "C:\\PyProjects\\server\\audio\\18_SPUTARE.wav",
        "C:\\PyProjects\\server\\audio\\19_TESCHIO.wav",
        "C:\\PyProjects\\server\\audio\\20_UNO.wav",
        "C:\\PyProjects\\server\\audio\\21_MILLE.wav",
        "C:\\PyProjects\\server\\audio\\22_INMILLARSI.wav",
        "C:\\PyProjects\\server\\audio\\23_PUNTO.wav",
        "C:\\PyProjects\\server\\audio\\24_CERCHIO.wav",
        "C:\\PyProjects\\server\\audio\\25_STELLE.wav"]

class Server():
    #global IsPlaying
    #IsPlaying = False


    def ServerInfo():
        print("Server listening on Port " + str(PORT) + " ip: " + HOST)




    def play(i):
        executor = ThreadPoolExecutor()
        if q.qsize() == 0:
            q.put(1)

            global wf
            global p
            global stream
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
            while len(data) > 0:
                stream.write(data)
                data = wf.readframes(CHUNK)

            # stop stream
            stream.stop_stream()
            stream.close()

            # close PyAudio
            p.terminate()

            q.get()
        else:
            try:
                # stop stream
                stream.stop_stream()
                stream.close()

                # close PyAudio
                p.terminate()
            
                q.get()
            except Exception:
                print("Errore PyAudio: " + Exception)



    async def socket(websocket):

        print("A client just connected")

        async for message in websocket:
                print("Received message from client: " + message)
                if message == 'a':
                    i="0"
                    
                    asyncio.get_event_loop().run_in_executor(None, Server.play, i)
                elif message == 'b':
                    i="1"

                    asyncio.get_event_loop().run_in_executor(None, Server.play, i)
                elif message == 'c':
                    i="2"
                    
                    asyncio.get_event_loop().run_in_executor(None, Server.play, i)
                elif message == 'd':
                    i="3"
                    
                    asyncio.get_event_loop().run_in_executor(None, Server.play, i)
                elif message == 'e':
                    i="4"
                    
                    asyncio.get_event_loop().run_in_executor(None, Server.play, i)
                elif message == 'f':
                    i="5"
                    
                    asyncio.get_event_loop().run_in_executor(None, Server.play, i)
                elif message == 'g':
                    i="6"
                    
                    asyncio.get_event_loop().run_in_executor(None, Server.play, i)
                elif message == 'h':
                    i="7"
                    
                    asyncio.get_event_loop().run_in_executor(None, Server.play, i)
                elif message == 'i':
                    i="8"
                    
                    asyncio.get_event_loop().run_in_executor(None, Server.play, i)
                elif message == 'j':
                    i="9"
                    
                    asyncio.get_event_loop().run_in_executor(None, Server.play, i)
                elif message == 'k':
                    i="10"
                    
                    asyncio.get_event_loop().run_in_executor(None, Server.play, i)
                elif message == 'l':
                    i="11"
                    
                    asyncio.get_event_loop().run_in_executor(None, Server.play, i)
                elif message == 'm':
                    i="12"
                    
                    asyncio.get_event_loop().run_in_executor(None, Server.play, i)
                elif message == 'n':
                    i="13"
                    
                    asyncio.get_event_loop().run_in_executor(None, Server.play, i)
                elif message == 'o':
                    i="14"
                    
                    asyncio.get_event_loop().run_in_executor(None, Server.play, i)
                elif message == 'p':
                    i="15"
                    
                    asyncio.get_event_loop().run_in_executor(None, Server.play, i)
                elif message == 'q':
                    i="16"
                    
                    asyncio.get_event_loop().run_in_executor(None, Server.play, i)
                elif message == 'r':
                    i="17"
                    
                    asyncio.get_event_loop().run_in_executor(None, Server.play, i)
                elif message == 's':
                    i="18"
                    
                    asyncio.get_event_loop().run_in_executor(None, Server.play, i)
                elif message == 't':
                    i="19"
                    
                    asyncio.get_event_loop().run_in_executor(None, Server.play, i)
                elif message == 'u':
                    i="20"
                    
                    asyncio.get_event_loop().run_in_executor(None, Server.play, i)
                elif message == 'v':
                    i="21"
                    
                    asyncio.get_event_loop().run_in_executor(None, Server.play, i)
                elif message == 'w':
                    i="22"
                    
                    asyncio.get_event_loop().run_in_executor(None, Server.play, i)
                elif message == 'x':
                    i="23"
                    
                    asyncio.get_event_loop().run_in_executor(None, Server.play, i)
                elif message == 'y':
                    i="24"
                    
                    asyncio.get_event_loop().run_in_executor(None, Server.play, i)
                elif message == 'z':
                    i="25"
                
                    try:
                        asyncio.get_event_loop().run_in_executor(None, Server.play, i)
                    except Exception:
                        print("Errore ThreadPoolExecutor: ", Exception)
                

if __name__ == "__main__":
    Server.ServerInfo()

    #logging.basicConfig(
        #format="%(message)s",
        #level=logging.DEBUG,
        #)

    start_server = websockets.serve(Server.socket, HOST, PORT)
    asyncio.get_event_loop().set_default_executor(ThreadPoolExecutor())
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()