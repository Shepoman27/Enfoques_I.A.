# Definimos las probabilidades
P_A = 0.5
P_B_given_A = {0: 0.3, 1: 0.7}  # P(B=0|A), P(B=1|A)
P_C_given_AB = {(0, 0): 0.1, (0, 1): 0.2, (1, 0): 0.3, (1, 1): 0.4}  # P(C=0|A,B), P(C=1|A,B)

# Calculamos P(A, B, C)
P_ABC = {}
for a in [0, 1]:
    for b in [0, 1]:
        for c in [0, 1]:
            P_ABC[(a, b, c)] = P_C_given_AB[(a, b)] * P_B_given_A[b] * P_A

# Imprimimos los resultados
print("P(A, B, C):")
for abc, p_abc in P_ABC.items():
    print("P({}): {:.4f}".format(abc, p_abc))
