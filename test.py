import random
import plotly.figure_factory as ff
import statistics

diceResult = []
count = []
for i in range(0,4000):
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  diceResult.append(dice1+dice2)

  count.append(i)

fig = ff.create_distplot([diceResult],['Result'])
fig.show()

mean = sum(diceResult)/len(diceResult)
median = statistics.median(diceResult)
mode = statistics.mode(diceResult)
st = statistics.stdev(diceResult)
print(mean,st)
print(median,mode)