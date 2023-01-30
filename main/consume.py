#Quick doc for api consumption
#
##
###
####
#####

####################################################
#/app/sign-up/
{
"username": "ray10",
"phone": "0908765456",
"email": "ray10@gmail.com",
"password": "0000"
}

#/app/sign-in/
{
"username": "ray11",
"password": "0000"
}

#/app/verify/
{
"auth_code": "92f7wqv545idyhbwb48skiuh65rehhlf",
"otp_code": "giz0NR"
}


#/app/reset/
{
"auth_code": "92f7wqv545idyhbwb48skiuh65rehhlf",
"password1": "9999",
"password2": "9999"
}

################################################################
#/business/add/
{
"auth_code": "n4v58yp8ttuq83sc5g7vhppgn70kqw1v",
"name": "business name",
"category": "business category here",
"location": "business location here",
"bio": "bio here",
"category": "business category here",
"phone": "business phone here",
"email": "email here",
"address": "address here"
}

#/business/edit/
{
"auth_code": "n4v58yp8ttuq83sc5g7vhppgn70kqw1v",
"business_id": "1",
"name": "business name",
"category": "business category here",
"location": "business location here",
"bio": "bio here",
"category": "business category here",
"phone": "business phone here",
"email": "email here",
"address": "address here"
}

#/business/delete/
{
"auth_code": "n4v58yp8ttuq83sc5g7vhppgn70kqw1v",
"business_id": "1"
}

#########################################################
#/blog/add/
{
"auth_code": "n4v58yp8ttuq83sc5g7vhppgn70kqw1v",
"business_id": "1",
"title": "blog title",
"detail": "lorem lorem lorem"
}

#/blog/edit/
{
"auth_code": "n4v58yp8ttuq83sc5g7vhppgn70kqw1v",
"blog_id": "1",
"title": "blog title new and changed ",
"detail": "lorem lorem lorem changed lorem"
}

#/blog/delete/
{
"auth_code": "n4v58yp8ttuq83sc5g7vhppgn70kqw1v",
"blog_id": "1"
}
