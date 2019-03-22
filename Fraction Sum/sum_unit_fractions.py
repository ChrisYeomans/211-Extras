#! usr/bin/env python3
from fractions import Fraction as f
import sys, math

def main():
	o_sl = [f(1, 2), f(1, 3), f(1, 6)]
	o_bl = reset_bl(o_sl)
	n_sl = []
	f_sl = o_sl[:]
	s_sl = o_sl[:]
	while True:
		while True:
			sys.stderr.write("prime break\n")
			n_sl = []
			for i in range(len(o_sl)):
				tmp = prime_break(o_sl[i].denominator, o_bl)
				#sys.stderr.buffer.write(bytes(str(tmp)+'\n', 'utf-8'))
				if tmp:
					n_sl += tmp
					for j in tmp:
						o_bl[j.denominator] = True
				else:
					n_sl = n_sl + [o_sl[i]]
			print(n_sl, sum(n_sl), len(n_sl), "pb",'\n')
			#sys.stderr.buffer.write(bytes('\n'+"stand out text "+str(len(o_sl))+'\n\n', 'utf-8'))
			if o_sl == n_sl:
				f_sl = o_sl[:]
				break
			if len(set(o_sl)) == len(o_sl):
				break
			o_sl = n_sl[:]
			o_bl = reset_bl(o_sl)
			if sum(n_sl) != 1:
				break

		while True:
			sys.stderr.write("break lower\n")
			n_sl = []
			for i in range(len(o_sl)):
				tmp = break_lower(o_sl[i], o_bl)
				#sys.stderr.buffer.write(bytes(str(tmp)+'\n', 'utf-8'))
				if tmp:
					n_sl += tmp
					for j in tmp:
						o_bl[j.denominator] = True
				else:
					n_sl = n_sl + [o_sl[i]]
			print(n_sl, sum(n_sl), len(n_sl), "bl",'\n')
			if o_sl == n_sl:
				s_sl = o_sl[:]
				break
			if len(set(o_sl)) == len(o_sl):
				break
			o_sl = n_sl[:]
			o_bl = reset_bl(o_sl)
			if sum(n_sl) != 1:
				break
		
		while True:
			sys.stderr.write("factor break\n")
			n_sl = []
			for i in range(len(o_sl)):
				tmp = f_break(o_sl[i].denominator, o_bl)
				#sys.stderr.write(str(tmp)+" "+str(sum(tmp))+'\n')
				#sys.stderr.buffer.write(bytes(str(tmp)+'\n', 'utf-8'))
				if tmp:
					n_sl += tmp
					for j in tmp:
						o_bl[j.denominator] = True
				else:
					n_sl = n_sl + [o_sl[i]]
			print(n_sl, sum(n_sl), len(n_sl), "fb",'\n')
			#sys.stderr.buffer.write(bytes('\n'+"stand out text "+str(len(o_sl))+'\n\n', 'utf-8'))
			if o_sl == n_sl:
				f_sl = o_sl[:]
				break
			if len(set(o_sl)) == len(o_sl):
				break
			o_sl = n_sl[:]
			o_bl = reset_bl(o_sl)
			if sum(n_sl) != 1:
				break

		while True:
			o_sl = n_sl[:]
			sys.stderr.write("three break\n")
			n_sl = []
			for i in range(len(o_sl)):
				tmp = three_break(o_sl[i].denominator, o_bl)
				#sys.stderr.write(str(tmp)+" "+str(sum(tmp))+'\n')
				#sys.stderr.buffer.write(bytes(str(tmp)+'\n', 'utf-8'))
				if tmp:
					n_sl += tmp
					for j in tmp:
						o_bl[j.denominator] = True
				else:
					n_sl = n_sl + [o_sl[i]]
			print(n_sl, sum(n_sl), len(n_sl), "tb",'\n')
			#sys.stderr.buffer.write(bytes('\n'+"stand out text "+str(len(o_sl))+'\n\n', 'utf-8'))
			if o_sl == n_sl:
				f_sl = o_sl[:]
				break
			if len(set(o_sl)) == len(o_sl):
				break
			o_bl = reset_bl(o_sl)
			if sum(n_sl) != 1:
				break
		if sum(n_sl) != 1:
			break
		if len(set(o_sl)) != len(o_sl):
			break

def break_lower(fr, bl):
	tot = 0
	out_lst = []
	for i in range(fr.denominator+1, 1000):
		#sys.stderr.buffer.write(bytes(str(i)+" "+str(tot)+'\n', 'utf-8'))
		if not bl[i]:
			#sys.stderr.buffer.write(bytes(str(tot+f(1,i)), 'utf-8'))
			if tot+f(1,i) == fr:
				return out_lst + [f(1,i)]
			elif tot+f(1,i) < fr:
				bl[i] = True
				tot+=f(1,i)
				out_lst.append(f(1,i))
	return []

def prime_break(n, bl):
	p = lpf(n, bl)
	#sys.stderr.buffer.write(bytes(str(p)+'\n', 'utf-8'))
	if p:
		y = n+p
		x = (y*n)//(y-n)
		if y<=1000 and x <=1000:
			if (not bl[y] and not bl[x]) and x != y:
				return [f(1,x), f(1,y)]
	return []

