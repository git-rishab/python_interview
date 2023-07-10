employees = [{
  "name": "John",
  "salary": 3000,
  "designation": "developer"
}, {
  "name": "Emma",
  "salary": 4000,
  "designation": "manager"
}, {
  "name": "Kelly",
  "salary": 3500,
  "designation": "tester"
}]


def maxSalary(emp):
  res = emp[0]
  for el in emp:
    if el['salary'] > res['salary']:
      res = el

  return res


print(maxSalary(employees))