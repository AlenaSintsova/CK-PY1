from random import randint

def get_unique_list_numbers(count=15, min_value=-10, max_value=10):
   list_numbers = []

   while len(list_numbers) < count:
       cur_rand_number = randint(min_value, max_value)
       if cur_rand_number not in list_numbers:
           list_numbers.append(cur_rand_number)

   return list_numbers

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
