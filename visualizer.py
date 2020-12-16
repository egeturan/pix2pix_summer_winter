import numpy as np
import plotly.graph_objects as go

# Using readlines() 
file1 = open('cityscapes/other_data/loss_log.txt', 'r') 
Lines = file1.readlines() 
  
count = 1
index = []

#loss data
ggan = []
g_l1 = []
d_real = []
d_fake = []

epoch = []

time = 0

for line in Lines: 
    res = line.split()   
    ep = res[1]
    ep = ep[:-1]
    
    t = res[1]
    t = t[:-1]
    time = time + float(t) 
    epoch.append(int(ep))
    
    #read data
    ggan.append(float(res[9]))
    g_l1.append(float(res[11]))
    d_real.append(float(res[13]))
    d_fake.append(float(res[15]))
    
    count = count + 1

control = epoch[0]  
epochs = []  
epoch_count = 0
epoch_count = epoch_count + 1
for i in range(len(epoch)):
    if epoch[i] != control:
        epoch_count = epoch_count + 1
        epochs.append(epoch_count)
        control = epoch[i]
        
epochs = np.asarray(epochs, dtype=int)
ggan = np.asarray(ggan, dtype=float)
g_l1 = np.asarray(g_l1, dtype=float)
d_real = np.asarray(d_real, dtype=float)
d_fake = np.asarray(d_fake, dtype=float)



# Create traces
fig = go.Figure()
fig.add_trace(go.Scatter(x=epochs, y=ggan,
                    mode='lines',
                    name='GGAN'))
fig.add_trace(go.Scatter(x=epochs, y=g_l1,
                    mode='lines',
                    name='GL1'))
fig.add_trace(go.Scatter(x=epochs, y=d_real,
                    mode='lines',
                    name='D_Real'))
fig.add_trace(go.Scatter(x=epochs, y=d_fake,
                    mode='lines',
                    name='D_Fake'))

fig.show()


print(max(g_l1))
print(min(g_l1))