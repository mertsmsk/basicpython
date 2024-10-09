def reverse_nested(input_list):
    # Önce dış listeyi ters çevir
    reversed_list = input_list[::-1]
    
    # Her bir elemanı kontrol et ve iç listeleri de ters çevir
    for i in range(len(reversed_list)):
        if isinstance(reversed_list[i], list):
            reversed_list[i] = list(reversed(reversed_list[i]))
    return reversed_list

# Örnek kullanım
input_data = [[1, 2], [3, 4], [5, 6, 7]]
output_data = reverse_nested(input_data)
print(output_data)