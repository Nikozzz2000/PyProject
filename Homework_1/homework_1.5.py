proceeds = int(input("ввидите сумму выручки:"))
costs = int(input("ввидите сумму издержек:"))
losses = 0
income = proceeds - costs
premium = 0
if income < 0:
    losses = costs - proceeds
    print("Ваши убытки составили", losses, "едениц")
if income == 0:
    print("Вы смогли покрыть свои расходы и ничего не заработали")
if income > 0:
    workers = int(input("введите количество рабочих:"))
    premium = income / workers
    print("Премиальные на человека состовляют", premium, "едениц")


