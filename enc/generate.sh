COUNT=0
for i in `seq 1 7`; do
    curl --data "name=group$i&description=$i" http://emeister:testing@127.0.0.1:8001/enc/groups/; 
    let COUNT=COUNT+1
    curl --data "group=$COUNT&classname=test$i&classparams={}" http://emeister:testing@127.0.0.1:8001/enc/classes/groups/;
done
for i in `seq 1 7`; do
    for j in `seq 1 7`; do
      let PARENT=$i
      curl --data "name=group-$i-$j&description=$j&parents=$PARENT" http://emeister:testing@127.0.0.1:8001/enc/groups/; 
      let COUNT=COUNT+1
      curl --data "group=$COUNT&classname=test$i-$j&classparams={}" http://emeister:testing@127.0.0.1:8001/enc/classes/groups/;
   done
done

for i in `seq 1 7`; do
    for j in `seq 1 7`; do
        for k in `seq 1 7`; do
	    let PARENT=$i*7+1
	    curl --data "name=group-$i-$j-$k&description=$i&parents=$PARENT" http://emeister:testing@127.0.0.1:8001/enc/groups/ &
# 	    curl --data "group=$COUNT&classname=test$i-$j&classparams={}" http://emeister:testing@127.0.0.1:8001/enc/classes/groups/;
	done
    done
done

# for i in `seq 1 7`; do
#     for j in `seq 1 7`; do
#         for k in `seq 1 7`; do
# 	    for l in `seq 1 7`; do
# 	        let PARENT=$i*7+49+$l
# 	        curl --data "name=group-$i-$j-$k-$l&description=$i&parents=$PARENT" http://emeister:testing@127.0.0.1:8001/enc/groups/ &
# 	        let COUNT=COUNT+1
# # 	        curl --data "group=$COUNT&classname=test$i&classparams={}" http://emeister:testing@127.0.0.1:8001/enc/classes/groups/;
# 	done
# 	done
#     done
# done

