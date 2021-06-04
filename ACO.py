import time

import pandas as pd
import pants


# function to read the excel with the distance matrix
def parse_input(path):
    distances = pd.read_excel(path, index_col=0)
    return distances


dists = parse_input('Lab10DistancesMatrix.xlsx')


# function to get the distance between two points
def getDist(a, b):
    return dists[a][b]


# function to check if the initial route has duplicate cities
def is_valid_route(list_of_cities):
    return not any(list_of_cities.count(element) > 1 for element in list_of_cities)


# function to run the algorithm
def ACO_algorithm(cities_list):
    world = pants.World(cities_list, getDist)
    start_time = time.time()
    solver = pants.Solver(alpha=10, beta=30, ant_count=10, limit=2500)
    solution = solver.solve(world)
    end_time = time.time()
    duration = end_time - start_time
    return solution, duration


# function to print the results starting in P1
def p_print(solution, duration):
    best_path = solution.tour
    indexP1 = best_path.index('P1')
    best_path = best_path[indexP1:] + best_path[:indexP1]
    print("******************************** BEST RESULT ********************************")
    print("The best route is: ")
    print(best_path)
    print('Final distance:   {0:.3f}'.format(solution.distance))
    print("'Found in:   {0:.2f} seconds".format(duration))


def main():
    # input lists (change on the two functions below)
    cities_list15 = ['P' + str(i) for i in range(1, 16)]
    cities_list25 = ['P' + str(i) for i in range(1, 26)]
    cities_list65 = ['P' + str(i) for i in range(1, 66)]
    cities_list100 = [cols for cols in dists.columns]

    # checking if the list is valid
    if not is_valid_route(cities_list100):
        print("Route not valid, has duplicate cities!!")
        return

    # run the algorithm
    solution, duration = ACO_algorithm(cities_list100)

    # print the solution
    p_print(solution, duration)


if __name__ == '__main__':
    main()
