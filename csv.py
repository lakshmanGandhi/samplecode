import pandas as pd
url_prefix = "http://"
df1 = pd.read_csv(url_prefix + "github.com/ppotlakayala/samplecode/blob/feature2/employees.csv")
df2 = df1.set_index("EMAIL", drop = False)
print(df2)
