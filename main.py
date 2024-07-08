import streamlit as st

# st.title("Hi.Shoeb Raza")
# st.header("python")
# st.subheader("Java")
# st.markdown("Feature engineering is the process that takes raw data and transforms it into features that can be used "
#             "to create a predictive model using machine learning or statistical modeling, such as deep learning.")
# code = ''' def swapList(NewList):  # Swap function
#     size = len(NewList)
#
#     temp = NewList[0]  # applying the logic of this code..! # Swapping
#     NewList[0] = NewList[size - 1]
#     NewList[size - 1] = temp
#     return NewList
#
#
# NewList = [12, 35, 9, 56, 24]
#
# # function calling
# print((swapList(NewList))) '''
# st.code(code,language='python')
# st.code('''for i in range(1,5,1):
#             print(i)''')
# dataset = pd.read_csv("ipl-matches.csv")
# st.dataframe(dataset)

name = st.text_input("Enter Your Name : ")
father_name = st.text_input("Enter Your Father Name : ")

addr = st.text_area("Enter Your Text.......... : ")
class_data = st.selectbox("Enter Your Class : ", (1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12))

button = st.button("Done")
if button:
    st.markdown(f"""
    Name : {name},
    Father : {father_name},
    address : {addr},
    class : {class_data}""")
