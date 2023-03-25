from src.One_D_Problem_file import One_D_Problem

if __name__ == '__main__':
    problem = One_D_Problem()
    x, num_calls = problem.uniform_search_method(10, 1e-1)
    print(x, num_calls)
