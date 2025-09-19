import cv2
import datetime
import os
import json
import time
from flask import Flask, Response
from flask import render_template



cam = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

is_recording = False
writer=None
current_path=None
start_ts=None



fps = cam.get(cv2.CAP_PROP_FPS)
if not fps or fps <= 30 :
    fps = 30

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
extension = ".mp4"

folder_clips = "clips"



h = cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
w = cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
 
h_get = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
w_get = cam.get(cv2.CAP_PROP_FRAME_WIDTH)

size = (int(w_get),int(h_get))


print(f'The Height is {h_get}, the Width is {w_get}...')


       

def generate_frames():
    while cam.isOpened():
        ret, frame = cam.read()
        if not ret:
            print('The frame was not read!')
            break

        if is_recording and writer != None:
                writer.write(frame)
        else:
            ...
        

        #cv2.imencode leva 3 args, o formato, a imagem, params de qualidade
        #serve para alocar a imagem em um pedaco da memoria temporario
        retval, buf = cv2.imencode('.jpg', frame,[int(cv2.IMWRITE_JPEG_QUALITY), 80])

        #retval é uma bool que fala se a operacao de encodar teve sucesso
        #buf é um array NumPy que diz os bytes contidos nos dados da imagem encodada 
        #print(retval, buf)
        frame_bytes = buf.tobytes()

        

        
        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" +
               frame_bytes +
               b"\r\n")
        




        
app = Flask(__name__)



@app.route('/')
def homepage():
    return render_template("view.html")


@app.route('/video')
def index(): 
    return Response(generate_frames(), 
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/start', methods=['POST'])
def recording():
    global is_recording, writer, current_path, start_ts, writer

    start_ts = time.time()

    now = datetime.datetime.now()

    timestamp_formatado = now.strftime('%Y%m%d-%H%M%S')
    archive_name= (f"teste_{timestamp_formatado}{extension}")
    path = os.path.join(folder_clips, archive_name)

    current_path = path

    
    

    if not os.path.exists(folder_clips):
        os.makedirs(folder_clips)
        print(f"Pasta '{folder_clips}' criada!")

    if is_recording:
        return('Ja esta gravando!'), 409
    else:
        is_recording = True
        writer = cv2.VideoWriter(path, fourcc, fps, size)
        
        
        
        return('Começou a gravar!')

@app.route('/stop', methods = ['POST'])
def stop_recording():

    global is_recording, writer, current_path, start_ts, writer

    if not is_recording:
        return 409


    is_recording = False
    if writer != None:
        writer.release()
        writer = None
    duration_sec = time.time() - start_ts
    byte_size = os.path.getsize(current_path)
    
    video_data = {
        "current_path" : current_path,
        "duration_sec" : duration_sec,
        "size_bytes" : byte_size,
    }
    return json.dumps(video_data)
    




app.run(host='0.0.0.0', port=8000)

cam.release()