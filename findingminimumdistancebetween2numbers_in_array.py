N = 16
N_input = '1 5 3 7 2 8 3 4 5 9 9 3 1 3 2 9'

number_list = N_input.split()

UV = '2 5'
UV_list = UV.split()

U = UV_list[0]
V = UV_list[1]

U_index = []
V_index = []

U_index = [i for i in range(len(number_list)) if number_list[i] == U]

V_index = [i for i in range(len(number_list)) if number_list[i] == V]


distance_list = []

for i in range(0,len(U_index)):
    for j in range(0,len(V_index)):
        distance_list.append(abs(U_index[i] - V_index[j]))



print(min(distance_list))