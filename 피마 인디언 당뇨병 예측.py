from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import pandas as pd
!git clone https://github.com/taehojo/data.gitdf = pd.read_csv('./data/pima-indians-diabetes3.csv’)
train_X = df.iloc[:720, 0:8]
train_y = df.iloc[:720, 8]
test_X = df.iloc[720:, 0:8]
test_y = df.iloc[720:, 8]
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu', name='Dense_1'))
model.add(Dense(8, activation='relu', name='Dense_2'))
model.add(Dense(1, activation='sigmoid', name='Dense_3'))
model.summary()
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
history = model.fit(X, y, epochs=100, batch_size=5)
test_loss, test_accuracy = model.evaluate(test_X, test_y)
print('테스트 데이터 정확도', test_accuracy)
