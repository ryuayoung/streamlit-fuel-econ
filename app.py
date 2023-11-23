import streamlit as st

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

def main() :

    st.title('자동차 데이터 분석')
    
    df = pd.read_csv('./data/fuel_econ.csv') # 파일 가져오기

    # 체크박스 생성 # if => 체크박스가 체크 되었을 때~
    if st.checkbox('데이터 프레임 보기') :
            st.dataframe( df )
    else :
         st.text('')

    st.text('컬럼을 선택하면, 중복제거한 데이터의 갯수를 보여줍니다.')

    choice = st.selectbox('컬럼선택',df.columns)

    count = df[choice].nunique()
    
    # {} => choice라는 변수로 바꾼다
    st.text( '{}컬럼의 중복제거한 데이터의 갯수는 {}개 입니다.'.format(choice, count) )

    # 유저가 두개의 컬럼을 선택하게끔
    seleced_list = st.multiselect('두개의 컬럼을 선택하세요', df.columns[ 8 : ] , max_selections= 2 )

    # if 리스트가 2개 일때!
    if len(seleced_list) == 2 :
        fig = plt.figure()
        plt.scatter( data= df, x = seleced_list[0] , y = seleced_list[1] )
        plt.title( seleced_list[0] + 'Vs' + seleced_list[1] )
        plt.xlabel( seleced_list[0] )
        plt.ylabel( seleced_list[1] )
        st.pyplot(fig)

        st.text('상관계수')

        st.dataframe( df[ seleced_list ].corr() )
        
if __name__ == '__main__':
    main()