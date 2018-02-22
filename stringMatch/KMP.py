# Knuth-Morris-Pratt字符串匹配算法，重点是前缀转移函数的计算
def prefix_function(pattern):
    m = len(pattern)
    transition = [None] * m
    transition[0] = -1
    k = -1
    for q in range(1, m):
        while k > -1 and pattern[k + 1] != pattern[q]:
            k = transition[k]
        if pattern[k + 1] == pattern[q]:
            k = k + 1
        transition[q] = k
    return transition





def KMP(text, pattern):
    m = len(text)
    n = len(pattern)
    tr = prefix_function(pattern)
    q = -1
    result = []
    for i in range(0, m):
        while q > 0 and text[i] != pattern[q + 1]:
            q = tr[q]
        if text[i] == pattern[q + 1]:
            q = q + 1
        if q == n - 1:
            result.append(i - n + 1)
            q = tr[q]
    return result



# test
tr = prefix_function("ababccd")
print(tr)
result=prefix_function("abab")
print(result)
"""
from time import time
a = "习近平强调，希望全国政法战线深入学习贯彻党的十九大精神，强化“四个意识”，坚持党对政法工作的绝对领导，坚持以人民为中心的发展思想，增强工作预见性、主动性，深化司法体制改革，推进平安中国、法治中国建设，加强过硬队伍建设，深化智能化建设，严格执法、公正司法，履行好维护国家政治安全、确保社会大局稳定、促进社会公平正义、保障人民安居乐业的主要任务，努力创造安全的政治环境、稳定的社会环境、公正的法治环境、优质的服务环境，增强人民群众获得感、幸福感、安全感。"
a = a * 1000
p = "学习贯彻党的十九大精神"
tt = time()
r = KMP(a, p)
tt = time() - tt
print(tt)
# print(r)
"""