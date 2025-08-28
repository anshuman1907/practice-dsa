// scopchain and lexical enviroment menas contectin chain find perticulrar valuee 

function a()
{
    console.log(b,"single fucntion")
    console.log(d,"single fucntion")

    function c(){

        var d =14
        console.log(d,"nested function")
    }

    c()

}

var b =12
var d =1


a()