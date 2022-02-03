
import numpy 
def inputs():
    inputs_=[]
    input_=[]
    txt=open('input.txt')
    for linea in txt:
        input_=[]
        for lettle in linea:
            if lettle=='\n':
                continue
            elif  lettle == ",":
                continue
            else:
                change=int(lettle)
                input_.append(change)
        
        inputs_.append(input_) 
    txt.close()
    return inputs_


def activation_funtion(u):
    if u<0:
        return False
    else:
        True


def perceptron(inputs, theta):
    w=[1,1]
    #print(inputs)
    for input_ in inputs:
        u=numpy.dot(w,input_)-theta
        print(u)
        print(activation_funtion(u)) 


def run():
    input_=inputs()
    perceptron(input_,1.5)


if __name__ == '__main__':
    run()