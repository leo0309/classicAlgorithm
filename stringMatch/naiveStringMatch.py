#朴素的字符串匹配方法
def naiveStringMatch(text,pattern):
    text_length=len(text)
    pattern_length=len(pattern)
    if pattern_length>text_length:
        return None
    result=[]
    i=0
    while i < text_length:
        j=0
        k=i
        while j<pattern_length and text[i]==pattern[j]:
            j+=1
            i+=1
        if j == pattern_length:
            result.append(i-j)
        else:
            i=k+1
    return result

#test
a="习近平强调，希望全国政法战线深入学习贯彻党的十九大精神，强化“四个意识”，坚持党对政法工作的绝对领导，坚持以人民为中心的发展思想，增强工作预见性、主动性，深化司法体制改革，推进平安中国、法治中国建设，加强过硬队伍建设，深化智能化建设，严格执法、公正司法，履行好维护国家政治安全、确保社会大局稳定、促进社会公平正义、保障人民安居乐业的主要任务，努力创造安全的政治环境、稳定的社会环境、公正的法治环境、优质的服务环境，增强人民群众获得感、幸福感、安全感。"
a=a*10000
p="十九大精神"
from time import time
tt=time()
r=naiveStringMatch(a,p)
tt=time()-tt
print(tt)
#print(r)
