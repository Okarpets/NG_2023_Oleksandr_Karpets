import re
lstuser = input('Write your lst:\n')
without = re.sub("[B,b,C,c,D,d,F,f,G,g,H,h,J,j,K,k,L,l,M,m,N,n,P,p,Q,q,R,r,S,s,T,t,V,v,W,w,X,x,Y,y,Z,z]", "", lstuser)
print("It's your list without consonants vowels: {}". format(without))