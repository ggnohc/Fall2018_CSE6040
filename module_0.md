### Topic 1 - Reivew Python

### Topic 2 - Pairwise association mining   
#### Conditional Probablities
* Pr[b|a] = Pr[a,b] / Pr[a]
* Pr[b|a] conditional probability, when a happesn, with Pr[b|a], b will happen
* Pr[a,b] joint probability, with Pr[b|a], a and b will happen together
#### Association Rule 
* estimates (R, a => b)
	* n_a <- count of # of receipts in R containting a
	* n_ab <- count # of receipts in R containing a&b
	* return n_ab/n_a
	=====> estimates Pr [b|a]
* Support(a,b) == n_ab/m ~ Pr[a,b]
* Confidence(a=>b) == n_ab/n_a ~ Pr[b|a]
* Algorithm (R(receipt), A(items), S(threshold))
	* define T[a,b] -> n_ab
	* define C[a] -> n_a 
	* set T[a,b] and C[a] == 0 for all a,b in A
```python
	for every r in R:
		for every pair(a,b) in r:
			T[a,b] <- T[a,b] + 1
			T[b,a] <- T[b,a] + 1
		for every a in r:
			C[a] <- C[a] + 1
	for every (a in A, b in A):
		if T[a,b]/ >=S:
			then output a=> b```
* Implementation ([Notebook2]())
