dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
data = input().split()
word = [word for word in data if word not in dictionary]
print("\n".join(word) if len(word) > 0 else "OK")
