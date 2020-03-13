scores = [101, 28, 33]

def calAvg (score):
    assert len(scores) > 0
    assert max(scores) <= 100
    assert min(scores) >= 0
    return sum(score) / len(score)

print(calAvg(scores))