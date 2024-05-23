GRAVITY = 9.8

def main():
    time_of_fall = int(input("Enter the amount of time the object will be falling: "))

    fallingDistance(time_of_fall)

def fallingDistance(t):
    for t in range(1, t+1):
        distance_traveled_per_second = 0.5 * GRAVITY * t**2
        print(distance_traveled_per_second)

main()