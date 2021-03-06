#include <stdio.h>
int gcd(int x,int y){return y?gcd(y,x%y):x;}
int main(){
	int r=0,i,j1,j2;
	for(i=2;i<=125;i++){ //125==最大の1辺
		j2=i-1;
		//直角二等辺三角形の斜辺以外の2辺が有理数の時、斜辺は無理数である。∴j1≠j2
		for(j1=1;j1<j2;j1++){
			for(;j1*(i*2-j1)+j2*(i*2-j2)>i*i;j2--); //尺取り法
			if(j1*(i*2-j1)+j2*(i*2-j2)==i*i && gcd(gcd(j1,j2),i)==1){
				printf("%d*%d,%d*%d,%d*%d\n",j1,i*2-j1,j2,i*2-j2,i,i);
				r++;
			}
		}
	}
	printf("%d\n",r);
	return 0;
}
//can be passed to: ruby -e 'p $<.map{|e|eval "["+e+"]"}[0..-2]'
//[[9, 16, 25], [25, 144, 169], [64, 225, 289], [49, 576, 625], [400, 441, 841], [144, 1225, 1369], [81, 1600, 1681], [784, 2025, 2809], [121, 3600, 3721], [256, 3969, 4225], [1089, 3136, 4225], [2304, 3025, 5329], [169, 7056, 7225], [1296, 5929, 7225], [1521, 6400, 7921], [4225, 5184, 9409], [400, 9801, 10201], [3600, 8281, 11881], [225, 12544, 12769], [1936, 13689, 15625]]