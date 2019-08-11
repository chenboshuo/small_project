
# 安装
在github中找到类的定义,并导入

https://github.com/chenboshuo/small_project/blob/master/lingo_analysis/src/LingoOut.py



# 导入
可以直接定义类或者在这个文件夹内导入


```python
import sys

sys.path.append('../src/')
from LingoOut import LingoOut
```

# 定义类
假设有这样的结果文件`sample.txt`
```plaintext
Global optimal solution found.
  Objective value:                              19660.00
  Objective bound:                              19660.00
  Infeasibilities:                              0.000000
  Extended solver steps:                               0
  Total solver iterations:                          4667

  Model Class:                                      MILP

  Total variables:                   2600
  Nonlinear variables:                  0
  Integer variables:                   50

  Total constraints:                 2602
  Nonlinear constraints:                0

  Total nonzeros:                   10100
  Nonlinear nonzeros:                   0

                                                    Variable           Value
                                                       X( 1)        0.000000
                                                       X( 2)        0.000000
                                                       X( 3)        0.000000
                                                       X( 4)        0.000000
                                                       X( 5)        0.000000
                                                       X( 6)        0.000000
                                                       X( 7)        0.000000
                                                       X( 8)        0.000000
```  
可以通过一下代码定义


```python
o = LingoOut('sample.txt')
```

# 开始

## 打印原始文档

可以通过`raw`函数输出文档信息


```python
o.raw()
```


```plaintext
  1   Global optimal solution found.
     2   Objective value:                              19660.00
     3   Objective bound:                              19660.00
     4   Infeasibilities:                              0.000000
     5   Extended solver steps:                               0
     6   Total solver iterations:                          4667
     7
     8   Model Class:                                      MILP
     9
     10   Total variables:                   2600
     11   Nonlinear variables:                  0
     12   Integer variables:                   50
     13
     14   Total constraints:                 2602
     15   Nonlinear constraints:                0
     16
     17   Total nonzeros:                   10100
     18   Nonlinear nonzeros:                   0
     19
     20                                                     Variable           Value
     21                                                        X( 1)        0.000000
     22                                                        X( 2)        0.000000
     23                                                        X( 3)        0.000000
     24                                                        X( 4)        0.000000
     25                                                        X( 5)        0.000000
     26                                                        X( 6)        0.000000
     27                                                        X( 7)        0.000000
     28                                                        X( 8)        0.000000
     29                                                        X( 9)        0.000000
     .
     .
     .

     2602        0.000000            0.000000

```
可以通过参数控制行数


```python
o.raw(50) # 打印文件前50行
```

    1   Global optimal solution found.
     2   Objective value:                              19660.00
     3   Objective bound:                              19660.00
     4   Infeasibilities:                              0.000000
     5   Extended solver steps:                               0
     6   Total solver iterations:                          4667
     7
     8   Model Class:                                      MILP
     9
     10   Total variables:                   2600
     11   Nonlinear variables:                  0
     12   Integer variables:                   50
     13
     14   Total constraints:                 2602
     15   Nonlinear constraints:                0
     16
     17   Total nonzeros:                   10100
     18   Nonlinear nonzeros:                   0
     19
     20                                                     Variable           Value
     21                                                        X( 1)        0.000000
     22                                                        X( 2)        0.000000
     23                                                        X( 3)        0.000000
     24                                                        X( 4)        0.000000
     25                                                        X( 5)        0.000000
     26                                                        X( 6)        0.000000
     27                                                        X( 7)        0.000000
     28                                                        X( 8)        0.000000
     29                                                        X( 9)        0.000000
     30                                                       X( 10)        0.000000
     31                                                       X( 11)        0.000000
     32                                                       X( 12)        0.000000
     33                                                       X( 13)        0.000000
     34                                                       X( 14)        0.000000
     35                                                       X( 15)        1.000000
     36                                                       X( 16)        0.000000
     37                                                       X( 17)        0.000000
     38                                                       X( 18)        0.000000
     39                                                       X( 19)        0.000000
     40                                                       X( 20)        0.000000
     41                                                       X( 21)        1.000000
     42                                                       X( 22)        0.000000
     43                                                       X( 23)        0.000000
     44                                                       X( 24)        0.000000
     45                                                       X( 25)        0.000000
     46                                                       X( 26)        0.000000
     47                                                       X( 27)        0.000000
     48                                                       X( 28)        0.000000
     49                                                       X( 29)        0.000000
     50                                                       X( 30)        0.000000


## 查看基本信息


```python
print(o)
```

    Objective value:          19660.0
    Objective bound:          19660.0
    Infeasibilities:          0.0
    Extended solver steps:    0.0
    Total solver iterations:  4667.0
    Model Class:              MILP
    Nonlinear variables:      0.0
    Integer variables:        50.0
    Total constraints:        2602.0
    Nonlinear constraints:    0.0
    Total nonzeros:           10100.0
    Nonlinear nonzeros:       0.0



以上信息存储在字典`info`中


```python
o.info
```




    {'Objective value': 19660.0,
     'Objective bound': 19660.0,
     'Infeasibilities': 0.0,
     'Extended solver steps': 0.0,
     'Total solver iterations': 4667.0,
     'Model Class': 'MILP',
     'Total variables': 2600.0,
     'Nonlinear variables': 0.0,
     'Integer variables': 50.0,
     'Total constraints': 2602.0,
     'Nonlinear constraints': 0.0,
     'Total nonzeros': 10100.0,
     'Nonlinear nonzeros': 0.0}



