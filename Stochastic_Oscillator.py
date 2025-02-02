prices = [
    687.20, 678.55, 685.20, 693.20, 693.90, 688.00, 702.10, 704.30, 710.35, 713.85,
    716.25, 732.15, 735.80, 744.95, 741.00, 747.55, 768.40, 749.55, 742.85, 768.00,
    746.45, 731.05, 749.60, 745.35, 735.15, 745.40, 733.75, 739.15, 742.55, 745.60,
    755.65, 742.60, 744.95, 755.75, 757.45, 767.20, 780.15, 789.50, 782.20, 773.65,
    775.70, 791.05, 768.00, 755.10, 750.65, 750.00, 749.90, 755.25, 755.65, 750.90,
    746.00, 758.15, 750.65, 758.05, 769.35, 763.70, 753.45, 753.15, 742.30, 744.60,
    744.15, 723.25, 731.95, 733.00, 741.45, 742.50, 720.05, 720.05, 718.20, 724.30,
    728.75, 739.25, 738.65, 726.05, 700.05, 714.20, 728.60, 734.70, 735.95, 723.85,
    719.05, 724.90, 701.70, 694.25, 638.40, 633.80, 643.40, 654.80, 654.35, 654.25,
    651.15, 653.35, 660.75, 646.50, 636.35, 643.00, 633.45, 634.40, 620.35, 616.70,
    605.70, 599.65, 596.50, 600.35, 605.40
]
interval = 14
K_values = [0 for i in range(interval - 1)]
for i in range (interval - 1, len(prices)):
    minima = min(prices[i + 1 - interval : i+1])
    maxima = max(prices[i + 1 - interval : i+1])
    diff = maxima - minima
    current = prices[i]
    K_values.append(((current - minima) * 100 ) / diff)

D_smoothness = 3
D_values = [0 for i in range(D_smoothness - 1)]
for i in range (D_smoothness - 1, len(K_values)):
    a = K_values[i - 2] + K_values[i - 1] + K_values[i]
    a = a / 3
    D_values.append(a)

print(K_values)
print()
print(D_values)
    
