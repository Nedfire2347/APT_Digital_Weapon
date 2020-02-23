Comparing with MISP database

grep  -f ./nameAttack.txt -r -i  ../../misp-galaxy/Research/apt_list > taxonomyAttackMisp.txt 

cat nameAttack.txt | grep -f ./galaxyAttackMisp.txt -v
diff --side-by-side nameAttack.txt galaxyAttackMisp.txt --color

#No matching difference : Project Abondonned

**Alias**  
APT_Digital_Weapon
 
Description : Here are indicators of compromise (IOCs) collected from public resources and our own investigations. 
References : 
	https://github.com/RedDrip7/APT_Digital_Weapon
	Copyright © @RedDrip (https://ti.qianxin.com/)
Version : 1


# Fichier - README.md 
# **NAME**
# "Name" 
#
# **Alias**  
# "Alias, Alias2"
#
# **Description**
# "Description"
# 
# **References**
# "Link1" 
# "Link2" 

Name : Attack name 
Description : 
References : 

# Fichier - name_hash.md 
# Plusieurs lignes au format 
# |["hash"]("linkVirusTotal")|"Type"|"Family"|"Name"|  
Hash : 
Type : 
Family :
First_Seen : 
Name : 
