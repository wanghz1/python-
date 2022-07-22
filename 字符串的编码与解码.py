s = '能与不能，全凭我敢'
# 编码
print(s.encode(encoding='GBK'))  # 在GBK编码格式中一个中文占两个字节
print(s.encode(encoding='UTF-8'))  # 在UTF-8编码格式中一个中文占三个字节

# 解码
byte = s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))


byte = s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))
