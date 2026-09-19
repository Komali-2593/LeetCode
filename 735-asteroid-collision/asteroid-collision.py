class Solution:
    def asteroidCollision(self, asteroids):
        stack = []

        for i in range(len(asteroids)):
            while stack and stack[-1] > 0 and asteroids[i] < 0:

                if stack[-1] < abs(asteroids[i]):
                    stack.pop()

                elif stack[-1] == abs(asteroids[i]):
                    stack.pop()
            # current asteroid also explodes
                    break

                else:
            # current asteroid explodes
                    break

            else:
                stack.append(asteroids[i])
        return stack