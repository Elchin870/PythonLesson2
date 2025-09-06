import pandas as pd
from functools import reduce
filelocation="C:\\Users\\Elchin\\Desktop\\data.xlsx"
df = pd.read_excel(filelocation,sheet_name = 0)
list_of_dicts = df.to_dict('records')
# print(list_of_dicts)

#1) Map: 'Name' sütununu hamısını böyük hərflərə çevirərək yeni siyahı yaradın.

# new_list_upper_name=list(map(lambda d:d["Name"].upper(),list_of_dicts))
# print(new_list_upper_name)

#2) Map: 'SalaryAZN' dəyərlərini 10% artımla (round) yeni siyahıda göstərin.

# new_list_of_salary = list(map(lambda x: round(x["SalaryAZN"] * 1.1), list_of_dicts))
# print(new_list_of_salary)


#3) Filter: Yalnız 'City' = 'Baku' olan əməkdaşları seçin (sətir siyahısı).

# new_list_of_employees=list(filter(lambda x:x["City"]=="Baku",list_of_dicts))
# print(new_list_of_employees)

#4) Filter: 'Age' >= 30 və 'Department' = 'Engineering' olanları çıxarın.

# new_list_of_employees = list(filter(lambda x:x["Age"]>=30 and x["Department"]=="Engineering",list_of_dicts))
# print(new_list_of_employees)

#5) Filter: 'Remote' = True və 'Performance' >= 80 olan sətirləri seçin.

# new_list_of_employees=list(filter(lambda x:x['Remote']==True and x["Performance"]>=80,list_of_dicts))
# print(new_list_of_employees)

#6) Reduce: Bütün 'SalaryAZN' toplamını hesablayın.

# new_list_of_salary=reduce(lambda total,x:total+x["SalaryAZN"],list_of_dicts,0)
# print(new_list_of_salary)

#7) Reduce: 'SalaryAZN' üzrə maksimumu və minimumu tapın.

# min_max_salary = reduce(lambda acc, x: (min(acc[0], x["SalaryAZN"]), max(acc[1], x["SalaryAZN"])),list_of_dicts,(float('inf'), float('-inf')))
# print(min_max_salary)

#8) Map+Filter: 'Skills' içində 'python' olan əməkdaşların adlarını böyük hərflərlə qaytarın.

# new_list_of_employees = list(map(lambda x: x["Name"].upper(),filter(lambda x: "python" in x["Skills"], list_of_dicts)))
# print(new_list_of_employees)

#9) Map: 'JoinDate' dəyərlərini 'YYYY-MM' formatına salın.
# from datetime import datetime
#
# new_list_of_dates = list(map(lambda x: datetime.strptime(x["JoinDate"], "%Y-%m-%d").strftime("%Y-%m"),list_of_dicts))
# print(new_list_of_dates)

#10) Filter+Reduce: 'City' = 'Baku' olanların 'SalaryAZN' cəmini hesablayın.

# baku_employees = filter(lambda x: x["City"] == "Baku", list_of_dicts)
# total_salary = reduce(lambda total, x: total + x["SalaryAZN"], baku_employees, 0)
# print(total_salary)

#11) Map: 'Performance' balına görə kateqoriya təyin edin: 1-59='Low', 60-79='Medium', 80-100='High'.

# def performance_category(score):
#     if 1 <= score <= 59:
#         return "Low"
#     elif 60 <= score <= 79:
#         return "Medium"
#     elif 80 <= score <= 100:
#         return "High"
#
# new_list_of_categories = list(map(lambda x: performance_category(x["Performance"]), list_of_dicts))
# print(new_list_of_categories)

#12) Filter: 'Skills' içində 'django' VƏ 'docker' olan sətirləri çıxarın.

# new_list_of_employees = list(filter(lambda x: "django" in x["Skills"] and "docker" in x["Skills"], list_of_dicts))
# print(new_list_of_employees)

#13) Map: 'Age' → gələn il üçün yaş (Age+1) siyahısını yaradın.

# next_year_age = list(map(lambda x: x["Age"] + 1, list_of_dicts))
# print(next_year_age)

#14) Filter+Map: 'Department' = 'Data' olanların maaşını 15% artırıb yeni siyahı yaradın.

# data_department = filter(lambda x: x["Department"] == "Data", list_of_dicts)
# new_list_of_salaries = list(map(lambda x: round(x["SalaryAZN"] * 1.15), data_department))
# print(new_list_of_salaries)

#15) Bonus: 'Engineering' şöbəsində 'python' bilənlərin orta maaşını hesablayın.

# salaries = list(map(lambda x: x["SalaryAZN"],filter(lambda x: x["Department"] == "Engineering" and "python" in x["Skills"], list_of_dicts)))
# avg_salary = reduce(lambda acc, x: acc + x, salaries, 0) / (len(salaries))
# print(avg_salary)


