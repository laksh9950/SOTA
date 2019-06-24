def iterPower(base, exp):
        if exp==0:
                return 1:
                elif exp












	if exp==0:
		return 1
	elif exp == 1:
        return base
    else:
    	prod=base
    	for i in range(exp):
    		base=base*prod
        return base
print(iterPower(2, 3))   
