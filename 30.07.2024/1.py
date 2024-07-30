def can_modify_to_advance(usernames):
    results = []
    for username in usernames:
        sorted_username = ''.join(sorted(username))
        if sorted_username < username:
            results.append("YES")
        else:
            results.append("NO")
    return results
n = int(input().strip())
usernames = [input().strip() for _ in range(n)]
results = can_modify_to_advance(usernames)
for result in results:
    print(result)
