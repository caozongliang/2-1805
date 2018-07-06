str = "python"
print(str)
def daoxu(str):
    if len(str)<1:
        return str
    else:
        return str[::-1]



a = daoxu(str)
print(a)

