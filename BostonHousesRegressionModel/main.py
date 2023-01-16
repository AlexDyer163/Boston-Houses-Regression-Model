from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor




def GradientBoostingRegression(x_train, x_test, y_train, y_test):
    model = GradientBoostingRegressor(random_state=0).fit(x_train, y_train)
    print(model.score(x_train, y_train))
    print(model.score(x_test,y_test))
    print(model.predict(x_test))

def RandomForestRegression(x_train, x_test, y_train, y_test):
    model = RandomForestRegressor(random_state = 0).fit(x_train,y_train)
    print(model.score(x_train, y_train))
    print(model.score(x_test, y_test))
    print(model.predict(x_test))

def LinearRegressionMethod(x_train,x_test,y_train,y_test):
    x, y = load_boston(return_X_y=True)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=0)
    model = LinearRegression().fit(x_train, y_train)
    print(model.score(x_train, y_train))
    print(model.score(x_test, y_test))
    # gets the coefficient of determination for the test data
    print(model.predict(x_test))
    # predicts using the model




while True:
    x, y = load_boston(return_X_y=True)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=0)
    try:
        Selection = int(input("What regression form would you like to use?: \n 1) Linear Regression \n 2) Gradient Boosting Regression \n 3) Random Forest Regression"))
    except:
        continue
    else:
        if Selection == 1:
            LinearRegressionMethod(x_train,x_test,y_train,y_test)# An issue is caused due to the version of the particular package, the others function as normal
        elif Selection == 2:
            GradientBoostingRegression(x_train, x_test, y_train, y_test)
        elif Selection == 3:
            RandomForestRegression(x_train, x_test, y_train, y_test)
        break
