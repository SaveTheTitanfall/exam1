import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#1
df_sales = pd.read_csv('company_sales_data.csv')
df_sales[['facecream', 'facewash']].plot(kind='bar', color=['blue', 'orange'])
plt.title('Продажі кремів та засобів для вмивання')
plt.xlabel('mounth')
plt.ylabel('k-st')
plt.xticks(range(12), df_sales['month_number'])
plt.show()

#2
df_voltage = pd.read_excel('voltage.xlsx')

# Омічна провідність
plt.loglog(df_voltage['Voltage_1'], np.abs(df_voltage['Current11']), 'b-')
plt.title('om')
plt.xlabel('Voltage_1')
plt.ylabel('|Current11|')
plt.show()

# Інші графіки (аналогічно)
# ...

# Мінімальні та максимальні значення
print(f"Мax: {df_voltage['Iabs'].max()}, min: {df_voltage['Iabs'].min()}")
print(f"max: {df_voltage['Uabs'].max()}, min: {df_voltage['Uabs'].min()}")

# Завдання 3: Рух тіла
time = np.linspace(0, 10, 20)
position = 5 * time + np.random.randn(20)
velocity = np.random.randn(20)
acceleration = np.random.randn(20)

df_motion = pd.DataFrame({
    't': time,
    'pos': position,
    'shv': velocity,
    'shv*dt': acceleration
})

print(f"sered1: {df_motion['shv'].mean()}")
print(f"sered2: {df_motion['shv*dt'].mean()}")

plt.plot(df_motion['t'], df_motion['pos'], 'g-')
plt.title('pos(t)')
plt.show()

# 4
solutions = []
for a in range(-30, 31):
    A = np.array([[1, 1], [2, -1]])
    B = np.array([a, 3])
    try:
        x, y = np.linalg.solve(A, B)
        solutions.append({'a': a, 'x': x, 'y': y})
    except:
        solutions.append({'a': a, 'x': 'eror', 'y': 'eror'})
        print(f"Error occurred for a = {a}")
    

df_solutions = pd.DataFrame(solutions)
print(df_solutions.head())