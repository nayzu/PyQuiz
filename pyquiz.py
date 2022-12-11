
#  ███▄    █  ▄▄▄     ▓██   ██▓▒███████▒ █    ██
#  ██ ▀█   █ ▒████▄    ▒██  ██▒▒ ▒ ▒ ▄▀░ ██  ▓██▒
# ▓██  ▀█ ██▒▒██  ▀█▄   ▒██ ██░░ ▒ ▄▀▒░ ▓██  ▒██░
# ▓██▒  ▐▌██▒░██▄▄▄▄██  ░ ▐██▓░  ▄▀▒   ░▓▓█  ░██░
# ▒██░   ▓██░ ▓█   ▓██▒ ░ ██▒▓░▒███████▒▒▒█████▓
# ░ ▒░   ▒ ▒  ▒▒   ▓▒█░  ██▒▒▒ ░▒▒ ▓░▒░▒░▒▓▒ ▒ ▒
# ░ ░░   ░ ▒░  ▒   ▒▒ ░▓██ ░▒░ ░░▒ ▒ ░ ▒░░▒░ ░ ░
#    ░   ░ ░   ░   ▒   ▒ ▒ ░░  ░ ░ ░ ░ ░ ░░░ ░ ░
#          ░       ░  ░░ ░       ░ ░       ░
#                      ░ ░     ░

bad_response = "Mauvaise réponse !"
good_response = "Bonne réponse !"
total_good_response = 0
total_bad_response = 0

# Question 1
question1 = input("Combien de lettres contient l'alphabet ?\n")
if question1 == 26:
    print(good_response)
    total_good_response += 1
else:
    print(bad_response)
    total_bad_response += 1

# Question 2
question2 = input("Quand YouTube a-t-il été créé (année) ?\n")
if question2 == "2005":
    print(good_response)
    total_good_response += 1
else:
    print(bad_response)
    total_good_response += 1

# Question 3
print("Quand s'est déroulé la seconde guerre mondiale (années) ?\n")
question3_1 = input("Année de début : ")
question3_2 = input("Année de fin : ")

if (question3_1 == 1939, 39) and (question3_2 == 1945, 45):
    print(good_response)
    total_good_response += 1
else:
    print(bad_response)
    total_bad_response += 1

# Question 4
question2 = input("Quand Facebook a-t-il été créé (année) ?\n")
if question2 == "2004":
    print(good_response)
    total_good_response += 1
else:
    print(bad_response)
    total_good_response += 1

# Question 5
question2 = input("Quand Discord a-t-il été créé (année) ?\n")
if question2 == "2015":
    print(good_response)
    total_good_response += 1
else:
    print(bad_response)
    total_good_response += 1


print("Vous avez obtenu :\n", total_good_response, "bonne(s) réponse(s)\n", total_bad_response, "mauvaise(s) réponse(s)")