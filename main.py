import math
import numpy as np
from scipy import stats


def timings():

    timings_a = []
    with open('personKeyTimingA.txt') as topo_file:
        for line in topo_file:
            timings_a.append(line.rsplit(',')[0]);
    a_timings = []
    a_timings.append(float(timings_a[0]))
    for i in range(len(timings_a)):
        timings_a[i] = float(timings_a[i])
        if i != 0:
            a_timings.append(timings_a[i] - timings_a[i - 1])

    mean_timing_a = sum(a_timings) / len(a_timings)

    timings_b = []
    with open('personKeyTimingB.txt') as topo_file:
        for line in topo_file:
            timings_b.append(line.rsplit(',')[0])

    b_timings = []
    b_timings.append(float(timings_b[0]))
    for i in range(len(timings_b)):
        timings_b[i] = float(timings_b[i])
        if i != 0:
            b_timings.append(timings_b[i] - timings_b[i - 1])

    mean_timing_b = sum(b_timings) / len(b_timings)

    print("Mean for person A: ", mean_timing_a)

    print("Mean for person B: ", mean_timing_b)

    timings_email = []
    with open('email.txt') as topo_file:
        for line in topo_file:
            timings_email.append(line.rsplit(',')[0])

    email_timings = []
    email_timings.append(float(timings_email[0]))
    for i in range(len(timings_email)):
        timings_email[i] = float(timings_email[i])
        if i != 0:
            email_timings.append(timings_email[i] - timings_email[i - 1])


    total = 1

    print(mean_timing_a)
    print(mean_timing_b)
    print(np.std(a_timings))
    print(np.std(b_timings))

    for keystroke in email_timings:
        probability_A = stats.norm.pdf(keystroke, mean_timing_a, np.std(a_timings))
        probability_B = stats.norm.pdf(keystroke, mean_timing_b, np.std(b_timings))
        total *= (probability_A/probability_B)

    print(total)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    timings()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
