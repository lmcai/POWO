x=open('wcvp/wcvp_names.csv').readlines()
z=open('wcvp/wcvp_distribution.csv').readlines()

##################################################
##Species level records


sp2accepted_id={}
id2taxonrec={}
id2distrrec={}

#associate id and taxonomy for each species name
for l in x[1:]:
	y=l.split('|')
	id2taxonrec[y[0]]=l
	sp2accepted_id[y[21]]=y[23]

id2native={}
id2introduced={}
#consolidate country for each id
for l in z[1:]:
	y=l.split('|')
	if y[10]=='0\n' and y[8]=='0':
		#native and not doubtful
		try:id2native[y[1]].append(y[6])
		except KeyError:id2native[y[1]]=[y[6]]
	elif y[10]=='0\n' and y[8]=='1':
		#introduced and not doubtful
		try:id2introduced[y[1]].append(y[6])
		except KeyError:id2introduced[y[1]]=[y[6]]


sp=open('host_sp.list').readlines()
failed_sp=[]
out=open('wcvp_info.host.tsv','a')
out.write('Query\tFamily\tGenus\tSpecies\tAuthor\tRegion\tlifeform\tClimate\tNative_range\tIntroduced_range\n')
for l in sp:
	query=l.split('\t')[1].strip()
	try:
		valid_id=sp2accepted_id[query]
		valid_taxon_rec=id2taxonrec[valid_id]
		family=valid_taxon_rec.split('|')[4]
		genus=valid_taxon_rec.split('|')[6]
		species=valid_taxon_rec.split('|')[21]
		author=valid_taxon_rec.split('|')[22]
		region=valid_taxon_rec.split('|')[18]
		lifeform=valid_taxon_rec.split('|')[19]
		climate=valid_taxon_rec.split('|')[20]
		try:native=id2native[valid_id]
		except KeyError:native=['NA']
		try:introduced=id2introduced[valid_id]
		except KeyError:introduced=['NA']
		d=out.write('\t'.join([query,family,genus,species,author,region,lifeform,climate,', '.join(native),', '.join(introduced)])+'\n')
	except KeyError:
		#pass
		out.write(query+'\n')
		failed_sp.append(query)
		print(query)


out.close()
fail_file=open('failed_wcvp_search.list','a')
fail_file.write('\n'.join(failed_sp))
fail_file.close()


##################################################
##Genus level records
gn2accepted_id={}
id2distrrec={}

x=open('wcvp/wcvp_names.csv').readlines()
z=open('wcvp/wcvp_distribution.csv').readlines()

for l in x[1:]:
	y=l.split('|')
	if y[2]=='Genus':
		gn2accepted_id[y[21]]=y[23]

id2native={}
id2introduced={}
#consolidate country for each id
for l in z[1:]:
	y=l.split('|')
	if y[10]=='0\n' and y[8]=='0':
		#native and not doubtful
		try:id2native[y[1]].append(y[6])
		except KeyError:id2native[y[1]]=[y[6]]
	elif y[10]=='0\n' and y[8]=='1':
		#introduced and not doubtful
		try:id2introduced[y[1]].append(y[6])
		except KeyError:id2introduced[y[1]]=[y[6]]

gn=open('/Users/lcai/Downloads/host_genus.list').readlines()
gn=[i.strip() for i in gn]

failed_gn=[]
out=open('wcvp_info.genus.tsv','a')
out.write('Query_genus\tNative_range\tIntroduced_range\n')
for l in gn:
	query=l
	try:
		valid_id=gn2accepted_id[query]
		try:native=id2native[valid_id]
		except KeyError:native=['NA']
		try:introduced=id2introduced[valid_id]
		except KeyError:introduced=['NA']
		d=out.write('\t'.join([query,', '.join(native),', '.join(introduced)])+'\n')
	except KeyError:
		pass
		failed_gn.append(query)
		print(query)


out.close()
fail_file=open('failed_wcvp_search.list','a')
fail_file.write('\n'.join(failed_sp))
fail_file.close()




