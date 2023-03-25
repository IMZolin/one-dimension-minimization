from One_D_Problem_file import One_D_Problem

p1 = One_D_Problem()
print(p1.uniform_search_method(10, 1e-10))
print(p1.trial_point_method(0.0001))
print(p1.golden_search(0.0001))
