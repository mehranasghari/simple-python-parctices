import random
import timeit

def waiting_game():
    target_time = random.randint(2, 4)
    print("\nYou'r target time is :", target_time, "\n")
    print("   ---Press Enter to Begin---")
    input()
    start_time = timeit.default_timer()
    print("   ...Press Enter again after", target_time, "seconds...")
    input()
    end_time = timeit.default_timer()
    print("\nYour time was: {0:.3f} seconds\n".format(end_time - start_time))
    if end_time - start_time > target_time:
        print("You were {0:3f} seconds slow!".format((end_time - start_time) - target_time))
    elif end_time - start_time == target_time:
        print("You were right on the mark!")
    else:
        print("You were {0:.3f} fast!".format(target_time - (end_time - start_time)))




waiting_game()