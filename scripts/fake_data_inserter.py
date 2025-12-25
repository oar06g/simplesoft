from faker import Faker
import psycopg2
from psycopg2.extras import execute_values
from datetime import date
import csv

csv_filename = 'fake_users.csv'
fieldnames = ['name', 'birth_date', 'job', 'years_experience', 'email', 'is_active']

fake = Faker()
conn = psycopg2.connect(
    host='localhost',
    database='simple_db',
    user='admin',
    password='admin123',
    port=5432
)

cur = conn.cursor()

def write_users_to_csv(filename, data, headers):
    # Open the file in write mode ('w') to ensure it's fresh or overwritten
    # Use newline='' to prevent extra blank lines on Windows
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Write the header row
        writer.writerow(headers)
        # Write all data rows from the list of tuples
        writer.writerows(data)
    print(f"Successfully wrote all data to {filename}")

# Function to append a single new row to an existing CSV file
def append_user_to_csv(filename, new_row):
    # Open the file in append mode ('a')
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Write the single new row (tuple) to the file
        writer.writerow(new_row)
    print(f"Successfully appended a new row to {filename}")

users_data = []

try:
    for _ in range(500_000):
        name = fake.name()
        birth_date = fake.date_of_birth(minimum_age=16, maximum_age=55)
        job = fake.job()
        age = date.today().year - birth_date.year
        years_experience = fake.random_int(min=0, max=max(0, age - 18))
        email = fake.unique.email()
        is_active = fake.random_element(elements=(True, False))
        
        users_data.append(
            (
                name,
                birth_date,
                job,
                years_experience,
                email,
                is_active
            )
        )

except KeyboardInterrupt:
    print("Data insertion interrupted by user.")
finally:
    insert_query = """
INSERT INTO users
(name, birth_date, job, years_experience, email, is_active)
VALUES %s
"""
    execute_values(cur, insert_query, users_data, page_size=5000)
    write_users_to_csv(csv_filename, users_data, fieldnames)
    
    conn.commit()
    cur.close()
    conn.close()
    print("done add {}".format(500_000))