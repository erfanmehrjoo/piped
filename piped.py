import re
#get neccery data from user
print("Haj erfan production was in here.... \n")
youtube_url = input("tell me know your youtube link: ")

# make another function to do a regex stuff on a youtube link
def regexx(url):
    pattern = r'(?:https?:\/\/)?(?:[0-9A-Z-]+\.)?(?:youtube|youtu|youtube-nocookie)\.(?:com|be)\/(?:watch\?v=|watch\?.+&v=|embed\/|v\/|.+\?v=)?([^&=\n%\?]{11})'

    result = re.findall(pattern, url, re.MULTILINE | re.IGNORECASE)[0]
    
    return result

#make our little program functional
def main(youtube_url):
    if "youtube" in youtube_url:
        id = regexx(youtube_url)
        piped_url = f"https://piped.video/v/{id}"
    
        print("piped url : " + piped_url + "\n")
        print("original youtube link: "+ youtube_url)
        
    else:
        print("make sure that you have valid youtube link")
    
   
#call out main function
main(youtube_url)