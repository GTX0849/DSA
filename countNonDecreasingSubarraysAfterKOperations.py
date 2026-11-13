
class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # Prefix sums
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        # Find next greater element for every index
        nxt = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if stack:
                nxt[i] = stack[-1]

            stack.append(i)

        # Binary lifting tables
        up = [nxt + [n]]
        costs = [[
            nums[i] * (nxt[i] - i) -
            (pref[nxt[i]] - pref[i])
            for i in range(n)
        ] + [0]]

        levels = 1

        while (1 << levels) <= n:
            prev_up = up[-1]
            prev_cost = costs[-1]

            curr_up = [n] * (n + 1)
            curr_cost = [0] * (n + 1)

            for i in range(n):
                mid = prev_up[i]
                curr_up[i] = prev_up[mid]
                curr_cost[i] = prev_cost[i] + prev_cost[mid]

            up.append(curr_up)
            costs.append(curr_cost)
            levels += 1

        # Calculate minimum operations for nums[l:r+1]
        def get_cost(l, r):
            total = 0
            cur = l

            for j in range(len(up) - 1, -1, -1):
                nxt_idx = up[j][cur]

                if nxt_idx <= r:
                    total += costs[j][cur]
                    cur = nxt_idx

            total += (
                nums[cur] * (r - cur + 1)
                - (pref[r + 1] - pref[cur])
            )

            return total

        # Sliding window
        left = 0
        ans = 0

        for right in range(n):
            while get_cost(left, right) > k:
                left += 1

            ans += right - left + 1

        return ans
