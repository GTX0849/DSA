class Solution:
    def minimumCost(
        self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int
    ) -> int:
        c1 = min(cost1, costBoth)
        c2 = min(cost2, costBoth)

        shared = min(need1, need2)
        rem1 = need1 - shared
        rem2 = need2 - shared

        ans1 = shared * min(costBoth, c1 + c2) + rem1 * c1 + rem2 * c2
        ans2 = max(need1, need2) * costBoth

        return min(ans1, ans2)