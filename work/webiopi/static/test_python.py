def create_file(path):
	f = open(path + '/test.txt','a')
	f.write('run from web')
	f.close()
	return 'OK : create file'
