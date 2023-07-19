To view TensorBoard for the given log directory, you can follow these steps:

Open a terminal or command prompt.
Activate your virtual environment (if applicable) by running the command:
```
source <path_to_virtual_environment>/bin/activate
cd /home/tltydl2/neural-diffusion-processes/experiments/image_regression/logs/eval-May29-test/tensorboard
tensorboard --logdir=.
```
If you are learning on an SSH server and want to access TensorBoard on your local computer's window, you can use SSH port forwarding to establish a secure connection between the server and your local machine. Here's how you can do it:

On your local machine, open a terminal or command prompt.

Use the following SSH command to establish an SSH connection with port forwarding:
```
ssh -L localhost:6006:localhost:6006 username@server_ip_address
http://localhost:6006/
```
Press Enter to access TensorBoard. You should see the TensorBoard interface in your web browser.

By setting up SSH port forwarding, you create a secure tunnel between your local machine and the SSH server, allowing you to access TensorBoard running on the server as if it were running locally. Remember to keep the SSH connection open in the terminal or command prompt window to maintain the connection to TensorBoard.

If you have any further questions or encounter any issues, please let me know.
