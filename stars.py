import pandas

df = pandas.read_csv("List_of_brown_dwarfs.csv")

df = df[df["Star_name"].notna()]
df = df[df["Distance"].notna()]
df = df[df["Mass"].notna()]
df = df[df["Radius"].notna()]

df["Radius"] = 0.102763 * df["Radius"]

df["Mass"] = df["Mass"].apply(lambda x: x.replace(
    "$", "").replace(",", "")).astype("float")
df["Mass"] = 0.000954588 * df["Mass"]

df.drop(['Unnamed: 0'], axis=1, inplace=True)
df.reset_index(drop=True, inplace=True)

df.to_csv("List_of_star.csv")
