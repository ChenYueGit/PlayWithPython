'''
%s - string
%d - decimal
%x - hexadecimal
%.1f - float with 1 decimal places
%.2f - float with 2 decimal places
'''

szName = "Chen Xinxin"
fPrice = 33.888
n = 5
szText = "%s bought %d goods with price %.2f"\
    " the totol price is %.1f"%(szName,n,fPrice,fPrice*5)
print(szText)