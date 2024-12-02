'''
Author: Sourav V s
Date: 08-10-2024
This program is to familiarize time and date in various formats
'''
from datetime import datetime
current_time=datetime.now()
print(current_time)
format_1=current_time.strftime("%Y-%m-%d %H:%M:%S")
format_2=current_time.strftime("%m/%d/%Y")
format_3=current_time.strftime("%A,%B %d,%Y")
format_4=current_time.strftime("%A,%B %d,%Y %H:%M:%S %p")
format_5=current_time.strftime("%a-%b-%d %H:%M:%S %Z %Y")
format_6=current_time.isoformat()
format_7=current_time.strftime("%d-%m-%Y")
format_8=current_time.strftime("%I:%M:%S")
format_9=current_time.strftime("%B")
format_10=current_time.strftime("%Y")
print(format_1)
print(format_2)
print(format_3)
print(format_4)
print(format_5)
print(format_6)
print(format_7)
print(format_8)
print(format_9)
print(format_10)
