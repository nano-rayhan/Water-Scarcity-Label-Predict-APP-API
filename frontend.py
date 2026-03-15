import streamlit as st
import requests
import pandas as pd

country_list = [
"Afghanistan","Albania","Algeria","Andorra","Angola","Antigua and Barbuda",
"Argentina","Armenia","Australia","Austria","Azerbaijan",
"Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bhutan","Bolivia",
"Bosnia and Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina Faso","Burundi",
"Cabo Verde","Cambodia","Cameroon","Canada","Central African Republic","Chad","Chile","China","Colombia","Comoros",
"Congo (Congo-Brazzaville)","Costa Rica","Croatia","Cuba","Cyprus","Czechia",
"Democratic Republic of the Congo","Denmark","Djibouti","Dominica","Dominican Republic",
"Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Eswatini","Ethiopia",
"Fiji","Finland","France",
"Gabon","Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guinea-Bissau","Guyana",
"Haiti","Honduras","Hungary",
"Iceland","India","Indonesia","Iran","Iraq","Ireland","Israel","Italy",
"Jamaica","Japan","Jordan",
"Kazakhstan","Kenya","Kiribati","Kuwait","Kyrgyzstan",
"Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg",
"Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Micronesia","Moldova","Monaco","Mongolia","Montenegro","Morocco","Mozambique","Myanmar",
"Namibia","Nauru","Nepal","Netherlands","New Zealand","Nicaragua","Niger","Nigeria","North Korea","North Macedonia","Norway",
"Oman",
"Pakistan","Palau","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal",
"Qatar",
"Romania","Russia","Rwanda",
"Saint Kitts and Nevis","Saint Lucia","Saint Vincent and the Grenadines","Samoa","San Marino","Sao Tome and Principe",
"Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia",
"South Africa","South Korea","South Sudan","Spain","Sri Lanka","Sudan","Suriname","Sweden","Switzerland","Syria",
"Tajikistan","Tanzania","Thailand","Timor-Leste","Togo","Tonga","Trinidad and Tobago","Tunisia","Turkey","Turkmenistan","Tuvalu",
"Uganda","Ukraine","United Arab Emirates","United Kingdom","United States","Uruguay","Uzbekistan",
"Vanuatu","Vatican City","Venezuela","Vietnam",
"Yemen",
"Zambia","Zimbabwe"
]
API_URL = 'https://water-scarcity-label-predict-app-api.onrender.com/predict'

st.title('Water Scarcity Level App')
st.markdown('Enter the details below')


country = country = st.selectbox(
    "Country",
    options=country_list,
    index=None,
    placeholder="Type country name..."
)
year = st.number_input("Year", min_value=1900, max_value=2100,step=1)
total_water = st.number_input("Total Water Consumption (Billion m3)", min_value=0.0, step=0.1)
per_capital = st.number_input("Per Capita Water Use (L/Day)", min_value=0.0, step=1.0)
agricultural = st.slider("Agricultural Water Use (%)", 0, 100, 50)
industrial = st.slider("Industrial Water Use (%)", 0, 100, 30)
household = st.slider("Household Water Use (%)", 0, 100, 20)
rainfall = st.number_input("Rainfall Impact (mm)", min_value=0.0, step=1.0)
groundwater = st.slider("Groundwater Depletion Rate (%)", 0.0, 10.0, step=0.01)
    
submitted = st.button("Submit")


if submitted:
    data = {
        "country": country,
        "year": year,
        "total_water": total_water,
        "per_capital": per_capital,
        "agricultural": agricultural,
        "industrial": industrial,
        "household": household,
        "rainfall": rainfall,
        "groundwater": groundwater
    }
    

    try:

        response = requests.post(API_URL, json=data)
        if response.status_code ==200:
            result = response.json()
            st.success(f'Result: {result}')
            

        else:
            st.error(f'API Error: {response.status_code}')

    except Exception as e:
        st.error(f'API call failed: {e}')
    