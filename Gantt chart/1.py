
import matplotlib.pyplot as plt

execute_time=[]
trans_time=[]


#功能说明：文件里输入execute time和speed参数，画图


s=input('输入参数文件：')
#D:\pycharm\huawei_demo\data.txt
with open(s,'r') as f:
    for line in f:
        if 'execute time' in line:
            execute_time.append(int(line[-3:-1]))
        if 'speed' in line:
            trans_time.append(int(line[-3:-1]))


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x=['PE_execute1','trans_1to2','PE_execute2']
y=[execute_time[0],trans_time[0],execute_time[1]]
y.reverse()
x.reverse()

sum=execute_time[0]+trans_time[0]+execute_time[1]
for i in range(0,2*len(execute_time)-1):
    if i==0:
        plt.barh(x[i], y[i], color=(0, 0, 1), height=0.5, left=y[1]+y[2])
    elif i ==1:
        plt.barh(x[i],y[i],color=(0,0,1),height=0.5,left=y[2])
    elif i==2 :
        plt.barh(x[i], y[i], color=(0, 0, 1), height=0.5, left=0)




plt.xlabel("时间")
plt.ylabel("进程")


plt.show()