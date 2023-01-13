import numpy as np

a = [1,2,3,9]
b = [4,5,6,7,11]
print([a[i] * b[i] for i in range(len(a))])
print(np.convolve(a,b))
print(np.__version__)


# conda env list
# conda activate <env>
# jupyter-lab