import pandas as pd
import numpy as np

from statsmodels.stats.proportion import power_proportions_2indep, test_proportions_2indep
from statsmodels.stats.weightstats import ttest_ind
from statsmodels.stats.power import tt_ind_solve_power

'''
Berikut adalah rangkaian code untuk memproses data A/B testing. Bisa copy dan dicoba sendiri di notebook masing-masing.
'''
def p_value(ab_test_ready):

  result = test_proportions_2indep(count1=ab_test_ready["treatment_converted"], 
                                   nobs1=ab_test_ready["treatment_visit"], 
                                   count2=ab_test_ready["control_converted"], 
                                   nobs2=ab_test_ready["control_visit"],
                                   alternative="two-sided")
  return result[1]

def power(ab_test_ready):

  test_split = ab_test_ready['treatment_visit'] / (ab_test_ready['treatment_visit'] + ab_test_ready['control_visit'])
  relative_effect = (ab_test_ready['treatment_converted_rate'] - ab_test_ready['control_converted_rate'])/ab_test_ready['control_converted_rate']  

  power_result = power_proportions_2indep(diff=ab_test_ready['control_converted_rate'] * relative_effect,
                                               prop2=ab_test_ready['control_converted_rate'], 
                                               nobs1=ab_test_ready['treatment_visit'],
                                               ratio=(1-test_split)/test_split,
                                               alpha=0.05,
                                               alternative='two-sided',
                                               return_results=False)
  return power_result


ab = pd.read_excel("../1. DATASETS/CleanedBDMarketing.xlsx")

# remove beberapa data
ab = ab[((ab['BD_Group']=='control')&(ab['BD_Landing']=='old_page')) |
        ((ab['BD_Group']=='treatment')&(ab['BD_Landing']=='new_page'))]

data = ab.copy().drop(columns=['BD_UserId', 'BD_Landing'])

# sort data sesuai tanggal
data['date'] = pd.to_datetime(data['BD_Timestamp']).dt.date
data.sort_values(by='BD_Timestamp', inplace=True)

ab_test = data[['BD_Group', 'BD_Conversion', 'date']]

# menghitung jumlah visit dan converted per hari
valuenya = ab_test.groupby(['date', 'BD_Group']).agg(['count', 'sum']).unstack().reset_index().values
ab_test1 = pd.DataFrame(valuenya, columns=['date_ab_test', 'control_visit', 'treatment_visit', 'control_converted', 'treatment_converted'])

# mengubah data menjadi cumulative dan menghitung powe dan p value per harian nya
ab_test_ready = ab_test1.set_index('date_ab_test').cumsum() 
ab_test_ready['control_converted_rate'] = ab_test_ready['control_converted'] / ab_test_ready['control_visit'] 
ab_test_ready['treatment_converted_rate'] = ab_test_ready['treatment_converted'] / ab_test_ready['treatment_visit'] 
ab_test_ready['p_value'] = ab_test_ready.apply(p_value, axis=1)
ab_test_ready['power'] = ab_test_ready.apply(power, axis=1)

#
ab_test_ready.to_excel('../3. ARTIFACTS/AB_test_cumulative.xlsx')