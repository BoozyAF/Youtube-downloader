from pytube import YouTube
from colorama import init, Fore
 
def on_complete(stream, filepath):
    print("Yea bitch, it's downloaded!")
    print(filepath)
 
def on_progress(stream, chunk, bytes_remaining):
    progress_bar = f'{round(100 - (bytes_remaining / stream.filesize * 100),2)}%'
    print(progress_bar)
 
init()
link = input('Youtube link: ')
video = YouTube(link, on_complete_callback = on_complete, on_progress_callback = on_progress)
 
# Youtube video stats
print(Fore.RED + f'Title:  \033[39m {video.title}')
print(Fore.RED + f'Length: \033[39m {round(video.length / 60,2)} minutes')
print(Fore.RED + f'Views:  \033[39m {video.views}')
print(Fore.RED + f'Channel: \033[39m {video.author}')
 
# Download
print(
    Fore.RED + 'Settings:' + 
    Fore.GREEN + '(b)est quality \033[39m|' + 
    Fore.YELLOW + '(w)orst quality \033[39m|' + 
    Fore.BLUE + '(a)udio only \033[39m| (e)xit')
choice = input('choice: ')
 
match choice:
    case 'b':
        video.streams.get_highest_resolution().download(r'Folder location here')
    case 'w':
        video.streams.get_lowest_resolution().download(r'Folder location here')
    case 'a':
        video.streams.get_audio_only().download(r'Folder location here')