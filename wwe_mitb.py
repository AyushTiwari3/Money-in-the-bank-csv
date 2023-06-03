import pandas
data=pandas.read_csv("/Users/Asus/Downloads/MITB Winners - Sheet1.csv")
winner_list=data["Winner"]
days_mitb=data["Days With MITB"]
date_won=data["Date"]

data_dict={
    "Winner": winner_list,
    "Days With MITB": days_mitb,
    "Date":date_won

}

data=pandas.DataFrame(data_dict)
print(data)
data.to_csv("WINNERS_WITH_DAYS.csv")