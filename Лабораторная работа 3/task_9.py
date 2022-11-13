def main():
    salary = 5000
    spend = 6000
    months = 10
    increase = 0.03

    need_money = get_money_capital(salary, spend, months, increase)
    print(round(need_money))


def get_money_capital(salary, spend, months=10, increase=0.03):
    total_need_money = 0
    for _ in range(months):

        current_need_money = spend - salary
        total_need_money += current_need_money

        spend *= (1 + increase)

    return total_need_money

main()


