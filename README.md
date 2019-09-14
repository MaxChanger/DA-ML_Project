## 应用综合实验 - 整理 Data Analysis & Medical Learning

- 统计字母/单词的频率 + 可视化

  ```shell
  python .\countFrequencyGUI.py --filePath '../Data/bio.txt' --sort --countLetter
  ```

  |                                   |                                   |                                   |
  | --------------------------------- | --------------------------------- | --------------------------------- |
  | ![](./img/countFrequencyGUI1.png) | ![](./img/countFrequencyGUI2.png) | ![](./img/countFrequencyGUI3.png) |

  <img src="./img/countFrequencyGUI4.png" width=50%>

- 批量重命名

  ```shell
  python .\renamefilter.py myimage###.jpg
  ```

  <img src="./img/rename.png">

- 收发邮件

  ```shell
  python .\readMail.py
  python .\send.py		python sendMail.py
  ```

  <img src="./img/email.png"  width=50%>

- 模拟股票涨跌（尚未使用爬虫，利用随机数模拟，动态图）

  ```shell
  python .\showTime.py --update 0.1 --xmax 100 --fixed
  ```

  <img src="./img/simstock.png"  width=80%>

- 手动实现K-means

  ```shell
  python .\kmeans.py --n_iteration 100 --n_clusters 4
  ```
  |                        |                        |
  | ---------------------- | ---------------------- |
  | ![](./img/kmeans1.png) | ![](./img/kmeans2.png) |



- 手写MLP（只写了一个输入层一个隐层一个输出层）

  ```shell
  python .\BpNN.py		# epoch: 19000 accuracy: 0.9777777777777777
  ```
  |                        |                        |
  | ---------------------- | ---------------------- |
  | ![](./img/mlp.png) | ![](./img/mlp2.png) |


