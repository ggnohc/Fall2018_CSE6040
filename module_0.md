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
		if T[a,b]/C[a] >=S:
			then output a=> b
```
* Efficiency
	* not necessary to have a table, since most of the entries might be zero, instead using dictionary. (collections.Defaultdict does not need to check if the key exists, if not, the new entry will be created by Python)
	
* Implementation ([Notebook2](https://github.com/qixuanHou/Fall2018_CSE6040/blob/master/Notebook_2.md))
	
### Topic 3 - Representation Number
### Representing numbers
