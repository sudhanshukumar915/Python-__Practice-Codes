import os  # OS ke sath kaam karne ke liye built-in module

# User se command lena #.lower() ka matlb mai ki agar user yES,Yes,YES jase v likhe wo yes mai convert ho jaayega
command = input("Enter command (res or mm): ").lower()

# Agar user 'film1' likhe
if command == "res":
    print("Playing RES...")
    os.startfile("E:\WEB SERIES IN HOLLYWOOD\res.mp4")  # apna path daalo

# Agar user 'film2' likhe
elif command == "mm":
    print("Playing MM...")
    os.startfile("E:\WEB SERIES IN HOLLYWOOD\mm.mp4")  # apna path daalo

# Agar user galat command de
else:
    print("Unknown command! Please type film1, film2, or film3.")
