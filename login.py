import mysql.connector
import bcrypt

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='nimesh1111',
    database='login'
)
conn = db.cursor()

def register():
    user = input("Enter Your User Name : ")
    passw = input("Enter Your Password : ")
    
    # Hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(passw.encode(), salt)
    
    # Insert the user into the database
    sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
    conn.execute(sql, (user, hashed_password))
    db.commit()
    print("Registration successful!")

def login():
    user = input("Enter Your User Name : ")
    passw = input("Enter Your Password : ")
    
    # Get the hashed password from the database
    sql = "SELECT password FROM users WHERE username = %s"
    conn.execute(sql, (user,))
    result = conn.fetchone()
    
    if result:
        hashed_password = result[0].encode('utf-8')
        
        # Verify the password
        if bcrypt.checkpw(passw.encode(), hashed_password):
            print("Login successful!")
        else:
            print("Invalid password.")
    else:
        print("User does not exist.")

while True:
    switch = input(">>")

    if switch == "register":
        register()
    elif switch == "login":
        login()
    else:
        print("Check Your Credentials OR Register Using Register Command")