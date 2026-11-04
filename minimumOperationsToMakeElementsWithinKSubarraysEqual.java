import java.util.*;

class Solution {

    TreeMap<Integer, Integer> low = new TreeMap<>();
    TreeMap<Integer, Integer> high = new TreeMap<>();

    int lowSize = 0, highSize = 0;
    long lowSum = 0, highSum = 0;

    void addMap(TreeMap<Integer, Integer> map, int num) {
        map.put(num, map.getOrDefault(num, 0) + 1);
    }

    void removeMap(TreeMap<Integer, Integer> map, int num) {
        int count = map.get(num);

        if (count == 1) {
            map.remove(num);
        } else {
            map.put(num, count - 1);
        }
    }

    void add(int num) {

        if (low.isEmpty() || num <= low.lastKey()) {
            addMap(low, num);
            lowSize++;
            lowSum += num;
        } else {
            addMap(high, num);
            highSize++;
            highSum += num;
        }

        balance();
    }

    void remove(int num) {

        if (low.containsKey(num)) {
            removeMap(low, num);
            lowSize--;
            lowSum -= num;
        } else {
            removeMap(high, num);
            highSize--;
            highSum -= num;
        }

        balance();
    }

    void balance() {

        int target = (lowSize + highSize + 1) / 2;

        while (lowSize > target) {

            int num = low.lastKey();

            removeMap(low, num);
            lowSize--;
            lowSum -= num;

            addMap(high, num);
            highSize++;
            highSum += num;
        }

        while (lowSize < target) {

            int num = high.firstKey();

            removeMap(high, num);
            highSize--;
            highSum -= num;

            addMap(low, num);
            lowSize++;
            lowSum += num;
        }
    }

    long getCost() {

        long median = low.lastKey();

        return median * lowSize - lowSum
             + highSum - median * highSize;
    }

    public long minOperations(int[] nums, int x, int k) {

        int n = nums.length;

        // Step 1: Calculate cost of every window

        int m = n - x + 1;
        long[] cost = new long[m];

        for (int i = 0; i < x; i++) {
            add(nums[i]);
        }

        cost[0] = getCost();

        for (int i = 1; i < m; i++) {

            remove(nums[i - 1]);
            add(nums[i + x - 1]);

            cost[i] = getCost();
        }

        // Step 2: Dynamic Programming

        long INF = Long.MAX_VALUE / 2;

        long[] prev = new long[n + 1];
        long[] curr = new long[n + 1];

        for (int j = 1; j <= k; j++) {

            Arrays.fill(curr, INF);

            for (int i = 1; i <= n; i++) {

                // Don't select a window ending here
                curr[i] = curr[i - 1];

                // Select a window of size x
                if (i >= x && prev[i - x] != INF) {

                    long take = prev[i - x] + cost[i - x];

                    curr[i] = Math.min(curr[i], take);
                }
            }

            prev = curr.clone();
        }

        return prev[n];
    }
}