<div align= "center">
    <h1> Resilience of Multi-Agent Systems🤖🤖</h1>
</div>


<div align="center">
<img src="Figures/cover.png" width="750px">
</div>


## 🛠️ Install
Clone the repository:
```bash
$ git clone https://github.com/CUHK-ARISE/MAS-Resilience.git
$ cd MAS-Resilience
```

## 🔧 How to Use

First, set the OpenAI apikey:
```bash
$ $env:OPENAI_API_KEY="<your_api_key>"
```

<div align="center">
<img src="Figures/method.png" width="750px">
</div>

### AutoTransform
AutoTransform can turn any agent into a malicious agent, by tampering with their profile.

To see an example, run:
```bash
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

## 📊 Results
<div align="center">
<img src="Figures/result-structure.png" width="750px">
</div>

<div align="center">
<img src="Figures/result-task.png" width="750px">
</div>

<div align="center">
<img src="Figures/result-increase.png" width="750px">
</div>

<div align="center">
<img src="Figures/result-defense.png" width="750px">
</div>

## 👉 Paper and Citation
For more details, please refer to our paper <a href="https://arxiv.org/abs/2408.00989">here</a>.

If you find our paper&tool interesting and useful, please feel free to give us a star and cite us through:
```
@article{huang2024resilience,
  author    = {Jen{-}tse Huang and
               Jiaxu Zhou and
               Tailin Jin and
               Xuhui Zhou and
               Zixi Chen and
               Wenxuan Wang and
               Youliang Yuan and
               Michael R. Lyu and
               Maarten Sap},
  title     = {On the Resilience of LLM-Based Multi-Agent Collaboration with Faulty Agents},
  journal   = {arXiv Preprint: 2408.00989},
  year      = {2024}
}
```
