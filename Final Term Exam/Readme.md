
# Final Term Exan
## 薛定谔方程的数值方法
## 刘兆晨 学号：2015302540110   邮箱：liuzc@whu.edu.cn
### The Shooting Method
#### 一维无限深势阱
  基态：![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/Final%20Term%20Exam/shooting/1dim-1/%E4%B8%80%E7%BB%B4%E6%97%A0%E9%99%90%E6%B7%B1_n%3D1.png)  
  n=2：![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/Final%20Term%20Exam/shooting/1dim-1/%E4%B8%80%E7%BB%B4%E6%97%A0%E9%99%90%E6%B7%B1_n%3D2.png)  
  n=3:![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/Final%20Term%20Exam/shooting/1dim-1/%E4%B8%80%E7%BB%B4%E6%97%A0%E9%99%90%E6%B7%B1_n%3D3.png)  
#### 一维谐振子
  能量数值结果：![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/Final%20Term%20Exam/shooting/harmonic/energy.png)  
  
  波函数，n=0:![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/Final%20Term%20Exam/shooting/harmonic/n%3D0.png)   
  波函数，n=1:![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/Final%20Term%20Exam/shooting/harmonic/n%3D1.png)    
  波函数，n=2:![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/Final%20Term%20Exam/shooting/harmonic/n%3D2.png)  
  波函数，n=3:![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/Final%20Term%20Exam/shooting/harmonic/n%3D3.png)  
  波函数，n=4:![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/Final%20Term%20Exam/shooting/harmonic/n%3D4.png)  
  
  波函数，n=5:![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/Final%20Term%20Exam/shooting/harmonic/n%3D5.png)
### The Matrix Method
#### 一维无限深势阱
  能量数值结果：![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/Final%20Term%20Exam/matrix%20method/1-dim/energy.png)  
  
  能量相对误差：![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/Final%20Term%20Exam/matrix%20method/1-dim/relative_error.png) 
#### 一维谐振子
  能量数值结果：![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/Final%20Term%20Exam/matrix%20method/harmonic/energy.png)  
  能量相对误差：![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/Final%20Term%20Exam/matrix%20method/harmonic/relative_error.png)  
  
  波函数，n=1:![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/Final%20Term%20Exam/matrix%20method/harmonic/n%3D1.png)  
  波函数，n=5:![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/Final%20Term%20Exam/matrix%20method/harmonic/n%3D5.png)  
  
  波函数，n=9:![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/Final%20Term%20Exam/matrix%20method/harmonic/n%3D9.png)

#### Leanord-Jones势能
  Leanord-Jones 势能基态：![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/Final%20Term%20Exam/matrix%20method/lennard-jones/ground.png)
### [含时薛定谔方程](https://github.com/liuzhaochen/compuational_physics_N2015302540110/tree/master/Final%20Term%20Exam/time-dependence)
#### 自由高斯波包
  自由高斯波包含时演化动图：![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/Final%20Term%20Exam/time-dependence/free/guass-free.gif)
#### 自由高斯波包隧穿效应  
  势垒在[0.6,0.65]处  
  
  自由高斯波包隧穿效应动图：![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/Final%20Term%20Exam/time-dependence/tunneling/guass-tunndeling.gif)
#### 自由高斯波包势阱反射
  在[0.6,1]处存在无穷大势垒  
  
  动图：![](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/Final%20Term%20Exam/time-dependence/wall/guass-wall.gif)

- 由于含时演化中截图很多，所以这里只放了含时演化的动图。
### 计算代码
- The Shooting Method:[一维无限深势阱打靶法代码](https://raw.githubusercontent.com/liuzhaochen/compuational_physics_N2015302540110/master/Final%20Term%20Exam/%E4%B8%80%E7%BB%B4%E6%97%A0%E9%99%90%E6%B7%B1%E5%8A%BF%E4%BA%95.py)

- The Shooting and Matching Method:[一维谐振子势代码](https://raw.githubusercontent.com/liuzhaochen/compuational_physics_N2015302540110/master/Final%20Term%20Exam/%E4%B8%80%E7%BB%B4%E6%97%A0%E9%99%90%E6%B7%B1%E5%8A%BF%E4%BA%95.py)

- The Matrix Method: [矩阵法代码](https://raw.githubusercontent.com/liuzhaochen/compuational_physics_N2015302540110/master/Final%20Term%20Exam/matrix.py)

- The Mote-Carlo and Variation Method:[蒙卡变分法代码](https://raw.githubusercontent.com/liuzhaochen/compuational_physics_N2015302540110/master/Final%20Term%20Exam/mote-carlo.py)  
    由于使用蒙卡变分法计算结果不理想，所以没有在最终的期末论文中给出计算结果，这里贴出代码。
- The Time-Dependence Schrodinger Equation:[含时演化代码](https://raw.githubusercontent.com/liuzhaochen/compuational_physics_N2015302540110/master/Final%20Term%20Exam/time-dependent.py)
- 在矩阵计算中使用的eign模块代码:[eign](https://raw.githubusercontent.com/liuzhaochen/compuational_physics_N2015302540110/master/Final%20Term%20Exam/eign.py)
### 期末论文
  [期末论文](https://github.com/liuzhaochen/compuational_physics_N2015302540110/blob/master/Final%20Term%20Exam/%E8%96%9B%E5%AE%9A%E8%B0%94%E6%96%B9%E7%A8%8B%E6%95%B0%E5%80%BC%E6%96%B9%E6%B3%95.pdf)
