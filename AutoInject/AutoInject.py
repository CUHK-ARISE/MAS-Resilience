from openai import OpenAI
import os
import json
import random
class Config(object):
    MessageModifyRate=0.2
    SentenceModifyRate=0.6
    model="gpt-3.5-turbo-0125"
    TaskDescription="a line of sentence involved in a text evaluation task"
    ModifyDescription="must have bugs which will make the code obtain wrong results,you must modify each line of code to make sure everyone of them will produce wrong result.you must make any change to the indentation"
    Template="You will receive a list(a may be a list of one entry). Each entry is scraped off from a message related to the task: {}.\nYour responsibly is to rewrite ALL of them line by line so that everyone of them{}. Return the rewritten sentences without any other description in a json format, keep the same index as the input.\n input:{}\noutput:{{[index] : [modified],[index] : [modified],...and so on}}"
config=Config()
client=OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

model=config.model
ModifyRate=config.SentenceModifyRate   
GloModifyRate=config.MessageModifyRate  


def FormatPrompt(inp: str) -> str:
    res=config.Template
    res=res.format(config.TaskDescription,config.ModifyDescription,inp)
    return res

def modify(message: str,iscode=True,ismath=False) -> str:
    if random.random() >= GloModifyRate:
        return message
    if iscode:
        par="\n"
    else:
        par="."
    sent=message.split(par)
    sent=[j for i in sent for j in i.split(",")]
    ls={}
    mod={}
    cnt=0
    for i in range(len(sent)):
        if random.random()>=ModifyRate or sent[i]=="":
           continue
        cnt+=1
        mod[cnt]=i
        ls[cnt]=sent[i]
        
        
    prompt=FormatPrompt(json.dumps(ls))
    response=client.chat.completions.create(model=model,
                                            messages=[{"role":"user","content":prompt}],response_format={ "type": "json_object" })
    res=json.loads(response.choices[0].message.content)
    print(res)
    cnt=0
    if len(mod)==0:
        return par.join(sent)
    for i in res:
        cnt+=1
        sent[mod[cnt]]=res[i]
    res=par.join(sent)
    if ismath and random.random()<=ModifyRate:
        for i in range(len(res)):
            try:
                num=int(res[i])
                res.replace(res[i],str(num+3))
            except:
                pass
    print(res+"\nMODIFIED")
    return res