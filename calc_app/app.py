import streamlit as st
import pandas as pd

# Cargar datos desde el archivo CSV local
@st.cache_data
def load_house_data():
    try:
        houses = pd.read_csv('dict_data.csv')
        houses['fecha'] = houses['fecha'].astype(int)
        houses['SalePrice'] = houses['SalePrice'].astype(int)
        return houses
    except FileNotFoundError:
        st.error("Error: No se encontró el archivo 'dict_data.csv'. Asegúrate de que esté en la misma carpeta que esta aplicación.")
        return pd.DataFrame()

# Cargar los datos
houses = load_house_data()

COL = {
    1989: 26.82,
    1990: 29.12,
    1991: 26.79,
    1992: 25.12,
    1993: 22.60,
    1994: 22.58,
    1995: 19.50,
    1996: 21.63,
    1997: 17.68,
    1998: 16.70,
    1999: 9.23,
    2000: 8.75,
    2001: 7.65,
    2002: 6.99,
    2003: 6.49,
    2004: 5.99,
    2005: 4.85,
    2006: 4.48,
    2007: 5.69,
    2008: 7.67,
    2009: 2.00,
    2010: 3.17,
    2011: 3.73,
    2012: 2.44,
    2013: 1.94,
    2014: 3.66,
    2015: 6.77,
    2016: 5.75,
    2017: 4.09,
    2018: 3.18,
    2019: 3.80,
    2020: 1.61,
    2021: 5.62,
    2022: 13.12,
    2023: 10.77
}

USA = {
    1989: 4.8,
    1990: 5.4,
    1991: 4.2,
    1992: 3.0,
    1993: 3.0,
    1994: 2.6,
    1995: 2.8,
    1996: 3.0,
    1997: 2.3,
    1998: 1.6,
    1999: 2.2,
    2000: 3.4,
    2001: 2.8,
    2002: 1.6,
    2003: 2.3,
    2004: 2.7,
    2005: 3.4,
    2006: 3.2,
    2007: 2.8,
    2008: 3.8,
    2009: -0.4,
    2010: 1.6,
    2011: 3.2,
    2012: 2.1,
    2013: 1.5,
    2014: 1.6,
    2015: 0.1,
    2016: 1.3,
    2017: 2.1,
    2018: 2.4,
    2019: 1.8,
    2020: 1.4,
    2021: 7.0,
    2022: 6.5,
    2023: 3.4
}


def calculate_value(year, country, amount):
    '''Calculate the value of the money today
    from a given year and country using the inflation rate
    for each year until 2023'''
    if country == 'USD':
        while year <= 2023:
            amount *= (1 + USA[year] / 100)
            year += 1
    elif country == 'COP':
        while year <= 2023:
            amount *= (1 + COL[year] / 100)
            year += 1
    return amount


def main():
    st.title('Inflation Calculator')
    st.write('- This app calculates the current value of an amount of money in a given year ')
    st.write('- The data is based on the inflation rate of Colombia and the USA')
    st.write('- The available years are from 1989 to 2023')
    st.write('                                                         ')
    
    country = st.selectbox('Currency', ['USD', 'COP'])
    year = st.select_slider('Year', options=list(range(1989, 2024)))
    amount = st.number_input('Amount', min_value=0, value=1000, step=500)
    
    if st.button('Calculate'):
        result = calculate_value(year, country, amount)
        st.write(f'{amount} from {year} is equivalent to {result:.2f} {country} in 2023')
    
    st.title('Current value of a property')
    st.write('- This app uses DreamHouses dataset to show the current value of a property based on the year of purchase')
    st.write('- We have real state properties. The prices are in USD')
    
    if not houses.empty:
        st.write(f'Total properties available: {len(houses)}')
        max_id = len(houses) - 1
        id_house = st.number_input('Property ID', min_value=0, max_value=max_id, value=None, placeholder='Enter a property ID from 0 to {}'.format(max_id))
        
        if st.button('Search'):
            id_house = int(id_house)
            fecha = houses.iloc[id_house]['fecha']
            monto = houses.iloc[id_house]['SalePrice']
            result = calculate_value(fecha, 'USD', monto)
            st.write(f'Property with ID: {id_house} was bought in {fecha} for {monto} USD')
            st.write(f'The current value is {int(result)} USD')
    else:
        st.warning("No hay datos de propiedades disponibles. Asegúrate de que el archivo 'dict_data.csv' esté en la misma carpeta.")


if __name__ == '__main__':
    main()
