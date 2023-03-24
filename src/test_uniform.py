from src.oneD_Problem_file import OneDProblem

if __name__ == '__main__':
    problem = OneDProblem()
    x, num_calls = problem.uniform_search_method(10, 1e-1)
    print(x, num_calls)
