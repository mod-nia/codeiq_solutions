#!/usr/bin/python

### quite similar, but not the same as q3360 ###

### previous code is important, really. ###
b=lambda s,c: ((s[0]==c and s[1]==c and s[2]==c)or(s[3]==c and s[4]==c and s[5]==c)or(s[6]==c and s[7]==c and s[8]==c)or(s[0]==c and s[3]==c and s[6]==c)or(s[1]==c and s[4]==c and s[7]==c)or(s[2]==c and s[5]==c and s[8]==c)or(s[0]==c and s[4]==c and s[8]==c)or(s[2]==c and s[4]==c and s[6]==c))

visited=set()
r0=[0]*9
r1=[0]*9
def dfs(st,s,n):
	for i in range(0,9):
		if s[i]<0:
			s[i]=n%2
			if b(s,n%2):
				r0[n]+=1
				key=tuple(s)
				if key not in visited:
					visited.add(key)
					r1[n]+=1
			else:
				st_orig=st[n%2]
				st[n%2]=i+1
				dfs(st,s,n+1)
				st[n%2]=st_orig
			s[i]=-1


dfs([0,0],[-1]*9,0)
#import sys;print(r0[int(sys.stdin.read())-1])
print(sum(r0))
print(sum(r1))
