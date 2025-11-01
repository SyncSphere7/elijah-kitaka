#!/usr/bin/env python3

import re

# Read the file
with open('/Users/syncsphere/Desktop/elijah-kitaka/247artists.com/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Old description
old_desc = "The world's most comprehensive ecosystem for creatives, combining Education Technology and a global Network of like - minded artists and industry pros."

# New description
new_desc = "Elijah Kitaka is a soulful Afro-soul artist from Uganda, signed to Swangz Avenue. Experience his unique blend of African rhythms, heartfelt lyrics, and captivating live performances."

# Replace all occurrences
content = content.replace(old_desc, new_desc)

# Write back
with open('/Users/syncsphere/Desktop/elijah-kitaka/247artists.com/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Description updated successfully!")
