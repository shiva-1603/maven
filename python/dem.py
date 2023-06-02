def enterence(r=10,c=8):
    if r in range(25) and c==8:
        print("valid")
    elif r in range(26,50) and c==8:
        print("allowed")
    else:
        print("invalid")
enterence()