def lpf(n, bl):
	primes = [
	2, 3, 4, 5, 7, 9, 11, 13, 17, 19, 23, 25, 29,
	31, 37, 41, 43, 47, 49, 53, 59, 61, 67, 71, 73,
	79, 83, 89, 97, 101, 103, 107, 109, 113, 121,
	127, 131, 137, 139, 149, 151, 157, 163, 167,
	169, 173, 179, 181, 191, 193, 197, 199, 211,
	223, 227, 229, 233, 239, 241, 251, 257, 263,
	269, 271, 277, 281, 283, 289, 293, 307, 311,
	313, 317, 331, 337, 347, 349, 353, 359, 361,
	367, 373, 379, 383, 389, 397, 401, 409, 419,
	421, 431, 433, 439, 443, 449, 457, 461, 463,
	467, 479, 487, 491, 499, 503, 509, 521, 523,
	529, 541, 547, 557, 563, 569, 571, 577, 587,
	593, 599, 601, 607, 613, 617, 619, 631, 641,
	643, 647, 653, 659, 661, 673, 677, 683, 691,
	701, 709, 719, 727, 733, 739, 743, 751, 757,
	761, 769, 773, 787, 797, 809, 811, 821, 823,
	827, 829, 839, 841, 853, 857, 859, 863, 877,
	881, 883, 887, 907, 911, 919, 929, 937, 941,
	947, 953, 961, 967, 971, 977, 983, 991, 997
	]
	for i in primes:
		#sys.stderr.buffer.write(bytes(str(n)+' '+str(i)+' '+str(bl[i])+'\n', 'utf-8'))
		if i > n:
			break
		elif not n%i and (not bl[i] or n==i):
			return i
	return 0

def f_break(n, bl):
	fl = factors(n)
	#sys.stderr.write("\n\n"+str(n)+" "+str(fl)+"\n\n")
	for i in range(len(fl)):
		m = n//fl[i]
		j = m+fl[i]
		#sys.stderr.write(str(j*m)+" "+str(j*fl[i])+" "+str(sum([f(1, j*m), f(1, j*fl[i])]))+'\n')
		if j*m <= 1000 and j*fl[i] <= 1000:
			if not bl[j*m] and not bl[j*fl[i]]:
				bl[j*m] = True
				bl[j*fl[i]] = True
				return [f(1, j*m), f(1, j*fl[i])]
	return []
    
def factors(n):
	primes = [
	2, 3, 4, 5, 7, 9, 11, 13, 17, 19, 23, 25, 29,
	31, 37, 41, 43, 47, 49, 53, 59, 61, 67, 71, 73,
	79, 83, 89, 97, 101, 103, 107, 109, 113, 121,
	127, 131, 137, 139, 149, 151, 157, 163, 167,
	169, 173, 179, 181, 191, 193, 197, 199, 211,
	223, 227, 229, 233, 239, 241, 251, 257, 263,
	269, 271, 277, 281, 283, 289, 293, 307, 311,
	313, 317, 331, 337, 347, 349, 353, 359, 361,
	367, 373, 379, 383, 389, 397, 401, 409, 419,
	421, 431, 433, 439, 443, 449, 457, 461, 463,
	467, 479, 487, 491, 499, 503, 509, 521, 523,
	529, 541, 547, 557, 563, 569, 571, 577, 587,
	593, 599, 601, 607, 613, 617, 619, 631, 641,
	643, 647, 653, 659, 661, 673, 677, 683, 691,
	701, 709, 719, 727, 733, 739, 743, 751, 757,
	761, 769, 773, 787, 797, 809, 811, 821, 823,
	827, 829, 839, 841, 853, 857, 859, 863, 877,
	881, 883, 887, 907, 911, 919, 929, 937, 941,
	947, 953, 961, 967, 971, 977, 983, 991, 997
	]
	if n in primes:
		return []
	else:
		out_lst = []
		for i in range(2, n):
			if n%i == 0:
				out_lst.append(i);
		return out_lst

def three_break(n, bl):
	fl = factors(n)
	three_facts = get_three_not_used(fl, bl)
	if three_facts and (three_facts[0] != three_facts[1] != three_facts[2]):
		if three_facts[0] >=1000 and three_facts[1] >= 1000 and three_facts[2] >= 1000:
			return [f(1, (n//three_facts[0])*(sum(three_facts))), f(1, (n//three_facts[1])*(sum(three_facts))), f(1, (n//three_facts[0])*(sum(three_facts)))]
	return []
def get_three_not_used(fl, bl):
	out_lst = []
	for i in fl:
		if not bl[i]:
			out_lst.append(i)
			if len(out_lst) == 3:
				return out_lst
	return []

def punch_fill(a, b, sl, bl):
	x = sl[a]
	y = sl[b]
	z = x+y
	tot = 0
	out_lst = []
	for i in range(1, 1000):
		#sys.stderr.buffer.write(bytes(str(i)+" "+str(tot)+'\n', 'utf-8'))
		if not bl[i]:
			#sys.stderr.buffer.write(bytes(str(tot+f(1,i)), 'utf-8'))
			if tot+f(1,i) == z:
				return out_lst + [f(1,i)] + sl[:a] + sl[a+1:b] + sl[b+1:]
			elif tot+f(1,i) < z:
				bl[i] = True
				tot+=f(1,i)
				out_lst.append(f(1,i))
	return []

def reset_bl(fl):
	out = [False]*1001
	for i in fl:
		out[i.denominator] = True
	return out

if __name__ == "__main__":
	main()
