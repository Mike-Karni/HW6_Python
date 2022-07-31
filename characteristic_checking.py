def same_by(characteristic, objects):
  return len(set(map(characteristic, objects))) < 2
values = [1,1,1,1]
print(same_by(lambda x:x%2,values))
values = [2,2,2,3]
print(same_by(lambda x:x%2,values))



