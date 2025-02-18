function solution(spell, dic) {
    for(let i=0;i<dic.length;i++){
        let temp=0;
        for(let j=0;j<spell.length;j++){
            if(dic[i].includes(spell[j])){
                temp++;
            }
            
        }
        if(temp==spell.length){
            return 1
        }
    }
    return 2;
}