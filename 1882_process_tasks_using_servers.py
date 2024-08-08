class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:

        # available servers sorted by (weight, index)
        heap_free = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(heap_free)

        # unavailable servers sorted by (time, weight, idx)
        heap_busy = []

        idx_task = 0

        ans = []

        while idx_task < len(tasks):
            # check workers became free
            while heap_busy and heap_busy[0][0] == idx_task:
                t, weight, server_idx = heapq.heappop(heap_busy)
                heapq.heappush(heap_free, (servers[server_idx], server_idx))

            if heap_free:
                # pick a free server
                weight, server_idx = heapq.heappop(heap_free)
                ans.append(server_idx)

                # process the current task: mark unavailable and when it becomes free
                heapq.heappush(heap_busy, (idx_task + tasks[idx_task], weight, server_idx))
            else:
                # skip time period where no server is availble
                # find a server that becomes available first
                finish_time, weight, server_idx = heapq.heappop(heap_busy)
                ans.append(server_idx)

                # process the current task
                heappush(heap_busy, (finish_time + tasks[idx_task], weight, server_idx))

            idx_task += 1
        return ans
