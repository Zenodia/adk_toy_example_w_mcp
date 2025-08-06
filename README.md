# adk_toy_example_w_mcp
a minimalistic toy example using google-adk + nvidia nim endpoints + mcp as tool

## step_1 : installing the uv environment and activate it
``` 
python -m venv .venv
``` 

### windows
``` 
.venv/Scripts/activate 
``` 
### linux 
``` 
source .venv/bin/activate
``` 
## Step_2 : install all requirements 
### ensure python >=3.10
I am using 3.11.10

``` 
pip install -r requirements.txt
``` 
## Step_3 : create a .env file under simple_agent folder
``` 
NVIDIA_API_KEY="fill in your nvidia api key"
``` 

## Step_4 : run the app 
``` 
adk run simple_agent 
``` 
expected output , might be different in your environment 
``` 
(.venv) PS C:\Users\zcharpy\Contacts\adk-exp> adk run .\simple_agent\
Log setup complete: C:\Users\zcharpy\AppData\Local\Temp\agents_log\agent.20250806_115338.log
To access latest log: tail -F C:\Users\zcharpy\AppData\Local\Temp\agents_log\agent.latest.log

  super().__init__()
Valid NVIDIA_API_KEY already in environment. Delete to reset
Running agent dice_agent, type exit to exit.
[user]: 
``` 