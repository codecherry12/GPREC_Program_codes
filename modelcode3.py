def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    five=0
    one=0
    f=0
    if rupees_to_make<=(5*no_of_five+no_of_one):
        five=rupees_to_make//5
        one=rupees_to_make-(no_of_five*5)
        if five<=no_of_five and one<=no_of_one:
            five_needed=five
            one_needed=one
            f=1
        elif five>no_of_five:
            five_needed=no_of_five
            one_needed=rupees_to_make-(five_needed*5)
            f=1
    if f==1:
        print("No. of Five needed :", five_needed)
        print("No.of One needed :",one_needed)
    else:
        print(-1)

make_amount(28,8,5)