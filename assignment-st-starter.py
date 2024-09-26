# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# show the title
st.title('Titanic App By Yachen Xu')


# read csv and show the dataframe
df = pd.read_csv('train.csv')
st.dataframe(df)

# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

sns.boxplot(x='Pclass', y='Fare', data=df_train[df_train['Pclass'] == 1], ax=axes[0])
sns.boxplot(x='Pclass', y='Fare', data=df_train[df_train['Pclass'] == 2], ax=axes[1])
sns.boxplot(x='Pclass', y='Fare', data=df_train[df_train['Pclass'] == 3], ax=axes[2])

axes[0].set_title('Ticket Price for Pclass 1',fontsize=16)
axes[0].set_xlabel('PClass',fontsize=12)
axes[0].set_ylabel('Fare',fontsize=12)

axes[1].set_title('Ticket Price for Pclass 2',fontsize=16)
axes[1].set_xlabel('PClass',fontsize=12)
axes[1].set_ylabel('Fare',fontsize=12)

axes[2].set_title('Ticket Price for Pclass 3',fontsize=16)
axes[2].set_xlabel('PClass',fontsize=12)
axes[2].set_ylabel('Fare',fontsize=12)

plt.tight_layout()
plt.show()

