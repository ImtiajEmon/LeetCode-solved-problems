class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def crosscheck():
            while ans[-1] < 0 and ans[-2] > 0:
                if abs(ans[-1]) < abs(ans[-2]):
                    ans.pop(-1)
                elif abs(ans[-1]) > abs(ans[-2]):
                    ans.pop(-2)
                else:
                    ans.pop(-1)
                    ans.pop(-1)
                
                if len(ans) < 2:
                    break

        ans = [asteroids[0]]

        for i in range(1, len(asteroids)):
            if len(ans) == 0:
                ans.append(asteroids[i])
            elif ans[-1] < 0:
                ans.append(asteroids[i])
            else:
                if asteroids[i] < 0:
                    if abs(asteroids[i]) > ans[-1]:
                        ans.pop()
                        ans.append(asteroids[i])
                    #elif abs(asteroids[i]) < ans[-1]:
                        #Noting to do. Juust ignore
                    elif abs(asteroids[i]) == ans[-1]:
                        ans.pop()
                else:
                    ans.append(asteroids[i])

            if len(ans) >= 2:
                crosscheck()

        return ans
