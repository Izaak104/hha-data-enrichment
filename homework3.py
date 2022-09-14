from ossaudiodev import AFMT_IMA_ADPCM
import pandas as pd
import datetime as dt
import uuid
import numpy as np

#load datasets
sparcs = pd.read_csv("Hospital_Inpatient_Discharges__SPARCS_De-Identified___2015.csv")
adi = pd.read_csv("NY_2015_ADI_9 Digit Zip Code_v3.1.csv")

#run code to print out the names of columns in the dataframe
list(sparcs.columns)
list(adi.columns)


#run code to insert underscore (_) into the columns to make it more human & machine readable
sparcs.columns = sparcs.columns.str.replace('[^A-Za-z0-9]+', '_')
adi.columns = adi.columns.str.replace('[^A-Za-z0-9]+', '_')

#change all column names to upper case
sparcs.columns = sparcs.columns.str.upper()
adi.columns = adi.columns.str.upper()

#print out contents of dataframes
print(sparcs)
print(adi)

#create create smaller tables from both datasets using selected columns
df_sparcs_small = sparcs[["HEALTH_SERVICE_AREA", "HOSPITAL_COUNTY", "ZIP_CODE_3_DIGITS", "TOTAL_CHARGES", "TOTAL_COSTS"]]
print(df_sparcs_small)

df_adi_small = adi[["ZIPID", "ADI_NATRANK",]]
print(df_adi_small)


###merging selected columns from both datasets
combined_df = df_adi_small.merge(df_sparcs_small, how="left", left_on="HEALTH_SERVICE_AREA", right_on="ZIPID")











