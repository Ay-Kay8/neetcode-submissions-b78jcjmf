class Solution:
    from collections import deque

    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Build heap with only frequencies
        dict = {}
        for t in tasks:
            if t not in dict:
                dict[t] = -1
            else:
                dict[t] -= 1

        heap = list(dict.values())
        heapq.heapify(heap)

        # (freq, time when it will be availabe again)
        queue = deque()

        time = 0
        while heap or queue:

            # Multiple tasks might be ready at the same time, pop all of them
            while queue and queue[0][1] <= time:
                new_freq, _ = queue.popleft()
                heapq.heappush(heap, new_freq)
                # else, it's idle or another letter

            # If the heap is empty, then we must idle until time is sufficient
            if heap:
                freq = heapq.heappop(heap) + 1 # Remove 1 of the letters

                # If there are still tasks of this letter
                if not freq == 0:
                    queue.append((freq, time + n + 1))
            time += 1

        return time