# Tutorial material

[Official Cheat Sheet](https://github.com/pandas-dev/pandas/blob/master/doc/cheatsheet/Pandas_Cheat_Sheet.pdf)

## Practice Material

:star2: [EDA on Titanic DataSet](https://github.com/TarekDib03/titanic-EDA/blob/master/Titanic%20-%20Project.ipynb)

:star: [EDA on Automobile DataSet](https://github.com/rushabh-mehta/EDA-on-Automobile-Dataset/blob/master/AutomobileEDA.ipynb)

# Maintaining Data Science Projects

:zap: [ProjectStructure](https://drivendata.github.io/cookiecutter-data-science/)

# Understanding Bias and Variance Trade off

:star2: [Bias Vs Variance](http://scott.fortmann-roe.com/docs/BiasVariance.html)

# Central limit theorem

:star: [Central limit theorem](http://demonstrations.wolfram.com/CentralLimitTheoremForTheContinuousUniformDistribution/)

# Distance Metrics

:star2: [Distance Metrics](https://numerics.mathdotnet.com/Distance.html)

# Metrics to Evaluate Classifiers

:star2: [Precision&Recall](https://en.wikipedia.org/wiki/Precision_and_recall)

# Cook's Distance

:zap: [Cook's Distance](https://www.statisticshowto.datasciencecentral.com/cooks-distance/)

# Statistical course

:+1: [StanfordCourse](https://online.stanford.edu/courses/sohs-ystatslearning-statistical-learning-self-paced)

# Introductory Text Book on Statistics

:book: [Statistic Priciples & Methods](Stats-6th-Edition-by-Johnson-and-Bhattacharyya.pdf)

# Bigger dataset for LinearRegression

:star: [House Prices](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data)

# Using files in google colab

To access files in google drive

```
from google.colab import drive
drive.mount('/gdrive')
%cd /gdrive
```

To upload files to google colab

```
from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))
```

![Or Other way is use the Files tab shown below to upload the files]
(Screenshot 2019-10-11 at 8.14.32 AM.png)
