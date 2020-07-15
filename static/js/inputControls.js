function setReadonly(targetKey, triggerKey, triggerValue){
    let target = document.getElementById(targetKey);
    // 変数testの要素を入力不可にする
    target.readOnly = true;

    let trigger = document.getElementById(triggerKey);

    // 入力不可を解除する条件を定義
    trigger.addEventListener('change',
    function(){
        if(trigger.checked===triggerValue){
            target.readOnly = true;
        }else{
            target.readOnly = false;
        }
    }, false);
};

setReadonly("X", "radio1a", true)
setReadonly("Y", "radio1a", true)