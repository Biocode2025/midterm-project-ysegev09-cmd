def s_charge (seq):
  pro=0
  i=0
  charge = {'K': 1, 'R': 1, 'H': 0.5, 'D':-1 , 'E': -1} 
  while i < len(seq):
    sd=seq[i]
    val=charge.get(sd,"not found") 
    if val!="not found":
      pro=pro+val
    i = i + 1
  return (pro)


def RNA_prot (seq):
  pro=""
  i=0
 

  while i < len(seq):
    
    sd=seq[i]
    
    pro=pro+RNA_codon_table.get(sd,"not found")
    i = i + 1
  
  H_C=pro.count('H')
  C_C=pro.count('C')
  P_C=pro.count('P')
  H_T_F="Percentage of H is "+str(round((H_C*100)/len(seq),2))+"%"
  C_T_F="Percentage of C is "+str(round((C_C*100)/len(seq),2))+"%"
  P_T_F="Percentage of P is "+str(round((P_C*100)/len(seq),2))+"%"
  file_a.write(pro+"\n" )
  file_a.write( H_T_F+"\n")
  file_a.write(C_T_F+"\n")
  file_a.write(P_T_F+"\n")
    
    
  return pro

def Read_dict() :
  global RNA_codon_table
  
  RNA_codon_table={}
  milon = open('data/AA_Type.txt', 'r')
  for line in (milon):
    line = line.rstrip("\r\n")
    num=line[0]
    RNA_codon_table[num] = line[2]   
last_line=""  
protin_pra=0
file_a=open('results/an.txt', 'w')
biggest_C=0
lowest_C=0
pro_b=""
pro_l=""
amut=0
seq=""  
file = open('data/short_seq.txt', 'r')
make_mil=Read_dict()
for line in(file):
  
  if line[0]!=">":
    
    line = line.rstrip("\r\n")
    seq=seq+line
    
  elif line[0]==">":
    last_line=line
    amut=amut+1
    
    if seq!="":
      protin_pra=RNA_prot(seq)
      protin_C=s_charge(seq)
      file_a.write(str(protin_C)+"\n")
      file_a.write("....................." +"\n")
      file_a.write(line+"\n")
      
      if protin_C>biggest_C:
        biggest_C=protin_C
        pro_b=line+seq
      if protin_C<lowest_C:
        lowest_C=protin_C
        pro_l=line+seq
        
    else:
      file_a.write(line+"\n")
    seq=""  
if seq!="":
 # file_a.write(last_line+"\n")
  protin_pra=RNA_prot(seq)
  protin_C=s_charge(seq)
  
  file_a.write(str(protin_C)+"\n")
  file_a.write(".........." +"\n")
  

camot= "Number of proteins:"+ str(amut)   
file_a.write(camot+"\n")

file_a.write("Protein with highest positive charge:"+str(pro_b)+"\n")
file_a.write("Charge is:"+ str(biggest_C)+"\n")
file_a.write(".........." +"\n")
file_a.write("Protein with lowes nagative charge:"+str(pro_l)+"\n")
file_a.write("Charge is:"+ str(lowest_C)+"\n")
file_a.close()
file_a=open('results/an.txt', 'r')
for line in (file_a):
  print(line)