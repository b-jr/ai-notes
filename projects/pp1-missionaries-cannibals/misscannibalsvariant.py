from search import *

class MissCannibalsVariant(Problem):
    """ The problem of Missionaries and Cannibals. 
    N1 and N2 are the total number of missionaries and cannibals starting from the left bank.
    A state is represented as a 3-tuple, two numbers and a boolean:
    state[0] is the number of missionaries on the left bank (note: the number of missionaries on the right bank is N1-m)
    state[1] is the number of cannibals on the left bank (note: the number of cannibals on the right bank is N2-c)
    state[2] is true if boat is at the left bank, false if at the right bank """

    def __init__(self, N1=4, N2=4, goal=(0, 0, False)):
        """ Define goal state and initialize a problem """
        initial = (N1, N2, True)
        self.N1 = N1
        self.N2 = N2
        super().__init__(initial, goal)


if __name__ == '__main__':
    mc = MissCannibalsVariant(4,4)
    # print(mc.actions((3, 3, True))) # Test your code as you develop! This should return  ['MC', 'MMM']

    path = depth_first_graph_search(mc).solution()
    print(path)
    path = breadth_first_graph_search(mc).solution()
    print(path)

