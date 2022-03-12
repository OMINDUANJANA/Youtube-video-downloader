from moviepy.editor import VideoFileClip
import telebot

bot = telebot.TeleBot("5170739237:AAEZ5oKFb_PQmdHP4oPAl0OXr0ko-_6lGMM")

def convert_to_mp3(filename):
    clip = VideoFileClip(filename)
    clip.audio.write_audiofile(filename[:-4] + ".mp3")
    clip.close()
