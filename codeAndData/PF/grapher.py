import numpy as np
import matplotlib.pyplot as plt

def pic1():
    f1 = open("/home/wentao/firstData.txt", "r")
    x1 = []
    y1 = []
    for line in f1:
        line = line.split()
        x1.append(int(line[0]))
        y1.append(float(line[1]))

    f2 = open("/home/wentao/firstData2.txt", "r")
    x2 = []
    y2 = []
    for line in f2:
        line = line.split()
        x2.append(int(line[0]))
        y2.append(float(line[1]))

    f3 = open("/home/wentao/firstData3.txt", "r")
    x3 = []
    y3 = []
    for line in f3:
        line = line.split()
        x3.append(int(line[0]))
        y3.append(float(line[1]))

    f4 = open("/home/wentao/firstData4.txt", "r")
    x4 = []
    y4 = []
    for line in f4:
        line = line.split()
        x4.append(int(line[0]))
        y4.append(float(line[1]))

    f5 = open("/home/wentao/firstData5.txt", "r")
    x5 = []
    y5 = []
    for line in f5:
        line = line.split()
        x5.append(int(line[0]))
        y5.append(float(line[1]))


    plt.semilogy(x1, y1, label = "BDDC")
    plt.semilogy(x2, y2, label = "Jacobi")
    plt.semilogy(x3, y3, label = "Gauss-Seidel")
    plt.semilogy(x4, y4, label = "Block-Jacobi")
    plt.semilogy(x5, y5, label="Multigrid")
    plt.xlabel('Iteration')
    plt.ylabel('Absolute Error')
    plt.title('CG Preconditioner')
    plt.legend()
#plt.grid(True)
    plt.savefig("/home/wentao/test.png")
    plt.show()

def pic2():
    f1 = open("/home/wentao/firstData11.txt", "r")
    x1 = []
    y1 = []
    for line in f1:
        line = line.split()
        x1.append(int(line[0]))
        y1.append(int(line[1]))

    f2 = open("/home/wentao/firstData12.txt", "r")
    x2 = []
    y2 = []
    for line in f2:
        line = line.split()
        x2.append(int(line[0]))
        y2.append(int(line[1]))

    f3 = open("/home/wentao/firstData13.txt", "r")
    x3 = []
    y3 = []
    for line in f3:
        line = line.split()
        x3.append(int(line[0]))
        y3.append(int(line[1]))

    f4 = open("/home/wentao/firstData14.txt", "r")
    x4 = []
    y4 = []
    for line in f4:
        line = line.split()
        x4.append(int(line[0]))
        y4.append(int(line[1]))

    f5 = open("/home/wentao/firstData27.txt", "r")
    x5 = []
    y5 = []
    for line in f5:
        line = line.split()
        x5.append(int(line[0]))
        y5.append(int(line[1]))

    plt.plot(x1, y1, label = "Jacobi")
    plt.plot(x2, y2, label = "Block-jacobi")
    plt.plot(x3, y3, label = "Gauss-Seidel")
    plt.plot(x4, y4, label = "BDDC")
    plt.plot(x5, y5, label="multigrid")
    plt.xlabel('Order')
    plt.ylabel('Iteration Required')
    plt.title('CG Preconditioner')
    plt.legend()
#plt.grid(True)
    plt.savefig("/home/wentao/test2.png")
    plt.show()

def pic3():
    f1 = open("/home/wentao/firstData21.txt", "r")
    x1 = []
    y1 = []
    for line in f1:
        line = line.split()
        x1.append(int(line[0]))
        y1.append(float(line[1]))

    f2 = open("/home/wentao/firstData22.txt", "r")
    #x2 = []
    #y2 = []
    plus = len(x1)
    for line in f2:
        line = line.split()
        x1.append(int(line[0]) + plus)
        y1.append(float(line[1]))

    f3 = open("/home/wentao/firstData23.txt", "r")
    #x3 = []
    #y3 = []
    plus = len(x1)
    for line in f3:
        line = line.split()
        x1.append(int(line[0]) + plus)
        y1.append(float(line[1]))

    f4 = open("/home/wentao/firstData24.txt", "r")
    x2 = []
    y2 = []
    for line in f4:
        line = line.split()
        x2.append(int(line[0]))
        y2.append(float(line[1]))

    f5 = open("/home/wentao/firstData25.txt", "r")
    plus = len(x2)
    for line in f5:
        line = line.split()
        x2.append(int(line[0]) + plus)
        y2.append(float(line[1]))

    f6 = open("/home/wentao/firstData26.txt", "r")
    plus = len(x2)
    for line in f6:
        line = line.split()
        x2.append(int(line[0]) + plus)
        y2.append(float(line[1]))




    plt.semilogy(x1, y1, label = "BDDC")
    plt.semilogy(x2, y2, label = "MultiGrid")
    #plt.plot(x3, y3, label = "Gauss-Seidel")
    #plt.plot(x4, y4, label = "BDDC")
    plt.xlabel('Iteration')
    plt.ylabel('AbsoluteError')
    plt.title('MultiLevelCGPreconditioner')
    plt.legend()
#plt.grid(True)
    plt.savefig("/home/wentao/test3.png")
    plt.show()

def pic4():
    f1 = open("/home/wentao/firstData31.txt", "r")
    x1 = []
    y1 = []
    for line in f1:
        line = line.split()
        x1.append(int(line[2]))
        y1.append(float(line[5]))

    f2 = open("/home/wentao/firstData32.txt", "r")
    x2 = []
    y2 = []
    for line in f2:
        line = line.split()
        x2.append(int(line[2]))
        y2.append(float(line[5]))

    f3 = open("/home/wentao/firstData33.txt", "r")
    x3 = []
    y3 = []
    for line in f3:
        line = line.split()
        x3.append(int(line[2]))
        y3.append(float(line[5]))

    plt.semilogy(x1, y1, label = "BDDC")
    plt.semilogy(x2, y2, label = "Jacobi")
    plt.semilogy(x3, y3, label="Multigrid")
    plt.xlabel('Iteration')
    plt.ylabel('Absolute Error')
    plt.title('CG Preconditioner')
    plt.legend()
#plt.grid(True)
    plt.savefig("/home/wentao/test5.png")
    plt.show()
pic2()