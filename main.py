import pandas as pd
import xlsxwriter

df0 = pd.read_csv('install-base-0.csv')
df1 = pd.read_csv('install-base-1.csv')
df2 = pd.read_csv('install-base-2.csv')
df3 = pd.read_csv('install-base-3.csv')
df4 = pd.read_csv('install-base-4.csv')
df5 = pd.read_csv('install-base-5.csv')
df6 = pd.read_csv('install-base-6.csv')
df7 = pd.read_csv('install-base-7.csv')

#install-base-0
#US
#Germany
#France
#Japan
#South Korea
#Brazil
#Italy
#Taiwan
#Netherlands

#install-base-1
#Poland
#Thailand
#Canada
#Russia
#Spain
#Finland
#Switzerland
#Czechia
#Mexico
#Belgium

#install-base-2
#Indonesia
#Denmark
#India
#Sweden
#United Kingdom
#Slovakia
#Australia
#Hungary
#Egypt
#Vietnam

#install-base-3
#Austria
#Malaysia
#Hong Kong
#Morocco
#Colombia
#Peru
#Saudi Arabia
#Ireland
#Tunisia

#install-base-4
#Jordan
#Argentina
#Portugal
#New Zealand
#Norway
#South Africa
#Croatia
#Greece
#Israel
#Chile

#install-base-5
#Phillipines
#Paraguay
#Nicaragua
#Lithuania
#Singapore
#Latvia
#Romania
#Panama
#Ecuador
#Estonia

#install-base-6
#Domninican Republic
#Guatemala
#United Arab Emirates
#Puerto Rico
#Luxembourg
#Bolivia
#Costa Rica
#Uruguay
#Kuwait
#El Salvador

#install-base-7
#Honduras
#Haiti
#Jamaica
#Qatar
#Brunei
#Barbados

country_install_base = []
for x in range(74):
    country_install_base.append(0)




def intx(c):
    try:
        return int(c.replace(',',''))
    except:
        return int(c)


