# ©️ Applied Sciences Division - CM

# import dependencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# import data
df = pd.read_csv("data_2021.csv")


outreachOverall = df.loc[df["Outreach"] == "checked"].shape[0]
winOverall = df.loc[df["Win"] == "checked"].shape[0]

industries = {}
outreachIndustries = {}
winIndustries = {}

# separate data according to industry
industries["Community Services"] = df.loc[df["Industry"].str.contains("Community Services")]
industries["Insurance"] = df.loc[df["Industry"].str.contains("Insurance")]
industries["Finance"] = df.loc[df["Industry"].str.contains("Finance")]
industries["Energy"] = df.loc[df["Industry"].str.contains("Energy")]
industries["FinTech"] = df.loc[df["Industry"].str.contains("FinTech")]
industries["HealthTech"] = df.loc[df["Industry"].str.contains("HealthTech")]
industries["Travel and Tourism"] = df.loc[df["Industry"].str.contains("Travel and Tourism")]
industries["Food and Beverage"] = df.loc[df["Industry"].str.contains("Food/Beverage")]
industries["AgriTech"] = df.loc[df["Industry"].str.contains("AgriTech")]
industries["EdTech"] = df.loc[df["Industry"].str.contains("EdTech")]
industries["Not-for-Profit"] = df.loc[df["Industry"].str.contains("Not-for-Profit")]
industries["Real Estate"] = df.loc[df["Industry"].str.contains("Real Estate")]
industries["TMT"] = df.loc[df["Industry"].str.contains("TMT")]
industries["Fitness"] = df.loc[df["Industry"].str.contains("Fitness")]
industries["Hospitality"] = df.loc[df["Industry"].str.contains("Hospitality")]
industries["FoodTech"] = df.loc[df["Industry"].str.contains("Foodtech")]
industries["Personal Care"] = df.loc[df["Industry"].str.contains("Personal Care")]
industries["Venture Capital"] = df.loc[df["Industry"].str.contains("Venture Capital")]
industries["Beauty and Lifestyle"] = df.loc[df["Industry"].str.contains("Beauty and Lifestyle")]
industries["eCommerce"] = df.loc[df["Industry"].str.contains("eCommerce")]
industries["Transport, Logistics and Delivery"] = df.loc[df["Industry"].str.contains("Transport, Logistics and Delivery")]
industries["Dev Sector"] = df.loc[df["Industry"].str.contains("Dev Sector")]
industries["Consumer"] = df.loc[df["Industry"].str.contains("Consumer")]
industries["Entertainment"] = df.loc[df["Industry"].str.contains("Entertainment")]
industries["SaaS"] = df.loc[df["Industry"].str.contains("SaaS")]
industries["Consumer"] = df.loc[df["Industry"].str.contains("Consumer")]
industries["PaaS"] = df.loc[df["Industry"].str.contains("PaaS")]
industries["Professional Services"] = df.loc[df["Industry"].str.contains("Professional Services")]
industries["Sustainability"] = df.loc[df["Industry"].str.contains("Sustainability")]

# populate outreach and win numbers for each industry
for label, data in industries.items():
    outreachIndustries[label] = data.loc[data["Outreach"] == "checked"].shape[0]
    winIndustries[label] = data.loc[data["Win"] == "checked"].shape[0]
    data.to_csv(label + '.csv')
    
print(industries)





