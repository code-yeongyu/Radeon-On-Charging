# What is this?

It's a simple python script that automatically changes your Macbook to use Radeon Graphics when you connect to a charger.

# How to use?

Clone this project, and make sure you know the directory of this python script.  
And execute following command:

```
pip install -r requirements.txt
```

## Set to use when boot

Then create a file named "GPU_CHANGER" (or whatever you want), and give permissions to it by executing following command:

```bash
chmod u+x GPU_CHANGER
```

then write following lines to GPU_CHANGER.

```bash
#!/usr/bin/env bash
python3 {write here the path of your python script} &;
```

Then open "System Preferences" -> "Users & Groups" -> "Login Items", click the '+' button, find your "GPU_CHANGER", and add it.

Now all done!
