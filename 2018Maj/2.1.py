X = [-2,1,2,3]
Y = [2,3,1,4]

tabForPoints = []
for A in range(0, len(X)-1):
        if X[A] <X[A+1] and Y[A] <Y[A+1]:
                pointsX= str(X[A])
                pointsY = str(Y[A])
print(pointsX,pointsY)