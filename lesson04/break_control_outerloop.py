outer_break=False

for i in range(10):
    for j in range(10):
        if j ==5:
            outer_break=True
            break
        print("outer:",i,"inner:",j)
    if outer_break:
        break
