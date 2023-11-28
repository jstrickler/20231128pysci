s1 = "spam\n"   #  \n \t \b \f 
s2 = 'spam\n'  

print("Guido's the ex-BDFL of Python")
print('Guido is the ex-"BDFL" of Python')

print("""Guido's the ex-"BDFL" of Python""")

query = """
select *
from purchases
where state = 'VA'
order by purchase_amount
limit 100
"""

s3 = r"spam\n"
print(s3)


