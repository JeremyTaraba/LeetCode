class Twitter:

    def __init__(self):
        self.time = 0 # decrement this for use with min heap
        self.tweets = defaultdict(list) # userID -> [(time,tweetID)] minheap
        self.followers = defaultdict(set) # userID -> set()

    def postTweet(self, userId: int, tweetId: int) -> None: # add to most recent tweets and decrement time
        heapq.heappush(self.tweets[userId], (self.time, tweetId)) 
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        newsFeed = []
        if self.tweets[userId]:
            newsFeed = self.tweets[userId].copy() # min heap
        for user in self.followers[userId]:
            heap = []
            if self.tweets[user]:
                heap = self.tweets[user].copy()
            while heap:
                heapq.heappush(newsFeed, heapq.heappop(heap))
    
        topTen = []
        for i in range(10):
            if newsFeed:
                tweetTime, tweetId = heapq.heappop(newsFeed)
                topTen.append(tweetId)
        return topTen




    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.followers[followerId]:
            self.followers[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)