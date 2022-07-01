from gtts import gTTS
from subprocess import call

def converter(question: str, videoImg = ""):
    '''
    Convert the question to video
    '''
    #Conver question to audio
    tts = gTTS(question + ' comment down below')
    tts.save('newQuestion.mp3')

    #Convert audio to video
    call(["ffmpeg", "-y", "-loglevel", "quiet", "-loop", "1", "-framerate", "1", "-i", f"{videoImg}", "-i", "newQuestion.mp3", "-map", "0:v", "-map", "1:a", "-r", "10", "-vf", "scale='iw-mod(iw,2)':'ih-mod(ih,2)',format=yuv420p", "-movflags", "+faststart", "-shortest", "-fflags", "+shortest", "-max_interleave_delta", "100M", "input.mp4"])

    #Add text to the viceo
    call(["ffmpeg", "-y", "-loglevel", "quiet", "-i", "input.mp4", "-vf", "drawtext=fontfile=/usr/share/fonts/truetype/Poppins/Poppins-Regular.ttf:textfile=question.txt:fontcolor=white:fontsize=12:box=1:boxcolor=black@0.5:boxborderw=5:x=(w-text_w)/2:y=(h-text_h)/2", "-codec:a", "copy", "final.mp4"])


