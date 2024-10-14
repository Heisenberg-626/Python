from datetime import datetime
current_time=datetime.now()
print(current_time)
format1=current_time.strftime("%Y-%m-%d %H:%M:%S")
print(format1)
format2=current_time.strftime("%m/%d/%Y")
print(format2)
format3=current_time.strftime("%A,%B %d,%Y")
print(format3)
format4=current_time.strftime("%A,%B %d,%Y %H:%M:%S %p")
print(format4)
format5=current_time.strftime("%a-%b-%d %H:%M:%S %Z %Y")
print(format5)


