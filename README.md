# DatabaseProject


#Technology Stack

##Backend:Django w/ MySQL

##Frontend:Bootstrap,JQuery

How constraints are handled:

1. Records get cascaded if you parent table gets deleted

2. Within the models there are checks like
```python
if (self.address != self.phone.address):
            raise ValidationError(('Phone and address phone need to be the same.'))

if (len(str(self.phone))!= 10):
            raise ValidationError(('Need 10 digits'))
        if(int(self.phone)<0):
            raise ValidationError("Enter valid phone")
```

3. Within views, there are checks in frontend to ensure 'valid data' gets passed to backend like
```python
if(( (form.cleaned_data['albumident'])) < 0 ):
	return HttpResponseRedirect()

if(((re.search('[a-zA-Z]', form.cleaned_data['ssn'])) != None)):
	return HttpResponseRedirect()

Basically, user keeps getting redirected to appropriate page
```

###Running
1.Setup MySQL Backend

2. Python Server setup
```bash



git clone https://github.com/akohli96/DatabaseProject

cd DatabaseProject

virtualenv myenv

source env/bin/activate

pip install -r requirements

cd notown

python manage.py runserver
```


