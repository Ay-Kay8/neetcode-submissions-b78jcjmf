from collections import defaultdict
from typing import List

class Twitter:
    # Class variable, shared accross all instances of the class (like a static variable)
    # Since we need a max heap, we're gonna store the times as negative values
    # 0, -1, -2 ...
    time = 0

    def __init__(self):
        self.users = defaultdict(User) # id -> User

    # def createUser(self, id):
    #     if id not in self.users:
    #         self.users[id] = User(id)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].tweet(Twitter.time, tweetId)
        Twitter.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Your own tweets + Your following tweets
        # Note: .update() is .extend() but for sets
        user = self.users[userId]
        tweets = user.tweets.copy()

        for following_id in user.following:
            tweets += self.users[following_id].tweets

        heapq.heapify(tweets)

        # We need a max heap
        max_heap = tweets.copy()
        news_feed = []
        for i in range(len(max_heap) if len(max_heap) < 10 else 10):
            news_feed.append(heapq.heappop(max_heap)[1])
            
        print(news_feed)
        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        # If attempt to follow themselves, do nothing
        if followerId is not followeeId:
            self.users[followerId].follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].unfollow(followeeId)

    def showUsers(self):
        for item in list(self.users.items()):
            print(item)
    
class User:
    def __init__(self):
        self.tweets = [] # heap
        self.following = set()

    def follow(self, id):
        self.following.add(id)

    # I use a tuple to keep track of the time when the tweet was posted
    def tweet(self, time, id):
        self.tweets.append((time, id))

    def unfollow(self, id):
        if id in self.following:
            self.following.remove(id)

    def __repr__(self):
        return f"Tweets: {self.tweets if self.tweets else "None"}, Following: {self.following if self.following else "None"}"