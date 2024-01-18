function solution(s){
    var answer = true;
    let a=0;

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    console.log('Hello Javascript')
    for(let i=0;i<s.length;i++){
        if(s.charAt(i)=='('){
            a+=1;
        }
        else if(s.charAt(i)==')'){
            a-=1;
        }
        if(a<0){
            return false;
        }
    }
    console.log(a);
    if(a==0){
        answer=true;
    }
    else{
        answer=false;
    }

    return answer;
}