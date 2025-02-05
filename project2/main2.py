from user import User
print("""       @-_________________-@
          @-_____|   NOW SHOWING   |_____-@
           |                             |
    _______|_____________________________|__________
   |________________________________________________|
   |               -                -               |
   |   -       -             -                    - |
   |        ____    ______________-   ____          |
   | -  -  |    |   |  TICKETS   |   |    | -       |
   |       |    |   |            |   |    |         |
   |  --   |____| - |_o___oo___o_| - |____|     -   |
   | -     |    |  |     --       |  |    |         |
   |    -  |    |- | -      -     |  |    | --      |
   |_______|====|__|______________|__|====|_________|

     """)
print("          WELCOME TO MY CINNAMA       ")
rows = int(input("\n Enter number of rows:"))
columns = int(input("\n Enter the number of seats in each row:"))
# build
seat_rows = []
for i in range(rows):
    seats = []
    for j in range(columns):
        seats.append('#')
    seat_rows.append(seats)


def calculate_price(rows):
    if rows * columns <= 50:
        return 20
    else:
        if rows <= (rows // 2):
            return 20
        else:
            return 10


booking_dict = {}
number_of_tickets = 0
current_income = 0
total_income = 0


def booking_ticket():
    rows = int(input("\nEnter row: "))
    columns = int(input("\nEnter column: "))
    price = calculate_price(rows)
    answer = input("\nPrice of your ticket is " + str(price) +
                   ". Please enter (y) if you want to book.")
    if answer == 'y':
        name = str(input("\n Name:"))
        age = str(input("\n Age: "))
        phone = int(input("\n phone number: "))
        booking = User(name, age, phone, price)
        booking_dict[(rows, columns)] = booking
        seat_rows[rows - 1][columns - 1] = 'X'
        return price
    elif seat_rows[rows - 1][columns - 1] == 'X':

        print("Seat already booked  please enter another seat")
        booking_ticket()
    else:
        return


def print_seat_map():
    for i in range(rows + 1):
        for j in range(columns + 1):
            if i == 0:
                print(j, " ", end="")
            else:
                if j == 0:
                    print(i, " ", end="")
                else:
                    print(seat_rows[i - 1][j - 1], " ", end="")
        print("\n")


def income():
    if price == 10:
        print((rows * columns) * 10)
    elif price == 8:
        print((rows * columns) * 8)


def info(rows, columns):
    user_info = booking_dict[(rows, columns)]
    print("\nName:" + user_info.Name)
    print("Age:" + user_info.Age)
    print("Ticket price:" + str(user_info.Price))
    print("Phone no:" + str(user_info.Phone))


n = 0
while n != 5:
    print("\n1. Show the seats\n2. Buy a ticket\n3. Statistics\n4. Show booked tickets user info\n5. Exit")
    n = int(input())
    if n == 1:
        print("_______________")
        print_seat_map()
        print("_______________")
    elif n == 2:
        price = booking_ticket()
        current_income = price
        number_of_tickets += 1
        total_income += price

        print("Your Ticket is booked , Thankyou  ")

    elif n == 3:
        print("\nNumber of booked tickets:" + str(number_of_tickets))
    elif n == 4:
        rows = int(input("Enter row: "))
        columns = int(input("Enter column: "))
        info(rows, columns)
