class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        res = []

        for i in range(len(drones)):
            x_dist = abs(target[0] - drones[i][0])
            y_dist = abs(target[1] - drones[i][1])
            total_dist = x_dist + y_dist

            if total_dist <= drones[i][2]:
                res.append((total_dist, i))

        if not res:
            return -1

        return min(res)[1]