for i in range(1, 10):
    print('\t'.join([f"{j}×{i}={i*j}" for j in range(1, i +1)]))
