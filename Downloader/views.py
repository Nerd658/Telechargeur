from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
import yt_dlp

@csrf_protect
def youtube(request):
    messages = []
    if request.method == "POST":
        link = request.POST.get("video_url")
        ydl_opts = {
            'outtmpl': 'downloads/%(title)s.%(ext)s',
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            messages.append("Video download successfully!")
        except Exception as e:
            messages.append(f"An error occurred: {e}")
    
    return render(request, "downloader.html", {'messages': messages})


    
    

# Create your views here.