## 查看变量信息

变量存储在字典`variable`中,可以直接查看


```python
o.variable
```
```plaintext





    {'X': {1: 0.0,
      2: 0.0,
      3: 0.0,
      4: 0.0,
      5: 0.0,
      6: 0.0,
      7: 0.0,
      8: 0.0,
      9: 0.0,
      10: 0.0,
      11: 0.0,
      12: 0.0,
      ...
```



因为是字典, 可以转化为`DataFame`查看


```python
import pandas as pd
df = pd.DataFrame(o.variable)
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>X</th>
      <th>L</th>
      <th>D</th>
      <th>U</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>0.0</td>
      <td>630.0</td>
      <td>{1: 0.0, 2: 400.0, 3: 450.0, 4: 700.0, 5: 910....</td>
      <td>{1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0....</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.0</td>
      <td>230.0</td>
      <td>{1: 400.0, 2: 0.0, 3: 850.0, 4: 300.0, 5: 510....</td>
      <td>{1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0....</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.0</td>
      <td>1080.0</td>
      <td>{1: 450.0, 2: 850.0, 3: 0.0, 4: 600.0, 5: 810....</td>
      <td>{1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0....</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.0</td>
      <td>530.0</td>
      <td>{1: 700.0, 2: 300.0, 3: 600.0, 4: 0.0, 5: 210....</td>
      <td>{1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0....</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.0</td>
      <td>655.0</td>
      <td>{1: 910.0, 2: 510.0, 3: 810.0, 4: 210.0, 5: 0....</td>
      <td>{1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0....</td>
    </tr>
  </tbody>
</table>
</div>




```python
d = pd.DataFrame(o.variable["D"])
d
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
      <th>...</th>
      <th>41</th>
      <th>42</th>
      <th>43</th>
      <th>44</th>
      <th>45</th>
      <th>46</th>
      <th>47</th>
      <th>48</th>
      <th>49</th>
      <th>50</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>0.0</td>
      <td>400.0</td>
      <td>450.0</td>
      <td>700.0</td>
      <td>910.0</td>
      <td>1140.0</td>
      <td>1110.0</td>
      <td>1280.0</td>
      <td>1480.0</td>
      <td>1614.0</td>
      <td>...</td>
      <td>1840.0</td>
      <td>1320.0</td>
      <td>1310.0</td>
      <td>1050.0</td>
      <td>1200.0</td>
      <td>1390.0</td>
      <td>540.0</td>
      <td>1110.0</td>
      <td>1310.0</td>
      <td>1510.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>400.0</td>
      <td>0.0</td>
      <td>850.0</td>
      <td>300.0</td>
      <td>510.0</td>
      <td>740.0</td>
      <td>710.0</td>
      <td>880.0</td>
      <td>1080.0</td>
      <td>1214.0</td>
      <td>...</td>
      <td>1440.0</td>
      <td>920.0</td>
      <td>910.0</td>
      <td>650.0</td>
      <td>800.0</td>
      <td>990.0</td>
      <td>140.0</td>
      <td>710.0</td>
      <td>910.0</td>
      <td>1110.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>450.0</td>
      <td>850.0</td>
      <td>0.0</td>
      <td>600.0</td>
      <td>810.0</td>
      <td>1040.0</td>
      <td>1010.0</td>
      <td>1180.0</td>
      <td>1380.0</td>
      <td>1560.0</td>
      <td>...</td>
      <td>2205.0</td>
      <td>1745.0</td>
      <td>1735.0</td>
      <td>1475.0</td>
      <td>1650.0</td>
      <td>1840.0</td>
      <td>990.0</td>
      <td>1560.0</td>
      <td>1760.0</td>
      <td>1875.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>700.0</td>
      <td>300.0</td>
      <td>600.0</td>
      <td>0.0</td>
      <td>210.0</td>
      <td>440.0</td>
      <td>410.0</td>
      <td>580.0</td>
      <td>780.0</td>
      <td>960.0</td>
      <td>...</td>
      <td>1605.0</td>
      <td>1145.0</td>
      <td>1135.0</td>
      <td>875.0</td>
      <td>1100.0</td>
      <td>1290.0</td>
      <td>440.0</td>
      <td>1010.0</td>
      <td>1210.0</td>
      <td>1275.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>910.0</td>
      <td>510.0</td>
      <td>810.0</td>
      <td>210.0</td>
      <td>0.0</td>
      <td>230.0</td>
      <td>200.0</td>
      <td>370.0</td>
      <td>570.0</td>
      <td>750.0</td>
      <td>...</td>
      <td>1815.0</td>
      <td>1355.0</td>
      <td>1345.0</td>
      <td>1085.0</td>
      <td>1310.0</td>
      <td>1500.0</td>
      <td>650.0</td>
      <td>1220.0</td>
      <td>1420.0</td>
      <td>1485.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1140.0</td>
      <td>740.0</td>
      <td>1040.0</td>
      <td>440.0</td>
      <td>230.0</td>
      <td>0.0</td>
      <td>320.0</td>
      <td>340.0</td>
      <td>540.0</td>
      <td>720.0</td>
      <td>...</td>
      <td>1950.0</td>
      <td>1490.0</td>
      <td>1480.0</td>
      <td>1220.0</td>
      <td>1540.0</td>
      <td>1730.0</td>
      <td>880.0</td>
      <td>1450.0</td>
      <td>1650.0</td>
      <td>1620.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1110.0</td>
      <td>710.0</td>
      <td>1010.0</td>
      <td>410.0</td>
      <td>200.0</td>
      <td>320.0</td>
      <td>0.0</td>
      <td>170.0</td>
      <td>370.0</td>
      <td>550.0</td>
      <td>...</td>
      <td>1630.0</td>
      <td>1170.0</td>
      <td>1160.0</td>
      <td>900.0</td>
      <td>1254.0</td>
      <td>1444.0</td>
      <td>850.0</td>
      <td>1164.0</td>
      <td>1364.0</td>
      <td>1300.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1280.0</td>
      <td>880.0</td>
      <td>1180.0</td>
      <td>580.0</td>
      <td>370.0</td>
      <td>340.0</td>
      <td>170.0</td>
      <td>0.0</td>
      <td>200.0</td>
      <td>380.0</td>
      <td>...</td>
      <td>1800.0</td>
      <td>1340.0</td>
      <td>1330.0</td>
      <td>1070.0</td>
      <td>1424.0</td>
      <td>1614.0</td>
      <td>1020.0</td>
      <td>1334.0</td>
      <td>1534.0</td>
      <td>1470.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1480.0</td>
      <td>1080.0</td>
      <td>1380.0</td>
      <td>780.0</td>
      <td>570.0</td>
      <td>540.0</td>
      <td>370.0</td>
      <td>200.0</td>
      <td>0.0</td>
      <td>180.0</td>
      <td>...</td>
      <td>1940.0</td>
      <td>1540.0</td>
      <td>1530.0</td>
      <td>1270.0</td>
      <td>1624.0</td>
      <td>1814.0</td>
      <td>1220.0</td>
      <td>1534.0</td>
      <td>1734.0</td>
      <td>1640.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1614.0</td>
      <td>1214.0</td>
      <td>1560.0</td>
      <td>960.0</td>
      <td>750.0</td>
      <td>720.0</td>
      <td>550.0</td>
      <td>380.0</td>
      <td>180.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>1760.0</td>
      <td>1470.0</td>
      <td>1460.0</td>
      <td>1200.0</td>
      <td>1554.0</td>
      <td>1744.0</td>
      <td>1334.0</td>
      <td>1464.0</td>
      <td>1664.0</td>
      <td>1460.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>1764.0</td>
      <td>1364.0</td>
      <td>1710.0</td>
      <td>1110.0</td>
      <td>900.0</td>
      <td>870.0</td>
      <td>700.0</td>
      <td>530.0</td>
      <td>330.0</td>
      <td>150.0</td>
      <td>...</td>
      <td>1610.0</td>
      <td>1440.0</td>
      <td>1430.0</td>
      <td>1170.0</td>
      <td>1600.0</td>
      <td>1790.0</td>
      <td>1484.0</td>
      <td>1510.0</td>
      <td>1710.0</td>
      <td>1310.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>1904.0</td>
      <td>1504.0</td>
      <td>1850.0</td>
      <td>1250.0</td>
      <td>1040.0</td>
      <td>1010.0</td>
      <td>840.0</td>
      <td>670.0</td>
      <td>470.0</td>
      <td>290.0</td>
      <td>...</td>
      <td>1570.0</td>
      <td>1580.0</td>
      <td>1570.0</td>
      <td>1310.0</td>
      <td>1740.0</td>
      <td>1930.0</td>
      <td>1624.0</td>
      <td>1650.0</td>
      <td>1850.0</td>
      <td>1440.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2104.0</td>
      <td>1704.0</td>
      <td>2050.0</td>
      <td>1450.0</td>
      <td>1240.0</td>
      <td>1210.0</td>
      <td>1040.0</td>
      <td>870.0</td>
      <td>670.0</td>
      <td>490.0</td>
      <td>...</td>
      <td>1370.0</td>
      <td>1400.0</td>
      <td>1480.0</td>
      <td>1510.0</td>
      <td>1690.0</td>
      <td>1930.0</td>
      <td>1824.0</td>
      <td>1850.0</td>
      <td>2050.0</td>
      <td>1240.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1644.0</td>
      <td>1244.0</td>
      <td>1604.0</td>
      <td>1004.0</td>
      <td>845.0</td>
      <td>815.0</td>
      <td>645.0</td>
      <td>475.0</td>
      <td>460.0</td>
      <td>280.0</td>
      <td>...</td>
      <td>1480.0</td>
      <td>1310.0</td>
      <td>1300.0</td>
      <td>1040.0</td>
      <td>1470.0</td>
      <td>1660.0</td>
      <td>1364.0</td>
      <td>1380.0</td>
      <td>1580.0</td>
      <td>1180.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>1454.0</td>
      <td>1054.0</td>
      <td>1414.0</td>
      <td>814.0</td>
      <td>655.0</td>
      <td>625.0</td>
      <td>455.0</td>
      <td>285.0</td>
      <td>340.0</td>
      <td>160.0</td>
      <td>...</td>
      <td>1670.0</td>
      <td>1310.0</td>
      <td>1300.0</td>
      <td>1040.0</td>
      <td>1394.0</td>
      <td>1584.0</td>
      <td>1174.0</td>
      <td>1304.0</td>
      <td>1504.0</td>
      <td>1340.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>1284.0</td>
      <td>884.0</td>
      <td>1244.0</td>
      <td>644.0</td>
      <td>490.0</td>
      <td>610.0</td>
      <td>290.0</td>
      <td>455.0</td>
      <td>510.0</td>
      <td>330.0</td>
      <td>...</td>
      <td>1560.0</td>
      <td>1140.0</td>
      <td>1130.0</td>
      <td>870.0</td>
      <td>1224.0</td>
      <td>1414.0</td>
      <td>1004.0</td>
      <td>1134.0</td>
      <td>1334.0</td>
      <td>1230.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>1424.0</td>
      <td>1024.0</td>
      <td>1384.0</td>
      <td>784.0</td>
      <td>630.0</td>
      <td>750.0</td>
      <td>430.0</td>
      <td>535.0</td>
      <td>590.0</td>
      <td>410.0</td>
      <td>...</td>
      <td>1420.0</td>
      <td>1220.0</td>
      <td>1210.0</td>
      <td>950.0</td>
      <td>1364.0</td>
      <td>1554.0</td>
      <td>1144.0</td>
      <td>1274.0</td>
      <td>1474.0</td>
      <td>1090.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>1154.0</td>
      <td>754.0</td>
      <td>1114.0</td>
      <td>514.0</td>
      <td>360.0</td>
      <td>480.0</td>
      <td>160.0</td>
      <td>330.0</td>
      <td>530.0</td>
      <td>460.0</td>
      <td>...</td>
      <td>1470.0</td>
      <td>1010.0</td>
      <td>1000.0</td>
      <td>740.0</td>
      <td>1094.0</td>
      <td>1284.0</td>
      <td>874.0</td>
      <td>1004.0</td>
      <td>1204.0</td>
      <td>1140.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>950.0</td>
      <td>550.0</td>
      <td>910.0</td>
      <td>310.0</td>
      <td>520.0</td>
      <td>684.0</td>
      <td>364.0</td>
      <td>534.0</td>
      <td>734.0</td>
      <td>664.0</td>
      <td>...</td>
      <td>1295.0</td>
      <td>835.0</td>
      <td>825.0</td>
      <td>565.0</td>
      <td>890.0</td>
      <td>1080.0</td>
      <td>670.0</td>
      <td>800.0</td>
      <td>1000.0</td>
      <td>965.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>810.0</td>
      <td>410.0</td>
      <td>1050.0</td>
      <td>450.0</td>
      <td>660.0</td>
      <td>824.0</td>
      <td>504.0</td>
      <td>674.0</td>
      <td>874.0</td>
      <td>804.0</td>
      <td>...</td>
      <td>1310.0</td>
      <td>850.0</td>
      <td>840.0</td>
      <td>580.0</td>
      <td>750.0</td>
      <td>940.0</td>
      <td>530.0</td>
      <td>660.0</td>
      <td>860.0</td>
      <td>980.0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>630.0</td>
      <td>230.0</td>
      <td>1080.0</td>
      <td>530.0</td>
      <td>740.0</td>
      <td>970.0</td>
      <td>684.0</td>
      <td>854.0</td>
      <td>1054.0</td>
      <td>984.0</td>
      <td>...</td>
      <td>1210.0</td>
      <td>690.0</td>
      <td>680.0</td>
      <td>420.0</td>
      <td>570.0</td>
      <td>760.0</td>
      <td>350.0</td>
      <td>480.0</td>
      <td>680.0</td>
      <td>880.0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>930.0</td>
      <td>530.0</td>
      <td>1380.0</td>
      <td>830.0</td>
      <td>1040.0</td>
      <td>1270.0</td>
      <td>984.0</td>
      <td>1154.0</td>
      <td>1354.0</td>
      <td>1284.0</td>
      <td>...</td>
      <td>1250.0</td>
      <td>730.0</td>
      <td>420.0</td>
      <td>160.0</td>
      <td>270.0</td>
      <td>460.0</td>
      <td>650.0</td>
      <td>180.0</td>
      <td>380.0</td>
      <td>920.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>900.0</td>
      <td>500.0</td>
      <td>1325.0</td>
      <td>725.0</td>
      <td>935.0</td>
      <td>1070.0</td>
      <td>750.0</td>
      <td>920.0</td>
      <td>1120.0</td>
      <td>1050.0</td>
      <td>...</td>
      <td>940.0</td>
      <td>420.0</td>
      <td>410.0</td>
      <td>150.0</td>
      <td>580.0</td>
      <td>770.0</td>
      <td>620.0</td>
      <td>490.0</td>
      <td>690.0</td>
      <td>610.0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>1000.0</td>
      <td>600.0</td>
      <td>1085.0</td>
      <td>485.0</td>
      <td>695.0</td>
      <td>830.0</td>
      <td>510.0</td>
      <td>680.0</td>
      <td>880.0</td>
      <td>810.0</td>
      <td>...</td>
      <td>1120.0</td>
      <td>660.0</td>
      <td>650.0</td>
      <td>390.0</td>
      <td>820.0</td>
      <td>1010.0</td>
      <td>720.0</td>
      <td>730.0</td>
      <td>930.0</td>
      <td>790.0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>1170.0</td>
      <td>770.0</td>
      <td>1255.0</td>
      <td>655.0</td>
      <td>540.0</td>
      <td>660.0</td>
      <td>340.0</td>
      <td>510.0</td>
      <td>710.0</td>
      <td>640.0</td>
      <td>...</td>
      <td>1290.0</td>
      <td>830.0</td>
      <td>820.0</td>
      <td>560.0</td>
      <td>990.0</td>
      <td>1180.0</td>
      <td>890.0</td>
      <td>900.0</td>
      <td>1100.0</td>
      <td>960.0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>1460.0</td>
      <td>1060.0</td>
      <td>1545.0</td>
      <td>945.0</td>
      <td>1010.0</td>
      <td>1005.0</td>
      <td>810.0</td>
      <td>665.0</td>
      <td>650.0</td>
      <td>470.0</td>
      <td>...</td>
      <td>1290.0</td>
      <td>1120.0</td>
      <td>1110.0</td>
      <td>850.0</td>
      <td>1280.0</td>
      <td>1470.0</td>
      <td>1180.0</td>
      <td>1190.0</td>
      <td>1390.0</td>
      <td>990.0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>1320.0</td>
      <td>920.0</td>
      <td>1405.0</td>
      <td>805.0</td>
      <td>870.0</td>
      <td>990.0</td>
      <td>670.0</td>
      <td>775.0</td>
      <td>790.0</td>
      <td>610.0</td>
      <td>...</td>
      <td>1180.0</td>
      <td>980.0</td>
      <td>970.0</td>
      <td>710.0</td>
      <td>1140.0</td>
      <td>1330.0</td>
      <td>1040.0</td>
      <td>1050.0</td>
      <td>1250.0</td>
      <td>850.0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>1130.0</td>
      <td>730.0</td>
      <td>1215.0</td>
      <td>615.0</td>
      <td>825.0</td>
      <td>960.0</td>
      <td>640.0</td>
      <td>810.0</td>
      <td>980.0</td>
      <td>800.0</td>
      <td>...</td>
      <td>990.0</td>
      <td>790.0</td>
      <td>780.0</td>
      <td>520.0</td>
      <td>950.0</td>
      <td>1140.0</td>
      <td>850.0</td>
      <td>860.0</td>
      <td>1060.0</td>
      <td>660.0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>1110.0</td>
      <td>710.0</td>
      <td>1475.0</td>
      <td>875.0</td>
      <td>1085.0</td>
      <td>1220.0</td>
      <td>900.0</td>
      <td>1070.0</td>
      <td>1240.0</td>
      <td>1060.0</td>
      <td>...</td>
      <td>730.0</td>
      <td>560.0</td>
      <td>620.0</td>
      <td>360.0</td>
      <td>790.0</td>
      <td>980.0</td>
      <td>830.0</td>
      <td>700.0</td>
      <td>900.0</td>
      <td>400.0</td>
    </tr>
    <tr>
      <th>30</th>
      <td>1190.0</td>
      <td>790.0</td>
      <td>1615.0</td>
      <td>1015.0</td>
      <td>1225.0</td>
      <td>1360.0</td>
      <td>1040.0</td>
      <td>1210.0</td>
      <td>1410.0</td>
      <td>1340.0</td>
      <td>...</td>
      <td>660.0</td>
      <td>130.0</td>
      <td>210.0</td>
      <td>440.0</td>
      <td>420.0</td>
      <td>660.0</td>
      <td>910.0</td>
      <td>780.0</td>
      <td>980.0</td>
      <td>330.0</td>
    </tr>
    <tr>
      <th>31</th>
      <td>1300.0</td>
      <td>900.0</td>
      <td>1665.0</td>
      <td>1065.0</td>
      <td>1275.0</td>
      <td>1410.0</td>
      <td>1090.0</td>
      <td>1260.0</td>
      <td>1430.0</td>
      <td>1250.0</td>
      <td>...</td>
      <td>540.0</td>
      <td>370.0</td>
      <td>450.0</td>
      <td>550.0</td>
      <td>660.0</td>
      <td>900.0</td>
      <td>1020.0</td>
      <td>890.0</td>
      <td>1090.0</td>
      <td>210.0</td>
    </tr>
    <tr>
      <th>32</th>
      <td>1530.0</td>
      <td>1130.0</td>
      <td>1895.0</td>
      <td>1295.0</td>
      <td>1505.0</td>
      <td>1640.0</td>
      <td>1320.0</td>
      <td>1385.0</td>
      <td>1370.0</td>
      <td>1190.0</td>
      <td>...</td>
      <td>570.0</td>
      <td>600.0</td>
      <td>680.0</td>
      <td>780.0</td>
      <td>890.0</td>
      <td>1130.0</td>
      <td>1250.0</td>
      <td>1120.0</td>
      <td>1320.0</td>
      <td>440.0</td>
    </tr>
    <tr>
      <th>33</th>
      <td>1720.0</td>
      <td>1320.0</td>
      <td>2075.0</td>
      <td>1475.0</td>
      <td>1540.0</td>
      <td>1535.0</td>
      <td>1340.0</td>
      <td>1195.0</td>
      <td>1180.0</td>
      <td>1000.0</td>
      <td>...</td>
      <td>760.0</td>
      <td>790.0</td>
      <td>870.0</td>
      <td>970.0</td>
      <td>1080.0</td>
      <td>1320.0</td>
      <td>1440.0</td>
      <td>1310.0</td>
      <td>1510.0</td>
      <td>630.0</td>
    </tr>
    <tr>
      <th>34</th>
      <td>1780.0</td>
      <td>1380.0</td>
      <td>1865.0</td>
      <td>1265.0</td>
      <td>1330.0</td>
      <td>1325.0</td>
      <td>1130.0</td>
      <td>985.0</td>
      <td>970.0</td>
      <td>790.0</td>
      <td>...</td>
      <td>970.0</td>
      <td>1000.0</td>
      <td>1080.0</td>
      <td>1170.0</td>
      <td>1290.0</td>
      <td>1530.0</td>
      <td>1500.0</td>
      <td>1510.0</td>
      <td>1710.0</td>
      <td>840.0</td>
    </tr>
    <tr>
      <th>35</th>
      <td>1670.0</td>
      <td>1270.0</td>
      <td>2035.0</td>
      <td>1435.0</td>
      <td>1645.0</td>
      <td>1780.0</td>
      <td>1460.0</td>
      <td>1525.0</td>
      <td>1510.0</td>
      <td>1330.0</td>
      <td>...</td>
      <td>710.0</td>
      <td>740.0</td>
      <td>820.0</td>
      <td>920.0</td>
      <td>1030.0</td>
      <td>1270.0</td>
      <td>1390.0</td>
      <td>1260.0</td>
      <td>1460.0</td>
      <td>580.0</td>
    </tr>
    <tr>
      <th>36</th>
      <td>1560.0</td>
      <td>1160.0</td>
      <td>1925.0</td>
      <td>1325.0</td>
      <td>1535.0</td>
      <td>1670.0</td>
      <td>1350.0</td>
      <td>1520.0</td>
      <td>1610.0</td>
      <td>1430.0</td>
      <td>...</td>
      <td>330.0</td>
      <td>580.0</td>
      <td>710.0</td>
      <td>810.0</td>
      <td>920.0</td>
      <td>1160.0</td>
      <td>1280.0</td>
      <td>1150.0</td>
      <td>1350.0</td>
      <td>380.0</td>
    </tr>
    <tr>
      <th>37</th>
      <td>1830.0</td>
      <td>1430.0</td>
      <td>2195.0</td>
      <td>1595.0</td>
      <td>1805.0</td>
      <td>1940.0</td>
      <td>1620.0</td>
      <td>1685.0</td>
      <td>1670.0</td>
      <td>1490.0</td>
      <td>...</td>
      <td>575.0</td>
      <td>900.0</td>
      <td>980.0</td>
      <td>1080.0</td>
      <td>1190.0</td>
      <td>1430.0</td>
      <td>1550.0</td>
      <td>1420.0</td>
      <td>1620.0</td>
      <td>740.0</td>
    </tr>
    <tr>
      <th>38</th>
      <td>1870.0</td>
      <td>1470.0</td>
      <td>2235.0</td>
      <td>1635.0</td>
      <td>1845.0</td>
      <td>1980.0</td>
      <td>1660.0</td>
      <td>1820.0</td>
      <td>1805.0</td>
      <td>1625.0</td>
      <td>...</td>
      <td>440.0</td>
      <td>890.0</td>
      <td>1020.0</td>
      <td>1120.0</td>
      <td>1230.0</td>
      <td>1470.0</td>
      <td>1590.0</td>
      <td>1460.0</td>
      <td>1660.0</td>
      <td>690.0</td>
    </tr>
    <tr>
      <th>39</th>
      <td>1740.0</td>
      <td>1340.0</td>
      <td>2105.0</td>
      <td>1505.0</td>
      <td>1715.0</td>
      <td>1850.0</td>
      <td>1530.0</td>
      <td>1700.0</td>
      <td>1790.0</td>
      <td>1610.0</td>
      <td>...</td>
      <td>310.0</td>
      <td>760.0</td>
      <td>890.0</td>
      <td>990.0</td>
      <td>1100.0</td>
      <td>1340.0</td>
      <td>1460.0</td>
      <td>1330.0</td>
      <td>1530.0</td>
      <td>560.0</td>
    </tr>
    <tr>
      <th>40</th>
      <td>1700.0</td>
      <td>1300.0</td>
      <td>2065.0</td>
      <td>1465.0</td>
      <td>1675.0</td>
      <td>1810.0</td>
      <td>1490.0</td>
      <td>1660.0</td>
      <td>1800.0</td>
      <td>1620.0</td>
      <td>...</td>
      <td>140.0</td>
      <td>390.0</td>
      <td>730.0</td>
      <td>950.0</td>
      <td>940.0</td>
      <td>1180.0</td>
      <td>1420.0</td>
      <td>1290.0</td>
      <td>1490.0</td>
      <td>190.0</td>
    </tr>
    <tr>
      <th>41</th>
      <td>1840.0</td>
      <td>1440.0</td>
      <td>2205.0</td>
      <td>1605.0</td>
      <td>1815.0</td>
      <td>1950.0</td>
      <td>1630.0</td>
      <td>1800.0</td>
      <td>1940.0</td>
      <td>1760.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>530.0</td>
      <td>870.0</td>
      <td>1090.0</td>
      <td>1080.0</td>
      <td>1320.0</td>
      <td>1560.0</td>
      <td>1430.0</td>
      <td>1630.0</td>
      <td>330.0</td>
    </tr>
    <tr>
      <th>42</th>
      <td>1320.0</td>
      <td>920.0</td>
      <td>1745.0</td>
      <td>1145.0</td>
      <td>1355.0</td>
      <td>1490.0</td>
      <td>1170.0</td>
      <td>1340.0</td>
      <td>1540.0</td>
      <td>1470.0</td>
      <td>...</td>
      <td>530.0</td>
      <td>0.0</td>
      <td>340.0</td>
      <td>570.0</td>
      <td>550.0</td>
      <td>790.0</td>
      <td>1040.0</td>
      <td>910.0</td>
      <td>1110.0</td>
      <td>200.0</td>
    </tr>
    <tr>
      <th>43</th>
      <td>1310.0</td>
      <td>910.0</td>
      <td>1735.0</td>
      <td>1135.0</td>
      <td>1345.0</td>
      <td>1480.0</td>
      <td>1160.0</td>
      <td>1330.0</td>
      <td>1530.0</td>
      <td>1460.0</td>
      <td>...</td>
      <td>870.0</td>
      <td>340.0</td>
      <td>0.0</td>
      <td>260.0</td>
      <td>210.0</td>
      <td>450.0</td>
      <td>1030.0</td>
      <td>600.0</td>
      <td>800.0</td>
      <td>540.0</td>
    </tr>
    <tr>
      <th>44</th>
      <td>1050.0</td>
      <td>650.0</td>
      <td>1475.0</td>
      <td>875.0</td>
      <td>1085.0</td>
      <td>1220.0</td>
      <td>900.0</td>
      <td>1070.0</td>
      <td>1270.0</td>
      <td>1200.0</td>
      <td>...</td>
      <td>1090.0</td>
      <td>570.0</td>
      <td>260.0</td>
      <td>0.0</td>
      <td>430.0</td>
      <td>620.0</td>
      <td>770.0</td>
      <td>340.0</td>
      <td>540.0</td>
      <td>760.0</td>
    </tr>
    <tr>
      <th>45</th>
      <td>1200.0</td>
      <td>800.0</td>
      <td>1650.0</td>
      <td>1100.0</td>
      <td>1310.0</td>
      <td>1540.0</td>
      <td>1254.0</td>
      <td>1424.0</td>
      <td>1624.0</td>
      <td>1554.0</td>
      <td>...</td>
      <td>1080.0</td>
      <td>550.0</td>
      <td>210.0</td>
      <td>430.0</td>
      <td>0.0</td>
      <td>240.0</td>
      <td>920.0</td>
      <td>450.0</td>
      <td>650.0</td>
      <td>750.0</td>
    </tr>
    <tr>
      <th>46</th>
      <td>1390.0</td>
      <td>990.0</td>
      <td>1840.0</td>
      <td>1290.0</td>
      <td>1500.0</td>
      <td>1730.0</td>
      <td>1444.0</td>
      <td>1614.0</td>
      <td>1814.0</td>
      <td>1744.0</td>
      <td>...</td>
      <td>1320.0</td>
      <td>790.0</td>
      <td>450.0</td>
      <td>620.0</td>
      <td>240.0</td>
      <td>0.0</td>
      <td>1110.0</td>
      <td>280.0</td>
      <td>480.0</td>
      <td>990.0</td>
    </tr>
    <tr>
      <th>47</th>
      <td>540.0</td>
      <td>140.0</td>
      <td>990.0</td>
      <td>440.0</td>
      <td>650.0</td>
      <td>880.0</td>
      <td>850.0</td>
      <td>1020.0</td>
      <td>1220.0</td>
      <td>1334.0</td>
      <td>...</td>
      <td>1560.0</td>
      <td>1040.0</td>
      <td>1030.0</td>
      <td>770.0</td>
      <td>920.0</td>
      <td>1110.0</td>
      <td>0.0</td>
      <td>830.0</td>
      <td>1030.0</td>
      <td>1230.0</td>
    </tr>
    <tr>
      <th>48</th>
      <td>1110.0</td>
      <td>710.0</td>
      <td>1560.0</td>
      <td>1010.0</td>
      <td>1220.0</td>
      <td>1450.0</td>
      <td>1164.0</td>
      <td>1334.0</td>
      <td>1534.0</td>
      <td>1464.0</td>
      <td>...</td>
      <td>1430.0</td>
      <td>910.0</td>
      <td>600.0</td>
      <td>340.0</td>
      <td>450.0</td>
      <td>280.0</td>
      <td>830.0</td>
      <td>0.0</td>
      <td>200.0</td>
      <td>1100.0</td>
    </tr>
    <tr>
      <th>49</th>
      <td>1310.0</td>
      <td>910.0</td>
      <td>1760.0</td>
      <td>1210.0</td>
      <td>1420.0</td>
      <td>1650.0</td>
      <td>1364.0</td>
      <td>1534.0</td>
      <td>1734.0</td>
      <td>1664.0</td>
      <td>...</td>
      <td>1630.0</td>
      <td>1110.0</td>
      <td>800.0</td>
      <td>540.0</td>
      <td>650.0</td>
      <td>480.0</td>
      <td>1030.0</td>
      <td>200.0</td>
      <td>0.0</td>
      <td>1300.0</td>
    </tr>
    <tr>
      <th>50</th>
      <td>1510.0</td>
      <td>1110.0</td>
      <td>1875.0</td>
      <td>1275.0</td>
      <td>1485.0</td>
      <td>1620.0</td>
      <td>1300.0</td>
      <td>1470.0</td>
      <td>1640.0</td>
      <td>1460.0</td>
      <td>...</td>
      <td>330.0</td>
      <td>200.0</td>
      <td>540.0</td>
      <td>760.0</td>
      <td>750.0</td>
      <td>990.0</td>
      <td>1230.0</td>
      <td>1100.0</td>
      <td>1300.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>50 rows × 50 columns</p>
