class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        from queue import Queue

        def neighbour(lock):
            neighbours = []

            for i in range(4): # as lock length 4
                # Increment
                digit = str((int(lock[i]) + 1) % 10)
                neighbour1 = lock[: i] + digit + lock[i + 1 :]
                neighbours.append(neighbour1)

                # Decrement
                digit = str((int(lock[i]) - 1 + 10) % 10)
                neighbour2 = lock[: i] + digit + lock[i + 1 :]
                neighbours.append(neighbour2)

            return neighbours


        def bfs(source):
            visited.add(source)
            q = Queue()
            q.put((source, 0)) # (node, level) or (lock, level)

            while not q.empty():
                lock, level = q.get()

                if lock == target:
                    return level

                for new_lock in neighbour(lock):
                    if new_lock not in visited:
                        q.put((new_lock, level + 1))
                        visited.add(new_lock)

            return -1


        if '0000' in deadends:
            return -1

        visited = set(deadends)
        return bfs('0000')
        
