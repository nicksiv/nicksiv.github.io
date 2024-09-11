---
title: Using Youtube downloader
cdate: 2023-08-10
tags: #music
---

yt-dlp is a perfect utility for downloading youtube videos, even playlists.
I'm keeping a note for the playlist to audio mp3s command in case I lose it.

```
# Playlist
yt-dlp --ignore-errors --format bestaudio --extract-audio --audio-format mp3 --audio-quality 160K --output "%(title)s.%(ext)s" --yes-playlist '<YouTube playlist URL>'

# Audio only mp3
yt-dlp --ignore-errors --format bestaudio --extract-audio --audio-format mp3 --audio-quality 160K --output "%(title)s.%(ext)s" <Video URL>
```

## video (list formats and choose format id)

`yt-dlp --list-formats https://www.youtube.com/watch?v=f6wtF_2eyrU`

`yt-dlp -f 140 https://www.youtube.com/watch?v=f6wtF_2eyrU`

!! best available video+audio
`yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" https://www.youtube.com/watch?v=cTLTG4FTNBQ&pp=ygULbmlrIGtlcnNoYXc%3D`


References:
* <https://www.linuxuprising.com/2019/10/how-to-download-youtube-playlist-and.html>


