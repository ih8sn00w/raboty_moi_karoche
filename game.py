from random import randint

E = ["*" for i in range(16)]
W = [" " for i in range(5)]

score = 0

s_counter = 0

heart_points = 3


def main() -> None:
    egg().field_change()

    print(f"--------------------------------")
    print(f"|{E[0]}                            {E[8]}|")
    print(f"|   {E[1]}                      {E[9]}   |")
    print(f"|      {E[2]}                {E[10]}      |")
    print(f"|         {E[3]}          {E[11]}         |")
    print(f"|            {W[0]}    {W[1]}            |")
    print(f"|{E[4]}              {W[4]}             {E[12]}|")
    print(f"|   {E[5]}                      {E[13]}   |")
    print(f"|      {E[6]}                {E[14]}      |")
    print(f"|         {E[7]}          {E[15]}         |")
    print(f"|            {W[2]}    {W[3]}            |")
    print(f"--------------------------------")

    wolf().change_position()
    egg().egg_move()

    print(f"\n\n\n\nВаш счёт: {score}\n")

    if heart_points == 0:
        print(f"""
  ****    ***    *     *  ******      ****   *     *   ******  ****   
 *       *    *  **   **  *          *    *   *    *   *       *   *  
 *  **   *    *  * * * *  *          *    *    *   *   *       *   *  
 *    *  ******  *  *  *  ******     *    *     *  *   ******  ****   
 *    *  *    *  *     *  *          *    *      * *   *       *  *   
  ****   *    *  *     *  ******      ****        **   ******  *    * 
        """)
        input()
        exit()

    heart_string = heart_points * "♥️"
    print(f"У вас осталось жизней: {heart_string}")

    main()


class egg(object):
    egg_add = randint(0, 3)

    def field_change(self) -> None:

        egg_add = randint(0, 3)

        if egg_add == 0:
            E[0] = "O"
        elif egg_add == 1:
            E[8] = "O"
        elif egg_add == 2:
            E[4] = "O"
        elif egg_add == 3:
            E[12] = "O"

    def egg_move(self) -> None:

        if any(E[i] == "O" for i in range(16)):
            egg.upper_left(self)
            egg.upper_right(self)
            egg.lower_right(self)
            egg.lower_left(self)

    def upper_left(self) -> None:

        global score, heart_points

        if any(E[i] == "O" for i in range(4)):

            if E[3] == "O" and W[0] == "W":
                print("Вы поймали яичко!")
                E[3] = "*"

                score += 1

            elif E[3] == "O" and W[0] != "W":
                print("Ну почти, старайся лучше")
                E[3] = "*"

                heart_points -= 1

            if E[2] == "O":
                E[3] = "O"
                E[2] = "*"

            if E[1] == "O":
                E[2] = "O"
                E[1] = "*"

            if E[0] == "O":
                E[1] = "O"
                E[0] = "*"

    def upper_right(self) -> None:

        global score, heart_points

        if any(E[i] == "O" for i in range(8, 12)):

            if E[11] == "O" and W[1] == "W":
                print("Вы поймали яичко!")
                E[11] = "*"

                score += 1

            elif E[11] == "O" and W[1] != "W":
                print("Ну почти, старайся лучше")
                E[11] = "*"

                heart_points -= 1

            if E[10] == "O":
                E[11] = "O"
                E[10] = "*"

            if E[9] == "O":
                E[10] = "O"
                E[9] = "*"

            if E[8] == "O":
                E[9] = "O"
                E[8] = "*"

    def lower_left(self) -> None:

        global score, heart_points

        if any(E[i] == "O" for i in range(4, 8)):

            if E[7] == "O" and W[2] == "W":
                print("Вы поймали яичко!")
                E[7] = "*"

                score += 1

            elif E[7] == "O" and W[2] != "W":
                print("Ну почти, старайся лучше")
                E[7] = "*"

                heart_points -= 1

            if E[6] == "O":
                E[7] = "O"
                E[6] = "*"

            if E[5] == "O":
                E[6] = "O"
                E[5] = "*"

            if E[4] == "O":
                E[5] = "O"
                E[4] = "*"

    def lower_right(self) -> None:

        global score, heart_points

        if any(E[i] == "O" for i in range(12, 16)):

            if E[15] == "O" and W[3] == "W":
                print("Вы поймали яичко!")
                E[15] = "*"

                score += 1

            elif E[15] == "O" and W[3] != "W":
                print("Ну почти, старайся лучше")
                E[15] = "*"

                heart_points -= 1

            if E[14] == "O":
                E[15] = "O"
                E[14] = "*"

            if E[13] == "O":
                E[14] = "O"
                E[13] = "*"

            if E[12] == "O":
                E[13] = "O"
                E[12] = "*"


class wolf(object):

    def change_position(self) -> None:

        global s_counter

        stay_move = input("Волк двигается или стоит на месте?(S - стоит на месте, M - двигается)\n")

        while stay_move not in {"S", "M"}:
            print("Вы ввели неправильное значение, попробуйте еще раз")
            stay_move = input("Волк двигается или стоит на месте?(S - стоит на месте, M - двигается)\n")

        if all(W[i] == " " for i in range(4)) and stay_move == "S":
            print("Сейчас волк находится в центре, советую вам получше следить за тем, куда его направить!")
            return None

        if stay_move == "S":
            s_counter += 1
            return None

        if stay_move != "S":
            s_counter = 0

        if s_counter >= 4:
            print("Оло, у тебя яиц не будет!!!")
            print("")

        if stay_move == "M":
            W[4] = " "

        high_low = input("Волк стоит или пригинается? (S - стоит, D - пригинается)\n")

        while high_low not in {"S", "D"}:
            print("Вы ввели неправильное значение, попробуйте еще раз")
            high_low = input("Волк стоит или пригинается? (S - стоит, D - пригинается)\n")

        direction = input("Волк идет влево или вправо? (R - идет вправо, L - идет влево)\n")

        while direction not in {"R", "L"}:
            print("Вы ввели неправильное значение, попробуйте еще раз")
            direction = input("Волк идет влево или вправо? (R - идет вправо, L - идет влево)\n")

        if high_low == "S":

            W[2] = W[3] = " "

            if direction == "R":
                W[0] = " "
                W[1] = "W"
            elif direction == "L":
                W[0] = "W"
                W[1] = " "

        elif high_low == "D":

            W[0] = W[1] = " "

            if direction == "R":
                W[2] = " "
                W[3] = "W"
            elif direction == "L":
                W[2] = "W"
                W[3] = " "

if __name__ == "__main__":
    main()
