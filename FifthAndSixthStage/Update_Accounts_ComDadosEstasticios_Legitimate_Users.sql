UPDATE accounts 
join legitimate_users on accounts.userid = legitimate_users.userid 
set 
	accounts.D1_media = legitimate_users.D1_media,
	accounts.D2_media = legitimate_users.D2_media,
	accounts.D3_media = legitimate_users.D3_media,
	accounts.D4_media = legitimate_users.D4_media,
	accounts.D5_media = legitimate_users.D5_media,
	accounts.D6_media = legitimate_users.D6_media,
	accounts.D7_media = legitimate_users.D7_media,
	accounts.D8_media = legitimate_users.D8_media,
	accounts.D9_media = legitimate_users.D9_media,
	accounts.D10_media = legitimate_users.D10_media,
	accounts.D11_media = legitimate_users.D11_media,
	accounts.D12_media = legitimate_users.D12_media,
	accounts.D13_media = legitimate_users.D13_media,
	accounts.D14_media = legitimate_users.D14_media,
	accounts.D15_media = legitimate_users.D15_media,
	accounts.D16_media = legitimate_users.D16_media,
	accounts.D17_media = legitimate_users.D17_media,
	accounts.D18_media = legitimate_users.D18_media,
	accounts.D19_media = legitimate_users.D19_media,
	accounts.D20_media = legitimate_users.D20_media,
	accounts.D21_media = legitimate_users.D21_media,
	accounts.D22_media = legitimate_users.D22_media,
	accounts.D23_media = legitimate_users.D23_media,
	accounts.D24_media = legitimate_users.D24_media,
	accounts.D25_media = legitimate_users.D25_media,
	accounts.D26_media = legitimate_users.D26_media,
	accounts.D27_media = legitimate_users.D27_media,
	accounts.D28_media = legitimate_users.D28_media,
	accounts.D29_media = legitimate_users.D29_media,
	accounts.D30_media = legitimate_users.D30_media,
	accounts.D31_media = legitimate_users.D31_media,
	accounts.D32_media = legitimate_users.D32_media,
	accounts.D33_media = legitimate_users.D33_media,
	accounts.D34_media = legitimate_users.D34_media,
	accounts.D35_media = legitimate_users.D35_media,
	accounts.D36_media = legitimate_users.D36_media,
	accounts.D37_media = legitimate_users.D37_media,
	accounts.D38_media = legitimate_users.D38_media,
	accounts.D39_media = legitimate_users.D39_media,
	accounts.D40_media = legitimate_users.D40_media,
	accounts.D41_media = legitimate_users.D41_media,
	accounts.D42_media = legitimate_users.D42_media,
	accounts.D43_media = legitimate_users.D43_media,
	accounts.D44_media = legitimate_users.D44_media,
	accounts.D45_media = legitimate_users.D45_media,
	accounts.D46_media = legitimate_users.D46_media,
	accounts.D47_media = legitimate_users.D47_media,
	accounts.D48_media = legitimate_users.D48_media,
	accounts.D49_media = legitimate_users.D49_media,
	accounts.D50_media = legitimate_users.D50_media,
	accounts.D1_1quartil = legitimate_users.D1_1quartil,
	accounts.D2_1quartil = legitimate_users.D2_1quartil,
	accounts.D3_1quartil = legitimate_users.D3_1quartil,
	accounts.D4_1quartil = legitimate_users.D4_1quartil,
	accounts.D5_1quartil = legitimate_users.D5_1quartil,
	accounts.D6_1quartil = legitimate_users.D6_1quartil,
	accounts.D7_1quartil = legitimate_users.D7_1quartil,
	accounts.D8_1quartil = legitimate_users.D8_1quartil,
	accounts.D9_1quartil = legitimate_users.D9_1quartil,
	accounts.D10_1quartil = legitimate_users.D10_1quartil,
	accounts.D11_1quartil = legitimate_users.D11_1quartil,
	accounts.D12_1quartil = legitimate_users.D12_1quartil,
	accounts.D13_1quartil = legitimate_users.D13_1quartil,
	accounts.D14_1quartil = legitimate_users.D14_1quartil,
	accounts.D15_1quartil = legitimate_users.D15_1quartil,
	accounts.D16_1quartil = legitimate_users.D16_1quartil,
	accounts.D17_1quartil = legitimate_users.D17_1quartil,
	accounts.D18_1quartil = legitimate_users.D18_1quartil,
	accounts.D19_1quartil = legitimate_users.D19_1quartil,
	accounts.D20_1quartil = legitimate_users.D20_1quartil,
	accounts.D21_1quartil = legitimate_users.D21_1quartil,
	accounts.D22_1quartil = legitimate_users.D22_1quartil,
	accounts.D23_1quartil = legitimate_users.D23_1quartil,
	accounts.D24_1quartil = legitimate_users.D24_1quartil,
	accounts.D25_1quartil = legitimate_users.D25_1quartil,
	accounts.D26_1quartil = legitimate_users.D26_1quartil,
	accounts.D27_1quartil = legitimate_users.D27_1quartil,
	accounts.D28_1quartil = legitimate_users.D28_1quartil,
	accounts.D29_1quartil = legitimate_users.D29_1quartil,
	accounts.D30_1quartil = legitimate_users.D30_1quartil,
	accounts.D31_1quartil = legitimate_users.D31_1quartil,
	accounts.D32_1quartil = legitimate_users.D32_1quartil,
	accounts.D33_1quartil = legitimate_users.D33_1quartil,
	accounts.D34_1quartil = legitimate_users.D34_1quartil,
	accounts.D35_1quartil = legitimate_users.D35_1quartil,
	accounts.D36_1quartil = legitimate_users.D36_1quartil,
	accounts.D37_1quartil = legitimate_users.D37_1quartil,
	accounts.D38_1quartil = legitimate_users.D38_1quartil,
	accounts.D39_1quartil = legitimate_users.D39_1quartil,
	accounts.D40_1quartil = legitimate_users.D40_1quartil,
	accounts.D41_1quartil = legitimate_users.D41_1quartil,
	accounts.D42_1quartil = legitimate_users.D42_1quartil,
	accounts.D43_1quartil = legitimate_users.D43_1quartil,
	accounts.D44_1quartil = legitimate_users.D44_1quartil,
	accounts.D45_1quartil = legitimate_users.D45_1quartil,
	accounts.D46_1quartil = legitimate_users.D46_1quartil,
	accounts.D47_1quartil = legitimate_users.D47_1quartil,
	accounts.D48_1quartil = legitimate_users.D48_1quartil,
	accounts.D49_1quartil = legitimate_users.D49_1quartil,
	accounts.D50_1quartil = legitimate_users.D50_1quartil,
	accounts.D1_mediana = legitimate_users.D1_mediana,
	accounts.D2_mediana = legitimate_users.D2_mediana,
	accounts.D3_mediana = legitimate_users.D3_mediana,
	accounts.D4_mediana = legitimate_users.D4_mediana,
	accounts.D5_mediana = legitimate_users.D5_mediana,
	accounts.D6_mediana = legitimate_users.D6_mediana,
	accounts.D7_mediana = legitimate_users.D7_mediana,
	accounts.D8_mediana = legitimate_users.D8_mediana,
	accounts.D9_mediana = legitimate_users.D9_mediana,
	accounts.D10_mediana = legitimate_users.D10_mediana,
	accounts.D11_mediana = legitimate_users.D11_mediana,
	accounts.D12_mediana = legitimate_users.D12_mediana,
	accounts.D13_mediana = legitimate_users.D13_mediana,
	accounts.D14_mediana = legitimate_users.D14_mediana,
	accounts.D15_mediana = legitimate_users.D15_mediana,
	accounts.D16_mediana = legitimate_users.D16_mediana,
	accounts.D17_mediana = legitimate_users.D17_mediana,
	accounts.D18_mediana = legitimate_users.D18_mediana,
	accounts.D19_mediana = legitimate_users.D19_mediana,
	accounts.D20_mediana = legitimate_users.D20_mediana,
	accounts.D21_mediana = legitimate_users.D21_mediana,
	accounts.D22_mediana = legitimate_users.D22_mediana,
	accounts.D23_mediana = legitimate_users.D23_mediana,
	accounts.D24_mediana = legitimate_users.D24_mediana,
	accounts.D25_mediana = legitimate_users.D25_mediana,
	accounts.D26_mediana = legitimate_users.D26_mediana,
	accounts.D27_mediana = legitimate_users.D27_mediana,
	accounts.D28_mediana = legitimate_users.D28_mediana,
	accounts.D29_mediana = legitimate_users.D29_mediana,
	accounts.D30_mediana = legitimate_users.D30_mediana,
	accounts.D31_mediana = legitimate_users.D31_mediana,
	accounts.D32_mediana = legitimate_users.D32_mediana,
	accounts.D33_mediana = legitimate_users.D33_mediana,
	accounts.D34_mediana = legitimate_users.D34_mediana,
	accounts.D35_mediana = legitimate_users.D35_mediana,
	accounts.D36_mediana = legitimate_users.D36_mediana,
	accounts.D37_mediana = legitimate_users.D37_mediana,
	accounts.D38_mediana = legitimate_users.D38_mediana,
	accounts.D39_mediana = legitimate_users.D39_mediana,
	accounts.D40_mediana = legitimate_users.D40_mediana,
	accounts.D41_mediana = legitimate_users.D41_mediana,
	accounts.D42_mediana = legitimate_users.D42_mediana,
	accounts.D43_mediana = legitimate_users.D43_mediana,
	accounts.D44_mediana = legitimate_users.D44_mediana,
	accounts.D45_mediana = legitimate_users.D45_mediana,
	accounts.D46_mediana = legitimate_users.D46_mediana,
	accounts.D47_mediana = legitimate_users.D47_mediana,
	accounts.D48_mediana = legitimate_users.D48_mediana,
	accounts.D49_mediana = legitimate_users.D49_mediana,
	accounts.D50_mediana = legitimate_users.D50_mediana,
	accounts.D1_3quartil = legitimate_users.D1_3quartil,
	accounts.D2_3quartil = legitimate_users.D2_3quartil,
	accounts.D3_3quartil = legitimate_users.D3_3quartil,
	accounts.D4_3quartil = legitimate_users.D4_3quartil,
	accounts.D5_3quartil = legitimate_users.D5_3quartil,
	accounts.D6_3quartil = legitimate_users.D6_3quartil,
	accounts.D7_3quartil = legitimate_users.D7_3quartil,
	accounts.D8_3quartil = legitimate_users.D8_3quartil,
	accounts.D9_3quartil = legitimate_users.D9_3quartil,
	accounts.D10_3quartil = legitimate_users.D10_3quartil,
	accounts.D11_3quartil = legitimate_users.D11_3quartil,
	accounts.D12_3quartil = legitimate_users.D12_3quartil,
	accounts.D13_3quartil = legitimate_users.D13_3quartil,
	accounts.D14_3quartil = legitimate_users.D14_3quartil,
	accounts.D15_3quartil = legitimate_users.D15_3quartil,
	accounts.D16_3quartil = legitimate_users.D16_3quartil,
	accounts.D17_3quartil = legitimate_users.D17_3quartil,
	accounts.D18_3quartil = legitimate_users.D18_3quartil,
	accounts.D19_3quartil = legitimate_users.D19_3quartil,
	accounts.D20_3quartil = legitimate_users.D20_3quartil,
	accounts.D21_3quartil = legitimate_users.D21_3quartil,
	accounts.D22_3quartil = legitimate_users.D22_3quartil,
	accounts.D23_3quartil = legitimate_users.D23_3quartil,
	accounts.D24_3quartil = legitimate_users.D24_3quartil,
	accounts.D25_3quartil = legitimate_users.D25_3quartil,
	accounts.D26_3quartil = legitimate_users.D26_3quartil,
	accounts.D27_3quartil = legitimate_users.D27_3quartil,
	accounts.D28_3quartil = legitimate_users.D28_3quartil,
	accounts.D29_3quartil = legitimate_users.D29_3quartil,
	accounts.D30_3quartil = legitimate_users.D30_3quartil,
	accounts.D31_3quartil = legitimate_users.D31_3quartil,
	accounts.D32_3quartil = legitimate_users.D32_3quartil,
	accounts.D33_3quartil = legitimate_users.D33_3quartil,
	accounts.D34_3quartil = legitimate_users.D34_3quartil,
	accounts.D35_3quartil = legitimate_users.D35_3quartil,
	accounts.D36_3quartil = legitimate_users.D36_3quartil,
	accounts.D37_3quartil = legitimate_users.D37_3quartil,
	accounts.D38_3quartil = legitimate_users.D38_3quartil,
	accounts.D39_3quartil = legitimate_users.D39_3quartil,
	accounts.D40_3quartil = legitimate_users.D40_3quartil,
	accounts.D41_3quartil = legitimate_users.D41_3quartil,
	accounts.D42_3quartil = legitimate_users.D42_3quartil,
	accounts.D43_3quartil = legitimate_users.D43_3quartil,
	accounts.D44_3quartil = legitimate_users.D44_3quartil,
	accounts.D45_3quartil = legitimate_users.D45_3quartil,
	accounts.D46_3quartil = legitimate_users.D46_3quartil,
	accounts.D47_3quartil = legitimate_users.D47_3quartil,
	accounts.D48_3quartil = legitimate_users.D48_3quartil,
	accounts.D49_3quartil = legitimate_users.D49_3quartil,
	accounts.D50_3quartil = legitimate_users.D50_3quartil,
	accounts.D1_desviopadrao = legitimate_users.D1_desviopadrao,
	accounts.D2_desviopadrao = legitimate_users.D2_desviopadrao,
	accounts.D3_desviopadrao = legitimate_users.D3_desviopadrao,
	accounts.D4_desviopadrao = legitimate_users.D4_desviopadrao,
	accounts.D5_desviopadrao = legitimate_users.D5_desviopadrao,
	accounts.D6_desviopadrao = legitimate_users.D6_desviopadrao,
	accounts.D7_desviopadrao = legitimate_users.D7_desviopadrao,
	accounts.D8_desviopadrao = legitimate_users.D8_desviopadrao,
	accounts.D9_desviopadrao = legitimate_users.D9_desviopadrao,
	accounts.D10_desviopadrao = legitimate_users.D10_desviopadrao,
	accounts.D11_desviopadrao = legitimate_users.D11_desviopadrao,
	accounts.D12_desviopadrao = legitimate_users.D12_desviopadrao,
	accounts.D13_desviopadrao = legitimate_users.D13_desviopadrao,
	accounts.D14_desviopadrao = legitimate_users.D14_desviopadrao,
	accounts.D15_desviopadrao = legitimate_users.D15_desviopadrao,
	accounts.D16_desviopadrao = legitimate_users.D16_desviopadrao,
	accounts.D17_desviopadrao = legitimate_users.D17_desviopadrao,
	accounts.D18_desviopadrao = legitimate_users.D18_desviopadrao,
	accounts.D19_desviopadrao = legitimate_users.D19_desviopadrao,
	accounts.D20_desviopadrao = legitimate_users.D20_desviopadrao,
	accounts.D21_desviopadrao = legitimate_users.D21_desviopadrao,
	accounts.D22_desviopadrao = legitimate_users.D22_desviopadrao,
	accounts.D23_desviopadrao = legitimate_users.D23_desviopadrao,
	accounts.D24_desviopadrao = legitimate_users.D24_desviopadrao,
	accounts.D25_desviopadrao = legitimate_users.D25_desviopadrao,
	accounts.D26_desviopadrao = legitimate_users.D26_desviopadrao,
	accounts.D27_desviopadrao = legitimate_users.D27_desviopadrao,
	accounts.D28_desviopadrao = legitimate_users.D28_desviopadrao,
	accounts.D29_desviopadrao = legitimate_users.D29_desviopadrao,
	accounts.D30_desviopadrao = legitimate_users.D30_desviopadrao,
	accounts.D31_desviopadrao = legitimate_users.D31_desviopadrao,
	accounts.D32_desviopadrao = legitimate_users.D32_desviopadrao,
	accounts.D33_desviopadrao = legitimate_users.D33_desviopadrao,
	accounts.D34_desviopadrao = legitimate_users.D34_desviopadrao,
	accounts.D35_desviopadrao = legitimate_users.D35_desviopadrao,
	accounts.D36_desviopadrao = legitimate_users.D36_desviopadrao,
	accounts.D37_desviopadrao = legitimate_users.D37_desviopadrao,
	accounts.D38_desviopadrao = legitimate_users.D38_desviopadrao,
	accounts.D39_desviopadrao = legitimate_users.D39_desviopadrao,
	accounts.D40_desviopadrao = legitimate_users.D40_desviopadrao,
	accounts.D41_desviopadrao = legitimate_users.D41_desviopadrao,
	accounts.D42_desviopadrao = legitimate_users.D42_desviopadrao,
	accounts.D43_desviopadrao = legitimate_users.D43_desviopadrao,
	accounts.D44_desviopadrao = legitimate_users.D44_desviopadrao,
	accounts.D45_desviopadrao = legitimate_users.D45_desviopadrao,
	accounts.D46_desviopadrao = legitimate_users.D46_desviopadrao,
	accounts.D47_desviopadrao = legitimate_users.D47_desviopadrao,
	accounts.D48_desviopadrao = legitimate_users.D48_desviopadrao,
	accounts.D49_desviopadrao = legitimate_users.D49_desviopadrao,
	accounts.D50_desviopadrao = legitimate_users.D50_desviopadrao,
	accounts.D1_amplitude = legitimate_users.D1_amplitude,
	accounts.D2_amplitude = legitimate_users.D2_amplitude,
	accounts.D3_amplitude = legitimate_users.D3_amplitude,
	accounts.D4_amplitude = legitimate_users.D4_amplitude,
	accounts.D5_amplitude = legitimate_users.D5_amplitude,
	accounts.D6_amplitude = legitimate_users.D6_amplitude,
	accounts.D7_amplitude = legitimate_users.D7_amplitude,
	accounts.D8_amplitude = legitimate_users.D8_amplitude,
	accounts.D9_amplitude = legitimate_users.D9_amplitude,
	accounts.D10_amplitude = legitimate_users.D10_amplitude,
	accounts.D11_amplitude = legitimate_users.D11_amplitude,
	accounts.D12_amplitude = legitimate_users.D12_amplitude,
	accounts.D13_amplitude = legitimate_users.D13_amplitude,
	accounts.D14_amplitude = legitimate_users.D14_amplitude,
	accounts.D15_amplitude = legitimate_users.D15_amplitude,
	accounts.D16_amplitude = legitimate_users.D16_amplitude,
	accounts.D17_amplitude = legitimate_users.D17_amplitude,
	accounts.D18_amplitude = legitimate_users.D18_amplitude,
	accounts.D19_amplitude = legitimate_users.D19_amplitude,
	accounts.D20_amplitude = legitimate_users.D20_amplitude,
	accounts.D21_amplitude = legitimate_users.D21_amplitude,
	accounts.D22_amplitude = legitimate_users.D22_amplitude,
	accounts.D23_amplitude = legitimate_users.D23_amplitude,
	accounts.D24_amplitude = legitimate_users.D24_amplitude,
	accounts.D25_amplitude = legitimate_users.D25_amplitude,
	accounts.D26_amplitude = legitimate_users.D26_amplitude,
	accounts.D27_amplitude = legitimate_users.D27_amplitude,
	accounts.D28_amplitude = legitimate_users.D28_amplitude,
	accounts.D29_amplitude = legitimate_users.D29_amplitude,
	accounts.D30_amplitude = legitimate_users.D30_amplitude,
	accounts.D31_amplitude = legitimate_users.D31_amplitude,
	accounts.D32_amplitude = legitimate_users.D32_amplitude,
	accounts.D33_amplitude = legitimate_users.D33_amplitude,
	accounts.D34_amplitude = legitimate_users.D34_amplitude,
	accounts.D35_amplitude = legitimate_users.D35_amplitude,
	accounts.D36_amplitude = legitimate_users.D36_amplitude,
	accounts.D37_amplitude = legitimate_users.D37_amplitude,
	accounts.D38_amplitude = legitimate_users.D38_amplitude,
	accounts.D39_amplitude = legitimate_users.D39_amplitude,
	accounts.D40_amplitude = legitimate_users.D40_amplitude,
	accounts.D41_amplitude = legitimate_users.D41_amplitude,
	accounts.D42_amplitude = legitimate_users.D42_amplitude,
	accounts.D43_amplitude = legitimate_users.D43_amplitude,
	accounts.D44_amplitude = legitimate_users.D44_amplitude,
	accounts.D45_amplitude = legitimate_users.D45_amplitude,
	accounts.D46_amplitude = legitimate_users.D46_amplitude,
	accounts.D47_amplitude = legitimate_users.D47_amplitude,
	accounts.D48_amplitude = legitimate_users.D48_amplitude,
	accounts.D49_amplitude = legitimate_users.D49_amplitude,
	accounts.D50_amplitude = legitimate_users.D50_amplitude	
WHERE accounts.userid = legitimate_users.userid 
