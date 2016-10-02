import pandas as pd
import numpy as np


"""exploratory analysis"""
# raw_data = pd.read_csv("dataset.csv")

# print raw_data.head()

# print raw_data.count()

# #removing duplicates from the data
# unique_data = raw_data.drop_duplicates()
# print unique_data.count()

# unique_data.to_csv("unique_dataset.csv")

"""aggregating the data and analysing"""
# raw_data = pd.read_csv("unique_dataset.csv")
# raw_data = raw_data.drop(raw_data.columns[[0,2]], axis =1)
# raw_data['Date'] = pd.to_datetime(raw_data['date'],format='%d%b%Y')
# raw_data = raw_data.drop(['date'],axis=1)
# print raw_data.head()
# # ThreeMonthAverageByBond = pd.pivot_table(raw_data,values='volume', index='isin', columns='side', aggfunc=np.sum)
# # ThreeMonthAverageByBond.to_csv("ThreeMonthAverageByBond.csv",sep=",")
# # ThreeMonthMedianByBond = pd.pivot_table(raw_data,values='volume', index='isin', columns='side', aggfunc=np.median)
# # ThreeMonthMedianByBond.to_csv("ThreeMonthMedianByBond.csv",sep=",")
# # NumberOfDaysByBond = pd.pivot_table(raw_data,values='date', index='isin', columns='side', aggfunc=np.size)
# # NumberOfDaysByBond.to_csv("NumberOfDaysByBond.csv",sep=",")
# # ThreeMonthVarianceByBond = pd.pivot_table(raw_data,values='volume', index='isin', columns='side', aggfunc=np.var)
# # ThreeMonthVarianceByBond.to_csv("ThreeMonthAverageByBond.csv",sep=",")
# data_by_date = pd.pivot_table(raw_data,values='volume', index=['isin','Date'], columns='side', aggfunc=np.sum)
# data_by_date.to_csv("aggregated_volume_by_date.csv",sep=",")

"""subsetting the data to analyse the nature of series"""

# subset = raw_data[raw_data['isin'].isin(['isin10720','isin9334','isin1075','isin16922','isin7759','isin10353','isin1446'])]
# print subset
# subset.to_csv("timeSeriesForSelectedBonds.csv",sep=",")


"""seasonality estimation of the time series"""
# import numpy as np
# import statsmodels.api as sm
# from pandas.tseries.offsets import *
# aggregated_data = pd.read_csv("aggregated_volume_by_date.csv",sep=",")
# aggregated_data = aggregated_data.fillna(0)
# loop = 0
# output_file =  open("high_frequency_bonds_trend_seasonality_based_prediction.csv","w")
# with open("high_freq_bonds.csv") as data_file:
# 	for line in data_file:
# 		loop += 1
# 		print loop
# 		bond = line.strip()
# 		if loop > 1:
# 			break
# 		subset = aggregated_data[aggregated_data['isin']==bond]
# 		subset['Date'] = pd.to_datetime(subset['Date'])
# 		buy_series = subset[['Date','B']]
# 		buy_series = buy_series.set_index('Date')
# 		sell_series = subset[['Date','S']]
# 		sell_series = sell_series.set_index('Date')
# 		resB = sm.tsa.seasonal_decompose(buy_series,freq=5)
# 		resB.seasonal.to_csv("seasonal.csv",sep=",")
# 		resB.trend.to_csv("trend.csv",sep=",")
# 		# resS = sm.tsa.seasonal_decompose(sell_series,freq=5)
# 		# buy_volume = int(np.sum(resB.seasonal.tail(3)['B']) + resB.trend.tail(3)['B'][0]*3)
# 		# sell_volume = int(np.sum(resS.seasonal.tail(3)['S']) + resS.trend.tail(3)['S'][0]*3)
# 		# to_write = bond+","+str(buy_volume)+","+str(sell_volume)+"\n"
# 		# output_file.writelines(to_write)


"""modelling liquidity"""
# aggregated_data = pd.read_csv("aggregated_volume_by_date.csv",sep=",")
# aggregated_data = aggregated_data.fillna(0)
# aggregated_data['liquidity'] = (aggregated_data['B']+aggregated_data['S'])/abs(aggregated_data['B']-aggregated_data['S']+100)
# subset = aggregated_data.head(10000)

