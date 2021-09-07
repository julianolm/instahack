import instaloader

class DNFBError(Exception):
    pass

class InstagramConnectionError(DNFBError):
    def __init__(self, message="we could not connect to instagram"):
        self.message = message

class UserNotFoundError(DNFBError):
    def __init__(self, message=""):
        self.message = message

class PrivateAccountError(DNFBError):
    def __init__(self, message):
        self.message = message

class TooBigAccountError(DNFBError):
    def __init__(self, message):
        self.message = message


def do_not_follow_user_back(queried_user):
    try:
        # Get instaloader instance
        L = instaloader.Instaloader()

        # Login or load session
        username = "whodonotfollowmeback" # "instahackworker"
        password = "zipinstagram"                     # "dumbledore"
        L.login(username, password)  # (login)
    except:
        raise InstagramConnectionError()

    try:
        # Obtain profile metadata
        profile = instaloader.Profile.from_username(L.context, queried_user)
    except:
        raise UserNotFoundError("we could not find user %s"%queried_user)

    if profile.is_private:
        raise PrivateAccountError(f"'{queried_user}' is a private profile and we can not access its data.")

    if profile.followers > 2500:
        raise TooBigAccountError("user %s has too many followers" % queried_user)
    if profile.followees > 2500:
        raise TooBigAccountError("user %s follows too many users" % queried_user)

    followee_list = []
    follower_dict = {}
    not_follow_back = []

    for followee in profile.get_followees():
        followee_list.append(followee.username)

    for follower in profile.get_followers():
        follower_dict[follower.username] = 1

    for followee in followee_list:
        try:
            val = follower_dict[followee]
        except:
            not_follow_back.append(followee)

    return not_follow_back