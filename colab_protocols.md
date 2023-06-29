## Useful colab_protocols

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
### Log path
```python
%cd path
!pwd #check
```

### Colab TPU settings
```python
!echo $COLAB_TPU_ADDR #check ip

# TPU gRPC 접근 URI
TPU_PATH = f"grpc://{os.environ['COLAB_TPU_ADDR']}"

resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu=TPU_PATH)
tf.config.experimental_connect_to_cluster(resolver)
tf.tpu.experimental.initialize_tpu_system(resolver)

strategy = tf.distribute.TPUStrategy(resolver)

### compile example
train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train)).batch(batch_size)
model = Model(config)
loss = tf.keras.losses.BinaryCrossentropy()
optimizer = tf.keras.optimizers.Adam()

with strategy.scope():
    metric = tf.keras.metrics.BinaryAccuracy()

    model.compile(optimizer=optimizer, loss=loss, metrics=[metric])
    model.fit(train_dataset, epochs=config.epoch)
```
