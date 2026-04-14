class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)

        fleets = 1
        time_car_ahead = (target - pair[0][0]) / pair[0][1]
        for i in range(1, len(pair)):
            car_behind = pair[i]
            car_behind_time = (target - car_behind[0]) / car_behind[1]
            if car_behind_time > time_car_ahead:
                fleets += 1
                time_car_ahead = car_behind_time

        return fleets