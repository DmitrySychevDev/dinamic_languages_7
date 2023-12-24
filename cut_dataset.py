import pandas as pd

# Загрузка CSV файла
df = pd.read_csv('Base.csv')

# Разделение данных на классы
class_0_df = df[df['fraud_bool'] == 0]
class_1_df = df[df['fraud_bool'] == 1]

class_0_sampled = class_0_df.sample(n=10000, random_state=42)
class_1_sampled = class_1_df.sample(n=2000, random_state=42)

# Объединение и перемешивание нового датасета
new_df = pd.concat([class_0_sampled, class_1_sampled])
new_df = new_df.sample(frac=1, random_state=42)

# Сохранение нового датасета
new_df.to_csv('Base_min_shuffled.csv', index=False)