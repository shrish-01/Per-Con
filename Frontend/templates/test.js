function check(){
    var c=0;
    var q1= document.test.q1.value;
    var q2= document.test.q2.value;
    var q3= document.test.q3.value;
    var q4= document.test.q4.value;
    var q5= document.test.q5.value;
    var q6= document.test.q6.value;
    var q7= document.test.q7.value;
    var q8= document.test.q8.value;
    var q9= document.test.q9.value;
    var q10= document.test.q10.value;
    var q11= document.test.q11.value;
    var q12= document.test.q12.value;
    var q13= document.test.q13.value;
    var q14= document.test.q14.value;
    var q15= document.test.q15.value;
    var q16= document.test.q16.value;
    var q17= document.test.q17.value;
    var q18= document.test.q18.value;
    var q19= document.test.q19.value;
    var q20= document.test.q20.value;
    // var result= document.getElelementById('result');
  




    if(q1=="1"){c+=0.25}
    if(q1=="2"){c+=0.50}
    if(q1=="3"){c+=0.75}
    if(q1=="4"){c+=1.00}

    if(q2=="1"){c+=0.25}
    if(q2=="2"){c+=0.50}
    if(q2=="3"){c+=0.75}
    if(q2=="4"){c+=1.00}

    if(q3=="1"){c+=0.25}
    if(q3=="2"){c+=0.50}
    if(q3=="3"){c+=0.75}
    if(q3=="4"){c+=1.00}

    if(q4=="1"){c+=0.25}
    if(q4=="2"){c+=0.50}
    if(q4=="3"){c+=0.75}
    if(q4=="4"){c+=1.00}

    if(q5=="1"){c+=0.25}
    if(q5=="2"){c+=0.50}
    if(q5=="3"){c+=0.75}
    if(q5=="4"){c+=1.00}
  
    if(q6=="1"){c+=0.25}
    if(q6=="2"){c+=0.50}
    if(q6=="3"){c+=0.75}
    if(q6=="4"){c+=1.00}
    
    if(q7=="1"){c+=0.25}
    if(q7=="2"){c+=0.50}
    if(q7=="3"){c+=0.75}
    if(q7=="4"){c+=1.00}

    if(q8=="1"){c+=0.25}
    if(q8=="2"){c+=0.50}
    if(q8=="3"){c+=0.75}
    if(q8=="4"){c+=1.00}

    if(q9=="1"){c+=0.25}
    if(q9=="2"){c+=0.50}
    if(q9=="3"){c+=0.75}
    if(q9=="4"){c+=1.00}

    if(q10=="1"){c+=0.25}
    if(q10=="2"){c+=0.50}
    if(q10=="3"){c+=0.75}
    if(q10=="4"){c+=1.00}

    if(q11=="1"){c+=0.25}
    if(q11=="2"){c+=0.50}
    if(q11=="3"){c+=0.75}
    if(q11=="4"){c+=1.00}

    if(q12=="1"){c+=0.25}
    if(q12=="2"){c+=0.50}
    if(q12=="3"){c+=0.75}
    if(q12=="4"){c+=1.00}

    if(q13=="1"){c+=0.25}
    if(q13=="2"){c+=0.50}
    if(q13=="3"){c+=0.75}
    if(q13=="4"){c+=1.00}

    if(q14=="1"){c+=0.25}
    if(q14=="2"){c+=0.50}
    if(q14=="3"){c+=0.75}
    if(q14=="4"){c+=1.00}

    if(q15=="1"){c+=0.25}
    if(q15=="2"){c+=0.50}
    if(q15=="3"){c+=0.75}
    if(q15=="4"){c+=1.00}

    if(q16=="1"){c+=0.25}
    if(q16=="2"){c+=0.50}
    if(q16=="3"){c+=0.75}
    if(q16=="4"){c+=1.00}

    if(q17=="1"){c+=0.25}
    if(q17=="2"){c+=0.50}
    if(q17=="3"){c+=0.75}
    if(q17=="4"){c+=1.00}

    if(q18=="1"){c+=0.25}
    if(q18=="2"){c+=0.50}
    if(q18=="3"){c+=0.75}
    if(q18=="4"){c+=1.00}

    if(q19=="1"){c+=0.25}
    if(q19=="2"){c+=0.50}
    if(q19=="3"){c+=0.75}
    if(q19=="4"){c+=1.00}

    if(q20=="1"){c+=0.25}
    if(q20=="2"){c+=0.50}
    if(q20=="3"){c+=0.75}
    if(q20=="4"){c+=1.00}

    

    var m=c*5;
    
    document.write("Your test score is = ")
    document.write(m);
    document.write("/100")
    document.write("\n")
    
    


  

    if (m<=50) {
        document.write('You are not suffering from depression ')
    }
    if (m<=70 & m>=50) {
        document.write('You are suffering from moderate depression .Do not take tension.Follow some tips from this website that will surely help you.')
    }
    if(m>=80){
        document.write('There is chance that you are suffering from sever depression. Do not take tension.Follow some tips from this website that will surely help you also Take some professional help')
    }


    
}