country_install_base[0] = intx(df0['Install base (All devices, Unique devices, Per interval, Daily): United States'].tolist()[0])
country_install_base[1] = intx(df0['Install base (All devices, Unique devices, Per interval, Daily): Germany'].tolist()[0])
country_install_base[2] = intx(df3['Install base (All devices, Unique devices, Per interval, Daily): Austria'].tolist()[0])
country_install_base[3] = intx(df0['Install base (All devices, Unique devices, Per interval, Daily): Japan'].tolist()[0])
country_install_base[4] = intx(df1['Install base (All devices, Unique devices, Per interval, Daily): Canada'].tolist()[0])
country_install_base[5] = intx(df0['Install base (All devices, Unique devices, Per interval, Daily): France'].tolist()[0])
country_install_base[6] = intx(df1['Install base (All devices, Unique devices, Per interval, Daily): Switzerland'].tolist()[0])
country_install_base[7] = intx(df0['Install base (All devices, Unique devices, Per interval, Daily): South Korea'].tolist()[0])
country_install_base[8] = intx(df0['Install base (All devices, Unique devices, Per interval, Daily): Netherlands'].tolist()[0])
country_install_base[9] = intx(df2['Install base (All devices, Unique devices, Per interval, Daily): United Kingdom'].tolist()[0])
country_install_base[10] = intx(df1['Install base (All devices, Unique devices, Per interval, Daily): Belgium'].tolist()[0])
country_install_base[11] = intx(df0['Install base (All devices, Unique devices, Per interval, Daily): Italy'].tolist()[0])
country_install_base[12] = intx(df0['Install base (All devices, Unique devices, Per interval, Daily): Brazil'].tolist()[0])
country_install_base[13] = intx(df0['Install base (All devices, Unique devices, Per interval, Daily): Taiwan'].tolist()[0])
country_install_base[14] = intx(df3['Install base (All devices, Unique devices, Per interval, Daily): Hong Kong'].tolist()[0])
country_install_base[15] = intx(df2['Install base (All devices, Unique devices, Per interval, Daily): Denmark'].tolist()[0])
country_install_base[16] = intx(df2['Install base (All devices, Unique devices, Per interval, Daily): Sweden'].tolist()[0])
country_install_base[17] = intx(df1['Install base (All devices, Unique devices, Per interval, Daily): Finland'].tolist()[0])
country_install_base[18] = intx(df2['Install base (All devices, Unique devices, Per interval, Daily): Australia'].tolist()[0])
country_install_base[19] = intx(df1['Install base (All devices, Unique devices, Per interval, Daily): Spain'].tolist()[0])
country_install_base[20] = intx(df1['Install base (All devices, Unique devices, Per interval, Daily): Poland'].tolist()[0])
country_install_base[21] = intx(df1['Install base (All devices, Unique devices, Per interval, Daily): Mexico'].tolist()[0])
country_install_base[22] = intx(df1['Install base (All devices, Unique devices, Per interval, Daily): Czechia'].tolist()[0])
country_install_base[23] = intx(df2['Install base (All devices, Unique devices, Per interval, Daily): Slovakia'].tolist()[0])
country_install_base[24] = intx(df1['Install base (All devices, Unique devices, Per interval, Daily): Thailand'].tolist()[0])
country_install_base[25] = intx(df2['Install base (All devices, Unique devices, Per interval, Daily): Hungary'].tolist()[0])
country_install_base[26] = intx(df3['Install base (All devices, Unique devices, Per interval, Daily): Ireland'].tolist()[0])
country_install_base[27] = intx(df4['Install base (All devices, Unique devices, Per interval, Daily): New Zealand'].tolist()[0])
country_install_base[28] = intx(df2['Install base (All devices, Unique devices, Per interval, Daily): Indonesia'].tolist()[0])
country_install_base[29] = intx(df2['Install base (All devices, Unique devices, Per interval, Daily): Vietnam'].tolist()[0])
country_install_base[30] = intx(df4['Install base (All devices, Unique devices, Per interval, Daily): Norway'].tolist()[0])
country_install_base[31] = intx(df4['Install base (All devices, Unique devices, Per interval, Daily): Croatia'].tolist()[0])
country_install_base[32] = intx(df6['Install base (All devices, Unique devices, Per interval, Daily): Luxembourg'].tolist()[0])
country_install_base[33] = intx(df4['Install base (All devices, Unique devices, Per interval, Daily): Israel'].tolist()[0])
country_install_base[34] = intx(df4['Install base (All devices, Unique devices, Per interval, Daily): Greece'].tolist()[0])
country_install_base[35] = intx(df4['Install base (All devices, Unique devices, Per interval, Daily): South Africa'].tolist()[0])
country_install_base[36] = intx(df1['Install base (All devices, Unique devices, Per interval, Daily): Russia'].tolist()[0])
country_install_base[37] = intx(df4['Install base (All devices, Unique devices, Per interval, Daily): Portugal'].tolist()[0])
country_install_base[38] = intx(df5['Install base (All devices, Unique devices, Per interval, Daily): Romania'].tolist()[0])
country_install_base[39] = intx(df2['Install base (All devices, Unique devices, Per interval, Daily): India'].tolist()[0])
country_install_base[40] = intx(df5['Install base (All devices, Unique devices, Per interval, Daily): Latvia'].tolist()[0])
country_install_base[41] = intx(df5['Install base (All devices, Unique devices, Per interval, Daily): Estonia'].tolist()[0])
country_install_base[42] = intx(df5['Install base (All devices, Unique devices, Per interval, Daily): Lithuania'].tolist()[0])
country_install_base[43] = intx(df5['Install base (All devices, Unique devices, Per interval, Daily): Singapore'].tolist()[0])
country_install_base[44] = intx(df3['Install base (All devices, Unique devices, Per interval, Daily): Malaysia'].tolist()[0])
country_install_base[45] = intx(df7['Install base (All devices, Unique devices, Per interval, Daily): Brunei'].tolist()[0])
country_install_base[46] = intx(df3['Install base (All devices, Unique devices, Per interval, Daily): Colombia'].tolist()[0])
country_install_base[47] = intx(df3['Install base (All devices, Unique devices, Per interval, Daily): Peru'].tolist()[0])
country_install_base[48] = intx(df4['Install base (All devices, Unique devices, Per interval, Daily): Argentina'].tolist()[0])
country_install_base[49] = intx(df5['Install base (All devices, Unique devices, Per interval, Daily): Philippines'].tolist()[0])
country_install_base[50] = intx(df5['Install base (All devices, Unique devices, Per interval, Daily): Paraguay'].tolist()[0])
country_install_base[51] = intx(df7['Install base (All devices, Unique devices, Per interval, Daily): Jamaica'].tolist()[0])
country_install_base[52] = intx(df7['Install base (All devices, Unique devices, Per interval, Daily): Haiti'].tolist()[0])
country_install_base[53] = intx(df6['Install base (All devices, Unique devices, Per interval, Daily): Guatemala'].tolist()[0])
country_install_base[54] = intx(df6['Install base (All devices, Unique devices, Per interval, Daily): Bolivia'].tolist()[0])
country_install_base[55] = intx(df5['Install base (All devices, Unique devices, Per interval, Daily): Ecuador'].tolist()[0])
country_install_base[56] = intx(df4['Install base (All devices, Unique devices, Per interval, Daily): Chile'].tolist()[0])
country_install_base[57] = intx(df5['Install base (All devices, Unique devices, Per interval, Daily): Panama'].tolist()[0])
country_install_base[58] = intx(df5['Install base (All devices, Unique devices, Per interval, Daily): Nicaragua'].tolist()[0])
country_install_base[59] = intx(df6['Install base (All devices, Unique devices, Per interval, Daily): Puerto Rico'].tolist()[0])
country_install_base[60] = intx(df6['Install base (All devices, Unique devices, Per interval, Daily): Costa Rica'].tolist()[0])
country_install_base[61] = intx(df7['Install base (All devices, Unique devices, Per interval, Daily): Barbados'].tolist()[0])
country_install_base[62] = intx(df6['Install base (All devices, Unique devices, Per interval, Daily): Uruguay'].tolist()[0])
country_install_base[63] = intx(df7['Install base (All devices, Unique devices, Per interval, Daily): Dominican Republic'].tolist()[0])
country_install_base[64] = intx(df6['Install base (All devices, Unique devices, Per interval, Daily): El Salvador'].tolist()[0])
country_install_base[65] = intx(df2['Install base (All devices, Unique devices, Per interval, Daily): Egypt'].tolist()[0])
country_install_base[66] = intx(df3['Install base (All devices, Unique devices, Per interval, Daily): Morocco'].tolist()[0])
country_install_base[67] = intx(df3['Install base (All devices, Unique devices, Per interval, Daily): Tunisia'].tolist()[0])
country_install_base[68] = intx(df4['Install base (All devices, Unique devices, Per interval, Daily): Jordan'].tolist()[0])
country_install_base[69] = intx(df3['Install base (All devices, Unique devices, Per interval, Daily): Saudi Arabia'].tolist()[0])
country_install_base[70] = intx(df6['Install base (All devices, Unique devices, Per interval, Daily): United Arab Emirates'].tolist()[0])
country_install_base[71] = intx(df7['Install base (All devices, Unique devices, Per interval, Daily): Qatar'].tolist()[0])
country_install_base[72] = intx(df6['Install base (All devices, Unique devices, Per interval, Daily): Kuwait'].tolist()[0])
country_install_base[73] = intx(df0 ['Install base (All devices, Unique devices, Per interval, Daily): All countries / regions'].tolist()[0])


