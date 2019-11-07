import sys
import os

channel_name = sys.argv[1]
stream_quality = sys.argv[2]
chat_command = 'firefox -new-window https://www.twitch.tv/popout/' + channel_name + '/chat &'
stream_command = "youtube-dl -f " + stream_quality + " -o - 'http://www.twitch.tv/" + channel_name + "' | vlc - &"

os.system(stream_command)
os.system(chat_command)