# meta_data = pd.read_csv("ML_Bond_metadata_corrected_dates.csv",sep=",")
# meta_data = meta_data.fillna('missing')

# def EventCheck(row):
# 	bond = row['isin']
# 	date = row['Date']
# 	meta_subset = meta_data[meta_data['isin']==bond]
# 	issue_date = meta_subset['issueDate'].iloc[0]
# 	eff_date1 = meta_subset['ratingAgency1EffectiveDate'].iloc[0]
# 	eff_date2 = meta_subset['ratingAgency2EffectiveDate'].iloc[0]
# 	if issue_date != 'missing':
# 		if pd.to_datetime(issue_date) == pd.to_datetime(date):
# 			return 3
# 	if eff_date1 != 'missing':
# 		if pd.to_datetime(eff_date1) == pd.to_datetime(date):
# 			return 1
# 	if eff_date2 != 'missing':
# 		if pd.to_datetime(eff_date2) == pd.to_datetime(date):
# 			return 2
# 	return 0



# # subset['EventIndicator'] = subset.apply(EventCheck,axis=1)
# # print subset
# # print subset[subset['EventIndicator']==1]
# print "marking events on the full data"
# aggregated_data['EventIndicator'] = aggregated_data.apply(EventCheck,axis=1)
# aggregated_data.to_csv('EventLiquidityindicator.csv',sep=",")

# liq_ind_aggregated = pd.read_csv("EventLiquidityindicator.csv",sep=",")
# liq_ind_aggregated = liq_ind_aggregated.drop(liq_ind_aggregated.columns[0], axis =1)
# print liq_ind_aggregated.head()

# #event type 1
# event1 = liq_ind_aggregated[liq_ind_aggregated['EventIndicator']==1]
# event1 = event1[event1['liquidity']>100]
# event1.to_csv("event1_affected_bonds.csv",sep=",")

#event type 1
# event2 = liq_ind_aggregated[liq_ind_aggregated['EventIndicator']==2]
# event2 = event2[event2['liquidity']>100]
# event2.to_csv("event2_affected_bonds.csv",sep=",")


# subset = liq_ind_aggregated[['liquidity','EventIndicator']]
# print subset.head()
# subset.to_csv("liquidity_events.csv",sep=",",index=False)
# event_subset = liq_ind_aggregated[liq_ind_aggregated['EventIndicator']==1]
# print len(event_subset)



"""var model"""
aggregated_data = pd.read_csv("aggregated_volume_by_date.csv",sep=",")
aggregated_data = aggregated_data.fillna(0)
# print aggregated_data.head()

meta_data = pd.read_csv("ML_Bond_metadata_corrected_dates.csv",sep=",")
meta_data = meta_data.fillna('missing')

b_file = open("buy_var_data.csv","w")
s_file = open("sell_val_data.csv","w")
loop = 0
with open("more_than_10.csv") as data_file:
	for line in data_file:
		# print line
		loop += 1
		print loop
		bond = line.strip()
		# if loop > 2:
		# 	break
		subset = aggregated_data[aggregated_data['isin']==bond]
		# b_write = bond + ","+str(subset['B'].iloc[-1]) + "," + str(subset['B'].iloc[-2]) + "," + str(subset['B'].iloc[-3]) + "," + str(subset['B'].iloc[-4]) + "," + str(subset['B'].iloc[-5]) + "," + str(subset['B'].iloc[-6]) + "," + str(subset['B'].iloc[-7])+","+str(subset['B'].iloc[-8])+","+str(subset['B'].iloc[-9])+","+str(subset['B'].iloc[-10])+"\n"
		# s_write = bond + ","+str(subset['S'].iloc[-1]) + "," + str(subset['S'].iloc[-2]) + "," + str(subset['S'].iloc[-3]) + "," + str(subset['S'].iloc[-4]) + "," + str(subset['S'].iloc[-5]) + "," + str(subset['S'].iloc[-6]) + "," + str(subset['S'].iloc[-7])+","+str(subset['S'].iloc[-8])+","+str(subset['S'].iloc[-9])+","+str(subset['S'].iloc[-10])+"\n"
		# b_file.writelines(b_write)
		# s_file.writelines(s_write)

