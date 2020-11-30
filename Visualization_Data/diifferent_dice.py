from Visualization_Data.die import Die
import pygal


# 创建一个D6 和 D10
die1 = Die(6)
die2 = Die(10)

# 掷几次骰子，并将结果存在一个列表中

results = []

for roll_num in range(100000):
    result = die1.roll() + die2.roll()
    results.append(result)


# 分析结果
max_result = die1.num_sides + die2.num_sides
frequencies = []
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#对结果进行可视化

hist = pygal.Bar()
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6+D10',frequencies)
hist.render_to_file('die_visual.svg')