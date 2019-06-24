balance = 999999
annualInterestRate =0.18
low = balance/12

high=  (balance *(1 + annualInterestRate/12)**12) / 12.0
while True:
    p0 = (low+high)/2
    b0=balance
    for i in range(12):
        ub0=b0-p0
        b0=ub0+(annualInterestRate/12)*ub0
    if ub0 <=0:
        high = p0
    else:
        low =p0
    if abs(ub0)<=0.01:
        print(round(p0,2))
        break