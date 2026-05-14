from collections import defaultdict
from typing import List

class Twitter:
    # Class variable, shared accross all instances of the class (like a static variable)
    time = 0

    def __init__(self):
        self.users = defaultdict(User) # id -> User

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].tweet(Twitter.time, tweetId)
        Twitter.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # 1. Your own tweets + Your following tweets
        # Heapify
        # Note: .update() is .extend() but for sets
        user = self.users[userId]
        tweets = user.tweets.copy()
        for following_id in user.following:
            tweets.update(self.users[following_id].tweets)
    
        news_feed = list(tweets)
        news_feed.sort(reverse=True)
        print([tweet_id for _, tweet_id in news_feed[:10]])
        return [tweet_id for _, tweet_id in news_feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].unfollow(followeeId)

    def showUsers(self):
        for item in list(self.users.items()):
            print(item)
    
class User:
    def __init__(self):
        self.tweets = set()
        self.following = set()

    def follow(self, id):
        self.following.add(id)

    def tweet(self, time, id):
        self.tweets.add((time, id))

    def unfollow(self, id):
        if id in self.following:
            self.following.remove(id)

    def __repr__(self):
        return f"Tweets: {self.tweets if self.tweets else "None"}, Following: {self.following if self.following else "None"}"