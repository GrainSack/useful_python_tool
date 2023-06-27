Useful colab_protocols

### Google amount
```python
from google.colab import drive
drive.mount('/content/drive')
```
### GPU check
```python
gpu_info = !nvidia-smi
gpu_info = '\n'.join(gpu_info)
if gpu_info.find('failed') >= 0:
  print('Select the Runtime > "Change runtime type" menu to enable a GPU accelerator, ')
  print('and then re-execute this cell.')
else:
  print(gpu_info)
```
### tensorboard call backs and upload protocols
```python
#dir
log_dir = "logs/my_board/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

# TensorBoard callbacks
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

#tensorboard upload
%load_ext tensorboard

%tensorboard --logdir=/content/logs

!tensorboard dev upload --logdir /content/logs
```
### Visualized model architecture
```python
!pip install torchviz hiddenlayer netron onnx
from torchviz import make_dot
make_dot(out, params=dict(model_gen.named_parameters())).render("generator_unet_graph", format="png")
```
