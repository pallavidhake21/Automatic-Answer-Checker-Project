function check(){
    var c=0;

    var q1=document.test.question1.value;
    var q2=document.test.question2.value;
    var q3=document.test.question3.value;
    var q4=document.test.question4.value;
    var q5=document.test.question5.value;
    var q6=document.test.question6.value;
    var q7=document.test.question7.value;
    var q8=document.test.question8.value;
    var q9=document.test.question9.value;
    var q10=document.test.question10.value;
    
    if(q1=="javascript"){c++}
    if(q2=="russia"){c++}
    if(q3=="nile"){c++}
    if(q4=="delhi"){c++}
    if(q5=="dennis ritchie"){c++}
    if(q6=="guido van rossum"){c++}
    if(q7==".py"){c++}
    if(q8=="8"){c++}
    if(q9=="32 and 64"){c++}
    if(q10=="rasmus lerdrof"){c++}

    
    document.write(c);
}