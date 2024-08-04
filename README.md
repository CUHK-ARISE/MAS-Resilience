# MAS-Resilience
## Install
Clone the repository:
```
$ git clone https://github.com/CUHK-ARISE/MAS-Resilience.git
$ cd MAS-Resilience
```
## How to Use

First, set the OpenAI apikey:
```
$ $env:OPENAI_API_KEY="<your_api_key>"
```

### AutoTransform
AutoTransform can turn any agent into a malicious agent, by tampering with their profile.

To see an example, run:
```
$ python AutoTransform.py
enter the file name for the prompt:
example.txt
```

The result will be saved in `Transformed_example.txt`

### AutoInject

AutoInject contains a function `modify`. You may config the function by changing the configuration in `Config`
You are recommended to change the `TaskDescription` and `ModifyDescription` for better result.

To use AutoInject in your code. you can put the python file under the same directory:
```python 
import AutoInject

message="your message"
result=AutoInject.modify(message,iscode=False,ismath=False) # you can turn on iscode or ismath if the message contain code or calculation
print(result)
```
### Defense
the two defense method `Inspector` and `challenger` works basically in the same manner. Below takes `Inspector` as example.
```python
import Inspector
myInspector=Inspector.inspector()
#create your Inspector
```
`myInspector.record(msg) `you should record all the message that is relevant, the inspector will take the messages into consideration

`myInspector.clear() `clears all the memory recorded

`result=myInspector.judge(msg)`this judge the message, if the inspector thinks message contain errorness content, he will return a rewrited version of the content. If the message is judged to be without error, he will simply return the original message.