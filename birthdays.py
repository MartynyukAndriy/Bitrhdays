from datetime import datetime


birthdays_list = [{"name": "Andriy", "birthday": "10/12/1992"},
                  {"name": "Tania", "birthday": "14/12/1996"},
                  {"name": "Vasil", "birthday": "16/12/1998"},
                  {"name": "Igor", "birthday": "19/12/1999"},
                  {"name": "Anna", "birthday": "22/12/1992"},
                  {"name": "Olga", "birthday": "24/12/1990"},
                  {"name": "Roman", "birthday": "28/12/1988"},
                  {"name": "Taras", "birthday": "31/12/2000"},
                  {"name": "Petro", "birthday": "01/01/1997"},
                  {"name": "Mark", "birthday": "07/01/1993"},
                  {"name": "Maria", "birthday": "10/01/1993"},
                  {"name": "Misha", "birthday": "10/12/1999"},
                  {"name": "Volodymyr", "birthday": "10/12/1998"},
                  {"name": "Katya", "birthday": "10/12/2001"}]


def get_birthdays_per_week(birthday_list, n=7):
    birthday_dict = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": []
    }
    for birthdays in birthday_list:
        birthday = birthdays["birthday"]
        birthday = datetime(year=int(datetime.now().year),
                            month=int(birthday[3:5]), day=int(birthday[:2]))
        birthday = birthday.date()
        time_now = datetime.now()
        time_now = time_now.date()
        delta = birthday - time_now
        if 0 <= int(delta.days) < n:
            if birthday.strftime('%A') in ["Sunday", "Saturday"]:
                birthday_dict["Monday"].append(birthdays["name"])
            else:
                birthday_dict[birthday.strftime('%A')].append(
                    birthdays["name"])

    for key, value in birthday_dict.items():
        if birthday_dict[key]:
            names = ""
            for i in range(len(value)):
                if i < len(value)-1:
                    names += value[i] + ", "
                else:
                    names += value[i]
            print(f"{key}: {names}")


if __name__ == "__main__":
    get_birthdays_per_week(birthdays_list)
