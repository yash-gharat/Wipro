distributions=("Ubuntu Fedora Manjaro Arch EndeavourOS Garuda kali-Linux red-hatDD")
for i in $distributions; do
	echo $i
done 

distributions=("Ubuntu Fedora Manjaro Arch EndeavourOS Garuda")

for distro in $distributions; do 
 if [[ "$distro" == "Arch" ]] ;   
   then   
   continue 
 fi 
 echo $distro
done
