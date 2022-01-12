#!/usr/bin/env python3

# Created by: Ina Tolo
# Created on: Jan. 12, 2022
# This program asks the user how many numbers they would like
# to add. It then uses a while loop to calculate and display
# the sum of x numbers. A continue statement is also used.


def main():
    # initialize the loop counter and sum
    loop_counter = 0
    sum = 0

    # get user number as a string
    user_num_a_string = input("How many numbers would you like to add?: ")
    print("")

    try:
        # converts the first user input to integer
        user_num_a_int = int(user_num_a_string)

        if user_num_a_int >= 0:
            # calculate the sum of the entered numbers
            while (loop_counter < user_num_a_int):
                user_num_b_string = input("Enter a whole number: ")

                try:
                    # converts entered number from string to integer
                    user_num_b_int = int(user_num_b_string)

                    if user_num_b_int >= 0:
                        print("{} added to the sum." . format(user_num_b_int))
                        print("{} + {}." .format(user_num_b_int, sum))
                        print("")
                        sum = sum + user_num_b_int
                        loop_counter = loop_counter + 1

                        if loop_counter == user_num_b_int:
                            continue
                    else:
                        print("Please enter a whole number!")
                        print("")
                except Exception:
                    print("{} is not a number.". format(user_num_b_string))
                    print("")

            print("")
            print("The total sum is {}.".
                  format(sum))
        else:
            print("Please enter a whole number!")
            print("")
    except Exception:
        print("{} is not a number.". format(user_num_a_string))
        print("")


if __name__ == "__main__":
    main()
