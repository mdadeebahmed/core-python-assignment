def calculate_fare(trips):
  base_fare = 50
  distance_fare = 10
  total_fare = 0

  for i in range(1, len(trips)+1):
    cost = base_fare + trips[i-1] * distance_fare
    print(f'Trip {i}: ${cost}')
    total_fare += cost

  return f'Total Fare: ${total_fare}'

    

trips = [5, 10, 3]
print(calculate_fare(trips))