s = input().strip()

last_seen = {}
left = 0
right = 0
max_len = 0

while right < len(s):
    ch = s[right]

    if ch in last_seen and last_seen[ch] >= left:
        left = last_seen[ch] + 1

    last_seen[ch] = right

    current_len = right - left + 1
    max_len = max(max_len, current_len)

    right += 1

print(max_len)
