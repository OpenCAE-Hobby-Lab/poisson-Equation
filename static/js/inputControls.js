let target1 = document.getElementById("Xnum");
// 変数testの要素を入力不可にする
target1.readOnly = true;
let target2 = document.getElementById("Ynum");
// 変数testの要素を入力不可にする
target2.readOnly = true;

let trigger1 = document.getElementById("radio1a");
let trigger2 = document.getElementById("radio1b");

// 入力不可を設定する条件を定義
trigger1.addEventListener('change',
function(){
    if(trigger1.checked===true){
        target1.readOnly = true;
        target2.readOnly = true;
    }else{
        target1.readOnly = false;
        target2.readOnly = false;
    }
}, false);

// 入力不可を解除する条件を定義
trigger2.addEventListener('change',
function(){
    if(trigger2.checked===true){
        target1.readOnly = false;
        target2.readOnly = false;
    }else{
        target1.readOnly = true;
        target2.readOnly = true;
    }
}, false);