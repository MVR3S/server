from concurrent.futures import ThreadPoolExecutor
import websockets
import asyncio
import pyaudio
import wave
import os
import logging

try:
    import serial
except:
    print("ERRORE IMPORT SERIAL")

#################################################################
print("***************************")
print("CREAZIONE OGGETTO PORTA SERIALE -- RIGA 16")
print("***************************")
try:
    arduino = serial.Serial(port='COM6', baudrate=9600, timeout=.1)
    print("***************************")
    print("OGGETTO PORTA SERIALE CREATO -- RIGA 21")
    print("***************************")
except:
    print("\nerrore apertura porta seriale")
#################################################################

logging.basicConfig(level=logging.DEBUG)

os.environ['PYTHONASYNCIODEBUG'] = '1'
os.environ['PYTHONDEVMODE'] = '1'

playing = -1

HOST = "192.168.90.250"

PORT = 8484
CHUNK = 1024
MIN_MSG = 0
MAX_MSG = 1000
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
        AUDIO_DIR + "25_STELLE.wav",
        AUDIO_DIR + "26_BIOGRAFIA.wav",
        AUDIO_DIR + "27_VERSI.wav",
        AUDIO_DIR + "28_PARLAMI_DI_TE.wav",
        AUDIO_DIR + "29_QUANDO_SEI_NATO.wav",
        AUDIO_DIR + "30_RACCONTAMI_DELLA_TUA_FAMIGLIA.wav",
        AUDIO_DIR + "31_COSA_FACEVANO_I_TUOI.wav",
        AUDIO_DIR + "32_E_BEATRICE.wav",
        AUDIO_DIR + "33_HAI_FRATELLI.wav",
        AUDIO_DIR + "34_SEI_SPOSATO.wav",
        AUDIO_DIR + "35_HAI_FIGLI.wav",
        AUDIO_DIR + "36_COSA_SUCCEDE_A_FIRENZE.wav",
        AUDIO_DIR + "37_TI_PIACE_LA_SCUOLA.wav",
        AUDIO_DIR + "38_CHI_ERA_IL_TUO_PRIMO_AMORE.wav",
        AUDIO_DIR + "39_HAI_UN_MIGLIORE_AMICO.wav",
        AUDIO_DIR + "40_E_UNA_MIGLIORE_AMICA.wav",
        AUDIO_DIR + "41_HAI_UN_LAVORO.wav",
        AUDIO_DIR + "42_E_ESILIO.wav",
        AUDIO_DIR + "43_INCIPIT_INFERNO.wav",
        AUDIO_DIR + "44_LA_PORTA.wav",
        AUDIO_DIR + "45_AMORE.wav",
        AUDIO_DIR + "46_MINOSSE.wav",
        AUDIO_DIR + "47_VUOLSI_COSI.wav",
        AUDIO_DIR + "48_PAOLO_E_FRANCESCA.wav",
        AUDIO_DIR + "49_ULISSE.wav",
        AUDIO_DIR + "50_CONTE_UGOLINO.wav",
        AUDIO_DIR + "51_USCITA_INFERNO.wav",
        AUDIO_DIR + "52_INCIPIT_PURGATORIO.wav",
        AUDIO_DIR + "53_CATONE.wav",
        AUDIO_DIR + "54_INVETTIVA_ITALIA.wav",
        AUDIO_DIR + "55_INVETTIVA_ITALIA2.wav",
        AUDIO_DIR + "56_USCITA_PURGATORIO.wav",
        AUDIO_DIR + "57_INCIPIT_PARADISO.wav",
        AUDIO_DIR + "58_PREGHIERA_VERGINE.wav",
        AUDIO_DIR + "59_OCCHI_BEATRICE.wav",
        AUDIO_DIR + "60_USCITA_PARADISO.wav"]

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

            ##################################
            print("***************************")
            print("AVVIO SCRITTURA SU SERIALE 1 -- RIGA 125")
            print("***************************")
            try:
                arduino.write(bytes("1", 'utf-8'))
                print("***************************")
                print("SCRITTURA SU SERIALE ESEGUITA 1 -- RIGA 130")
                print("***************************")
            except:
                print("\nerrore trasmissione")
            ##################################

            if(int(i) <= 60):
                print("***************************")
                print("APERTURA FILE AUDIO -- RIGA 138")
                print("***************************")
                wf = wave.open(audio[int(i)], 'rb')

            # instantiate PyAudio
            p = pyaudio.PyAudio()

            # open stream
            print("***************************")
            print("APERTURA STREAM AUDIO -- RIGA 147")
            print("***************************")
            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),   
                            output=True)

            # read data
            print("***************************")
            print("LETTURA DATI AUDIO -- RIGA 156")
            print("***************************")
            data = wf.readframes(CHUNK)

            # play stream
            print("***************************")
            print("RIPRODUZIONE FILE AUDIO -- RIGA 162")
            print("***************************")
            while (len(data) > 0) and (stream.is_active()):
                stream.write(data)
                data = wf.readframes(CHUNK)
            print("***************************")
            print("FINE RIPRODUZIONE FILE AUDIO -- RIGA 168")
            print("***************************")

            # stop stream
            if stream.is_active():

                ##################################
                print("***************************")
                print("AVVIO SCRITTURA SU SERIALE 0 -- RIGA 176")
                print("***************************")
                try:
                    arduino.write(bytes("0", 'utf-8'))
                    print("***************************")
                    print("SCRITTURA SU SERIALE ESEGUITA 0 -- RIGA 181")
                    print("***************************")
                except:
                    print("\n errore trasmissione")
                ##################################

                print("***************************")
                print("STOP AUDIO -- RIGA 188")
                print("***************************")
                stream.stop_stream()
                stream.close()
                # close PyAudio
                p.terminate()
               
            playing=INIT_MSG

        elif playing!=i:  # already playing this audio, ignore it!
            print("Already playing " + str(playing))
            try:
                print("Stop playing " + str(playing))

                ##################################
                print("***************************")
                print("AVVIO SCRITTURA SU SERIALE 0 -- RIGA 205")
                print("***************************")
                try:
                    arduino.write(bytes("0", 'utf-8'))
                    print("***************************")
                    print("SCRITTURA SU SERIALE ESEGUITA 0 -- RIGA 210")
                    print("***************************")
                except:
                    print("\n errore trasmissione")
                ##################################

                print("***************************")
                print("STOP AUDIO GIA' ATTIVO -- RIGA 217")
                print("***************************")
                # stop stream
                if stream.is_active():
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

    print("***************************")
    print("INIZIO INIZIALIZZAZIONE 0 -- RIGA 239")
    print("***************************")
    try:
        arduino.write(bytes("0", 'utf-8'))
        print("***************************")
        print("INIZIALIZZAZIONE ESEGUITA 0 -- RIGA 244")
        print("***************************")
    except:
        print("\nerrore trasmissione")

    asyncio.get_event_loop().set_default_executor(ThreadPoolExecutor())
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()