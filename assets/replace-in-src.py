import os
import re

folder_path = "~/nicksiv.gitub.io/src/"
for filename in os.listdir(folder_path):
    if filename.endswith(".html"):
        filepath = os.path.join(folder_path, filename)
        with open(filepath, 'r+', encoding='utf-8') as f:
            content = f.read()
            content = re.sub(r'^\s*<body[^>]*>', '', content, flags=re.IGNORECASE)
            content = re.sub(r'</body>\s*$', '', content, flags=re.IGNORECASE)
            f.seek(0)
            f.write(content)
            f.truncate()
