# Tutorial material

[Official Cheat Sheet](https://github.com/pandas-dev/pandas/blob/master/doc/cheatsheet/Pandas_Cheat_Sheet.pdf)

## Practice Material

:star2: [EDA on Titanic DataSet](https://github.com/TarekDib03/titanic-EDA/blob/master/Titanic%20-%20Project.ipynb)

:star: [EDA on Automobile DataSet](https://github.com/rushabh-mehta/EDA-on-Automobile-Dataset/blob/master/AutomobileEDA.ipynb)

# Maintaining Data Science Projects

:zap: [ProjectStructure](https://drivendata.github.io/cookiecutter-data-science/)

# Understanding Bias and Variance Trade off

:star2: [Bias Vs Variance](http://scott.fortmann-roe.com/docs/BiasVariance.html)

:star:[UnderFit Vs OverFit](https://github.com/WillKoehrsen/Data-Analysis/blob/master/over_vs_under/Over%20vs%20Under%20Fitting%20Example.ipynb)

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

# Project I -- LinearRegression

:star: [House Prices](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data)

# Project II -- Classification

:star: [Titanic](https://www.kaggle.com/c/titanic/overview)

:star2: [Fraud Detection](https://www.kaggle.com/c/ieee-fraud-detection/overview)

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

Or Other way is use the Files tab shown below to upload the files

<img src="https://github.com/HarshaVardhanBabu/TutorialMaterial/blob/master/Screenshot%202019-10-11%20at%208.14.32%20AM.png" />

# Demo

:+1: [Digit Recognition App](http://myselph.de/neuralNet.html)

:+1: [TensorFlow Playground](https://playground.tensorflow.org/)

:+1: [Dash SVM](https://github.com/plotly/dash-sample-apps/tree/master/apps/dash-svm)

:+1: [Movie Recommendation tool](https://github.com/abd1007/Movie-Recommendation-System-Web-Application)
