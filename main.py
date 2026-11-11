import json,os,urllib.request as u
V=[0,100,320,330,500,900]
CP,CA=1<<17,1<<19
D=[(33,31,18,14,-14,-18,-31,-33),(15,17,-15,-17),(1,-1,16,-16),(1,-1,16,-16,15,17,-15,-17)]
M=1e5;ND=120e3;F="abcdefgh"
KP=[15]*128
KP[0]=13;KP[7]=14;KP[4]=12;KP[112]=7;KP[119]=11;KP[116]=3
B=[0]*256;S=1;C=0;W=4;X=116;U=[];N=0;L=0;A=0;BM=0;K=[0]*512
SQ=[s for s in range(128)if not s&0x88]
def a(s,y):
 if y in(B[s-15*y],B[s-17*y]):return 1
 for d,v in((D[0],2),(D[3],6)):
  for q in d:
   if B[s+q]==v*y:return 1
 for t in(3,4):
  for d in D[min(t,5)-2]:
   v=s+d
   while not v&0x88:
    p=B[v]
    if p:
     if p in(t*y,5*y):return 1
     break
    v+=d
 return 0
def g(o=False):
 w=[]
 for s in SQ:
  p=B[s]
  if p==0 or(p>0)!=(S>0):continue
  t=abs(p)
  if t==1:
   d=16*S;l=(6,1)[S<0];r=s>>4;n=s+d
   if B[n]==0:
    if r==l:
     for q in(5,4,3,2):w.append(s|n<<7|q<<14)
    elif not o:
     w.append(s|n<<7)
     if r==(1,6)[S<0]and B[n+d]==0:w.append(s|(n+d)<<7)
   for dd in(d-1,d+1):
    v=s+dd
    if v&0x88:continue
    k=B[v]
    if k and(k>0)!=(S>0):
     if r==l:
      for q in(5,4,3,2):w.append(s|v<<7|q<<14|CP)
     else:w.append(s|v<<7|CP)
   continue
  for d in D[min(t,5)-2]:
   v=s+d
   while not v&0x88:
    k=B[v]
    if k:
     if(k>0)!=(S>0):w.append(s|v<<7|CP)
     break
    if not o:w.append(s|v<<7)
    if t in(2,6):break
    v+=d
  if t==6 and not o:_c(w,s)
 return w
def _c(w,k):
 b=0 if S>0 else 112
 if a(k,-S):return
 for q,tt,ee,aa in((1,6,(5,6),(5,6)),(2,2,(1,2,3),(2,3))):
  if C&(q*4 if S<0 else q) and all(B[b+x]==0 for x in ee)and all(not a(b+x,-S)for x in aa):w.append(k|(b+tt)<<7|CA)
def m(n):
 global S,C,W,X
 fr=n&127;to=n>>7&127;pr=n>>14&7;p=B[fr];cp=B[to]
 U.append((n,cp,C,W,X))
 B[fr]=0;B[to]=(pr if pr else abs(p))*S
 if abs(p)==6:W,X=(to,X)if S>0 else(W,to)
 if n&CA:
  rf=fr+3 if to>fr else fr-4;rt=fr+1 if to>fr else fr-1;B[rt]=B[rf];B[rf]=0
 C&=KP[fr]&KP[to]
 S=-S
 if a(W if S<0 else X,S):v();return False
 return True
def v():
 global S,C,W,X
 n,cp,c0,w0,x0=U.pop();fr=n&127;to=n>>7&127;pr=n>>14&7
 S=-S;pl=B[to];p=(1 if pr else abs(pl))*S;B[fr]=p;B[to]=0
 if n&CA:
  rf=fr+3 if to>fr else fr-4;rt=fr+1 if to>fr else fr-1;B[rf]=B[rt];B[rt]=0
 if cp:B[to]=cp
 C,W,X=c0,w0,x0
def e():
 s=0
 for sq in SQ:
  p=B[sq]
  if not p:continue
  t=abs(p);r=sq>>4;f=sq&7
  if t==6:
   s+=(7-r)*3 if p>0 else -r*3
   continue
  c=min(f,7-f)+min(r,7-r)
  if t==1:v=100+[0,0,6,12,24,40,70][r if p>0 else 7-r]
  else:v=V[t]+3*c-4
  s+=v if p>0 else-v
 return s if S>0 else-s
def o(w,p):
 def k(n):
  s=0
  if n&CP:s=100000+V[abs(B[n>>7&127])]
  elif n==K[p]:s=90000
  return-s
 w.sort(key=k);return w
def s(d,x,y,p):
 global N,A,BM
 N+=1
 if L and N>L:A=1;return 0
 if d<=0:
  c=a(W if S>0 else X,-S);bs=-M-1
  if not c:
   st=e()
   if st>=y:return st
   bs=st
   if st>x:x=st
  for n in o(g(not c),p):
   if not m(n):continue
   sc=-s(0,-y,-x,p+1);v()
   if A:return 0
   if sc>bs:bs=sc
   if sc>=y:return sc
   if sc>x:x=sc
  return bs
 w=o(g(),p);lg=0;bs=-M-1;bm=0
 for n in w:
  if not m(n):continue
  lg+=1;sc=-s(d-1,-y,-x,p+1);v()
  if A:return 0
  if sc>bs or not bm:bs=sc;bm=n
  if sc>x:x=sc
  if x>=y:
   if not(n&CP):K[p]=n
   break
 if lg==0:return-M+p if a(W if S>0 else X,-S)else 0
 if p==0 and bm:BM=bm;K[0]=bm
 return bs
def R():
 global N,A,L
 N=0;A=0
 for d in range(1,65):
  L=0 if d==1 else ND;sc=s(d,-M-1,M+1,0)
  if A or sc>=M-100:break
 return BM
def y(n):return F[n&7]+str((n>>4&7)+1)+F[n>>7&7]+str((n>>11&7)+1)+("nbrq"[((n>>14)&7)-2]if(n>>14)&7 else"")
def w(mv):
 global S,C,W,X
 B[:]=[0]*256
 for i,p in enumerate((4,2,3,5,6,3,2,4)):B[i]=p;B[i+16]=1;B[112+i]=-p;B[96+i]=-1
 S=1;C=15;W=4;X=116
 for k in mv:
  for n in g():
   if y(n)==k:m(n);break
  else:
   fr=(ord(k[0])-97)+(int(k[1])-1)*16;to=(ord(k[2])-97)+(int(k[3])-1)*16;B[to]=B[fr];B[fr]=0;B[to-16*S]=0;S=-S
EU=os.getenv("MAKEFUN_ENV_URL")
def po(p,b):return json.load(u.urlopen(EU+p,json.dumps(b).encode()))
def main():
 while 1:
  g=po("/game",{})
  if g["status"][0]=="d":break
  while g["status"][0]=="y":
   w(g["moves"]);g=po("/move",{"game":g["game"],"move":y(R())})
main()
