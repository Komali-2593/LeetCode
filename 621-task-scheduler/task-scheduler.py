class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:

        count = {}

        for task in tasks:
            if task not in count:
                count[task] = 1
            else:
                count[task] += 1

        time = 0

        while count:

            used = []

            for task in sorted(count, key=count.get, reverse=True):

                if task not in used:
                    count[task] -= 1
                    used.append(task)
                    time += 1

                    if count[task] == 0:
                        del count[task]

                if len(used) == n + 1:
                    break

            if len(used) < n + 1 and count:
                time += (n + 1 - len(used))

        return time