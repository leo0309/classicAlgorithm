#将字符串中的每一个字符转换成ord八进制数。然后用霍纳规则进行递推计算到pattern位，将该值进行散列
def RabinKarp(text,pattern,d,q):
    """
    text:待匹配的文本
    pattern:匹配模式
    d:字符串转换的进制
    q:取模的素数
    """
    text_length=len(text)
    pattern_length=len(pattern)
    if text_length<pattern_length:
        return None
    h=(d**(pattern_length-1))%q
    p=0
    t0=0
    result=[]
    for i in range(0,pattern_length):
        p=(d*p+ord(pattern[i]))%q
        t0=(d*t0+ord(text[i]))%q
    for i in range(0,text_length-pattern_length+1):
        if p == t0:
            j=0
            k=i
            while j<pattern_length and text[k] == pattern[j] :
                j+=1
                k+=1
            if j == pattern_length:
                result.append(i)
        if i < text_length-pattern_length:
            t0=(d*(t0-ord(text[i])*h)+ord(text[pattern_length+i]))%q
    return result

#test
from time import time
a="习近平强调，希望全国政法战线深入学习贯彻党的十九大精神，强化“四个意识”，坚持党对政法工作的绝对领导，坚持以人民为中心的发展思想，增强工作预见性、主动性，深化司法体制改革，推进平安中国、法治中国建设，加强过硬队伍建设，深化智能化建设，严格执法、公正司法，履行好维护国家政治安全、确保社会大局稳定、促进社会公平正义、保障人民安居乐业的主要任务，努力创造安全的政治环境、稳定的社会环境、公正的法治环境、优质的服务环境，增强人民群众获得感、幸福感、安全感。"
a=a*10000
p="十九大精神"
tt=time()
r=RabinKarp(a,p,10,251)
tt=time()-tt
print(tt)
#print(r)

        