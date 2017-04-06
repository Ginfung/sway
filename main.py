from Algorithms import sway_continous, sway_discrete


"""
DEMO for the continuous model- XOMO
"""


def demo1():
    from Benchmarks.XOMO import XOMO_OSP, generate_random_init

    # step1: generate initial candidates
    init = generate_random_init(XOMO_OSP, 10000)
    # step2: call the sway
    res = sway_continous.optimize(init, XOMO_OSP.eval)
    # step3: print results
    for i in res:
        print(i.fitness.values)

    return

if __name__ == '__main__':
    demo1()
