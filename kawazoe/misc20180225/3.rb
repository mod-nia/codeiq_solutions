#!/usr/bin/ruby
def f(k,n,mod)
	raise if k<=0
	return 1 if k==1
	h=Hash.new 0 # 添字が0より小さくなりうるので連想配列で手抜きをする
	h[0]=1
	h[1]=k
	s=k+1
	(2..n).each{|i|
		h[i]=((k+2)*h[i-1]-s-h[i-k-1])%mod
		s=(h[i]+s-h[i-k])%mod
		h.delete(i-k-1) # メモリが危ないので
	}
	h[n]
end
p f(3,1,100000000)
p f(3,2,100000000)
p f(3,3,100000000)
p f(3,4,100000000)
p f(5,10,100000000)

p f(10,10**10,100000000)
p f(10000,10**6,100000000)
__END__
【解答】
・68438232
・86731776
【方針】
F4(n+1)-F4(n)=4*F4(n)-F4(n-1)-F4(n-2)-F4(n-3)-F4(n-4)
より
F4(n)=5*F4(n-1)-F4(n-2)-F4(n-3)-F4(n-4)-F4(n-5) (*)
が成立する。
「F4(n-1)+F4(n-2)+F4(n-3)+F4(n-4)」を累積和により管理する。
これにより計算量はkによらなくなり、O(n)となる。

ただし、(*)式はn==1の場合には成立しないため注意を要する。
# 高校では差を取って計算する時(自明に成り立つ場合でも)
# n==1の確認はしないと減点とかありましたねぇ…
よって、累積和による管理自体がk==1だと成立しない。
万全を期すならば処理を分けなければならない。
【言語】
Ruby
【コード】
