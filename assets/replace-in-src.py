import os
import re

folder_path = "/home/nick/nicksiv.github.io/src/"
for filename in os.listdir(folder_path):
    if filename.endswith(".html"):
        filepath = os.path.join(folder_path, filename)
        with open(filepath, 'r+', encoding='utf-8') as f:
            content = f.read()
            # Remove opening body tag (anywhere in document)
            content = re.sub(r'<body[^>]*>', '', content, flags=re.IGNORECASE)

            # Remove closing body tag (anywhere in document)
            content = re.sub(r'</body>', '', content, flags=re.IGNORECASE)
            # Remove title tag and its content
            content = re.sub(r'<title>.*?</title>', '', content, flags=re.IGNORECASE)
           # Remove any resulting blank lines
            content = '\n'.join(line for line in content.split('\n') if line.strip())

            f.seek(0)
            f.write(content)
            f.truncate()