print(country_install_base)

countries_main = ["US",
"Germany",
"Austria",
"Japan",
"Canada",
"France",
"Switzerland",
"South Korea",
"Netherlands",
"UK",
"Belgium",
"Italy",
"Brazil",
"Taiwan",
"Hong Kong",
"Denmark",
"Sweden",
"Finland",
"Australia",
"Spain",
"Poland",
"Mexico",
"Czech Republic",
"Slovakia",
"Thailand",
"Hungary",
"Ireland",
"New Zealand",
"Indonesia",
"Viet nam",
"Norway",
"Croatia",
"Luxembourg",
"Israel",
"Greece",
"South Africa",
"Russia",
"Portugal",
"Romania",
"India",
"Latvia",
"Estonia",
"Lithuania",
"Singapore",
"Malaysia",
"Brunei",
"Colombia",
"Peru",
"Argentina",
"Philippinnes",
"Paraguay",
"Jamaica",
"Haiti",
"Guatemala",
"Bolivia",
"Ecuador",
"Chile",
"Panama",
"Nicaragua",
"Puerto Rico",
"Costa Rica",
"Barbados",
"Uruguay",
"Dominican R.",
"El Salvador",
"Egypt",
"Morocco",
"Tunisia",
"Jordan",
"Saudi Arabia",
"UAE",
"Qatar",
"Kuwait",
"All Countries"]
df = pd.DataFrame({
    'Countries': countries_main,
    'Install Base': country_install_base
})

writer = pd.ExcelWriter('install-data.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Ads', index=False)
writer.save()