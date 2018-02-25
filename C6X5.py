#C6X5
string='X-DSPAM-Donfidence: 0.08475'
point=string.find(':')
result=float(string[point+1:])
print(result)