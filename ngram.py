
# https://qiita.com/kazmaw/items/4df328cba6429ec210fb
def doNGram(target, n):
  # 基準を1文字(単語)ずつ ずらしながらn文字分抜き出す
  # return [ target[idx:idx + n] for idx in range(len(target) - n + 1)]
    li = []
    for i in range(len(target)- n + 1):
        il = []
        for j in range(n):
            il.append(target[i+j])
        li.append(il)
    return li