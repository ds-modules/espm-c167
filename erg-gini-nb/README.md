# ER190C
This homework will be the first of two using the California EnviroScreen data set (https://oehha.ca.gov/calenviroscreen/report/calenviroscreen-30) to explore tools for classification.

The focus here will be on application of classification trees to identify community characteristics (race, income, education) that predict environmental conditions in those communities.

Some resources on decision trees and classification: 
- https://machinelearningmastery.com/implement-decision-tree-algorithm-scratch-python/
- http://dataaspirant.com/2017/02/01/decision-tree-algorithm-python-with-scikit-learn/
- https://jakevdp.github.io/PythonDataScienceHandbook/05.08-random-forests.html
- https://www.youtube.com/watch?v=LDRbO9a6XPU

* Note: The California EnviroScreen dataset's environmental condition variables are real-valued and classification models predict discrete values, so the strategy here would be  to similar to that used in hw 11 - svm, partioning the pollution score data into percentiles, and only taking the observations with pollution scores that fall into the top percentile and bottom percentile. This will simplify the classification task into using socioeconomic factors (features) to predict whether a given observation falls into either the most or least polluted category. Although this simplifies the classification task, the way the data is sampled from the dataset introduces biases, which can serve as a pedogical segway to discussing the importance of carefully choosing proper sampling techniques.

