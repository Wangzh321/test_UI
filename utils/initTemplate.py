'''
初始化配置模板
'''
from utils.operateJson import saveFileByJson

templatecontext={
    "component":{},
    "other":{}
}

saveFileByJson(templatecontext,"../configuration/test.json")

