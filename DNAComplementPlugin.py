import PyPluMA

COMPLEMENT = dict()
COMPLEMENT['A'] = 'T'
COMPLEMENT['T'] = 'A'
COMPLEMENT['C'] = 'G'
COMPLEMENT['G'] = 'C'

class DNAComplementPlugin:
    def input(self, filename):
       fastafile = open(filename, 'r')
       self.header = fastafile.readline().strip()
       self.DNA = ''
       for line in fastafile:
           self.DNA += line.strip()

    def run(self):
       self.header += ' complemented'
       self.complement = ''
       for i in range(len(self.DNA)):
           self.complement += COMPLEMENT[self.DNA[i]]
        

    def output(self, filename):
       outfile = open(filename, 'w')
       outfile.write(self.header+"\n")
       outfile.write(self.complement)
