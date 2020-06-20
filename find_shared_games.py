import sys
from User import User

def create_user_objects():
    friends = []
    with open("friends_list.txt") as file_in:
        for line in file_in:
            line_list = line.split(", ")
            username = line_list[0]
            profile_url = line_list[1].rstrip()
            friend = User(username=username, url=profile_url)
            friends.append(friend)
    return friends

def main():
    friends = create_user_objects()
    common_games_set = None
    for friend in friends:
        if common_games_set == None:
            common_games_set = friend.games_dict
        else:
            common_games_set = common_games_set.intersection(friend.games_dict)
    
    common_games_list = list(common_games_set)
    common_games_list.sort()
    for game in common_games_list:
        print(game)

if __name__ == "__main__":
    main()