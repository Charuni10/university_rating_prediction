import streamlit as st
import pandas as pd
import pickle
import typeconv as tp

model = pickle.load(open('uni_model.pkl','rb'))

@st.cache(allow_output_mutation=True)
def uni_data(filepath):
    data = pd.read_csv(filepath)
    return data
    
    
def new_dataframe(new_data):
    uni=pd.DataFrame(new_data,columns=['GRE_Score','TOEFL_Score','SOP','Research','CGPA'])
    return uni

header_content = st.container()
dataset_descrb = st.container()
prediction = st.container()


with header_content:
    st.title('This is my data science project :smile:')
    first_para = '<p style="font-family: Georgia; color:Black; font-size: 20px;">This project is about prediciting the university rating with the help of GRE Scores,TOEFL Scores,Research experience,Statement of purpose strength,CGPA of UG.Let us try to predict it!</p>'
    st.markdown(first_para, unsafe_allow_html=True)

    st.header('Objective:')
    st.text('To predict the rating of a university. ')

with dataset_descrb:
    st.header('*University Rating dataset*')
    second_para = '<p style="font-family:Georgia; color:Black; font-size: 20px;">Lets see the insights of the dataset by visualizing the dataset...</p>'
    st.markdown(second_para, unsafe_allow_html=True)
    df = uni_data("uni.csv")
    uni_data = ['CGPA','University_Rating']
    features = df[uni_data]
    d=features.head(100)
    st.line_chart(d)
    load_data1= ['University_Rating','GRE_Score']
    features = df[load_data1]
    d2=features.head(100)
    st.line_chart(d2)
    with st.expander("See explanation"):
     st.write("""
         The visuals here is derived using the below given data set...
     """)
     st.dataframe(df)

with prediction:
    st.header(""" Let's predict the University Rating""")
    third_para = '<p style="font-family:Georgia; color:Black; font-size: 20px;">Enter the values below to find out the university rating</p>'
    st.markdown(third_para, unsafe_allow_html=True)
    a, b = st.columns(2)
    CGPA = a.text_input('Enter your CGPA(0-10):',1)
    CGPA= float(CGPA)
    GRE_Score= b.text_input('Enter your GRE Scores(0-340):', 0)
    GRE_Score= int(GRE_Score)
    TOEFL_Score = a.text_input('Enter your TOEFL Scores(0-120):', 0)
    TOEFL_Score = int(TOEFL_Score)
    Research= b.selectbox("Whether you have research experience or not",('Yes', 'No'))
    SOP= a.text_input('Enter your statement of purpose rating(0-5):',1)
    SOP= float(SOP)
    new_data = [[GRE_Score,TOEFL_Score,SOP,Research,CGPA]]
    new_df1=new_dataframe(new_data)
    new_data_after_typeconv = tp.typeconv(new_df1)
    
    predict_value = model.predict(new_data_after_typeconv )
    
    result = st.button("Predict")
   
    if result:
        if predict_value == 1:
            st.subheader('The rating of the university is 1')
        elif predict_value == 2:
            st.subheader('The rating of the university is 2')
        elif predict_value == 3:
            st.subheader('The rating of the university is 3')
        elif predict_value == 4:
            st.subheader('The rating of the university is 4')
        else:
            st.subheader('The rating of the university is 5')
    
        