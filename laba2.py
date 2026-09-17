user = {
    "alina": {
        "password": "1111",
        "grades": [10, 3, 12, 4, 5, 7]
    },
    "olesya": {
        "password": "2222",
        "grades": [6, 7, 12, 6, 7, 12]
    },
    "mariya": {
        "password": "3333",
        "grades": [5, 2, 4, 2, 11, 8]
    },
    "tanya": {
        "password": "4444",
        "grades": [4, 4, 12, 11, 10, 10]
    }
}

login = input("Enter login: ")
password = input("Enter password: ")

if login in user and user[login]["password"] == password:
    grades = user[login]["grades"]

    print("\nAll grades:", grades)

    good = 0
    bad = 0

    for grade in grades:
        if grade >= 5 and grade <= 12:
            good += 1
        elif grade >= 1 and grade <= 4:
            bad += 1

    print("Grades from 5 to 12:", good)
    print("Grades from 1 to 4:", bad)

else:
    print("Wrong!")
