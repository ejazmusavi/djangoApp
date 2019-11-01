function validateEmail(sEmail) 
{
  var filter = /^([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;
  if (filter.test(sEmail)) 
  {
      return true;
  }
  else 
  {
      return false;
  }
}

// $(document).on('click','#close_reload',function(e){  
//       location.reload(true);
// });


// $(document).on('click','#close_reload_symbol',function(e){  
//       location.reload(true);
// });

// $(document).ready(function () {
//    $('input[type=text]').on('keypress', function(e) {
//       if (e.which == 32)
//       {
//         console.log('no space')
//         return false;
//       }
//   });
// });

$(document).ready(function () {
$('#password').keypress(function( e ) {
       if(e.which === 32) 
         return false;
    });
$('#first_name').keypress(function( e ) {
       if(e.which === 32) 
         return false;
    });
$('#surname').keypress(function( e ) {
       if(e.which === 32) 
         return false;
    });
$('#email').keypress(function( e ) {
       if(e.which === 32) 
         return false;
    });
$('#date_of_birth').keypress(function( e ) {
         return false;
    });

$('#year_of_study').keypress(function( e ) {
         return false;
    });
});



$(document).on('click','#student_sign_up_btn',function(e){
 console.log("Hello !!")  
  var first_name = $('#first_name').val();
  var surname = $('#surname').val();
  var date_of_birth = $('#date_of_birth').val();
  var email = $('#email').val();
  var address = $('#address').val();
  var pin_code= $('#pin_code').val();
  var year_of_study =$('#year_of_study').val();
  var programme_studied =$('#programme_studied').val();
  var grades_obtained =$('#grades_obtained').val();
  var max_grades =$('#max_grades').val();
  var skills_interested =$('#skills_interested option:selected').val();
  var industry_interested =$('#industry_interested option:selected').val();
  var password =$('#password').val();
  var country =$('#country option:selected').val();
  var token=$('input[name="csrfmiddlewaretoken"]').val()
  first_name = first_name.trim()
  surname = surname.trim()
  date_of_birth = date_of_birth.trim()
  email = email.trim()
  address = address.trim()
  pin_code = pin_code.trim()
  year_of_study = year_of_study.trim()
  programme_studied = programme_studied.trim()
  grades_obtained = grades_obtained.trim()
  max_grades = max_grades.trim()



 if(first_name.length == 0)
 {
    // alert('First_name is required');
    $("#first_name_error").text('First Name is required.');
    document.getElementById("first_name_error").style.color = "red";
    return false;
 }
 else
 {
   if (first_name.match(/^[a-zA-Z\s]+$/))
     {
       first_name = first_name.replace(/  +/g, ' '); 
       console.log('name done.')
       $("#first_name_error").text('');
       // alert('valid');  
     }
   else
     {
       // alert('invalid')
       // alert('Only alphabets are allowed for this field.');
      $("#first_name_error").text('Only alphabets are allowed for this field.');
      document.getElementById("first_name_error").style.color = "red";
      return false;
     }

   
 }

  if(first_name.length > 25)
  {
    $("#first_name_error").text('Max length of Name is 25.');
    document.getElementById("first_name_error").style.color = "red";
    return false;
  }
  if(first_name.length > 0 && first_name.length <= 25)
  {
    console.log('name done.')
    $("#first_name_error").text('');
  }




if(surname.length == 0)
 {
    // alert('First_name is required');
    $("#surname_error").text('Last Name is required.');
    document.getElementById("surname_error").style.color = "red";
    return false;
 }
 else
 {
   if (surname.match(/^[a-zA-Z\s]+$/))
     {
       surname = surname.replace(/  +/g, ' '); 
       console.log('name done.')
       $("#surname_error").text('');
       // alert('valid');  
     }
   else
     {
       // alert('invalid')
       // alert('Only alphabets are allowed for this field.');
      $("#surname_error").text('Only alphabets are allowed for this field.');
      document.getElementById("surname_error").style.color = "red";
      return false;
     }

   
 }

  if(surname.length > 25)
  {
    $("#surname_error").text('Max length of Last Name is 25.');
    document.getElementById("first_name_error").style.color = "red";
    return false;
  }
  if(surname.length > 0 && surname.length <= 25)
  {
    console.log('name done.')
    $("#surname_error").text('');
  }





if(date_of_birth =='')
{
   $("#date_of_birth_error").text('Please enter DOB correctly.');
    document.getElementById("date_of_birth_error").style.color = "red";
    return false;
}
else
{
 $("#date_of_birth_error").text('');
    document.getElementById("date_of_birth_error").style.color = "red"; 
}





 if(email.length == 0)
  {
    $("#email_error").text('Email is required.');
    document.getElementById("email_error").style.color = "red";
    return false;
  }
  else
  {
    if(validateEmail(email))
    {
      console.log('valid email');
      $("#email_error").text('');
    }
    else
    {
      $("#email_error").text('Enter valid email.');
      document.getElementById("email_error").style.color = "red";
      return false;
    }
  }



  
 if(address.length == 0)
 {
  $("#address_error").text('Enter the address.');
      document.getElementById("address_error").style.color = "red";
      return false;
 }

 if(address.length > 25)
  {

    $("#address_error").text('Max length of Address is 25.');
        document.getElementById("address_error").style.color = "red";

    return false;

  }
  if(address.length > 0 && address.length <= 25)
  {
    $("#address_error").text('')
    console.log('address done.')
  }








  if(pin_code.length == 0)
 {
  $("#pin_code_error").text('Enter the Pin Code');
      document.getElementById("pin_code_error").style.color = "red";
      return false;
 }

 if(pin_code.length > 10)
  {

    $("#pin_code_error").text('Max length of PinCode is 10.');
        document.getElementById("pin_code_error").style.color = "red";

    return false;

  }
  if(pin_code.length > 0 && pin_code.length <= 10)
  {
    $("#pin_code_error").text('')
    console.log('pin code done.')
  }

  if(year_of_study =="")
  {
    $("#year_of_study_error").text('Enter the year of study.');
        document.getElementById("year_of_study_error").style.color = "red";

    return false;
  }

  year_of_study = parseInt(year_of_study);

if (year_of_study > 7)
{
 $("#year_of_study_error").text('Max value of Study year is 7.');
        document.getElementById("year_of_study_error").style.color = "red";

    return false;
}
if(year_of_study >=0 && year_of_study <=7)
{
  $("#year_of_study_error").text('');
  console.log('year of studey done.')
}


if(programme_studied.length == 0)
{
  $("#programme_studied_error").text('Enter the programme studied.');
        document.getElementById("programme_studied_error").style.color = "red";

    return false;
}
if(programme_studied.length > 15)
{
  $("#programme_studied_error").text('Max length of programme studied is 15.');
        document.getElementById("programme_studied_error").style.color = "red";

    return false;
}

  if(programme_studied.length > 0 && programme_studied.length <= 15)
  {
    $("#programme_studied_error").text('')
    console.log('pin code done.')
  }


if(grades_obtained.length == 0)
{
  $("#grades_obtained_error").text('Enter the grades obtained.');
        document.getElementById("grades_obtained_error").style.color = "red";

    return false;
}
if(grades_obtained.length >3)
{
  $("#grades_obtained_error").text('Length of max value of grade is 3');
        document.getElementById("grades_obtained_error").style.color = "red";

    return false;
}
if(grades_obtained.length >0 && grades_obtained.length <=3)
{
 $("#grades_obtained_error").text(''); 
}

if(max_grades.length == 0)
{
  $("#max_grades_error").text('Enter the  max grades.');
        document.getElementById("max_grades_error").style.color = "red";

    return false;
}
if(max_grades.length >3)
{
  $("#max_grades_error").text('Length of max value of grade is 3');
        document.getElementById("max_grades_error").style.color = "red";

    return false;
}
if(max_grades.length >0 && max_grades.length <=3)
{
 $("#max_grades_error").text(''); 
}

if(skills_interested.length ==0)
{
  
  $("#skills_interested_error").text('Select  the Skills Interested.');
        document.getElementById("skills_interested_error").style.color = "red";

    return false;
}
if(skills_interested.length !=0 )
{
$("#skills_interested_error").text('');
}



if(industry_interested.length ==0)
{
  
  $("#industry_interested_error").text('Select  the Skills Interested.');
        document.getElementById("industry_interested_error").style.color = "red";

    return false;
}
if(industry_interested.length !=0 )
{
$("#industry_interested_error").text('');
}




if(country.length ==0)
{
  
  $("#country_error").text('Select  the Skills Interested.');
        document.getElementById("country_error").style.color = "red";

    return false;
}
if(country.length !=0 )
{
$("#country_error").text('');
}




  if(password.length == 0)
  {
    $("#password_error").text('Password is required.');
      document.getElementById("password_error").style.color = "red";
    return false; 
  }

  if(password.length > 8)
  {
    console.log('pass done.')
   }
   else
  {
    $("#password_error").text('Min length of password is 8.');
        document.getElementById("password_error").style.color = "red";

    return false;    
  }

  console.log("before ajax")
  $.ajax({
    url: '/student_registration/',
    type: "POST",
    data: {'first_name':first_name,'surname':surname,'date_of_birth':date_of_birth,'email':email,'address':address,'pin_code':pin_code,'year_of_study':year_of_study,'programme_studied':programme_studied,'grades_obtained':grades_obtained,'max_grades':max_grades,'skills_interested':skills_interested,'industry_interested':industry_interested,'password':password,'country':country,'csrfmiddlewaretoken':token },
    dataType: 'json',
    cache: false,
    success: function(response){
     // if(response == '3')
     //  {
     //    // alert('Email already registered.');
     //    $("#email_txt").text('Email already registered.');
     //    document.getElementById("email_txt").style.color = "red";
     //    return false;
     //  }
     
        
     if(response=='1')
      {
        console.log(response)
        alert("Registration done.");
        // $('#info_model').modal('show');
        // $("#p_text").text("Registration done.");
        window.location.href='/login/';
      }
      else
      {
        if(response=='0')
        {
          alert('This Email is already registered.');
          console.log(response)
          console.log('e done.')
          // $("#email_txt").text('E-mail already registered.');
          // document.getElementById("email_txt").style.color = "red";
          return false;
        }       
      }
    }
  });
});


$(document).ready(function () {
  $('#confirm_password').keypress(function (e) {
    if (e.keyCode == 13)
    {
      $('#confirm_password').click();
    }
  });
});



