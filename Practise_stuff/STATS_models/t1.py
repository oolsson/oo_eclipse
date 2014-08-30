import statsmodels.api as sm
import pandas
from patsy import dmatrices
from statsmodels.graphics.regressionplots import plot_partregress


url = "http://vincentarelbundock.github.com/Rdatasets/csv/HistData/Guerry.csv"
df = pandas.read_csv(url)
vars = ['Department', 'Lottery', 'Literacy', 'Wealth', 'Region']
df = df[vars]
df = df.dropna()
y, X = dmatrices('Lottery ~ Literacy + Wealth + Region', data=df, return_type='dataframe')
mod = sm.OLS(y, X)
res = mod.fit()
print res.summary()
# plot_partregress(res)