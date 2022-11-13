def main():
    money_capital = 10000
    salary = 5000
    spend = 6000
    increase = 0.05
    result = task_2(money_capital, salary, spend, increase)
    print(result)

def task_1(money_capital, salary, spend, increase=0.05):
    month = 0
    while True:
        delta = spend - salary
        if delta > money_capital:
            break

        money_capital -= delta
        month += 1
        spend = spend + (spend * increase)
    return month

def task_2(money_capital, salary, spend, increase=0.05):
    month = 0
    while True:
        if spend > money_capital:
            break

        money_capital = money_capital - spend + salary
        month += 1
        spend *= (1 + increase) # spend = spend + (spend * increase)
    return month


main()




