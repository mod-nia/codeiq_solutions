#!/usr/bin/python3
#Using Python3 and very careful implementation, we can embed full CIDR file...
import base64,lzma
def d(s):
	r=0
	for e in s.split('.'):r=r<<8|int(e)
	return r
def f(s):
	x,y=s.decode('utf-8').split('/')
	y=int(y)
	return d(x)>>y==n>>y

n=d(input())
#<jp.txt lzma -c9|zbase85rfc|pbcopy
print(int(any(f(e) for e in lzma.LZMADecompressor().decompress(base64.b85decode('''
T>t<80ssI1|NsC0{{R?^f@NZHI|~zS*AV7?b5QoUIH)=_^P{opAzG6f^{34sp^nHTrTv654^k;)&WR$C%apN%?~6KZWM9E^1Z@bK<1H%^vahNJ4kNppnLnmT;8)p)0BUk%22=!Ta@KXSR&%e4;(urtsf*rh)>}
afiZsF2QrYN|;5nUGMuav#XY7`_%xch>%m!|cC=0qKl2byNj|>(~PFofcQ>r*NpuW2>{<ch}Rx~${?zssCn?~p<I1?LP#WS^$(r)%+g=X4O7nC_jHn@tQs~7(rRTz(!)hJGAP=k_JIaoHwi%fr_$=}a`)$v>yv
IP3D0uC+dlFpRxX~dcUrMgXx$gpGYr~UYiei-7bENW20XUEthRs#TBx@rS7D<RUh1}?2}&g_snnC(1Ij@z5*Y7K(?xM!$bx))%>M+U_bGT3!UWb^dr{izB`ZV2>PI$sBXTRQVa1B$>iFZZ-HMJLPUc9F_RHm{0
)0uPQ6Il|0<`$7Ahq?0F~R*ZmKtJ0YTlIlCEw4-O0|H7H4eIeZlY^QUECR}6ov;~ZmQq_>`%S25QVw-!*yZIId{%ab?Up%E&y|1zyr^&xRJ3=l?FHxf*Bm_n`0&X~U0tFnX&5;Q(fGKI{_khE&rki59o}A(RB~
I+OC{-ZYoI!;v>2x;|h8|Z1K9$)%zG8bUP>FDEo3<x+N|9x|i0YRu$T}GK%#=AZgFZ~wa<y{|JP{W~(}x=c<YGB6cdgnm58~aU_PlI)Bba?>#2uXkGeN~IbFx_KSrZEBQo-6~KniD{DR4(y;|&AA%!b6t{KQVq
3T6E_{I$T!%B<$>7wqfWV3weg<L2R&PdKNE-s~-|RC3IkD2q15&wN%PgPfu3GBt4CIHbax@VCFixTRpMd=B>Rk39}7DyV5!Li20<%d?nAKs}}7S*qXHFwn`cdA{H5*x~7Ny|4>^^GUaCVN~xd#KK-DYgRS|l?j
Eb*2=u33!>n)TGEuikZWtQ!#tC`p9n}J;zQgERO_MqAw{^gV^y-D)HN+E(aN<eiu`Q1tp3HnB*2Ek5j`c9b1!`_jx#*GQIf`=7u0{nCNc(fg#aIAro9U-Z?{a*5b1>+y1-9J?;e6@obyjI$>#KD5uiUB$7oOEq
Vf68+3_~S&%rP>qKKUQg12Yd8X|j2v%v{-0><$3ho;_!0X@fXq?;$d{xYm1!ds(;!F2vOxFeV&6J|q&cFxs{m;ye_;vW;&WZ60<rJe|D42T!0odX2^U!e_K5k~w*Pq^b;QXj$km#Kg-x;{Q|jvwPZ`)+we&G1`
DY<TSEp-%$MU93l%xF#8n;Q_%TwC@P*NfvEg{C3K;c+^s?Ev{EY*rrxws2w!UI*JF-*B}wRPudyX8LbsN4w(6rc}5F@`Am&z?q}2$nt2&kj>EyVh(O%)DBqryZn0^2rYB^^Y-+C@kER~GZ+y;;#?T=+{(%<&f3
N;LKUltU^%`fOS@5?K1(YREk0aY6zSEpb-EieVBAIR7EXt{+f8EPMW{Bk+zU-vS-HVik|L<*#)9n9R{i!gH(oDTS5$w@p>?kjSNMI3jOUG}q7V|teAxav*Vu}hWF<8?Noycx9lq!ysCQofI4kL1WvIX>;%*&}>
rJL?1SKI<aR_p;t3c6lbtqJT6fe39prHuxAH>wsk%fEBH(_QBytH<mFZTWV-2pu#g1|m|(FSDUbF}Dz+wy!m>e`X7SU+9zfWH#%qymuG2SiP=YX8^X&&n@Xt7fTy>vZPpmDmH0npKcwklv-hq_R8nut)jGK;e>
j!pa%lTXWps<-AZfUj28zhOmm=+kPi2-DId01xIk4jA$37Ds!r~4V~TqCSPA9->M@>f-w0hU8|#-*9c=7>`4t&%+yH~j;OsYAIYG0hf3!&MJ;TPlj5mI$Q)MzK_?!XFJ4S6kuq=5iylwH`5L>RYe0Chj-_U%ad
1LFtMgmLh53S=GWJ^EhPC{5;HA>j6f(V~ipz+#|AigMhU|CtueB0XvXu6-DgvYX9&D+v8F7fhp;Hr_Q*pK=*T}@S}`%M7NJf(YWEpdE`yXm^DCww_JNp2epMu?fN9becH+zvt;ecS<{qzz>eZRDilL(9OQBnGO
8ay`qBfu;iX<8jj`X_f-L9xMr8_Z{0MG`o8opsRbgdBJNORIwQm|69Gate1(W3#>>i4>C0f1#WCw3d;X!Z{OdQ(^Z}Yd+B++0{z8DpI84ZD{w=N3tTa|r-C<jka}uWg^7IEYTqieo$cYu-#B{$VVY&~BGM*JW4
IEQQZYr3SOQAuo6)WUu+xK!`0sCllIux!?osjl{LAikrFJ9JW&nnCnOY*L2#O-km>dv1RQ@)DN1lneXOugl)&|v+x}itUNo{p_v@Ggj@Q@1PCPGE-9mgI*NKAteZQsx6sPHhk|9-cSClM&77oPM?*+s;0?)lKo
Wy6nv?dm|t5sMk0>@w)$cfthRJJSK>{4x`BV_#APU8fR+F#ZULN_KQY#4!ogU(Uc{N-JT2(5BW}F@ZqtZ8<-WBRX?^S}G-i-KUICJb~rr1PFpC`~?lu=o+kA5R5tWK58FuL;>IU%~F)b-jpU`{En#&!~kUyR#>
Mc7e<TBKQa9$U%TW`E-YdLoJdVg%j8D2JXf@iX$M|gcvYU&5e~``D1XrQf&+=?#zouN1|PjZVGF;u5Q`AVfyvxwHhdK@3@@8k_Aaf3$6+0~{Mm=IAev|Hmk6|Ml(_cMDJ1;-93JIz#Eod7M|c0rr!SFWQCgxRA
3)gbi(Ca;_DZ#@fwoz^d~QSEZfLevbW0*{H+Yz672)|&SH)cCep$O;c3W86)A_ck7%O*Yq5n7>wN0BE-`J7|ZY-%Xx7AF`J6eTphwS*wXH98~YK;*7YrP&Qi|5lBYQiT!+L1(^&}m=c9c;L<j?>tgWX8sng&~K
!QHDn>h(65;?!L;(Z9~MsPpxYKPv=2dK1~qV@#}T+d@q035OQ8P-yIebKI4%ik~I@pSDZaVeno~rWL5w=L`zzrkaY0!n~KCudB!)Ck`ZsvP)aGZ?yn9bkFVaxd!X0!$cY0BvHUN^L|=S4H2fnq(3gNsI?-*O3x
nl)VD2{b_~^JO345SnB<-|HxAhkoB=jUvr6IV@8hIMUb&1T@TYl!%riq=@8dgZxE$d(+zzQkms@;vcG{Jg`6NgfTt?v*iIm++F_tLKnyBW7gLnS8z0rm~JtA#ph${sJT8QXNPznkyDEQ>(OCyYq?h%>;W9eL&X
7yd3EXsF#E***JpTVkmX!5H_8alVENL+d(Gy>CS0=IDWvWynUg@2d&;>e0;E&B*ZImkwKxf1{9qoctv<z+5E3p+Y*@i^d*Q3bStl)>-tEbxH0+>QQrnZZ;P(u0Ng;WjS^)W_8g+!nybaVC(tZS#Azs6e>|qwjC
?lDo8q3;=HJ^be&rAJ=H`f_46?M{H6tP?~z`+^}r=vAGJUP6vt``I}h*SiN~S^Z-NDg0)RO~8#Gzkd|Era=v=r7UW{r(M(#5nv<=LilaH-D6DksuACU9LwqHZ-y}aw)ERx%nbP<Lf*VbvK){f`3ZQu(RWqp*`R
#tH)`Vr3R8!D?r7zXFs{D@iCs?Az{r?MJrrn81-Y;16Hy&oPG?4ru__hAh)I`(;&fepX6eN@J>2XwMd*>V&}f9s5Qt`msNJQVaIEsM%To?*e_GNu#xM|pu-K#|e8pL5V44&hbIp1Nv2b4c${6Eq-<u&mKb6vGc
8(2mS>ndrX_pWh384kE;Q>If?X*r-MZ7(Uz1-p6XC`ah5Ge+BtN6y5YKZAJ9~E3`<P=4J565_GqQmqKlux9A)Sy!A7-FpeN@5MF(<(4|VXim#SCw=HZzf_aWmE=Gteh2e!f2+8jW_Bu3?8)hkP6@aIvB;M}7^c
=*A7l0vHpaBjvE)N>d$E8Q~EW1?!mxBs`B}>yE(R}JHI_>#XDP%Dj#srx959v_HN|`1_VJ&tRfZ8Y5@uHE*1^3NIiu4{t5(r<I55JM(rF{Aa4+sS^CgG0M@KQZQ*o3^?%=GrdfQLL5JlQ<(m|mZL$NHOf+=~SC
EHOFfTNAp;Dn5_F+)FF%>E16gP)8VIheQQ{E(3yj2K<biCiT{<yp<Up<i<+M&Msj+@Z||1ST9)PA^=Cq2ZDj-T^9nF)tQOqxPbN4=557`LUO{#ewLmTB=F4(VeG4>Ds*JWPgVK2q~N^i(MD)&C<@;$8<O9EyWd
6_21LwlZ#6e6BuLFI^+&|fcg!x7Pz?1+ma|cS0W0fWSlWFuT<+_`Y+HH0$6wCqr0^q6HlneE#GXdNB36IK=9!}9D@Jd`yJ8~xNk`D_@3+YzB`hD9*nv`{_Tv4|a}uUV2WC%h__7~md`eyYFxRtfHS0>G%Ypqad
~Ds#3A*3p1@&-tOrE!8{bWa~Hng5=d93qdNT47S?hS88C-Hmku-A9R@=1GKt>}_y)WnB9(y<kP-mbMQe&H=j$*B<FX8aVyh^d_2KRW9Af?YD#>lxa);Sbt3>1fkDFfEA{bB2O`-x=5gQ3{BrJZP04P!f@aO>WW
*w3AIqo(lXg0@ZuWavb_FjmA_JJ&zh}v>{5|ncO2Uq|CQ$^I4A{(mtn^sqv_L2Hqz78oQiqPgw@;w>Wh3U2kANhGhClW`_m?sBOf8dgtcKkX+9H;P2AtuN<BEsz*Bu&pWW2!6+|P;AR4L>l`SvUVmEH_fyhD97
VuSym0SQG!RY~T!}bp0|lIWi0EiLtHTtiotn1GRG0`uoH4v?K#$~Jfnw_X2LC@+WT7CBAG<19(Yu@kR|L=t=4I24Q_2#+v3%9>l1tF=2JTx(CHijFHs+0@Z|omJy>w2RL`+R%17a;H$II6GI@HB#HT2iihuVCU
A{#0+40{!8e>-#@kacdM_*Y0(^it=OHN`kP<%A8>DqiAFzE_m~=@`78r9PMT^NdwHLMnkp1T7KtK|)`l(nz_<n#|Md(v^<6wJun`*JSRfx&cI4c8QaZ4rgedS;zY}2M$I=eX%vM5oSJEQ7q&|_;-hPsaVWS9nT
Hsb^Sj*E<DxsoP1#(-q$F#HV{Nj`<fw3Z^C>k5-dpFkL}0RbUTpGY8bD2I)Epia6O$yeSLS0%L@IP&>WejqtGXiL$4aQPh4imEAF9TY8qvsNKnxImQt}DM{qGvQmoN6jXoxAP7NbTdicq(N$jnl7{>8%l#xIeQ
zGt<Am-;i)atDpRUXhb6=OBwByg$b+b;i*LNRKOc`MGa>_h#1Oukh?K(`vpEgp&D_}(?%$Dfs?66B5Bz_D>bV;z?(chLxJcS}4^cqbA3$EKa}Y_y8fx|#{-67+fp#Y$~md(xxaz1NtC!|jbmqxrKV8J|_1>g9s
f%+K9v2@}Hlt>#WodLX*XtY*tx{pd>+dm{sx6JLeh#q*4*8Y5N)bBl@&&#(bgdm|i$A0{sK4ItzvXnn@!2pT#cY^Q=GuG^xvpY<>?ai7Kz$SV~;Wxzyqz~sU|@FXN=ZI6C#RDoWftTJiy(S5(ybnZZWYyuyeM7
>&RSXBaj5kX4;Pb6N<B^-oAPbX+PjBX0Q=EhD-o6zombrM4FL~cu}bi?)bVd+He)8#!wj*I_5un45V6D?R&=yo##xsl=VH)4S=5FmI72jvveN(l%-xz`?!n=UVx0$}A8@ZhORKMX^OQ;Td9rGLMZg_x7hAJ6VK
7**Sf$!*$0z6{cb8fz5iFhmO$9~oLb!(xS(b+3*cZ+7`7L3GJkCfOZF$TWdCS$OU|vJUHzo1NbG`N)nd3*u6YgGeE{ekuR5jy*5&$h#wJZ+$>42tH|S7f}GI*n2h<*SFh5qN5tOTs<gdkuu8Ml3Ayb=X^AvoSF
KnF#X(O%laJSZZ)0^uZrq<GWj@2*rx#zXR%suS?=;Z{GfRD3hv#J@^HcJSJsk=sl-D|Z*Xpu<BEYIfs{p=kx+zs%dGh-@{<5sE9hvJd7WHB3U7vt>59pcnTcffp<^Y4jS*V8<(HZwmua%wc;|*ah9r_+cvei?`
Zx66RS2VwKC9^0P@A$8RM99&5Ncrr8NT?zA*|yI+TUN2B)aV`k=7Y?&F0BdhF8B!VRR)!!I1S1Qyfp-WvLVVn~DEk#zG`B1?u!a+qBI1RDC4ESk;<#DMQjaG}tFK858K{vQz9gGzSQCWDZDRy1IXa0N+!{sHy~
-A2cq6!M9SNw?q9D-D3Atc=bv&`(AHnz=|QwBQ#0m0Dqw-2@dj_V_s?rv_1r{{1(6N_2L$dLpW{a+5P+H-q9%|)Ow)47MI%2W7quP1TY?3(Baaz^K`P7%lxc1i3bs|y#Qob{fWmqEFG&w-89<6%u_Po@@<)gF!
~=bMg*db)xs3>aQ)&XvBWu?ZVI_@&9(u`GQrf`M}0C69ZULeV)~x+ByLK}zC>lak|_dpx|!<u%=isIC?Kz=?D&{~L#fb_<%FJB^|<E(kWlGVLx3z_4olg%_vpl8UcKwCS2990FX`QNvW<eeEN~usDLK{jMboD=
ODoxdN^DeupwRj!P9cZG|M?<HSh1bwvHXGWa<EiGatonV5adg|N?qa4Gw+4X?W;zHRXX^4fF#T3vWQoloDHbv4rsYz)A4^bqQSs%EL;m0o=uN8-m)!I=Hbhe?>IBuCg6|vEf_Z=C3p!iY1Dgh^tD}Npfik=bjD
wwjE4e2$Jha2Kp3BwDS?+VQ*rrGWqM&UkIdEaLEI{8wsuEXt8>b0>x4?SyE-<nqvvAXhVR2vAZC%fXxAOvWS7{$#CxqHvfx|yso9N(EI;IadqKR_`TI|e?kTq;Obayy444hxuwgwpc&PEA&z1hjHV&elpX7d+i
3R6=%(m5z$}e8egJX*zbzlp+*g_M%S$YOn8+njjEB^IQrJ6qrh!rjR1`0r9nah#T4oXSF&WCb&K0y2s68q_mj_*G<%AnGcD{eZEatbTf8qzD$Q*z}I=Bo)Fd<D?wY@nT{AFT0bYaidtbCwg&4ybx>?SWe@x;+`
LL9yb!!+e3vHeYCRXhksDV#{TzFLiH76@}T{PF=BRch~O-tq6O&c1Q%so#yoBA?%X*?`!sfL7UaQ-qEuRWy`#191PhBfwZ&dRc_?XMW#p$vqK+xNUowGG_)vbtH$aJSPvI-;b(e#6l{BoeHsoCpPVeD_nGBS*Q
IDIU)4l<EIJFDxn01`A@KB3q{RLW>Pw5(+}o5ZLS$Wox>)~3S)dv7=}H(}u>!CP498|0V(UUf8-snv18z^|3@>XeW^}L%AR5>UwGIM+Hv{)a&MF7tt+z&sw;pFAw}A}1AO=oF>+HZ5+#vYP<vb0N)Kvs}Ct1j{
+LO1PMg9;V0l_g1sCNM~R@05S|G_qgmeh9Ob!dIO+T64p4VX5}Kjvur?q?J2pVSC?uw$aeYlFEXq5V?}p;05kP-B~Bg9kG5Y!)GEhNwI24Fs1yf+ICuRiS*Sh@nhHF|w2K7uDzqm9f7LI7tVQtuD(mDACs7aWE
ZJdXfy~r99&o3#a0xUMoUtq)Zz^Cmm$#d@Qt@M(`{}L%v>iGqYUTM{z4qrd^8!VYyUOaS`3CJOLL%unc=QD%<%n`oIh%5dtIMe)p)Vn^&GEPzZc*c|WFPDU&Kgp&8TpGWMxsyt2#dw8G!mwiT$GVFOr}rE05AQ
QjpwIkRr^BMy(6sUA}p@SCbtP|5CNWC&!3ZX-;SjkQRg7qd}~o6H}5nbd6h&EO(7V^AVx_xIiixT&#A^IYA|D_Be_iivC9^JWji?%G~^^#a&Z=ab&qE2D3Nq-$B{+Dco6aD5)>X5BL{ZoKzYzAGeaAl!`nZ521
kpL!jh4(VrZ!7X#!K}-JGZvvTTM@!rc+($GaaSg9YP4zDNniUy@QZ0|-2j#3Fjkm@59=A6_L6E2C+%k@$@J2P)Sqjr<X&HFhX<W=zp_L16P3F5P3US-j1gexTJgaU3W?#J+Pm55Pu}{4c(}IxcwDl8jVccHCzI
dm}>dE+WtC!$K5?3m4wPMpd(LuYCbL!*>M^iH9K>PU9cUvFbdOFhr3pEcX*O+f**by@<n)3*m-4GkWIKiYjD&!2K>>-?OHbgaj-k?uUXl9J?IUdi<x(IlFuD`pppfOSO+eR&7jTfOYy4|&<X!GJ|sGbXaA)T@5
jZeO!28DgtEH(Y+P%DF<rz@5#uZaGBo)*HXC<HfDP~z$F99%r7#sW8}xo;lFpOOY2_cdc~%=_Lk+#+p?0N!V}A&O6>2=R}{X$cbs?z9U;Di+FfMsrlp$p)Atk<H7)_yE_Aq0NY=5=*FzW`)lXLoSTolM<}80*x
NpET05<v(1^;FxwpF^<_4n$}RTBm%tFo=tNg(;Dfk)^Hqa%(x*^C0JPml9N-RQ!K{rjj@{E=8QJn}=ooyO_0fV?4d2I7q`+0du;Q9G)1i_qPTk7Rx$v*a%C#u}8P!Am^pS!b&@>29--~fJuu+@^+=p8(TZ-*%i
{`ANb{i6y5xBiK3nNU(5<}Fm4MVmoh_j@nd0w&&zL$@Ly{|WJNPb_r-iA4Vy>jL*{bfqVFOvGwMla3)XE8@99Me=J0Dfm;i8R!nvI_Tv(@M7u@k=ql>{MWaf@0x7Y!W%{w2YL60xrRp2OI^FXs4AAq(ur6a~L7
&%;V{w;NcZdh<8>lWj5X?O!`XCu+H|L(}wl_CrV6Uoq5Cg+JzA<<0m`og+6DGJ~x~h1(<P20r$pM=HD^WnXcm%UiMgB$7^b3RL5|R+KoR69w*(sd*>?<ffvYOH&%oNz7vYMIX@%)7%1@!QvlT7kF+mAptmb<zo
>Eh4b$4C-~8CZot;B0vHt(h?p?j4pAPtC#?6zkKS}vY@GlD99juH?Wzs&2u^s<0Wa1Jg;tW8Q11n8wY^;n91~;PCAGX;2`9Ltv-Y47#;*~l~9K2^@vjh;mb`lRFdGRkZRPHTWiT90O+jJ~xiTV81;6@j{k<U_e
X?`r<E4K^?v>y}bTfN*P9!5P3dPbeiWAoHy_}?_k9PEato~XZxn&ort02sq!Ot?p<qik>YtJwwjl8|dAwLzCWn68;tpBd41mb-rJldZXvtcxCrkSAHT3;sc%fDReL<H#FNt4T0t6^caYqG2&ThLzoVzn@B9e!L
d&DROq_=uQw*^nW`s!Fd<S74S6eo9w?DBI}EA92MQ2Du1|&HpbaM4V<5|>sbdw%+K%*Gl|563|7ES99t(la95@rik>T*o6d4X)sX@f_Ek>hE;yk<|KbGae`UtcA(T&fNAiVH2h#+*tlAHxZ;X01twyRr&qi_EE
7NhT32?RqL8AkfYO!Q~9VWd%K|T$K?eblZ$YN1*!P-~i`=UXkH_9yB45VXFv>ai=1f{TK*RmWg%zdK^6A}-DjI%acJHzS@HL8Ynv44CjIV>N^V<!#SmUGo4nVf`4VlJIN3bdo+n-wcw=YNVQ7zHg2bv_qcF;dl
f#i17@F+r(`;`%qougK;N#7U*QM%F97EI;?>;8Yb?oaI7NL}Gok@daWo&A(4sUGZ27TS-jjT6Hm1O<(D7K=Q$f|FglP|H8OKhy
'''.replace("\n",""))).split())))
