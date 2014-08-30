'''
Created on Dec 26, 2011

@author: oo
'''
st='oskar hakan olsson'
st1=st.find('a')
print st1

st1=st.find('aka')
print st1

st1=st.replace('hakan', 'kung')
print st1

st1=st.split(' ')
print st1

st1=st.upper()
print st1

st1=st.rstrip()
print st1

st1=dir(st)
print st1

st1=help(st.rstrip)
print st1
print '----------------------'
st2='oo\nmm\tyy'
print st2