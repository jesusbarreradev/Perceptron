from random import *
import window
def inicialize_w(long_vw):
    for i in range(long_vw+1):
        w[i]= random.random()

    return w


def perceptron():# v_x, v_y, theta
    x=[2,3]
    y=[3,5]
    v_w= inicialize_w(x.__len__() +1)
    theta=0.1 ##soon user value 
    done=False
    epoch=0
    while done != False or epoch <100:
        done= True
        for j in range(1,3):
            err=y[j]-pw(x[j])
            if err!= 0:
                done= False
                v_w=v_w+theta*x[j]
        epoch+=1

def pw(x):# transfer function
    pass


def activation_function(u):
    if u>=0 :
        return True
    else: 
        return False


def run():
    window.run()
    

if __name__ == '__main__':
    run()
