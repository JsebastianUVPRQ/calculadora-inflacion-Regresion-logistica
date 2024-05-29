# web app with streamlit
# we wanna build an inflation calculator
# the value of IPC changes every year

# the data are in COL_inflacion_anual_Dic.dat and USA_inflacion_anual_Dic.dat
# we have to read them and create a dictionary with the data

# we have to create a function that receives the year, the country
# (two options) and the amount of money
# USD and COP (colombian pesos)

# we have to return the value of the money up to date (2023)
import streamlit as st


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
    amount = st.number_input('Amount', min_value=0.0, value=0.0, step=0.1)
    
    if st.button('Calculate'):
        result = calculate_value(year, country, amount)
        st.write(f'{amount} from {year} is equivalent to {result:.2f} {country} in 2023')
    
    st.title('Current value of a property')
    st.write('- This app use de DreamHouse data to show the current value of a property based on the year of purchase')
    st.write('- We have 4124 real state properties. The prices are in USD')
    
    house = st.number_input('House ID', min_value=0, max_value=4124, value=0, step=1)


if __name__ == '__main__':
    main()

