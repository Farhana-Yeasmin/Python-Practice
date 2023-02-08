records = {}
lst = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append(score)
        records[name] = score
    # min_val = sorted(set(lst))[1]
    min_val = sorted(set(lst))[1]
    records = sorted(records.items())

    for name,score in records:
        if score==min_val:
            print(name)