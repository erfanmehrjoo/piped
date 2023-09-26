import re

test_links = "https://www.youtube.com/watch?v=VWhthouhuEA&ab_channel=Vigiland"

pattern = r'(?:https?:\/\/)?(?:[0-9A-Z-]+\.)?(?:youtube|youtu|youtube-nocookie)\.(?:com|be)\/(?:watch\?v=|watch\?.+&v=|embed\/|v\/|.+\?v=)?([^&=\n%\?]{11})'

result = re.findall(pattern, test_links, re.MULTILINE | re.IGNORECASE)[0]

print(result)