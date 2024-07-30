#There is a Specific Need for Changes in a List of Usernames. In a given List of Usernames — For Each Username — If the Username can be Modified and Moved Ahead in a Dictionary.
#The Allowed Modification is that Alphabets can change Positions in the Given Username.
def username(usernames):
    results = []
    for username in usernames:
        # Get the lexicographically smallest permutation
        sorted_username = ''.join(sorted(username))
        if sorted_username < username:
            results.append("YES")
        else:
            results.append("NO")
    return results
username=input("")
print(username(username))

