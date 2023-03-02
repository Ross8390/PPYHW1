from datetime import datetime
import yadisk
from application.salary import calculate_salary
from application.db.people import get_employees


if __name__ == '__main__':
    print(datetime.now())
    calculate_salary()
    get_employees()