</div>



### 访问单个变量信息

单个变量可以直接通过以下方式访问,这样访问不区分大小写


```python
o['x']
```




    {1: 0.0,
     2: 0.0,
     3: 0.0,
     4: 0.0,
     5: 0.0,
     6: 0.0,
     7: 0.0,
     8: 0.0,
     9: 0.0,
     10: 0.0,
     11: 0.0,
     12: 0.0,
     13: 0.0,
     14: 0.0,
     15: 1.0,
     16: 0.0,
     17: 0.0,
     18: 0.0,
     19: 0.0,
     20: 0.0,
     21: 1.0,
     22: 0.0,
     23: 0.0,
     24: 0.0,
     25: 0.0,
     26: 0.0,
     27: 0.0,
     28: 0.0,
     29: 0.0,
     30: 0.0,
     31: 1.0,
     32: 0.0,
     33: 0.0,
     34: 0.0,
     35: 0.0,
     36: 0.0,
     37: 0.0,
     38: 0.0,
     39: 0.0,
     40: 0.0,
     41: 0.0,
     42: 0.0,
     43: 0.0,
     44: 0.0,
     45: 0.0,
     46: 0.0,
     47: 0.0,
     48: 0.0,
     49: 0.0,
     50: 0.0}



它等效于


```python
o.variable['X']
```




    {1: 0.0,
     2: 0.0,
     3: 0.0,
     4: 0.0,
     5: 0.0,
     6: 0.0,
     7: 0.0,
     8: 0.0,
     9: 0.0,
     10: 0.0,
     11: 0.0,
     12: 0.0,
     13: 0.0,
     14: 0.0,
     15: 1.0,
     16: 0.0,
     17: 0.0,
     18: 0.0,
     19: 0.0,
     20: 0.0,
     21: 1.0,
     22: 0.0,
     23: 0.0,
     24: 0.0,
     25: 0.0,
     26: 0.0,
     27: 0.0,
     28: 0.0,
     29: 0.0,
     30: 0.0,
     31: 1.0,
     32: 0.0,
     33: 0.0,
     34: 0.0,
     35: 0.0,
     36: 0.0,
     37: 0.0,
     38: 0.0,
     39: 0.0,
     40: 0.0,
     41: 0.0,
     42: 0.0,
     43: 0.0,
     44: 0.0,
     45: 0.0,
     46: 0.0,
     47: 0.0,
     48: 0.0,
     49: 0.0,
     50: 0.0}



