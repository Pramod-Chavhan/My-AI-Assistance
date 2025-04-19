from asyncio import sleep
import multiprocessing
import subprocess

# from video import play_video
# def video():
#         video_path = "C:/Users/pramo/OneDrive/Desktop/jarvisUI/jarvis-main/y.mp4"
#         play_video(video_path)

# To run Jarvis
def startJarvis():
        print("Process 1 is running.")
        from main import start
        start()

# To run hotword
def listenHotword():
        # Code for process 2
        print("Process 2 is running.")
        from engine.features import hotword
        hotword()


# Start both processes
if __name__ == '__main__':
        # p0 = multiprocessing.Process(target=video)
        p1 = multiprocessing.Process(target=startJarvis)
        p2 = multiprocessing.Process(target=listenHotword)
        # p0.start()
        p1.start()
        #subprocess.call([r'device.bat'])
        p2.start()
        p1.join()

        if p2.is_alive():
            p2.terminate()
            p2.join()

        print("system stop")