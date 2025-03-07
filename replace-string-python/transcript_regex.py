import re

REGEX_REPLACEMENTS = [
    (r"blast\w*", "😤"),
    (r" [-T:+\d]{25}", ""),
    (r"\[support\w*\]", "Agent "),
    (r"\[johndoe\]", "Client"),
]

transcript = """
[support_tom] 2025-01-24T10:02:23+00:00 : What can I help you with?
[johndoe] 2025-01-24T10:03:15+00:00 : I CAN'T CONNECT TO MY BLASTED ACCOUNT
[support_tom] 2025-01-24T10:03:30+00:00 : Are you sure it's not your caps lock?
[johndoe] 2025-01-24T10:04:03+00:00 : Blast! You're right!
"""

for new, old in REGEX_REPLACEMENTS:
    transcript = re.sub(new, old, transcript, flags=re.IGNORECASE)

print(transcript)