这种访问方式也可以获得基本信息


```python
o[0]
```

    Objective value:          19660.0
    Objective bound:          19660.0
    Infeasibilities:          0.0
    Extended solver steps:    0.0
    Total solver iterations:  4667.0
    Model Class:              MILP
    Nonlinear variables:      0.0
    Integer variables:        50.0
    Total constraints:        2602.0
    Nonlinear constraints:    0.0
    Total nonzeros:           10100.0
    Nonlinear nonzeros:       0.0



### 访问决策变量

在整数规划中,会有0-1的变量,当他们值为1是被储存到字典`decision`中


```python
o.decision
```




    {'X': [15, 21, 31],
     'U': [(1, 21),
      (2, 21),
      (3, 21),
      (4, 21),
      (5, 15),
      (6, 15),
      (7, 15),
      (8, 15),
      (9, 15),
      (10, 15),
      (11, 15),
      (12, 15),
      (13, 15),
      (14, 15),
      (15, 15),
      (16, 15),
      (17, 15),
      (18, 15),
      (19, 21),
      (20, 21),
      (21, 21),
      (22, 21),
      (23, 21),
      (24, 21),
      (25, 15),
      (26, 15),
      (27, 15),
      (28, 31),
      (29, 31),
      (30, 31),
      (31, 31),
      (32, 31),
      (33, 31),
      (34, 31),
      (35, 31),
      (36, 31),
      (37, 31),
      (38, 31),
      (39, 31),
      (40, 31),
      (41, 31),
      (42, 31),
      (43, 31),
      (44, 21),
      (45, 21),
      (46, 21),
      (47, 21),
      (48, 21),
      (49, 21),
      (50, 31)]}



也可以通过以下方式快速访问


```python
o[1]
```




    {'X': [15, 21, 31],
     'U': [(1, 21),
      (2, 21),
      (3, 21),
      (4, 21),
      (5, 15),
      (6, 15),
      (7, 15),
      (8, 15),
      (9, 15),
      (10, 15),
      (11, 15),
      (12, 15),
      (13, 15),
      (14, 15),
      (15, 15),
      (16, 15),
      (17, 15),
      (18, 15),
      (19, 21),
      (20, 21),
      (21, 21),
      (22, 21),
      (23, 21),
      (24, 21),
      (25, 15),
      (26, 15),
      (27, 15),
      (28, 31),
      (29, 31),
      (30, 31),
      (31, 31),
      (32, 31),
      (33, 31),
      (34, 31),
      (35, 31),
      (36, 31),
      (37, 31),
      (38, 31),
      (39, 31),
      (40, 31),
      (41, 31),
      (42, 31),
      (43, 31),
      (44, 21),
      (45, 21),
      (46, 21),
      (47, 21),
      (48, 21),
      (49, 21),
      (50, 31)]}




```python

```
