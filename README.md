# How to use?

Clone this project, and make sure you know the directory of this python script.  
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
