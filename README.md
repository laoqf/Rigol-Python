# Rigol-Python
This project is based on https://github.com/kearneylackas/DP832-Python/blob/master/DP832.py

In this project, I create a GUI to control RIGOL DP832A(with LAN) or RIGOL DP832(only USB) Power Supply.

In our lab, we use DP832A to control oven, PMT and flip mount.

# note：

调用pyvisa找到对应的仪器，传输SCPI命令，见产品说明书

## Reference：

[Pyvisa，简明介绍和教程（一） - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/357335933)

[Pyvisa，简明教程2，连接与仪器调试 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/357337164)

[PyVISA: Control your instruments with Python — PyVISA 1.11.4.dev39+g53a1d41 documentation](https://pyvisa.readthedocs.io/en/latest/)

[DP832-Python/DP832.py at master · kearneylackas/DP832-Python (github.com)](https://github.com/kearneylackas/DP832-Python/blob/master/DP832.py)

[下载NI-VISA - NI](https://www.ni.com/zh-cn/support/downloads/drivers/download.ni-visa.html#442805)

[Python find()方法 | 菜鸟教程 (runoob.com)](https://www.runoob.com/python/att-string-find.html)

[通过以太网/LAN连接仪器 - National Instruments (ni.com)](https://www.ni.com/getting-started/set-up-hardware/instrument-control/zhs/ethernet-connect)

[DP800_ProgrammingGuide_CN_tcm4-3044.pdf (rigol.com)](https://www.rigol.com/Images/DP800_ProgrammingGuide_CN_tcm4-3044.pdf)

[DP800_UserGuide_CN_tcm4-3049.pdf (rigol.com)](https://www.rigol.com/Images/DP800_UserGuide_CN_tcm4-3049.pdf)

unused：

[Programming the DP800 DC Power Supply in Python (nathankjer.com)](https://nathankjer.com/dp800/)

包含图形化界面

[Lxi 接口 visa 毕业设计论文 - jz.docin.com豆丁建筑](https://jz.docin.com/p-1120401186.html)

## 翻转电镜 控制

892 flipper card.qxd (newport.com)

rigol电源控制翻转

## 编写界面

Reference：
QT designer介绍 - 知乎 (zhihu.com)

《快速掌握PyQt5》第十四章 快速制作界面——Qt Designer - 知乎 (zhihu.com)

Problems：
PyQt5程序报错：TypeError: argument 1 has unexpected type 'NoneType'的解决办法_David-hu的博客-CSDN博客

pyqt5按钮点击时传递参数（通过lambda表达式）_whuzhang16的博客-CSDN博客_pyqt按钮点击事件带参数![image](https://user-images.githubusercontent.com/51507600/173515474-16e9978b-e452-4280-9e22-2760f57e6f9c.png)



