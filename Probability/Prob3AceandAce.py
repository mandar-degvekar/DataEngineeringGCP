event=0 #number of aces
tries=0 #number of cards after drawing one king
for prob in range(1,52):
    if prob < 4:
        event = event + 1
    tries = tries + 1
print(event / tries)