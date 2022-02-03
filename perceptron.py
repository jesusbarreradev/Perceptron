from random import *
import random
import numpy
def inicialize_w(long_vw):
    long_vw+=1
    w=[]
    for i in range(long_vw):
        w.append(random.random())
    print("EL primer vector W",w)
    return w


def rename_weight(v_w, theta,err,x):
    i=0
    for w in v_w:
        w=w+theta*err*x
        #print("soy w rara",w) error al obtener las nuevas w
        i+=1
    
    #print("soy w super rara",v_w) mistake when we change values 
    return w


def perceptron():# v_x, v_y, theta
    x=[[1,1],[1,0]]
    y=[0,1]
    v_w= inicialize_w(len(x))
    x=numpy.array(x)
    
    theta=0.1 ##soon user value, n
    done=False
    epoch=0
    while done != False or epoch <100:

        done= True
        for j in range(1,len(x)):
            have=pw(v_w,x[j])
            #print(have)
            err=y[j]-have
            if err!= 0:
                done= False
                v_w=rename_weight(v_w,theta, err,x[j])

        epoch+=1
    

def pw(w,x):# transfer function
    i=1
    pw_=0
    for e_x in x:
        pw_+=e_x*w[i]
    pw_-w[0]
    return pw_


def activation_function(u):
    if u>=0 :
        return True
    else: 
        return False


def run():
    perceptron()
    

if __name__ == '__main__':
    run()
