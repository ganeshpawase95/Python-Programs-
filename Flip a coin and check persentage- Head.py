import random

def run_flip_a_coin(n):
    head_count = 0
    for i in range(n):
        coin_sides_lst = ["Head","Tail"]
        result = random.choice(coin_sides_lst)
        if result == "Head":
            head_count = head_count + 1

    percentage_head = (head_count/n)*100
    print(f"After flipping the coin {n} times, the percentage of times head has come is:{percentage_head:.2f}%")

coin_flip_times = int(input("Enter the number of time to flip the coin:"))
run_flip_a_coin(coin_flip_times)