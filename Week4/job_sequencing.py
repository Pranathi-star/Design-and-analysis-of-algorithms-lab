class Solution:
    def job_sequencing(self, jobs, t):
        jobs.sort(key = lambda x: x[2], reverse = True)
        no_jobs = len(jobs)
        print(jobs)
        res = [-1] * t
        slots = [False] * t

        for i in range(no_jobs):
            last_possible_slot = min(t - 1, jobs[i][1] - 1)
            for j in range(last_possible_slot, -1, -1):
                if slots[j] == False:
                    slots[j] = True
                    res[j] = jobs[i][0]
                    break
        return res

no_jobs = int(input("Number of jobs: ").strip())
t = int(input("Deadline: ").strip())
jobs = []
print("Enter the name, deadline, profit of each job")
for i in range(no_jobs):
    a, b, c = input().split()
    jobs.append([a, int(b), int(c)])
sol = Solution()
print("Sequence for max profit: ", sol.job_sequencing(jobs, t))
    
