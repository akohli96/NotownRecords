# Notown Records


# Technology Stack

## Backend:Django w/ MySQL

## Frontend:Bootstrap,JQuery

### Used Django Class Based Views

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


```
Basically, user keeps getting redirected to appropriate page
### Running

#### Setup MySQL Backend

```bash
sudo apt-get update
sudo apt-get install python-pip python-dev mysql-server libmysqlclient-dev
sudo mysql_install_db
sudo mysql_secure_installation
mysql -u root -p
```
```sql
CREATE DATABASE notown CHARACTER SET UTF8;
CREATE USER notownuser@localhost IDENTIFIED BY 'notown';
GRANT ALL PRIVILEGES ON notown.* TO notownuser@localhost;
FLUSH PRIVILEGES;
EXIT;
```

#### Python Server setup

```bash
sudo pip install virtualenv

git clone https://github.com/akohli96/NotownRecords.git

virtualenv myenv

source myenv/bin/activate

pip install -r requirements

gunicorn notown.wsgi
```

### HEROKU APP w\SQLITE

[Heroku app](https://notownapp.herokuapp.com/notownapp/)
